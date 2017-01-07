define({ "api": [
  {
    "type": "GET",
    "url": "/dev/:id/diary/:date",
    "title": "Developers DiaryFile",
    "name": "DevDiary",
    "group": "Download",
    "description": "<p>Download a diary file of a developer</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID (dev1, dev2, ... dev6)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "date",
            "description": "<p>Date (YYYY-MM-DD)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>Download URL for this diary</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"_id\": \"dev1\",\n    \"request_id\": \"jp509893-a073-4d23-9f95-388d1c1e2c46\",\n    \"url\": [http://...],\n    \"_id\": \"dev1\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/dev/:id/diary/:date"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/diary/2008-10-17",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "Download"
  },
  {
    "type": "GET",
    "url": "/dev/:id/log/:date",
    "title": "Developers LogFile",
    "name": "DevLog",
    "group": "Download",
    "description": "<p>Download a log file of a developer</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID (dev1, dev2, ... dev6)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "date",
            "description": "<p>Date (YYYY-MM-DD)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>Download URL for this log</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"_id\": \"dev1\",\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"url\": [http://...],\n    \"_id\": \"dev1\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/dev/:id/log/:date"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/log/2008-10-17",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "Download"
  },
  {
    "type": "GET",
    "url": "/dev/:id/thinkaloud/:date",
    "title": "Developers ThinkaloudFile",
    "name": "DevTh",
    "group": "Download",
    "description": "<p>Download a thinkaloud file of a developer</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID (dev1, dev2, ... dev6)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "date",
            "description": "<p>Date (YYYY-MM-DD)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "file",
            "description": "<p>Download URL for this thinkaloud</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"thinkaloud\": [\n    {\n        \"date\": \"2008-11-07\",\n        \"file\": \"dev1_2008-11-07\"\n    }\n    ],\n        \"_id\": \"dev1\",\n        \"request_id\": \"ea99c971-c167-456d-ba69-bee4afb44efb\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/dev/:id/thinkaloud/:date"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/thinkaloud/2008-11-07",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "Download"
  },
  {
    "type": "GET",
    "url": "/experiment/:date",
    "title": "experiment",
    "name": "Experiment",
    "group": "Experiments",
    "description": "<p>Download a experiment</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "date",
            "description": "<p>Date (YYYY-MM-DD)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>Download URL for this log</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"url\": [http://...]\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/experiment/:date"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/experiment/2008-10-17",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "Experiments"
  },
  {
    "type": "GET",
    "url": "/dev/:id",
    "title": "Developers Metadata",
    "name": "DevMetadata",
    "group": "General",
    "description": "<p>Retrieves metadata for each developer</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID (dev1, dev2, ... dev6)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Developer's ID</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "Systems",
            "description": "<p>A list of all the systems that this developer was involved in</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Num_logs",
            "description": "<p>Total number of logs recorded for this developer</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Num_diaries",
            "description": "<p>Total number of diaries recorded for this developer</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "Num_thinkaloud",
            "description": "<p>Total number of thinkaluds recorded for this developer</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"_id\": \"dev1\",\n    \"Numb_logs\": 7,\n    \"Num_diaries\": 17,\n    \"systems\": [ ... ],\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"Num_thinkaloud\": 7,\n    \"_id\": \"dev1\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/dev/:id"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "General"
  },
  {
    "type": "GET",
    "url": "/info/",
    "title": "API Information",
    "name": "Info",
    "group": "General",
    "description": "<p>Retrieves general information about the API</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "results",
            "description": "<p>General information about the API</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"result\": \"Information!\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/info/"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/info/",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "General"
  },
  {
    "type": "GET",
    "url": "/meta/",
    "title": "API Metadata",
    "name": "Metadata",
    "group": "General",
    "description": "<p>Retrieves metadata for each collection</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "c_name",
            "description": "<p>Collection name (systems, developers, tasks)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "results",
            "description": "<p>Metadata and information about each collection</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"result\": \"Metadata showing information about the systems collection.\"\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/meta/:c_name"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/meta/systems",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "General"
  },
  {
    "type": "GET",
    "url": "/showcase/:date",
    "title": "Showcase",
    "name": "Showcase",
    "group": "Showcases",
    "description": "<p>Download a showcase</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "date",
            "description": "<p>Date (YYYY-MM-DD)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "UUID",
            "optional": false,
            "field": "request_id",
            "description": "<p>Request unique identifier</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>Download URL for this log</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.0 200 OK\n{\n    \"request_id\": \"ad506913-a073-4d23-9f95-388d1c1e2c46\",\n    \"url\": [http://...]\n}",
          "type": "js"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://opendata.soccerlab.polymtl.ca:5001/showcase/:date"
      }
    ],
    "examples": [
      {
        "title": "cURL example",
        "content": "$ curl -i http://opendata.soccerlab.polymtl.ca:5001/showcase/2008-10-17",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "/home/amir/opendatadb/api/code/server.py",
    "groupTitle": "Showcases"
  }
] });
