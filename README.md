onkf.routeros
=============

This roles configures a `routeros` device based on a few "simple" variables.

---

**DISCLAIMER**: This is a giant work in progress - only here for future reference

---

Introduction
------------

Imagine writing a single YAML file which descripes the configuration of a routeros device and then deploying that in "one go".
This role tries to make this wish come true.

Limitations
-----------

**non-atomic**:

`routeros` does not support atomic config changes and therefore:
* the order of config changes matter
* some changes depend on other changes that are not yet executed

Keep in mind that you potentially need to fix a device manually before it can continue to configure itself.

**biased**:

This role only implements a handfull of config statements needed for a few specific usecases

**custom variable layout**:

The configuration structure defined by this role is developed "on-the-fly" and will get worse over time :)

**lacks documentation**

Requirements
------------

* [`community.routeros`](https://github.com/hirnpfirsich/community.routeros) (custom fork)

Role Variables
--------------

**TBA**

Dependencies
------------

-

Example Playbook
----------------

    - hosts: switches
      roles:
         - onkf.routeros

License
-------

MIT

Author Information
------------------

Gregor Michels <hirnpfirsich@brainpeach.de>
