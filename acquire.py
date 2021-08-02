"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
import pandas as pd

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

def get_repo_list():
    '''
    This function is designed to create a repo list from the most starred 
    repositories on github.
    
    The function loops through 20 pages with 10 results per page of the most 
    starred repos on github using a range from 1 to 21.
    
    It then uses another loop to pull out all the titles of each repo using 
    the beautiful soup library and html per page.
    '''
    ## setting up authentication headers
    headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}
    
    ## initializing blank list for appending the repo's pulled
    repo_list = []
    clean_repo_list = []
    
    ## creating a list with a range of 1 to 21 to loop through 20 pages x being the 
    ## page number in the url
    for x in range(1,21):
        response = requests.get(f'https://github.com/search?p={x}&q=stars%3A%3E0&s=stars&type=Repositories', 
                                headers = headers)
        html = response.content
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        title = soup.find_all(class_= 'v-align-middle') ## <-- where the repo titles lie in html
        time.sleep(15)
        
        ## looping through the string to append a list of repo titles
        for y in title:
            repo_list.append(y.get_text())
        
    ## looping through the repo list again to remove any null elements or white space
    for repo in repo_list:
        if (len(repo)) > 3:
            clean_repo_list.append(repo)     
        
    return clean_repo_list  

REPOS = [
    'freeCodeCamp/freeCodeCamp',
 '996icu/996.ICU',
 'EbookFoundation/free-programming-books',
 'jwasham/coding-interview-university',
 'vuejs/vue',
 'facebook/react',
 'kamranahmedse/developer-roadmap',
 'sindresorhus/awesome',
 'tensorflow/tensorflow',
 'twbs/bootstrap',
 'public-apis/public-apis',
 'getify/You-Dont-Know-JS',
 'donnemartin/system-design-primer',
 'CyC2018/CS-Notes',
 'ohmyzsh/ohmyzsh',
 'flutter/flutter',
 'github/gitignore',
 'microsoft/vscode',
 'torvalds/linux',
 'trekhleb/javascript-algorithms',
 'TheAlgorithms/Python',
 'danistefanovic/build-your-own-x',
 'airbnb/javascript',
 'Snailclimb/JavaGuide',
 'jackfrued/Python-100-Days',
 'vinta/awesome-python',
 'ytdl-org/youtube-dl',
 'd3/d3',
 'facebook/react-native',
 'electron/electron',
 'labuladong/fucking-algorithm',
 'jlevy/the-art-of-command-line',
 'ossu/computer-science',
 'facebook/create-react-app',
 'golang/go',
 'axios/axios',
 'justjavac/free-programming-books-zh_CN',
 '30-seconds/30-seconds-of-code',
 'nodejs/node',
 'kubernetes/kubernetes',
 'denoland/deno',
 'microsoft/terminal',
 'angular/angular',
 'ant-design/ant-design',
 'microsoft/TypeScript',
 'mrdoob/three.js',
 'puppeteer/puppeteer',
 'animate-css/animate.css',
 'vercel/next.js',
 'tensorflow/models',
 'mui-org/material-ui',
 'PanJiaChen/vue-element-admin',
 'goldbergyoni/nodebestpractices',
 'iluwatar/java-design-patterns',
 'avelino/awesome-go',
 'laravel/laravel',
 'MisterBooo/LeetCodeAnimation',
 'FortAwesome/Font-Awesome',
 'storybookjs/storybook',
 'nvbn/thefuck',
 'awesome-selfhosted/awesome-selfhosted',
 'vuejs/awesome-vue',
 'moby/moby',
 'angular/angular.js',
 'gothinkster/realworld',
 'webpack/webpack',
 'django/django',
 'microsoft/PowerToys',
 'tonsky/FiraCode',
 'rust-lang/rust',
 'bitcoin/bitcoin',
 'elastic/elasticsearch',
 'atom/atom',
 'opencv/opencv',
 'yangshun/tech-interview-handbook',
 'doocs/advanced-java',
 'netdata/netdata',
 'typicode/json-server',
 'thedaviddias/Front-End-Checklist',
 'jquery/jquery',
 'doocs/advanced-java',
 'netdata/netdata',
 'typicode/json-server',
 'thedaviddias/Front-End-Checklist',
 'jquery/jquery',
 'ryanmcdermott/clean-code-javascript',
 'chartjs/Chart.js',
 'socketio/socket.io',
 'expressjs/express',
 'xingshaocheng/architect-awesome',
 'tuvtran/project-based-learning',
 'kdn251/interviews',
 'gohugoio/hugo',
 'shadowsocks/shadowsocks-windows',
 'adam-p/markdown-here',
 'Genymobile/scrcpy',
 'keras-team/keras',
 'httpie/httpie',
 'macrozheng/mall',
 'chrislgarry/Apollo-11',
 'h5bp/html5-boilerplate',
 'gatsbyjs/gatsby',
 'josephmisiti/awesome-machine-learning',
 'ElemeFE/element',
 'redis/redis',
 'nvm-sh/nvm',
 'lodash/lodash',
 'gin-gonic/gin',
 'h5bp/Front-end-Developer-Interview-Questions',
 'pytorch/pytorch',
 'protocolbuffers/protobuf',
 'Semantic-Org/Semantic-UI',
 'resume/resume.github.com',
 'ansible/ansible',
 'huggingface/transformers',
 'sveltejs/svelte',
 'rails/rails',
 'ripienaar/free-for-dev',
 'kelseyhightower/nocode',
 'apache/echarts',
 'fatedier/frp',
 'trimstray/the-book-of-secret-knowledge',
 'papers-we-love/papers-we-love',
 'moment/moment',
 'neovim/neovim',
 'psf/requests',
 'awesomedata/awesome-public-datasets',
 'Hack-with-Github/Awesome-Hacking',
 'scutan90/DeepLearning-500-questions',
 '521xueweihan/HelloGitHub',
 'tailwindlabs/tailwindcss',
 'ionic-team/ionic-framework',
 'ReactiveX/RxJava',
 'jaywcjlove/awesome-mac',
 'mtdvio/every-programmer-should-know',
 'necolas/normalize.css',
 'home-assistant/core',
 'enaqx/awesome-react',
 'jgthms/bulma',
 'spring-projects/spring-framework',
 'ReactTraining/react-router',
 'google/material-design-icons',
 'azl397985856/leetcode',
 'grafana/grafana',
 'florinpop17/app-ideas',
 'jekyll/jekyll',
 'meteor/meteor',
 'leonardomso/33-js-concepts',
 'sindresorhus/awesome-nodejs',
 'google/guava',
 'DopplerHQ/awesome-interview-questions',
 'NARKOZ/hacker-scripts',
 'sdmg15/Best-websites-a-programmer-should-visit',
 'scrapy/scrapy',
 'tesseract-ocr/tesseract',
 'soimort/you-get',
 'wasabeef/awesome-android-ui',
 'minimaxir/big-list-of-naughty-strings',
 'aymericdamien/TensorFlow-Examples',
 'ageitgey/face_recognition',
 'godotengine/godot',
 'square/okhttp',
 'serverless/serverless',
 'prettier/prettier',
 'yarnpkg/yarn',
 'juliangarnier/anime',
 'TheAlgorithms/Java',
 'apache/superset',
 'babel/babel',
 'syncthing/syncthing',
 'python/cpython',
 'android/architecture-samples',
 'ColorlibHQ/AdminLTE',
 'nestjs/nest',
 'git/git',
 'parcel-bundler/parcel',
 'Dogfalo/materialize',
 'ziishaned/learn-regex',
 'square/retrofit',
 'nwjs/nw.js',
 'astaxie/build-web-application-with-golang',
 'JetBrains/kotlin',
 'junegunn/fzf',
 'TryGhost/Ghost',
 'vsouza/awesome-ios',
 'strapi/strapi',
 'deepfakes/faceswap',
 'prometheus/prometheus',
 'v2ray/v2ray-core',
 'prakhar1989/awesome-courses',
 'gogs/gogs',
 'nuxt/nuxt.js',
 'iptv-org/iptv',
 'x64dbg/x64dbg',
 'mermaid-js/mermaid',
 'k88hudson/git-flight-rules',
 'kon9chunkit/GitHub-Chinese-Top-Charts',
 'Solido/awesome-flutter'
    ]
 

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_contents = requests.get(get_readme_download_url(contents)).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data2.json", "w"), indent=1)
    
    
def get_github_data():
    '''
    this function will bring in our NLP_df.csv into a pandas dataframe. 
    it will also drop any duplicates, and reset the index
    '''
    df = pd.read_csv('NLP_df.csv', index_col=0)
    df = df.reset_index(drop=True)
    df = df.drop_duplicates()
    return df 