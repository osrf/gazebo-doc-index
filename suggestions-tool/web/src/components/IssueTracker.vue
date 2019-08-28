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
          <!-- <input type="checkbox" id="jack" :value="issue.id" v-model="checkedIssues"> -->
          <a :href="issue.links.html.href" target="blank"><b>#{{issue.id}}</b></a>
          <br><br>
          <span v-if="showTitle">
            <b>Issue-title: </b>{{issue.title}}<br>
          </span>
          <span v-if="showContent">
            <b>Issue-content: </b>{{issue.content.raw}}<br>
          </span>
          <span v-if="showKeywords">
            <b>Title and description keywords: </b><span v-if="issue.keywords.length>0" v-for="(keyw,indx) in issue.keywords" :key="indx" style="background: rgba(221, 183, 189, 0.5);margin:3px;line-height:25px;padding:2px;border-radius:5px">{{keyw}}</span>
          </span>
          </div>
          <br>
          <div>Covered in:
            <select v-model="issue.index_category">
              <option selected :value=undefined> -- Select category -- </option>
              <option v-for="(category,id) in category_list" :key="id" :value="category">{{category}}</option>
            </select>
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
      <div v-if="status" style="color: #42BA94;text-align:center">{{status_msg}}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'IssueTracker',
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
      status: false,
      error: false,
      errorMsg: '',
      category_list: [],
      status_msg: ''
    }
  },
  methods: {
    update () {
      // eslint-disable-next-line
      Array.prototype.diff = function (a) {
        return this.filter(function (i) { return a.indexOf(i) < 0 })
      }

      var that = this
      var tmp = this.issues.filter(function (el) {
        return (Object.keys(el).indexOf('index_category') !== -1 && el.index_category !== undefined)
      })
      var nowMarked = (tmp.map(el => el.id))
      var nowMarkedCategories = (tmp.map(function (el) {
        return { id: el.id, index_category: el.index_category }
      }))

      var changedCatsArrObj = []
      this.marked.forEach(function (el) {
        var found = that.issues.find(er => er.id === el[0])
        if (found) {
          if (el[1] !== found.index_category) {
            changedCatsArrObj.push({id: el[0], new_category: found.index_category})
          }
        }
      })

      var newlyMarked = nowMarked.diff(this.checkedIssues)
      var newlyMarkedArrObj = nowMarkedCategories.filter(el => newlyMarked.includes(el.id))
      if (newlyMarkedArrObj.length > 0 || changedCatsArrObj.length > 0) {
        axios.post(this.url + '/update', {newly_marked: newlyMarkedArrObj, changed_categories: changedCatsArrObj})
          .then(data => {
            setTimeout(this.refresh, 300)
            that.status = true
            that.status_msg = 'Successfuly updated!'
          })
          .catch(error => console.error(error))
      } else {
        that.status = true
        that.status_msg = 'There are no changes to update!'
      }
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
    if (process.env.NODE_ENV === 'development') {
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
        that.category_list = data.category_list
        that.issues = data.values
        that.page = data.page
        that.marked = data.bb_completed
        for (var issue in that.issues) {
          var tmp
          if (data.bb_completed.find(function (el) {
            tmp = el[1]
            return el[0] === that.issues[issue].id
          })) {
            that.checkedIssues.push(that.issues[issue].id)
            that.issues[issue].index_category = tmp
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

.update-msg {
  text-align: center;
  margin:4%;
  font-size: 18px;
}

.update-msg > button {
  margin-bottom: 3%;
}

</style>
