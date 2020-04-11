function init(){
    var trace1 = {
        x: groupNames,
        y: numberOfRunnerByAge,
        type: "bar"
    };

    var data = [trace1];

    var layout = {
        title: "Number of Participants by Age",
        xaxis: {title: "Age Group"},
        yaxis: {title: "Number of Runners"}
    };

    console.log('Hello')
    console.log(groupNames)

    Plotly.newPlot("plot", data, layout);
}

init()

var trace2 = {
    x: groupNames,
    y: maleTimes,
    mode: 'scatter',
    name: 'M'
};

var trace3 = {
    x: groupNames,
    y: femaleTimes,
    mode: 'scatter',
    name: 'F'
};

var data_2 = [ trace2, trace3 ];

var layout_2 = {
    title : 'Average Offical Time by Age Group and Gender',
    xaxis : {title: 'Age Group'},
    yaxis : {title: 'Average Offical Time (Hrs)'}
};

Plotly.newPlot('plot_2', data_2, layout_2);

var data_3 = [{
    type: 'table',
    header: {
      values: [['Rank'],['Top 50 Male Runners'],['Age Group'], ['Country'], ['Finish Time (Hrs)']],
      align: "center",
      line: {width: 1, color: 'black'},
      fill: {color: "grey"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: [ranking, top50MaleNames, top50MaleAge, top50MaleCountry, top50MaleTimes],
      align: "center",
      line: {color: "black", width: 1},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]

  var layout_3 = {
    title: "Top 50 Male Runners"
  }


  Plotly.newPlot('myDiv', data_3, layout_3);

var data_4 = [{
    type: 'table',
    header: {
      values: [['Rank'],['Top 50 Female Runners'],['Age Group'], ['Country'], ['Finish Time (Hrs)']],
      align: "center",
      line: {width: 1, color: 'black'},
      fill: {color: "grey"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: [ranking, top50FemaleNames, top50FemaleAge, top50FemaleCountry, top50FemaleTimes],
      align: "center",
      line: {color: "black", width: 1},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]

  var layout_4 = {
    title: "Top 50 Female Runners"
  }

  Plotly.newPlot('myDiv2', data_4, layout_4);


  var data_5 = [{
    values: countryType,
    labels: ['USA', 'Foreign'],
    type: 'pie',
    marker: {
        colors: ['rgb(56, 75, 126)', 'rgb(23, 190, 207)']
      }
  }];
  
  var layout_5 = {
    title: "Number of Runners from USA vs. Foreign",
  };
  
  Plotly.newPlot('myDiv3', data_5, layout_5);

var trace4 = {
    x: groupNames,
    y: usaTimes,
    mode: 'scatter',
    name: 'USA',
    line: {
        color: 'rgb(56, 75, 126)',
      }
};

var trace5 = {
    x: groupNames,
    y: internationalTimes,
    mode: 'scatter',
    name: 'Foreign',
    line: {
        color: 'rgb(23, 190, 207)',
      }
};

var data_6 = [ trace4, trace5 ];

var layout_6 = {
    title : 'Average Offical Time by Age Group and Country',
    xaxis : {title: 'Age Group'},
    yaxis : {title: 'Average Offical Time (Hrs)'}
};

Plotly.newPlot('plot_3', data_6, layout_6);
