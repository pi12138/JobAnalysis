let navbarApp = new Vue({
    el: '#navbarApp',
    data: {
        navbarName: '岗位列表',
        navbarList: [
            {
                name: '岗位列表',
                url: '/job/',

            },
            {
                name: '数据分析',
                url: '/echarts/',

            }
        ],
        active: '岗位列表',
    },

    methods: {
        selectNavbar(name){
            this.active = name;
        }
    }
})