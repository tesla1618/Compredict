var ctx = document.getElementById("barChart");
var barChart = new Chart(ctx,{
  type: 'bar',
  data: {
    labels:["Startech","TechLand","Ryans","BUBT"],
    borderColor : "#eee",
    datasets: [
      {
        data: ["2","3","1","4"],
        borderColor : "#fff",
        borderWidth : "3",
        hoverBorderColor : "#000",
        backgroundColor: [
          "#f38b4a",
          "#56d798",
          "#ff8397",
          "#6970d5" 
        ],
        hoverBackgroundColor: [
          "#f38b4a",
          "#56d798",
          "#ff8397",
          "#6970d5"
        ]
      }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks:{
          min : 0,
          stepSize : 1,
          fontColor : "#000",
          fontSize : 14
        },
        gridLines:{
          color: "#eee",
          lineWidth:1,
          zeroLineColor :"#000",
          zeroLineWidth : 2
        },
        stacked: true
      }],
      xAxes: [{
        ticks:{
          fontColor : "#eee",
          fontSize : 14
        },
        gridLines:{
          color: "#fff",
          lineWidth:1
        }
      }]
    },
    responsive:true
  }
});