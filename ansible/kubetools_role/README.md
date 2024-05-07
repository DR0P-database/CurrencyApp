kubetools_role
=========

Role that installs kubeadm, kubelet and kubetools from deb packages and enable the kubelet service before running kubeadm

Requirements
------------

Totally deb platform

Variable roles
--------------

kubernetes_version: “v1.30” -- string to add signature from Kubernetes package with default version “v1.30”.

Dependencies
------------

--

Playbook example
----------------
    - name: Role Usage
       hosts: all
       remote_user: root
       tasks:
       - name: Importing the kubetools_role role
          ansible.builtin.import_role:
               name: kubetools_role

License
-------

BSD

Author information
------------------

--
