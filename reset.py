#!/usr/bin/env python

import requests
import json
from time import sleep
from os import environ


HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(environ.get('DO_KEY'))
}
REGION = 'fra1'
NODES = {
    #ceph
    44696352: {"name": "tendrl-ceph-01", "volumes": 2},
    44696411: {"name": "tendrl-ceph-02", "volumes": 2},
    44696462: {"name": "tendrl-ceph-03", "volumes": 2},
    44696550: {"name": "tendrl-ceph-04", "volumes": 2},
    44696617: {"name": "tendrl-ceph-05", "volumes": 2},

    # gluster
    44697211: {"name": "tendrl-gluster-01", "volumes": 2},
    44697264: {"name": "tendrl-gluster-02", "volumes": 2},
    44697317: {"name": "tendrl-gluster-03", "volumes": 2},

    # management
    44723317: {"name": "tendrl-node-01"},
    }



def reset_nodes():
    data = {"type":"rebuild","image":"centos-7-x64"}
    for node in NODES:
        r = requests.post(
                "https://api.digitalocean.com/v2/droplets/{}/actions".format(node),
                data=json.dumps(data),
                headers=HEADERS,
        )
        print r.json()
        sleep(5)


def create_volume_for_node(node):
    node_dict = NODES.get(node['id'])
    print node['id'], node.get('volume_ids')

    # check if it needs volumes according to config
    if not node_dict or not node_dict.get('volumes'):
        return

    # check if has volumes already attached
    # if node_dict.get('volumes') <= len(node.get('volume_ids')):
        # return

    # create correct number of volumes
    for count in range(node_dict.get('volumes')):
        data = {
                'size_gigabytes': 20,
                'name': "{}-{}".format(node_dict['name'], count),
                'region': node['region']['slug'],
        }
        r = requests.post(
                "https://api.digitalocean.com/v2/volumes",
                data=json.dumps(data),
                headers=HEADERS,
        )
        print r.json()
        vol = r.json().get('volume')
        sleep(5)
        # attach volumes
        data = {
                'type': 'attach',
                'droplet_id': node['id'],
                'region': node['region']['slug'],
        }
        r = requests.post(
                "https://api.digitalocean.com/v2/volumes/{}/actions".format(vol['id']),
                data=json.dumps(data),
                headers=HEADERS,
        )
        print r.json()


def delete_attached_volumes(node, volume_name):
    r = requests.get(
            "https://api.digitalocean.com/v2/volumes?name={}&region={}".format(volume_name, REGION),
            headers=HEADERS,
    )
    try:
        vol = r.json()['volumes'][0]['id']
    except IndexError:
        return

    data = {
            'type': 'detach',
            'droplet_id': node,
    }
    r = requests.post(
            "https://api.digitalocean.com/v2/volumes/{}/actions".format(vol),
            data=json.dumps(data),
            headers=HEADERS,
    )
    print r.json()
    sleep(5)
    r = requests.delete(
            "https://api.digitalocean.com/v2/volumes/{}".format(vol),
            headers=HEADERS,
    )
    print vol, r.status_code


def clean_up_volumes():
    for node_id, node in NODES.iteritems():
        if node.get('volumes'):
            for volid in range(node['volumes']):
                volume_name = "{}-{}".format(node['name'], volid)
                delete_attached_volumes(node_id, volume_name)


def create_volumes():
    r = requests.get(
            'https://api.digitalocean.com/v2/droplets?tag_name=tendrl',
            headers=HEADERS
    )
    for droplet in r.json().get('droplets'):
        create_volume_for_node(droplet)

clean_up_volumes()
reset_nodes()
create_volumes()
