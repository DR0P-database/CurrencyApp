crio_role
=========

Role that installs cri-o from deb packages and initializes the Kubernetes cluster

Requirements
------------

Totally deb platform

Variable roles
--------------

kubernetes_version: “v1.30” -- string to add a Kubernetes repository of the default version “v1.30”.
project_path: “prerelease:/main” -- string to add the CRI-O repository of the prerelease or stable version.


Dependencies
------------

--

Playbook example
----------------

    - name: Role Usage
       hosts: all
       remote_user: root
       tasks:
       - name: Role import cri-o
          ansible.builtin.import_role:
               name: crio_role

License
-------

BSD

Author information
------------------

--
