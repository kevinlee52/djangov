<template>
  <div>
    <div class="placeholder-container">
      <!--
      <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="Testcase Headline" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="add_testcase()" style="float:left; margin: 2px;">Add</el-button>
      </el-row>
      -->
      <div class="filter-container">
        <el-select v-model="listQuery.type" style="width: 300px; margin: 20px;" class="filter-item" @change="handleFilter">
          <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key" />
        </el-select>
      </div>
      <el-row>
        <el-table :data="caseList" style="width: 100%" border>
          <el-table-column label="Id" min-width="7">
            <template slot-scope="scope"> {{ scope.$index+1 }} </template>
          </el-table-column>
          <el-table-column prop="case_key" label="Case Key" min-width="50">
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="result" label="Result" min-width="11">
            <template slot-scope="scope"> {{ scope.row.fields.result }} </template>
          </el-table-column>
          <el-table-column prop="headline" label="Headline" min-width="70">
            <template slot-scope="scope"> {{ scope.row.fields.headline }} </template>
          </el-table-column>
          <el-table-column prop="timestamp" label="Timestamp" min-width="30">
            <template slot-scope="scope"> {{ scope.row.fields.timestamp }} </template>
          </el-table-column>
          <el-table-column prop="test_bed" label="Testbed" min-width="50">
            <template slot-scope="scope"> {{ scope.row.fields.test_bed }} </template>
          </el-table-column>
          <el-table-column prop="ci_online" label="Online" min-width="30">
            <template slot-scope="scope"> {{ scope.row.fields.ci_online }} </template>
          </el-table-column>
        </el-table>
      </el-row>
    </div>
    <el-tooltip placement="top" content="Back to top">
      <back-to-top :custom-style="myBackToTopStyle" :visibility-height="300" :back-position="50" transition-name="fade" />
    </el-tooltip>
  </div>
</template>

<script>
import { fetchList } from '@/api/djangoAPI'
import BackToTop from '@/components/BackToTop'
export default {
  name: 'CaselistDemo',
  components: { BackToTop },
  data() {
    return {
      input: '',
      baseUrl: 'http://10.245.243.229:8000',
      caseList: [],
      sortOptions: [{ label: 'GP1100X', key: 'gp1100x' }, { label: 'GS4227 XGS', key: 'gs4227_xgs' }],
      listQuery: {
        page: 1,
        limit: 20,
        importance: undefined,
        title: undefined,
        type: 'gp1100x',
        sort: '+id'
      },
      myBackToTopStyle: {
        right: '50px',
        bottom: '50px',
        width: '40px',
        height: '40px',
        'border-radius': '4px',
        'line-height': '45px', // Please keep consistent with height to center vertically
        background: '#e7eaf1'// The background color of the button
      }
    }
  },
  created: function() {
    this.show_testcases(this.listQuery.type)
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      // this.getList()
      this.show_testcases(this.listQuery.type)
    },
    add_testcase() {
      this.$http.get(this.baseUrl + '/api/add_testcase?headline=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.respCode === '20000') {
            this.show_testcases()
          } else {
            this.$message.error('Failed to add, please contact support.')
            console.log(res['respMsg'])
          }
        })
    },
    show_testcases(type) {
      this.$http.get(this.baseUrl + '/api/show_testcases_' + type)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.respCode === '20000') {
            this.caseList = res['list']
          } else {
            this.$message.error('Failed to show case list, please contact support.')
            console.log(res['respMsg'])
          }
        })
    }
  }
}
</script>

<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  .placeholder-container div {
    margin: 3px;
  }
  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
