<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      gradient: null,
    };
  },
  methods:{
    
  },
  computed:{
    obras(){
        return this.$store.state.obras.listado;
    },
    datos(){
      var today = new Date();
      var labels = [''];
      var data = [0];
      var encontrados = this.obras.filter((item) => {
          return (Date.parse(item.inicio) <= Date.parse(today) &&
              Date.parse(item.fin) >= Date.parse(today))
      });
      if(encontrados.length>0)
      {
        encontrados.forEach(element => {
          labels.push(element.nombre);
          data.push(element.presupuesto);
        });
      }
      return {labels:labels, data:data};
    }
  },
  watch:{
    datos(newValue){
      this.renderChart(
        {
          labels: this.datos.labels,
          datasets: [
            {
              label: "Presupuesto",
              borderColor: "#66BB6A",
              pointBackgroundColor: "#66BB6A",
              borderWidth: 2,
              pointBorderColor: "#66BB6A",
              backgroundColor: this.gradient,
              data: this.datos.data
            },
          ]
        },
        {
          responsive: true,
          maintainAspectRatio: false,
          legend: {
            labels: {
                // This more specific font property overrides the global property
                fontColor: 'white',
                fontFamily:'Roboto',
                fontSize:14,
            }
          },
          scales: {
            
            yAxes: [{
                gridLines:{
                  drawBorder: false,
                  display: true,
                  drawOnChartArea: true,
                  drawTicks: false,
                  borderDash: [5, 5],
                  color: 'rgba(255, 255, 255, 0.1)'
                },
                ticks: {
                    fontColor:'white',
                    fontFamily:'Roboto',
                    fontSize:14,
                    padding:5,
                    callback: function(value, index, values) {
                      var SI_SYMBOL = ["", "k", "M", "G", "T", "P", "E"];
                      var tier = Math.log10(Math.abs(value)) / 3 | 0;
                      if(tier == 0) return value;
                      var suffix = SI_SYMBOL[tier];
                      var scale = Math.pow(10, tier * 3);
                      var scaled = value / scale;
                      return '$'+scaled.toFixed(1) + suffix;
                    }
                }
            }],
            xAxes: [{
                gridLines:{
                  drawBorder: false,
                  display: true,
                  drawOnChartArea: true,
                  drawTicks: false,
                  borderDash: [5, 5],
                  color: 'rgba(255, 255, 255, .2)'
                },
                ticks: {
                    fontColor:'white',
                    fontFamily:'Roboto',
                    fontSize:14,
                    padding:5,
                }
            }]
          }
        },
      );
    }
  },
  mounted() {
    this.$store.dispatch('obras/listado');
    this.gradient = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.gradient.addColorStop(0, "rgba(102,187,106, 0.25)");
    this.gradient.addColorStop(0.5, "rgba(102,187,106, 0.10)");
    this.gradient.addColorStop(1, "rgba(102,187,106, 0)");
  }
};
</script>
