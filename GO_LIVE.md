# OpenAPIHub - 从上线到盈利的剩余步骤

站点已经完全上线，所有不需要用户身份的代码工作已完成。下面是从"站点
存在"到"站点赚钱"之间，唯一还需要你做的事。每一步都标了预计时间和
对收入的影响。

**当前状态**: 站点在线 (https://openapihub.410185103.workers.dev)，
变现框架完整 (广告/联盟/sponsor/捐赠/邮件)，SEO 完成，社交分享预览
图就位。收入 = $0，因为流量 = 0。

---

## 第 1 步：产生第一批反向链接（最高优先级，~20 分钟）

这是整个项目从"被动等待"变成"主动获取流量"的开关。没有反向链接，
Google 不会给一个新站排名，流量永远是 0。

### 1a. 发一篇 dev.to 文章（最重要）

1. 打开 https://dev.to，点 Sign Up（GitHub 登录最快，免费）
2. 登录后点右上角 **Create Post**
3. 打开这个文件，全选复制：
   `site/scripts/publish/best-free-apis-2026.md`
4. 粘贴到 dev.to 编辑器。文件开头的 --- 块会自动变成标题、标签、
   canonical URL
5. 点 **Publish**

dev.to 文章里的链接是指向你站点的 dofollow 反向链接。一篇像样的
技术清单文在 dev.to 通常能拿 2000-10000 阅读，这是第一批真实流量
+ 第一个高质量反向链接。

### 1b. 发到 Hashnode（可选，重复 1a 的步骤）

https://hashnode.com，同样粘贴同一篇文章。多一个 dofollow 反向链接。

### 1c. 提交到 Hacker News（可选，高方差）

https://news.ycombinator.com/submit
链接填：https://openapihub.410185103.workers.dev/best-free-apis-2026
标题建议："Show HN: I catalogued 1581 free public APIs"

---

## 第 2 步：打开赞助付款通道（让 sponsor 页能收钱，~10 分钟）

现在 /sponsor 页的购买按钮是"发邮件"，摩擦太大。注册一个收款账户
后，按钮会变成即时付款。

### 注册 Buy Me a Coffee（推荐，最简单）

1. 打开 https://www.buymeacoffee.com
2. 用邮箱注册（免费，不需要信用卡）
3. 完成个人资料后，复制你的页面 URL
   （类似 https://www.buymeacoffee.com/yourname）
4. 告诉我这个 URL，我帮你设成环境变量 SPONSOR_BMC
   （或者自己在 Cloudflare Workers 的环境变量里加）

完成后，/sponsor 页的三个套餐按钮会变成"Claim ... via Buy Me a
Coffee"，访客点一下就能付款。BMC 支持信用卡 / PayPal，收款打到你的
BMC 账户，提现到 PayPal 或银行。

---

## 第 3 步：打开邮件捕获（把访客变成长期资产，~10 分钟）

现在首页没有邮件订阅框（因为还没配 NEWSLETTER_FORM_URL）。

### 注册 Buttondown（免费，最适合开发者受众）

1. 打开 https://buttondown.email
2. 注册（免费，邮箱即可）
3. 创建一个 newsletter
4. 进 Settings，找到 form action URL
   （类似 https://buttondown.email/api/emails/subscribe/...）
5. 告诉我这个 URL，我帮你设成 NEWSLETTER_FORM_URL

完成后，首页和 best-of 页会出现订阅卡片。每多一个订阅者，就是一
个未来能反复触达的长期读者——这是开发者站点 ROI 最高的资产。

---

## 第 4 步：打开搜索流量闸门（~10 分钟，需要 Google 账号）

让 Google 开始收录站点的 1637 个页面。

1. 打开 https://search.google.com/search-console
2. 用 Google 账号登录
3. 添加属性，URL 填：https://openapihub.410185103.workers.dev
4. 验证方式选"HTML 标签"或"DNS"——如果 workers.dev 子域验证有困难，
   告诉我，我帮你查替代方案
5. 验证通过后，提交 sitemap：
   https://openapihub.410185103.workers.dev/sitemap.xml

完成后 Google 会开始爬取。1637 个页面通常 2-6 周开始出现在搜索结果。

---

## 第 5 步：看流量从哪来（~5 分钟）

### 开启 Cloudflare Web Analytics（免费，无 Cookie）

1. 打开 https://dash.cloudflare.com
2. 左侧菜单找 **Web Analytics**
3. 点 **Add a site**，填 openapihub.410185103.workers.dev
4. 它会给你一个 token（在生成的 beacon 代码里）
5. 告诉我这个 token，我帮你设成 CF_ANALYTICS_TOKEN

完成后你能看到每天多少访客、从哪来、看哪些页面。没有这个就是盲飞。

---

## 时间投入建议

如果只有 30 分钟：做第 1a 步（发 dev.to 文章）。这是投入产出比最高
的一步。

如果有 1 小时：1a + 2（dev.to + Buy Me a Coffee）。

如果想要完整闭环：全部 5 步，约 1 小时。

---

## 已经完成的部分（你不需要再做）

- 站点上线，1637 个页面，全部 SEO 优化
- 5 个变现渠道的代码框架（广告/联盟/sponsor/捐赠/邮件）
- RSS 订阅源、best-of 编辑精选页、详情页相关 API
- GitHub 仓库优化（10 个 topics，README，live demo 链接）
- 3 个公开 Gist（weather/crypto/countries，dofollow 反向链接）
- 社交分享预览图（og:image + summary_large_image）
- 结构化 sitemap.xml + FAQ schema

每一步的验证记录都在 git 提交历史里。
