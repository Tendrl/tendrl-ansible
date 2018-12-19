# based on Makefile of tendrl-commons

NAME = tendrl-ansible
VERSION = 1.6.3a
COMMIT := $(shell git rev-parse HEAD)
SHORTCOMMIT := $(shell echo $(COMMIT) | cut -c1-7)

all: srpm

clean:
	rm -rf $(NAME)-$(VERSION)
	rm -rf $(NAME)-$(VERSION).tar.gz
	rm -rf $(NAME)-$(VERSION)-*.el7.src.rpm

dist: clean
	mkdir $(NAME)-$(VERSION)
	cp -r roles $(NAME)-$(VERSION)
	cp .yamllint $(NAME)-$(VERSION)
	cp LICENSE $(NAME)-$(VERSION)
	cp README.md $(NAME)-$(VERSION)
	cp site.yml $(NAME)-$(VERSION)
	cp prechecks.yml $(NAME)-$(VERSION)
	cp hosts.example $(NAME)-$(VERSION)
	tar caf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)

srpm: dist
	fedpkg --dist epel7 srpm

rpm: dist
	mock -r epel-7-x86_64 rebuild $(NAME)-$(VERSION)-*.src.rpm --resultdir=. --define "dist .el7"

gitversion:
	# Set version and release to the latest values from Git
	sed -i $(NAME).spec \
	  -e "/^Release:/cRelease: $(shell date +"%Y%m%dT%H%M%S").$(SHORTCOMMIT)"

snapshot: gitversion srpm


.PHONY: dist rpm srpm gitversion snapshot
