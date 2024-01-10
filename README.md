# Ansible Playbook

## Introduction

This repository contains a collection of Ansible playbooks designed to automate various system configurations and deployments. These playbooks are intended to streamline the process of managing servers and applications, making it more efficient and error-free.

## Prerequisites

Before you begin, ensure you have the following installed:
| Software | Version |
| --- | --- |
| Centos | 7 |
| Python | 3.6.8 |
| Ansible | 2.11.12|

## Usage

- show available playbooks

```
make list-scripts
```

- run playbook

```
make up-<script>
```

## Playbook

| Name    | Description                               | ToDo |
| ------- | ----------------------------------------- | ---- |
| General | Create a general installation of Centos 7 | ✔️   |
| GCS     | Install Google Cloud Storage              | ✔️   |
| GKE     | Install Google Kubernetes Engine          |      |
| Docker  | Install Docker and Docker Compose         |      |


## Contributing

Contributions are welcome and I will review and consider pull requests. Feel free to open issues if you find missing configuration or customisation options.

## Bug Reports & Feature Requests

Please use the issue tracker to report any bugs or file feature requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

E-mail: [alandev9751210@gmail.com](mailto:<alandev9751210@gmail.com>)
