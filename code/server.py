#!/usr/bin/python
"""OPEN DATA API REST SERVER."""


def get_info():
    """
    @api {GET} /info/ API Information
    @apiName Info
    @apiGroup General
    @apiDescription Retrieves general information about the API
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} results General information about the API
    @apiSampleRequest /info/
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/info/
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "result": "Information!"
        }
    """


def get_list(c_name):
    """
    @api {GET} /meta/ API Metadata
    @apiName Metadata
    @apiGroup General
    @apiDescription Retrieves metadata for each collection
    @apiParam {String} c_name Collection name (systems, developers, tasks)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} results Metadata and information about each collection
    @apiSampleRequest /meta/:c_name
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/meta/systems
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "result": "Metadata showing information about the systems collection."
        }
    """


def get_devSystems(id):
    """
    @api {GET} /dev/:id Developers Metadata
    @apiName DevMetadata
    @apiGroup General
    @apiDescription Retrieves metadata for each developer
    @apiParam {String} _id Developer's ID (dev1, dev2, ... dev6)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} _id Developer's ID
    @apiSuccess (Success 200) {List} Systems A list of all the systems that this developer was involved in
    @apiSuccess (Success 200) {Number} Num_logs Total number of logs recorded for this developer
    @apiSuccess (Success 200) {Number} Num_diaries Total number of diaries recorded for this developer
    @apiSuccess (Success 200) {Number} Num_thinkaloud Total number of thinkaluds recorded for this developer
    @apiSampleRequest /dev/:id
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "_id": "dev1",
            "Numb_logs": 7,
            "Num_diaries": 17,
            "systems": [ ... ],
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "Num_thinkaloud": 7,
            "_id": "dev1"
        }
    """


def get_devLog(id, date):
    """
    @api {GET} /dev/:id/log/:date Developers LogFile
    @apiName DevLog
    @apiGroup Download
    @apiDescription Download a log file of a developer
    @apiParam {String} _id Developer's ID (dev1, dev2, ... dev6)
    @apiParam {String} date Date (YYYY-MM-DD)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} _id Developer's ID
    @apiSuccess (Success 200) {String} url Download URL for this log
    @apiSampleRequest /dev/:id/log/:date
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/log/2008-10-17
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "_id": "dev1",
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "url": [http://...],
            "_id": "dev1"
        }
    """


def get_devDiary(id, date):
    """
    @api {GET} /dev/:id/diary/:date Developers DiaryFile
    @apiName DevDiary
    @apiGroup Download
    @apiDescription Download a diary file of a developer
    @apiParam {String} _id Developer's ID (dev1, dev2, ... dev6)
    @apiParam {String} date Date (YYYY-MM-DD)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} _id Developer's ID
    @apiSuccess (Success 200) {String} url Download URL for this diary
    @apiSampleRequest /dev/:id/diary/:date
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/diary/2008-10-17
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "_id": "dev1",
            "request_id": "jp509893-a073-4d23-9f95-388d1c1e2c46",
            "url": [http://...],
            "_id": "dev1"
        }
    """


def get_devThL(id, date):
    """
    @api {GET} /dev/:id/thinkaloud/:date Developers ThinkaloudFile
    @apiName DevTh
    @apiGroup Download
    @apiDescription Download a thinkaloud file of a developer
    @apiParam {String} _id Developer's ID (dev1, dev2, ... dev6)
    @apiParam {String} date Date (YYYY-MM-DD)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} _id Developer's ID
    @apiSuccess (Success 200) {String} file Download URL for this thinkaloud
    @apiSampleRequest /dev/:id/thinkaloud/:date
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/dev/dev1/thinkaloud/2008-11-07
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "thinkaloud": [
            {
                "date": "2008-11-07",
                "file": "dev1_2008-11-07"
            }
            ],
                "_id": "dev1",
                "request_id": "ea99c971-c167-456d-ba69-bee4afb44efb"
        }
    """


def get_showcase(id, date):
    """
    @api {GET} /showcase/:date Showcase
    @apiName Showcase
    @apiGroup Showcases
    @apiDescription Download a showcase
    @apiParam {String} date Date (YYYY-MM-DD)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} url Download URL for this log
    @apiSampleRequest /showcase/:date
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/showcase/2008-10-17
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "url": [http://...]
        }
    """


def get_experiment(id, date):
    """
    @api {GET} /experiment/:date experiment
    @apiName Experiment
    @apiGroup Experiments
    @apiDescription Download a experiment
    @apiParam {String} date Date (YYYY-MM-DD)
    @apiSuccess (Success 200) {UUID} request_id Request unique identifier
    @apiSuccess (Success 200) {String} url Download URL for this log
    @apiSampleRequest /experiment/:date
    @apiExample cURL example
    $ curl -i http://opendata.soccerlab.polymtl.ca:5001/experiment/2008-10-17
    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "url": [http://...]
        }
    """
