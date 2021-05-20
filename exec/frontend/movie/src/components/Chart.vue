<script>
import { HorizontalBar } from 'vue-chartjs';
import { preferPerGenre } from '@/api/movie';

export default {
  extends: HorizontalBar,
  data() {
    return {
      isLoad: false,
      chartData: {
        hoverBackgroundColor: 'red',
        hoverBorderWidth: 10,
        labels: ['모험', '판타지', '애니메이션', '드라마', '공포', '액션', '코미디', '역사', '서부', '스릴러', '범죄', '다큐멘터리', 'SF', '미스터리', '음악', '로맨스', '가족', '전쟁', 'TV 영화'],
        datasets: [
          {
            backgroundColor: [
              'rgb(224, 58, 60)',
              'rgb(246, 130, 31)',
              'rgb(252, 184, 39)',
              'rgb(98, 187, 71)',
              'rgb(0, 157, 220)',
              'rgb(150, 61, 151)',
              'rgb(224, 58, 60)',
              'rgb(246, 130, 31)',
              'rgb(252, 184, 39)',
              'rgb(98, 187, 71)',
              'rgb(0, 157, 220)',
              'rgb(150, 61, 151)',
              'rgb(224, 58, 60)',
              'rgb(246, 130, 31)',
              'rgb(252, 184, 39)',
              'rgb(98, 187, 71)',
              'rgb(0, 157, 220)',
              'rgb(150, 61, 151)',
              'rgb(224, 58, 60)',
              'rgb(246, 130, 31)',
            ],
            data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          },
        ],
        hoverOffset: 4,
      },

      uuid: this.user_id,
      bestGenre: '',
    };
  },
  props: ['user_id'],

  async created() {
    try {
      const uuid = {
        uid: this.uuid,
      };
      const { data } = await preferPerGenre(uuid);
      console.log(data.message);

      this.chartData.datasets[0].data[0] = data.message['모험'];
      this.chartData.datasets[0].data[1] = data.message['판타지'];
      this.chartData.datasets[0].data[2] = data.message['애니메이션'];
      this.chartData.datasets[0].data[3] = data.message['드라마'];
      this.chartData.datasets[0].data[4] = data.message['공포'];
      this.chartData.datasets[0].data[5] = data.message['액션'];
      this.chartData.datasets[0].data[6] = data.message['코미디'];
      this.chartData.datasets[0].data[7] = data.message['역사'];
      this.chartData.datasets[0].data[8] = data.message['서부'];
      this.chartData.datasets[0].data[9] = data.message['스릴러'];
      this.chartData.datasets[0].data[10] = data.message['다큐멘터리'];
      this.chartData.datasets[0].data[11] = data.message['SF'];
      this.chartData.datasets[0].data[12] = data.message['미스터리'];
      this.chartData.datasets[0].data[13] = data.message['음악'];
      this.chartData.datasets[0].data[14] = data.message['로맨스'];
      this.chartData.datasets[0].data[15] = data.message['가족'];
      this.chartData.datasets[0].data[16] = data.message['전쟁'];
      this.chartData.datasets[0].data[17] = data.message['TV 영화'];
    } catch (err) {
      console.log(err);
    }

    // 실제 차트 랜더링 부분
    this.renderChart(this.chartData, {
      borderWidth: '10px',
      hoverBackgroundColor: 'red',
      hoverBorderWidth: '10px',
      maintainAspectRatio: false,
      responsive: true,
      width: '50%',
      height: '50%',

      legend: {
        display: false,
      },
      tooltips: {
        callbacks: {
          label: (tooltipItem) => `${tooltipItem.yLabel}: ${tooltipItem.xLabel}`,
          title: () => null,
        },
      },
    });
  },
};
</script>
