// Vue.createApp({
//             data() {
//                 return {
//                     option: {
//                         textStyle: {
//                             fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
//                         },
//                         title: {
//                             text: "Traffic Sources",
//                             left: "center"
//                         },
//                         tooltip: {
//                             trigger: "item",
//                             formatter: "{a} <br/>{b} : {c} ({d}%)"
//                         },
//                         legend: {
//                             orient: "vertical",
//                             left: "left",
//                             data: [
//                                 "Direct",
//                                 "Email",
//                                 "Ad Networks",
//                                 "Video Ads",
//                                 "Search Engines"
//                             ]
//                         },
//                         series: [
//                             {
//                                 name: "Traffic Sources",
//                                 type: "pie",
//                                 radius: "55%",
//                                 center: ["50%", "60%"],
//                                 data: [
//                                     {value: 335, name: "Direct"},
//                                     {value: 310, name: "Email"},
//                                     {value: 234, name: "Ad Networks"},
//                                     {value: 135, name: "Video Ads"},
//                                     {value: 1548, name: "Search Engines"}
//                                 ],
//                                 emphasis: {
//                                     itemStyle: {
//                                         shadowBlur: 10,
//                                         shadowOffsetX: 0,
//                                         shadowColor: "rgba(0, 0, 0, 0.5)"
//                                     }
//                                 }
//                             }
//                         ]
//                     }
//                 };
//             }
//         }).component("v-chart", VueECharts).mount("#app");


// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据 柱状图
// var option = {
//     title: {
//         text: 'ECharts 入门示例'
//     },
//     tooltip: {},
//     legend: {
//         data: ['销量']
//     },
//     xAxis: {
//         data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
//     },
//     yAxis: {},
//     series: [{
//         name: '销量',
//         type: 'bar',
//         data: [5, 20, 36, 10, 10, 20]
//     }]
// };

// 饼图

var option = {
    series: [
        {
            name: '访问来源',
            type: 'pie',
            radius: '80%',
            data: [
                {value: 235, name: '这是一个饼图'},
            ]
        }
    ]
}

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);


let analysisApp = new Vue({
    el: '#analysis-app',
    data: {
        analysisType: 0,
        analysisTypeList: [
            {'key': 0, 'name': '请选择分析类别', 'url': ''},
            {'key': 1, 'name': '岗位方向', 'url': '/api/job-position/job-direction/'},
            {'key': 2, 'name': '技能要求', 'url': '/api/job-position/skill-label/'},
            {'key': 3, 'name': '福利标签', 'url': '/api/job-position/welfare-label/'},
        ],
        checkboxList: [
            {'key': 1, 'name': '请先选择分析类别'},
        ],
        elementList: [],
        graphicTypeList: [
            {'name': '请选择图形类型', value: 'pie'},
            {'name': '饼图', value: 'pie'},
            {'name': '柱状图', value: 'bar'},
            {'name': '折线图', value: 'line'}
        ],
        graphicType: 'pie'

    },
    methods: {
        getCheckBoxList: function () {  // 获取复选框中的数据列表
            let url = '';
            for (let item of this.analysisTypeList) {
                if (item['key'] === this.analysisType) {
                    url = item['url'];
                }
            }

            if (!url) {
                return
            }
            axios.get(url).then((res) => {
                let result = res.data;
                this.checkboxList = [];

                for (let item of result) {
                    this.checkboxList.push(item);
                }

            }).catch((error) => {
                console.log('into catch', error)
            })
        },

        changeAnalysisType: function () {  // 切换分析类型
            this.getCheckBoxList();
        },

        changeEchartsData: function () {  // 更新分析图表数据
            let name = '';
            for (let item of this.analysisTypeList) {
                if (item['key'] === this.analysisType) {
                    name = item['name'];
                }
            }

            let url = '/api/job-position/analysis/';
            let params = {
                'analysis_type': this.analysisType,
                'elements': this.elementList.toString()
            }

            axios.get(url, {params}).then((res) => {
                console.log(res.data);

                if (this.graphicType === 'pie') {  // 饼图
                    console.log('饼图饼图饼图饼图')
                    let data = [];
                    for (let item of res.data) {
                        data.push(
                            {
                                'name': item['name'] + `(${item['percent']})`,
                                'value': item['value']
                            }
                        )
                    }

                    let option = {
                        series: [
                            {
                                name: name,
                                type: 'pie',
                                radius: '80%',
                                data: data,
                            }
                        ]
                    }
                    myChart.setOption(option);

                } else if (this.graphicType === 'bar') {  // 柱状图
                    console.log('柱状图柱状图柱状图')

                    let dataList = [];
                    let titleList = [];

                    for (item of res.data) {
                        titleList.push(item['name']);
                        dataList.push(item['value']);
                    }

                    console.log(dataList, titleList)
                    let option = {
                        xAxis: {
                            data: titleList,
                            axisLabel: {rotate: 45, interval: 'auto'}
                        },
                        yAxis: {},
                        series: [
                            {
                                'name': name,
                                'type': 'bar',
                                'data': dataList,
                            }
                        ]
                    }
                    myChart.setOption(option);
                } else if (this.graphicType === 'line') {  // 折线图
                    console.log('折线图')

                    let dataList = [];
                    let titleList = [];

                    for (item of res.data) {
                        titleList.push(item['name']);
                        dataList.push(item['value']);
                    }

                    console.log(dataList, titleList)
                    let option = {
                        xAxis: {
                            data: titleList,
                            axisLabel: {rotate: 45, interval: 'auto'}
                        },
                        yAxis: {},
                        series: [
                            {
                                'name': name,
                                'type': 'line',
                                'data': dataList,
                            }
                        ]
                    }
                    myChart.setOption(option);
                }

            }).catch((err) => {
                console.log('into catch', err)
            })

        },
    },
    beforeMount: function () {
        this.getCheckBoxList();
    }
})