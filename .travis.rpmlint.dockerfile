FROM centos:7
RUN yum install rpmlint -y
COPY tendrl-ansible.spec /root
ENTRYPOINT ["rpmlint", "/root/tendrl-ansible.spec"]
