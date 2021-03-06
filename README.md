ansible-role-binaries
=========

Installs several applications via downloading the executable and placing it in Path on Linux based systems. Does **not** install the package via package manager. Additionally, install several Python packages via pip as user.

Installs via binary download:

- awless
- aws
- bat
- bit
- broot
- delta
- direnv
- docker
- doctl
- dog
- dragon
- duf
- entr
- exa
- fasd
- fd
- fluxctl
- gh-md-toc
- githubcli
- glab
- helm
- helm2
- istioctl
- jq
- k6
- k9s
- kind
- kops
- kubectl
- kubectx
- kubens
- kubeval
- kustomize
- lf
- mdbook
- mgiststatus
- nnn
- pet
- polaris
- popeye
- prettyping
- ripgrep
- sdkman
- stern
- tflint
- tfswitch
- xbanish
- xsv
- yq

Install via pip:

- aws-shell
- awscli
- flake8
- gita
- gitlabber
- httpie
- jedi
- litecli
- molecule
- mycli
- neovim-remote
- python-rofi
- s4cmd
- speedtest-cli
- testinfra
- thefuck
- ueberzug
- yamllint

Requirements
------------

Role Variables
--------------

See Example Playbook

Dependencies
------------

- ansible-role-basic

Example Playbook
----------------

```
---
- name: Playbook
  hosts: localhost
  connection: local
  pre_tasks:
    - set_fact:
        tfswitch_version: 0.8.832
        awless_version: 0.1.11
        helm_version: 3.1.1
        githubcli_version: 0.6.2
        stern_version: 1.11.0
        popeye_version: 0.7.1
        bat_version: 0.12.1
        exa_version : 0.9.0
        docker_version: 19.03.8
        docker_compose_version: 1.25.4
        doctl_version: 1.39.0
        awscli_version: 1.18.2
        kind_version: 0.7.0
        kubectl_version: 1.18.0
        k9s_version: 0.19.1
        kops_version: 1.16.0
        istioctl_version: 1.5.1
        mdbook_version: 0.3.7
        fluxctl_version: 1.19.0
        kustomize_version: 3.5.5
        lazygit_version: 0.20.4
        kubeseal_version: 0.12.4
        argocdcli_version: 1.5.6
        xsv_version: 0.13.0
        ripgrep_version: 12.1.1
        fasd_version: 1.0.1
        direnv_version: 2.21.3
        entr_version: 4.6
        nnn_version: 3.3
        lf_version: r21
        delta_version: 0.3.0
        yq_version: 3.3.2
        jq_version: 1.6
        fd_version: v8.1.1
        helm2_version: v2.16.9
        kubeval_version: 0.15.0
        polaris_version: 1.2.1
        bit_version: 0.5.8
        glab_version: 1.11.1
        dog_version: v0.1.0
        tflint_version: v0.21.0
        k6_version: v0.29.0
        kubectx_version: v0.9.1
        kubens_version: v0.9.1
        duf_version: 0.6.0
        pet_version: 0.3.6
        kubectx_version: v0.9.1
        kubens_version: v0.9.1
  roles:
    - ansible-role-binaries
```

License
-------

MIT
