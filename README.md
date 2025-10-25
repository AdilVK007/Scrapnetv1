<!--<img src="https://i.imgur.com/UJh4QKS.png">-->

# SCRAPNET [WEB PROJECT] 🚗

The car scrapping process in India lacks organization compared to the sale of used cars. Transactions involving vehicles, primarily buying and selling, pose challenges in terms of tracking. Existing solutions using centralized systems face issues with transparency, trust, and access control. Deceptive practices by scrap dealers, such as fixing unfair prices, further complicate the process.



<!--[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
![Bitbucket open issues ](https://img.shields.io/bitbucket/issues/AdilVK007/Scrapnetv1)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/AdilVK007/Scrapnetv1/latest)
![GitHub Watchers](https://img.shields.io/github/watchers/AdilVK007/Scrapnetv1)-->
![Python](https://img.shields.io/badge/Python-3776AB?logo=Python&logoColor=white)
<!--![GitHub commit merge status](https://img.shields.io/github/commit-status/AdilVK007/Scrapnetv1/main/Myapp)
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCnLxjDIxr3tyZ9axvrJOITw?logo=youtube)-->


## Used versions and Softwares
- python Version = 3.6+ ![Python build](https://img.shields.io/badge/python-3.6-3.10-green)
- Framework = Django
- pycharm
- SQLyog
- [Ganache](https://archive.trufflesuite.com/docs/) (For blockchain)


<!---## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://lgrp.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammed-adil-7671a3231/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/a4techmalayalam/)-->

## Installation
To install Scrapnet, you can use the following steps:

```Copy code
# Clone the repository
git clone https://github.com/AdilVK007/Scrapnetv1.git
# Navigate into the project directory
cd scrapnet.
```


## Usage
Changes mades on the models which can be affecting the database

After updating models you can use this to update data
```
python3 manage.py makemigrations
```
```
{location python currently used version} manage.py makemigrations
```
```
{location python currently used version} manage.py migrate
```

Make config variables with ganache (Blockchain)

Ganache config
```
truffle migarations
```
```
truffle compile
```
After compilation create a work spece in ganache and do bc process as blocks every process as blocks , blocks are memory spaces for every process

<!--## __Documentation__
html table responsive


```html
<table class="table table-bordered">
    <tr>
        <td><input type="text" name="textfield" class="form-control"/></td>
        <td><input type="submit" value="search" class="btn btn-info"/></td>
    </tr>
</table>
```
Any feild should needs
Eg:
```
<div class="mb-3">
    <label for="password" class="form-label">Password</label>
    <input type="password" class="form-control" id="password" required>
</div>
```
-->

## Features

- Damage Detection and Price Prediction:

    Utilizing an Extreme Gradient Boosting model for accurate predictions (89.96% accuracy).
    Helping car owners realize the actual worth of their vehicles without being deceived.
- Transparent Transaction Process:

    Blockchain ensures transparency, trust, and access control in the scrapping process.
- Scrapping Certificate:

    A certificate is generated and issued to owners of scrapped cars.
    Owners can avail discounts when purchasing a new car, promoting the scrapping of old and pollution-causing cars.

## Legal notice


[License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
```
MIT License

Copyright YEAR COPYRIGHT-HOLDER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Contributing

Contributions are always welcome!

Please adhere to this project's `code of conduct`.

We welcome contributions from the community!

To contribute to Scrapnet:

Fork the repository.
Create a new branch
```
git checkout -b feature-branch
```
Commit your changes 
```
git commit -m 'Add new feature'
```
Push the branch 
```
git push origin feature-branch
```
Open a pull request.

> [!NOTE]
> Always welcoming pull requests and issues.

<!--- > [!TIP]
> Please suggest your ideas and implenatations.-->

# Planned features

- RTO submitting the details and auto genarate a certificate to the User.
- Changes on UI/UX 
