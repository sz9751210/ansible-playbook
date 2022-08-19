# ansible-elk

## 介紹
在gcp環境下使用ansible playbook 建立elk stack
- elasticsearch：主要會先需要先跑init master，接著再去跑seed host去加入master組成cluster架構，邏輯上還有可修改的地方，目前先以兩份yaml分開跑下去做建立，在跑完init master後會先建立iim以及index template
- logstash：直接將pipeline等設定都複製進去
## 資料夾結構
```shell
.
├── create_elasticsearch_master_instance.yaml
├── create_elasticsearch_slave_instance.yaml
├── create_filebeat_instance.yaml
├── create_kibana_instance.yaml
├── create_logstash_instance.yaml
├── files
│   ├── elasticsearch
│   │   ├── api.sh
│   │   ├── certs
│   │   └── elasticsearch.repo
│   ├── kibana
│   │   └── kibana.repo
│   └── logstash
│       ├── conf.d
│       │   └── logstash.conf
│       ├── logstash.repo
│       ├── logstash.yml
│       └── pipelines.yml
├── group_vars
│   └── all
│       ├── env.yml copy.example
│       └── package.yml
├── inventory
│   └── elk.test.node
├── inventory.instance.create.yml.example
├── README.md
├── roles
│   ├── elasticsearch
│   │   ├── tasks
│   │   │   ├── create_disk.yml
│   │   │   ├── install_elastic.yml
│   │   │   ├── main.yml
│   │   │   ├── setup_disk.yml
│   │   │   ├── setup_elastic_master.yml
│   │   │   └── setup_elastic_slave.yml
│   │   └── templates
│   │       └── elasticsearch.yml.j2
│   ├── instance
│   │   └── tasks
│   │       ├── create.yml
│   │       └── setup.yml
│   ├── kibana
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       └── kibana.yml.j2
│   └── logstash
│       └── tasks
│           └── main.yml
└── vars
    ├── elasticsearch
    │   ├── elasticsearch_var.yml
    │   └── elasticsearch_var.yml.example
    ├── instance
    │   ├── instance_var.yml
    │   └── instance_var.yml.example
    ├── kibana
    │   ├── kibana_var.yml
    │   └── kibana_var.yml.example
    └── logstash
        ├── logstash_var.yml
        └── logstash_var.yml.example
```

## 使用指南
1. 設定機器資訊：複製好inventory.instance.create.yml.example後，可參考inventory裡的設定，主要設定gcp的資訊，elasticsearch的node_role為data_role，可參考以下連結

[Elasticsearch Multi\-Tier Architecture \| Hot, Warm, Cold & Frozen](https://opster.com/guides/elasticsearch/capacity-planning/elasticsearch-hot-warm-cold-frozen-architecture/)

2. 設定group_vars的env.yml，改成自己的gcp的專案以及要設定的region

3. 設定vars裡的相對yml，可參考範例
   - elasticsearch：主要設定掛載的硬碟資訊
   - kibana,logstash：設定elasticsearch的host資訊

## 建置流程
elasticsearch_master -> elasticsearch_slave -> logstash -> kibana

- 指令
```shell
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.instance.create.yml create_xxx_instance.yaml -v
```

## todo

- [ ] elasticsearch playbook 優化
- [ ] 添加filebeat role
- [ ] disk 修改建置資料夾