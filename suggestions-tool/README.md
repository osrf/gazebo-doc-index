# suggestions-tool
The directory contains code for a suggestions-tool application for suggesting doc-index entries that scrapes Bitbucket issues of Gazebo's repository, extracts keywords from the content and allows us to mark and store the issues that have already been added to the doc index. This will help us in tracking Bitbucket issues efficiently for adding entries to the doc index.

- Only basic styling has been implemented, which can be improved later.
- Currently only Bitbucket issues have been handled, support for GazeboAnswers can also be added.

**Frontend framework:** Vuejs
**Backend server:** Flask

To store the issues (IDs) that have already been used in the doc index are currently stored in an array in a local file (`bitbucket_issues_completed.txt`).

### Prerequisites' installation:

```
python3 -m pip install flask numpy rake-ntlk requests
```

### How to run locally:

```
cd gazebo-doc-index/suggestions-tool/web
npm install
npm run build
cd ../api
python3 app.py
```
### Preview:

![image](https://user-images.githubusercontent.com/24846546/61666459-29d06900-acf5-11e9-955f-aae5820e23a5.png)
