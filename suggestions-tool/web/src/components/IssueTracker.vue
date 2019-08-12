<template>
  <div class="hello">
    <div style="margin-bottom: 10px">
      <button :disabled="(sort=='votes')||loading||error" @click="sortVoted()">SORT BY VOTED</button>
      <button :disabled="sort=='updated'||loading||error" @click="sortUpdated()">SORT BY UPDATED</button>
    </div>
    <div>
      <input type="checkbox" :disabled="loading||error" v-model="showTitle">
      Show title

      <input type="checkbox" :disabled="loading||error" v-model="showContent">
      Show content

      <input type="checkbox" :disabled="loading||error" v-model="showKeywords">
      Show keywords
    <span style="float:right;">
      <input type="button" :disabled="page==1||loading||error" value="Previous" v-on:click="previous()">
      <input type="button" :disabled="loading||error" value="Next" v-on:click="next()">
      <div style="margin-top: 5px">Page: {{page}}</div>
    </span>
    </div>
    <br>
    <ul v-for="issue in issues" :key="issue.id">
      <li>
        <div v-bind:style= "[marked.includes(issue.id)|| checkedIssues.includes(issue.id) ? {'color': 'lightgrey'} : {}]">
          <input type="checkbox" id="jack" :value="issue.id" v-model="checkedIssues">
          <a :href="issue.links.html.href" target="blank"><b>#{{issue.id}}</b></a>
          <br><br>
          <span v-if="showTitle">
            <b>Issue-title: </b>{{issue.title}}<br>
          </span>
          <span v-if="showContent">
            <b>Issue-content: </b>{{issue.content.raw}}<br>
          </span>
          <span v-if="showKeywords">
            <b>Title and description keywords: </b><span v-if="issue.keywords.length>0" v-for="keyw in issue.keywords" :key="keyw" style="background: rgba(221, 183, 189, 0.5);margin:3px;line-height:25px;padding:2px;border-radius:5px">{{keyw}}</span>
          </span>
          </div>
      </li><hr>
    </ul>
    <div v-if="loading" class="status">
      <b>Loading..Please wait</b>
    </div>
    <div v-if="error" class="status error">
      <b>{{errorMsg}}</b>
    </div>
    <div class="update-msg">
      <button :disabled="loading||error" v-if="!loading" v-on:click="update()" style="text-align:center">UPDATE COMPLETED ISSUES</button>
      <div v-if="success" style="color: #42BA94;text-align:center">Successfuly updated!</div>

    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      issues: [],
      checkedIssues: [],
      showTitle: true,
      showContent: false,
      showKeywords: true,
      url: '/issues',
      loading: true,
      page: null,
      marked: [],
      sort: null,
      success: false,
      error: false,
      errorMsg: ''
    }
  },
  methods: {
    update () {
      var newlyMarked = this.checkedIssues.filter(x => !this.marked.includes(x))
      var unmarked = this.marked.filter(x => !this.checkedIssues.includes(x) && this.issues.map(y => y.id).includes(x))
      console.log(unmarked)
      var that = this
      axios.post(this.url + '/update', {newly_marked: newlyMarked, unmarked: unmarked})
        .then(data => {
          console.log(data)
          setTimeout(this.refresh, 1000)
          that.success = true
        })
        .catch(error => console.error(error))
    },
    refresh () {
      this.$router.go()
    },
    next () {
      this.page += 1
      window.location.href = '?sort=' + this.sort + '&page=' + this.page
    },
    previous () {
      this.page -= 1
      window.location.href = '?sort=' + this.sort + '&page=' + this.page
    },
    sortVoted () {
      this.sort = 'votes'
      this.page = 1
      window.location.href = '?sort=' + this.sort
    },
    sortUpdated () {
      this.sort = 'updated'
      this.page = 1
      window.location.href = '?sort=' + this.sort
    }
  },
  created () {
    console.log()
    if (process.env.NODE_ENV == 'development') { // eslint-disable-line
      this.url = 'http://127.0.0.1:5000/issues'
    } else {
      this.url = '/issues'
    }
    var that = this
    if (typeof this.$route.query.page !== 'undefined') {
      this.page = this.$route.query.page
    } else {
      this.page = 1
    }

    if (typeof this.$route.query.sort !== 'undefined') {
      this.sort = this.$route.query.sort
    } else {
      this.sort = 'votes'
    }

    fetch(this.url + '?page=' + this.page + '&sort=' + this.sort)
      .then(response => response.json())
      .then(data => {
        that.issues = data.values
        that.page = data.page
        that.marked = data.bb_completed
        for (var issue in that.issues) {
          if (data.bb_completed.includes(that.issues[issue].id)) {
            console.log(that.issues[issue].id)
            that.checkedIssues.push(that.issues[issue].id)
          }
        }
        that.loading = false
      })
      .catch(err => {
        that.loading = false
        that.error = true
        that.errorMsg = err
        console.error(err)
      })
  },
  watch: {
    checkedIssues: () => {
      // console.log(this.checkedIssues)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
.status {
  margin: 10%;
}

.error {
  color: rgb(192, 38, 38);
}

.status-msg {
  margin-bottom: 10%
}
</style>
