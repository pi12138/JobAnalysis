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
        jobCount: 0,
        nextPage: '',
        previousPage: '',
        currentPageNumber: 1,
        jumpPageNumber: 1,
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
        setJobCount: function (count){
            this.jobCount = 0;
            this.jobCount = count;
        },
        setPreviousAndNextPage: function (previousPage, nextPage){
            this.previousPage = previousPage;
            this.nextPage = nextPage;
        },
        setPageElement: function (result){
                this.setItems(result.results);
                this.setJobCount(result.count);
                this.setPreviousAndNextPage(result.previous, result.next);
        },

        getJobList: function (pageUrl) { // 获取职位列表
            let url = pageUrl;
            if (!url){
                return
            }
            if (url.indexOf('page') === -1){
                url = url + '?page=1';
                console.log(url)
            }

            axios.get(url).then((response) => {
                console.log('into then');
                let result = response.data;
                this.setPageElement(result);
                let splitArray = url.split('=')
                this.currentPageNumber = splitArray[splitArray.length - 1]

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
                this.setPageElement(result)

            }).catch((error) => {

            })
        },
    },

    computed: {
        countStr: function (){
            return `一共有${this.jobCount}条数据`
        },
        jumpPageUrl: function (){
            return `/api/job-position/?page=${this.jumpPageNumber}`
        }
    },

    beforeMount: function (){
        let pageUrl = `/api/job-position/?page=${this.currentPageNumber}`
        this.getJobList(pageUrl)
    }
})