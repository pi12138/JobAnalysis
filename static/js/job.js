let jobApp = new Vue({
    el: "#job-app",
    data: {
        items: [
            {
                'jobName': '岗位名称',
                'company': {
                    'id': 1,
                    'name': '公司名称'
                },
                'salary': '1000k',
                'location': '地球村',
                'workExperience': '1000年',
                'education': '本科',
                'skillLabel': [
                    {'name': '技能标签1', 'id': 1},
                    {'name': '技能标签2'},
                    {'name': '技能标签3'},
                ],
                'welfareLabel': [
                    {'name': '福利标签1'},
                    {'name': '福利标签2'},
                    {'name': '福利标签3'},
                ]
            }
        ],
        jobName: '',
        companyName: '',
        jobDirection: '',
    },
    methods: {
        setItems: function (response_data){
             this.items = [];
                for (let item of response_data) {
                    this.items.push({
                        'jobName': item.name,
                        'company': item['company'],
                        'salary': item['salary'],
                        'location': item['location'],
                        'workExperience': item['work_experience'],
                        'education': item['education'],
                        'skillLabel': item['skill_label'],
                        'welfareLabel': item['welfare_label']
                    });
                }
        },

        getJobList: function () { // 获取职位列表
            let url = '/api/job-position/';
            axios.get(url).then((response) => {
                console.log('into then');
                let result = response.data;
                this.setItems(result.results)

            }).catch((error) => {
                console.log('into catch')
                console.log(error)
            })
        },

        getCompanyName: function (company){ // 获取公司名称
            let name = '';
            if (company){
                name = company.name;
            }
            return name
        },

        searchJob: function (){ // 搜索岗位
            let queryParams = {}
            if (this.jobName){
                queryParams['job_name'] = this.jobName;
            }
            if (this.companyName){
                queryParams['company_name'] = this.companyName;
            }

            let url = '/api/job-position/';

            axios.get(url, {
                'params': queryParams
            }).then((response) => {
                console.log('into then');
                let result = response.data;
                this.setItems(result.results)

            }).catch((error) => {

            })
        }
    },

    beforeMount: function (){
        this.getJobList()
    }
})