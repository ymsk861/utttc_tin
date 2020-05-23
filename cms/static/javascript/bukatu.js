//var random = Math.floor( Math.random() * 4 );

//var A=console.log( random );
//部活の名前
    const outputElementName = document.getElementById('output_csv_name');

    function getCsvDataName(dataPath) {
        const request = new XMLHttpRequest();
        request.addEventListener('load', (event) => {
            const response = event.target.responseText;
            convertArrayName(response);
        });
        request.open('GET', dataPath, true);
        request.send();
    }

    function convertArrayName(data) {
        const dataArrayName = [];
        const dataStringName = data.split('\n');
        for (let i = 0; i < dataStringName.length; i++) {
            dataArrayName[i] = dataStringName[i].split(',');
        }
        outputElementName.innerHTML = dataArrayName[idx][1];
    }

    getCsvDataName('../../static/csv/bukatu.csv');
//outputElementNameに変数が入っている。
//tag1
    const outputElementTag1 = document.getElementById('output_csv_tag1');

    function getCsvData(dataPath) {
        const request = new XMLHttpRequest();
        request.addEventListener('load', (event) => {
            const response = event.target.responseText;
            convertArray(response);
        });
        request.open('GET', dataPath, true);
        request.send();
    }

    function convertArray(data) {
        const dataArray = [];
        const dataString = data.split('\n');
        for (let i = 0; i < dataString.length; i++) {
            dataArray[i] = dataString[i].split(',');
        }
        outputElementTag1.innerHTML = dataArray[idx][2];
    }

    getCsvData('../../static/csv/bukatu.csv');
//tag2
    const outputElementTag2 = document.getElementById('output_csv_tag2');

    function getCsvDataTag2(dataPath) {
        const request = new XMLHttpRequest();
        request.addEventListener('load', (event) => {
            const response = event.target.responseText;
            convertArrayTag2(response);
        });
        request.open('GET', dataPath, true);
        request.send();
    }

    function convertArrayTag2(data) {
        const dataArrayTag2 = [];
        const dataStringTag2 = data.split('\n');
        for (let i = 0; i < dataStringTag2.length; i++) {
            dataArrayTag2[i] = dataStringTag2[i].split(',');
        }
        outputElementTag2.innerHTML = dataArrayTag2[idx][3];
    }

    getCsvDataTag2('../../static/csv/bukatu.csv');
//tag3
    const outputElementTag3 = document.getElementById('output_csv_tag3');

    function getCsvDataTag3(dataPath) {
        const request = new XMLHttpRequest();
        request.addEventListener('load', (event) => {
            const response = event.target.responseText;
            convertArrayTag3(response);
        });
        request.open('GET', dataPath, true);
        request.send();
    }

    function convertArrayTag3(data) {
        const dataArrayTag3 = [];
        const dataStringTag3 = data.split('\n');
        for (let i = 0; i < dataStringTag3.length; i++) {
            dataArrayTag3[i] = dataStringTag3[i].split(',');
        }
        outputElementTag3.innerHTML = dataArrayTag3[idx][4];
    }

    getCsvDataTag3('../../static/csv/bukatu.csv');
//部活詳細
    const outputElementDetail = document.getElementById('output_csv_detail');

    function getCsvDataDetail(dataPath) {
        const request = new XMLHttpRequest();
        request.addEventListener('load', (event) => {
            const response = event.target.responseText;
            convertArrayDetail(response);
        });
        request.open('GET', dataPath, true);
        request.send();
    }

    function convertArrayDetail(data) {
        const dataArrayDetail = [];
        const dataStringDetail = data.split('\n');
        for (let i = 0; i < dataStringDetail.length; i++) {
            dataArrayDetail[i] = dataStringDetail[i].split(',');
        }
        outputElementDetail.innerHTML = dataArrayDetail[idx][8];
    }

    getCsvDataDetail('../../static/csv/bukatu.csv');
