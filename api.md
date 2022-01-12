# Scrapex Scripts API <!-- GEN:version -->Tip-Of-Tree<!-- GEN:stop-->

<!-- GEN:empty-if-release --><!-- GEN:stop -->


<!-- prettier-ignore-start -->


<!-- prettier-ignore-end -->

##### Table of Contents

<!-- prettier-ignore-start -->

<!-- GEN:toc -->
- [Overview](#overview)
- [puppeteer vs puppeteer-core](#puppeteer-vs-puppeteer-core)
- [Environment Variables](#environment-variables)
- [Working with Chrome Extensions](#working-with-chrome-extensions)
- [class: Puppeteer](#class-puppeteer)
  * [puppeteer.clearCustomQueryHandlers()](#puppeteerclearcustomqueryhandlers)
  * [puppeteer.connect(options)](#puppeteerconnectoptions)
  * [puppeteer.createBrowserFetcher([options])](#puppeteercreatebrowserfetcheroptions)
  * [puppeteer.customQueryHandlerNames()](#puppeteercustomqueryhandlernames)
  * [puppeteer.defaultArgs([options])](#puppeteerdefaultargsoptions)
  * [puppeteer.devices](#puppeteerdevices)
  * [puppeteer.errors](#puppeteererrors)
  * [puppeteer.executablePath()](#puppeteerexecutablepath)
  * [puppeteer.launch([options])](#puppeteerlaunchoptions)
  * [puppeteer.networkConditions](#puppeteernetworkconditions)
  * [puppeteer.product](#puppeteerproduct)
  * [puppeteer.registerCustomQueryHandler(name, queryHandler)](#puppeteerregistercustomqueryhandlername-queryhandler)
  * [puppeteer.unregisterCustomQueryHandler(name)](#puppeteerunregistercustomqueryhandlername)
- [class: BrowserFetcher](#class-browserfetcher)
  * [browserFetcher.canDownload(revision)](#browserfetchercandownloadrevision)
  * [browserFetcher.download(revision[, progressCallback])](#browserfetcherdownloadrevision-progresscallback)
  * [browserFetcher.host()](#browserfetcherhost)
  * [browserFetcher.localRevisions()](#browserfetcherlocalrevisions)
  * [browserFetcher.platform()](#browserfetcherplatform)
  * [browserFetcher.product()](#browserfetcherproduct)
  * [browserFetcher.remove(revision)](#browserfetcherremoverevision)
  * [browserFetcher.revisionInfo(revision)](#browserfetcherrevisioninforevision)
- [class: Browser](#class-browser)
  * [event: 'disconnected'](#event-disconnected)
  * [event: 'targetchanged'](#event-targetchanged)
  * [event: 'targetcreated'](#event-targetcreated)
  * [event: 'targetdestroyed'](#event-targetdestroyed)
  * [browser.browserContexts()](#browserbrowsercontexts)
  * [browser.close()](#browserclose)
  * [browser.createIncognitoBrowserContext([options])](#browsercreateincognitobrowsercontextoptions)
  * [browser.defaultBrowserContext()](#browserdefaultbrowsercontext)
  * [browser.disconnect()](#browserdisconnect)
  * [browser.isConnected()](#browserisconnected)
  * [browser.newPage()](#browsernewpage)
  * [browser.pages()](#browserpages)
  * [browser.process()](#browserprocess)
  * [browser.target()](#browsertarget)
  * [browser.targets()](#browsertargets)
  * [browser.userAgent()](#browseruseragent)
  * [browser.version()](#browserversion)
  * [browser.waitForTarget(predicate[, options])](#browserwaitfortargetpredicate-options)
  * [browser.wsEndpoint()](#browserwsendpoint)
- [class: BrowserContext](#class-browsercontext)
  * [event: 'targetchanged'](#event-targetchanged-1)
  * [event: 'targetcreated'](#event-targetcreated-1)
  * [event: 'targetdestroyed'](#event-targetdestroyed-1)
  * [browserContext.browser()](#browsercontextbrowser)
  * [browserContext.clearPermissionOverrides()](#browsercontextclearpermissionoverrides)
  * [browserContext.close()](#browsercontextclose)
  * [browserContext.isIncognito()](#browsercontextisincognito)
  * [browserContext.newPage()](#browsercontextnewpage)
  * [browserContext.overridePermissions(origin, permissions)](#browsercontextoverridepermissionsorigin-permissions)
  * [browserContext.pages()](#browsercontextpages)
  * [browserContext.targets()](#browsercontexttargets)
  * [browserContext.waitForTarget(predicate[, options])](#browsercontextwaitfortargetpredicate-options)
- [class: Page](#class-page)
  * [event: 'close'](#event-close)
  * [event: 'console'](#event-console)
  * [event: 'dialog'](#event-dialog)
  * [event: 'domcontentloaded'](#event-domcontentloaded)
  * [event: 'error'](#event-error)
  * [event: 'frameattached'](#event-frameattached)
  * [event: 'framedetached'](#event-framedetached)
  * [event: 'framenavigated'](#event-framenavigated)
  * [event: 'load'](#event-load)
  * [event: 'metrics'](#event-metrics)
  * [event: 'pageerror'](#event-pageerror)
  * [event: 'popup'](#event-popup)
  * [event: 'request'](#event-request)
  * [event: 'requestfailed'](#event-requestfailed)
  * [event: 'requestfinished'](#event-requestfinished)
  * [event: 'response'](#event-response)
  * [event: 'workercreated'](#event-workercreated)
  * [event: 'workerdestroyed'](#event-workerdestroyed)
  * [page.$(selector)](#pageselector)
  * [page.$$(selector)](#pageselector-1)
  * [page.$$eval(selector, pageFunction[, ...args])](#pageevalselector-pagefunction-args)
  * [page.$eval(selector, pageFunction[, ...args])](#pageevalselector-pagefunction-args-1)
  * [page.$x(expression)](#pagexexpression)
  * [page.accessibility](#pageaccessibility)
  * [page.addScriptTag(options)](#pageaddscripttagoptions)
  * [page.addStyleTag(options)](#pageaddstyletagoptions)
  * [page.authenticate(credentials)](#pageauthenticatecredentials)
  * [page.bringToFront()](#pagebringtofront)
  * [page.browser()](#pagebrowser)
  * [page.browserContext()](#pagebrowsercontext)
  * [page.click(selector[, options])](#pageclickselector-options)
  * [page.close([options])](#pagecloseoptions)
  * [page.content()](#pagecontent)
  * [page.cookies([...urls])](#pagecookiesurls)
  * [page.coverage](#pagecoverage)
  * [page.createPDFStream([options])](#pagecreatepdfstreamoptions)
  * [page.deleteCookie(...cookies)](#pagedeletecookiecookies)
  * [page.emulate(options)](#pageemulateoptions)
  * [page.emulateCPUThrottling(factor)](#pageemulatecputhrottlingfactor)
  * [page.emulateIdleState(overrides)](#pageemulateidlestateoverrides)
  * [page.emulateMediaFeatures(features)](#pageemulatemediafeaturesfeatures)
  * [page.emulateMediaType(type)](#pageemulatemediatypetype)
  * [page.emulateNetworkConditions(networkConditions)](#pageemulatenetworkconditionsnetworkconditions)
  * [page.emulateTimezone(timezoneId)](#pageemulatetimezonetimezoneid)
  * [page.emulateVisionDeficiency(type)](#pageemulatevisiondeficiencytype)
  * [page.evaluate(pageFunction[, ...args])](#pageevaluatepagefunction-args)
  * [page.evaluateHandle(pageFunction[, ...args])](#pageevaluatehandlepagefunction-args)
  * [page.evaluateOnNewDocument(pageFunction[, ...args])](#pageevaluateonnewdocumentpagefunction-args)
  * [page.exposeFunction(name, puppeteerFunction)](#pageexposefunctionname-puppeteerfunction)
  * [page.focus(selector)](#pagefocusselector)
  * [page.frames()](#pageframes)
  * [page.goBack([options])](#pagegobackoptions)
  * [page.goForward([options])](#pagegoforwardoptions)
  * [page.goto(url[, options])](#pagegotourl-options)
  * [page.hover(selector)](#pagehoverselector)
  * [page.isClosed()](#pageisclosed)
  * [page.isDragInterceptionEnabled()](#pageisdraginterceptionenabled)
  * [page.isJavaScriptEnabled()](#pageisjavascriptenabled)
  * [page.keyboard](#pagekeyboard)
  * [page.mainFrame()](#pagemainframe)
  * [page.metrics()](#pagemetrics)
  * [page.mouse](#pagemouse)
  * [page.pdf([options])](#pagepdfoptions)
  * [page.queryObjects(prototypeHandle)](#pagequeryobjectsprototypehandle)
  * [page.reload([options])](#pagereloadoptions)
  * [page.saveSnapshot(title)](#pagescreenshotoptions)
  * [page.select(selector, ...values)](#pageselectselector-values)
  * [page.waitFor(selectorOrFunctionOrTimeout[, options[, ...args]])](#pagewaitforselectororfunctionortimeout-options-args)
  * [page.waitForNavigation([options])](#pagewaitfornavigationoptions)
  * [page.waitForSelector(selector[, options])](#pagewaitforselectorselector-options)
  * [page.waitForTag(scraper, tag[, options])](#pagewaitfortagelector-options)
  * [keyboard.down(key[, options])](#keyboarddownkey-options)
  * [keyboard.press(key[, options])](#keyboardpresskey-options)
  * [keyboard.sendCharacter(char)](#keyboardsendcharacterchar)
  * [keyboard.type(text[, options])](#keyboardtypetext-options)
  * [keyboard.up(key)](#keyboardupkey)
- [class: Mouse](#class-mouse)
  * [mouse.click(x, y[, options])](#mouseclickx-y-options)
  * [mouse.down([options])](#mousedownoptions)
  * [mouse.move(x, y[, options])](#mousemovex-y-options)
  * [mouse.up([options])](#mouseupoptions)
  * [mouse.wheel([options])](#mousewheeloptions)
<!-- GEN:stop -->

<!-- prettier-ignore-end -->

### Overview 

Scripts are executable crawlers that can perform some pre-configured automation along with scraping data from websites. Scripts can be accessed from the Scripts Table under Project details page under the Projects page.

Following are the attributes of a script:

- Script ID - unique ID for identifying each script
- Script Name - Customizable name for a script
- Script References - References to existing preset scrapers in scrapex that can be invoked in scripts using specific aliases
- Script Params - Run time parameters that have preset default (overridden) value.
- User Script - The driver logic for the user script.
<!-- 

- [`Puppeteer`](#class-puppeteer) communicates with the browser using [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/).
- [`Browser`](#class-browser) instance can own multiple browser contexts.
- [`BrowserContext`](#class-browsercontext) instance defines a browsing session and can own multiple pages.
- [`Page`](#class-page) has at least one frame: main frame. There might be other frames created by [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) or [frame](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/frame) tags.
- [`Frame`](#class-frame) has at least one execution context - the default execution context - where the frame's JavaScript is executed. A Frame might have additional execution contexts that are associated with [extensions](https://developer.chrome.com/extensions).
- [`Worker`](#class-worker) has a single execution context and facilitates interacting with [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). -->

### Sample user script


Here is an example of a user script: 
```js
let {newPage, end, except, extract, extractAndSave, store, runStore, waitFor} = __sandbox;
let {params, } = OPTIONS;
(async () => { try { //---> prefix
	// -- START --

	const page = await newPage()

	// CUSTOM LOGIC ON page ---> user script

	// -- END --
	end()
} catch(e) { except(e) } })(); // ---> suffix

```
Editing the user script can be achieved by using the script editor page. Only the logic part of the script is editable while suffix and prefix will be read only.

Here is a sample script that performs certain actions
```js
let {newPage, end, except, extract, extractAndSave, store, runStore, waitFor} = __sandbox;
let {params, } = OPTIONS;
(async () => { try {
	// -- START --

	const page = await newPage(); 	//creates new page
	await page.goto('https://www.example.org');	//opens example.org
	await store.saveOne('store', {id: 1, msg: 'data'})	//saves to store
	console.log(await store.getOne('store', 1))	//fetches from store
	if (await page.exists('a')) {	//check if anchor exists
		await page.click('a');	//click anchor
		await waitFor(2000);	//wait 2 seconds
		await page.saveSnapshot('clicked the anchor');	//save a snapshot of page

	}
	await page.close();	//close page

	// -- END --
	end()
} catch(e) { except(e) } })();
```

> **NOTE** On script errors, snapshots of all valid open pages are saved. If none were to be found, it's likely that the pages never had any context in the first place.

### Script Objects

- page: A page object is returned by invoking an awaited newPage() function. This object loads a webpage as well as interacts with it.
- references: A external reference to a scraper defined in scrapex so as to make use of the existing tag-based APIs.
- store: An outer level store that shares its inventory with other scripts in the same Project. This store is to be used when multiple script may be extracting data from different websites but the data accessed from one store for uniformity. Stores script specific data. This is the primary store choice.
- runStore: An inner level store that supposedly stores run-specific data. Although capable of storing all data, it is advised to use said store for debugging purposes as the use script has no access to stored data other than manually fetching the data by UI. It lacks the fetch APIs. 
- params: User parameters passed to the script that can be used to access passed values. This can be overridden in runtime to use non-default values.

### General functions

#### waitFor(timeout) 

Returns a promise waiting until timeout ms has passed. (Not page.waitFor)

- timeout <[number]> the amount of time in milliseconds to work
- Return <[Promise]> Promise that resolves after timeout milliseconds

#### newPage()

Returns a promise returning the page object. This spawns a new page object. The page will be a chromium tab instance. 

- Return <[Promise]<[Page]>> returns a Promise with a page object

#### end()

Terminates script.

- Return <[void]> terminates session

### extractAndSave(scraper, url[, idFn])

Extracts the scrapex scraper's data from the given url and saves it to the project-level store under the name of the scraper. 

- scraper <[string]> Name of scrapex scraper
- url <[string]> url to crawl
- idFn <[Function]> an ID generating function that creates the data ID
- Return <[Promise]> A promise that resolves to saving the extracted data

### class: Page

A page instance can be spawned in by using `await newPage()` call. Page provides methods to interact with a single tab in Chromium. You can spawn a maximum of two pages parallely in one user script.

This example creates a page, navigates it to a URL, and then saves a screenshot:

```js
  const page = await newPage();
  await page.goto('https://example.com');
  await page.saveSnapShot('example-page');
```

#### page.click(selector[, options])

Click an element on the page specified by its CSS selector.

- `selector` <[string]> A `selector` to search for element to click. If there are multiple elements satisfying the selector, the method throws.
- `options` <[Object]>
  - `button` <"left"|"right"|"middle"> Defaults to `left`.
  - `clickCount` <[number]> defaults to 1.
  - `delay` <[number]> Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
- returns: <[Promise]> Promise which resolves when the element matching `selector` is successfully clicked. The Promise will be rejected if there is no element matching `selector`.

This method fetches an element with `selector`, scrolls it into view if needed, and then uses [page.mouse](#pagemouse) to click in the center of the element.
If there's no element matching `selector`, the method throws an error.

Bear in mind that if `click()` triggers a navigation event and there's a separate `page.waitForNavigation()` promise to be resolved, you may end up with a race condition that yields unexpected results. The correct pattern for click and wait for navigation is the following:

```js
const [response] = await Promise.all([
  page.waitForNavigation(waitOptions),
  page.click(selector, clickOptions),
]);
```

> **NOTE** This race condition is handled by the `page.clickAndWait` API.

#### page.clickAndWait(selector[, options])

Click an element on the page specified by its CSS selector.

- `selector` <[string]> A `selector` to search for element to click. If there are multiple elements satisfying the selector, the method throws.
- `options` <[Object]> Navigation parameters which might have the following properties:
  - `timeout` <[number]> Maximum navigation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout) or [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) methods.
  - `waitUntil` <"load"|"domcontentloaded"|"networkidle0"|"networkidle2"|Array<PuppeteerLifeCycleMethod>> When to consider navigation succeeded, defaults to `load`. Given an array of event strings, navigation is considered to be successful after all events have been fired. Events can be either:
    - `load` - consider navigation to be finished when the `load` event is fired.
    - `domcontentloaded` - consider navigation to be finished when the `DOMContentLoaded` event is fired.
    - `networkidle0` - consider navigation to be finished when there are no more than 0 network connections for at least `500` ms.
    - `networkidle2` - consider navigation to be finished when there are no more than 2 network connections for at least `500` ms.
- returns: <[Promise]> Promise chain which resolves when the element matching `selector` is successfully clicked and then navigation is waited on. The Promise will be rejected if there is no element matching `selector`.

This method fetches an element with `selector`, scrolls it into view if needed, and then uses [page.mouse](#pagemouse) to click in the center of the element.
If there's no element matching `selector`, the method throws an error.

#### page.clickTag(scraper, tag[, options])

Click an element on the page specified by its CSS selector and wait for Navigation to finish.

- `scraper` <[string]]> A `scraper reference name` for the scrapex scraper configured using the references panel.
- `tag` <[string]> A `tag` to search for element to click in the `scraper`. If there are multiple elements satisfying the selector, the method throws.
- `options` <[Object]>
  - `button` <"left"|"right"|"middle"> Defaults to `left`.
  - `clickCount` <[number]> defaults to 1.
  - `delay` <[number]> Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
- returns: <[Promise]> Promise which resolves when the element matching `selector` is successfully clicked. The Promise will be rejected if there is no element matching `selector`.

This method fetches an element with `selector`, scrolls it into view if needed, and then uses [page.mouse](#pagemouse) to click in the center of the element.
If there's no element matching `selector`, the method throws an error.

Bear in mind that if `click()` triggers a navigation event and there's a separate `page.waitForNavigation()` promise to be resolved, you may end up with a race condition that yields unexpected results. The correct pattern for click and wait for navigation is the following:

```js
const [response] = await Promise.all([
  page.waitForNavigation(waitOptions),
  page.clickTag(scraper, tag, clickOptions),
]);
```

> **NOTE** This race condition is handled by the `page.clickTagAndWait` API.


#### page.clickTagAndWait(scraper, tag[, options])

Click an element on the page specified by its CSS selector and wait for Navigation to finish.

- `scraper` <[string]]> A `scraper reference name` for the scrapex scraper configured using the references panel.
- `tag` <[string]> A `tag` to search for element to click in the `scraper`. If there are multiple elements satisfying the selector, the method throws.
- `options` <[Object]> Navigation parameters which might have the following properties:
  - `timeout` <[number]> Maximum navigation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout) or [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) methods.
  - `waitUntil` <"load"|"domcontentloaded"|"networkidle0"|"networkidle2"|Array<PuppeteerLifeCycleMethod>> When to consider navigation succeeded, defaults to `load`. Given an array of event strings, navigation is considered to be successful after all events have been fired. Events can be either:
    - `load` - consider navigation to be finished when the `load` event is fired.
    - `domcontentloaded` - consider navigation to be finished when the `DOMContentLoaded` event is fired.
    - `networkidle0` - consider navigation to be finished when there are no more than 0 network connections for at least `500` ms.
    - `networkidle2` - consider navigation to be finished when there are no more than 2 network connections for at least `500` ms.
- returns: <[Promise]> Promise chain which resolves when the element matching `selector` is successfully clicked and then navigation is waited on. The Promise will be rejected if there is no element matching `selector`.

This method fetches an element with `selector`, scrolls it into view if needed, and then uses [page.mouse](#pagemouse) to click in the center of the element.
If there's no element matching `selector`, the method throws an error.


#### page.close([options])

Closes the specified tab.

- `options` <[Object]>
  - `runBeforeUnload` <[boolean]> Defaults to `false`. Whether to run the
    [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload)
    page handlers.
- returns: <[Promise]>

By default, `page.close()` **does not** run beforeunload handlers.

> **NOTE** if `runBeforeUnload` is passed as true, a `beforeunload` dialog might be summoned

#### page.exists(selector)

Checks if the specified selector exists on the page.

- `selector` <[string]> A `selector` to search for element to click. If there are multiple elements satisfying the selector, the method resolves if even one exists.
- returns: <[Promise]> Promise that resolve to either true or false depending upon the selectors existence on the page.

#### page.extract(scraper)

Extracts the content of the page.

- `name` <[string]> Name of the scraper reference
- returns: <[Promise]<[void]>> extracted text content of the value of the scraper.

#### page.goto(url[, options])

Go to the specified URL in the page that was spawned. options are wait and other nav options

- `url` <[string]> URL to navigate page to. The URL should include scheme, e.g. `https://`.
- `options` <[Object]> Navigation parameters which might have the following properties:
  - `timeout` <[number]> Maximum navigation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout) or [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) methods.
  - `waitUntil` <"load"|"domcontentloaded"|"networkidle0"|"networkidle2"|Array<PuppeteerLifeCycleMethod>> When to consider navigation succeeded, defaults to `load`. Given an array of event strings, navigation is considered to be successful after all events have been fired. Events can be either:
    - `load` - consider navigation to be finished when the `load` event is fired.
    - `domcontentloaded` - consider navigation to be finished when the `DOMContentLoaded` event is fired.
    - `networkidle0` - consider navigation to be finished when there are no more than 0 network connections for at least `500` ms.
    - `networkidle2` - consider navigation to be finished when there are no more than 2 network connections for at least `500` ms.
  - `referer` <[string]> Referer header value. If provided it will take preference over the referer header value set by [page.setExtraHTTPHeaders()](#pagesetextrahttpheadersheaders).
- returns: <[Promise]<?[HTTPResponse]>> Promise which resolves to the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect.

`page.goto` will throw an error if:

- there's an SSL error (e.g. in case of self-signed certificates).
- target URL is invalid.
- the `timeout` is exceeded during navigation.
- the remote server does not respond or is unreachable.
- the main resource failed to load.

`page.goto` will not throw an error when any valid HTTP status code is returned by the remote server, including 404 "Not Found" and 500 "Internal Server Error". The status code for such responses can be retrieved by calling [response.status()](#httpresponsestatus).

> **NOTE** `page.goto` either throws an error or returns a main resource response. The only exceptions are navigation to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.
page has JavaScript enabled, `false` otherwise.

#### page.keyboard

Invokes the keyboard object in page.

- returns: <[Keyboard]>

#### page.mouse

Invokes the mouse object in page.

- returns: <[Mouse]>

#### page.reload([options])

Reload the page. Options are waitOptions.

- `options` <[Object]> Navigation parameters which might have the following properties:
  - `timeout` <[number]> Maximum navigation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout) or [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) methods.
  - `waitUntil` <"load"|"domcontentloaded"|"networkidle0"|"networkidle2"|Array<PuppeteerLifeCycleMethod>> When to consider navigation succeeded, defaults to `load`. Given an array of event strings, navigation is considered to be successful after all events have been fired. Events can be either:
    - `load` - consider navigation to be finished when the `load` event is fired.
    - `domcontentloaded` - consider navigation to be finished when the `DOMContentLoaded` event is fired.
    - `networkidle0` - consider navigation to be finished when there are no more than 0 network connections for at least `500` ms.
    - `networkidle2` - consider navigation to be finished when there are no more than 2 network connections for at least `500` ms.
- returns: <[Promise]<[HTTPResponse]>> Promise which resolves to the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect.

#### page.saveSnapshot(name)

Saves the snapshot of the current page.

- `name` <[string]> Name of the snapshot
- returns: <[Promise]<[void]>> Promise which resolves to saving snapshot.

#### page.scrape(scraper)

Extracts the content of the page.

- `name` <[string]> Name of the scraper reference
- returns: <[Promise]<[void]>> extracted text content of the value of the scraper.

> **NOTE** This API is deprecated. Please check out the extract API.


#### page.scrapeSelector(selector[, options])

Extracts the content of the page by passing a barebone scraper.

- `selector` <[string]> selector to scrape on the page
- `options` <[Object]>: 
  - `required` <[boolean]> Whether it is a required tag
  - `type` <[string]> What type of tag it is. eg: standard,etc
  - `source_type` <[string]> Type of tag. dom/meta/builtin
  - `data_type` <[string]> What is the data type extracted. text,number, etc
  - `extractor` <[Object]>: 
    - `type` <[string]>: type/prop/attr
    - `name` <[string]>: href/etc
  - `modifers` <[Array]<[Object]>>: 
   -  `type` <[string]> regex/etc
    - `param` <[string]>: exp
- returns: <[Promise]<[void]>> extracted text content of the value of the scraper.

#### page.select(selector, ...values)

Select a checkbox on the page.

- `selector` <[string]> A [selector] to query page for
- `...values` <...[string]> Values of options to select. If the `<select>` has the `multiple` attribute, all values are considered, otherwise only the first one is taken into account.
- returns: <[Promise]<[Array]<[string]>>> An array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.
If there's no `<select>` element matching `selector`, the method throws an error.

```js
page.select('select#colors', 'blue'); // single selection
page.select('select#colors', 'red', 'green', 'blue'); // multiple selections
```

#### page.tagExists(scraper, tag)

Checks if the specified selector exists on the page.

- `scraper` <[string]]> A `scraper reference name` for the scrapex scraper configured using the references panel.
- `tag` <[string]> A `tag` to search for element to click in the `scraper`. If there are multiple elements satisfying the selector, the method resolves if even one exists.
- returns: <[Promise]> Promise that resolve to either true or false depending upon the selectors existence on the page.


#### page.waitFor(selectorOrFunctionOrTimeout[, options[, ...args]])

Explicit time wait on the page.

- `selectorOrFunctionOrTimeout` <[string]|[number]|[function]> A [selector], predicate or timeout to wait for
- `options` <[Object]> Optional waiting parameters
  - `visible` <[boolean]> wait for element to be present in DOM and to be visible. Defaults to `false`.
  - `timeout` <[number]> maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) method.
  - `hidden` <[boolean]> wait for element to not be found in the DOM or to be hidden. Defaults to `false`.
  - `polling` <[string]|[number]> An interval at which the `pageFunction` is executed, defaults to `raf`. If `polling` is a number, then it is treated as an interval in milliseconds at which the function would be executed. If `polling` is a string, then it can be one of the following values:
    - `raf` - to constantly execute `pageFunction` in `requestAnimationFrame` callback. This is the tightest polling mode which is suitable to observe styling changes.
    - `mutation` - to execute `pageFunction` on every DOM mutation.
- `...args` <...[Serializable]|[JSHandle]> Arguments to pass to `pageFunction`
- returns: <[Promise]<[JSHandle]>> Promise which resolves to a JSHandle of the success value

**This method is deprecated**. You should use the more explicit API methods available:

- `page.waitForSelector`
- `page.waitForXPath`
- `page.waitForFunction`
- `page.waitForTimeout`

This method behaves differently with respect to the type of the first parameter:

- if `selectorOrFunctionOrTimeout` is a `string`, then the first argument is treated as a [selector] or [xpath], depending on whether or not it starts with '//', and the method is a shortcut for
  [page.waitForSelector](#pagewaitforselectorselector-options) or [page.waitForXPath](#pagewaitforxpathxpath-options)
- if `selectorOrFunctionOrTimeout` is a `function`, then the first argument is treated as a predicate to wait for and the method is a shortcut for [page.waitForFunction()](#pagewaitforfunctionpagefunction-options-args).
- if `selectorOrFunctionOrTimeout` is a `number`, then the first argument is treated as a timeout in milliseconds and the method returns a promise which resolves after the timeout
- otherwise, an exception is thrown

```js
// wait for selector
await page.waitFor('.foo');
// wait for 1 second
await page.waitFor(1000);
// wait for predicate
await page.waitFor(() => !!document.querySelector('.foo'));
```

To pass arguments from node.js to the predicate of `page.waitFor` function:

```js
const selector = '.foo';
await page.waitFor(
  (selector) => !!document.querySelector(selector),
  {},
  selector
);
```

#### page.waitForNavigation([options])

Wait for page Navigation to finish.

- `options` <[Object]> Navigation parameters which might have the following properties:
  - `timeout` <[number]> Maximum navigation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout) or [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) methods.
  - `waitUntil` <"load"|"domcontentloaded"|"networkidle0"|"networkidle2"|Array<PuppeteerLifeCycleMethod>> When to consider navigation succeeded, defaults to `load`. Given an array of event strings, navigation is considered to be successful after all events have been fired. Events can be either:
    - `load` - consider navigation to be finished when the `load` event is fired.
    - `domcontentloaded` - consider navigation to be finished when the `DOMContentLoaded` event is fired.
    - `networkidle0` - consider navigation to be finished when there are no more than 0 network connections for at least `500` ms.
    - `networkidle2` - consider navigation to be finished when there are no more than 2 network connections for at least `500` ms.
- returns: <[Promise]<?[HTTPResponse]>> Promise which resolves to the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or navigation due to History API usage, the navigation will resolve with `null`.

This resolves when the page navigates to a new URL or reloads. It is useful when you run code
that will indirectly cause the page to navigate. Consider this example:

```js
const [response] = await Promise.all([
  page.waitForNavigation(), // The promise resolves after navigation has finished
  page.click('a.my-link'), // Clicking the link will indirectly cause a navigation
]);
```

#### page.waitForSelector(selector[, options])

Wait for selector to be available on the page.

- `selector` <[string]> A [selector] of an element to wait for. If there are multiple elements satisfying the selector, the method waits for all to finish.
- `options` <[Object]> Optional waiting parameters
  - `visible` <[boolean]> wait for element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties. Defaults to `false`.
  - `hidden` <[boolean]> wait for element to not be found in the DOM or to be hidden, i.e. have `display: none` or `visibility: hidden` CSS properties. Defaults to `false`.
  - `timeout` <[number]> maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) method.
- returns: <[Promise]<?[ElementHandle]>> Promise which resolves when element specified by selector string is added to DOM. Resolves to `null` if waiting for `hidden: true` and selector is not found in DOM.

Wait for the `selector` to appear in page. If at the moment of calling
the method the `selector` already exists, the method will return
immediately. If the selector doesn't appear after the `timeout` milliseconds of waiting, the function will throw.

This method works across navigations:

```js
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  let currentURL;
  page
    .waitForSelector('img')
    .then(() => console.log('First URL with image: ' + currentURL));
  for (currentURL of [
    'https://example.com',
    'https://google.com',
    'https://bbc.com',
  ]) {
    await page.goto(currentURL);
  }
  await browser.close();
})();
```

#### page.waitForTag(scraper, tag[, options])

Wait for selector to be available on the page, defined by a scrapex scraper. 

- `scraper` <[string]]> A `scraper reference name` for the scrapex scraper configured using the references panel.
- `tag` <[string]> A `tag` to search for element to click in the `scraper`. If there are multiple elements satisfying the selector, the method waits for all to finish.
- `options` <[Object]> Optional waiting parameters
  - `visible` <[boolean]> wait for element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties. Defaults to `false`.
  - `hidden` <[boolean]> wait for element to not be found in the DOM or to be hidden, i.e. have `display: none` or `visibility: hidden` CSS properties. Defaults to `false`.
  - `timeout` <[number]> maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout) method.
- returns: <[Promise]<?[ElementHandle]>> Promise which resolves when element specified by selector string is added to DOM. Resolves to `null` if waiting for `hidden: true` and selector is not found in DOM.

Wait for the `selector` to appear in page. If at the moment of calling
the method the `selector` already exists, the method will return
immediately. If the selector doesn't appear after the `timeout` milliseconds of waiting, the function will throw.

This method works across navigations:

```js
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  let currentURL;
  page
    .waitForSelector('img')
    .then(() => console.log('First URL with image: ' + currentURL));
  for (currentURL of [
    'https://example.com',
    'https://google.com',
    'https://bbc.com',
  ]) {
    await page.goto(currentURL);
  }
  await browser.close();
})();
```

**NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is considered a navigation.


### class: Keyboard

Keyboard provides an API for managing a virtual keyboard. The high-level API is [`keyboard.type`](#keyboardtypetext-options), which takes raw characters and generates proper keydown, keypress/input, and keyup events on your page.

For finer control, you can use [`keyboard.down`](#keyboarddownkey-options), [`keyboard.up`](#keyboardupkey), and [`keyboard.sendCharacter`](#keyboardsendcharacterchar) to manually fire events as if they were generated from a real keyboard.

An example of holding down `Shift` in order to select and delete some text:

```js
await page.keyboard.type('Hello World!');
await page.keyboard.press('ArrowLeft');

await page.keyboard.down('Shift');
for (let i = 0; i < ' World'.length; i++)
  await page.keyboard.press('ArrowLeft');
await page.keyboard.up('Shift');

await page.keyboard.press('Backspace');
// Result text will end up saying 'Hello!'
```

An example of pressing `A`

```js
await page.keyboard.down('Shift');
await page.keyboard.press('KeyA');
await page.keyboard.up('Shift');
```

> **NOTE** On macOS, keyboard shortcuts like `⌘ A` -> Select All does not work. See [#1313](https://github.com/puppeteer/puppeteer/issues/1313)

#### keyboard.down(key[, options])

- `key` <[string]> Name of key to press, such as `ArrowLeft`. See [USKeyboardLayout] for a list of all key names.
- `options` <[Object]>
  - `text` <[string]> If specified, generates an input event with this text.
- returns: <[Promise]>

Dispatches a `keydown` event.

If `key` is a single character and no modifier keys besides `Shift` are being held down, a `keypress`/`input` event will also be generated. The `text` option can be specified to force an input event to be generated.

If `key` is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that modifier active. To release the modifier key, use [`keyboard.up`](#keyboardupkey).

After the key is pressed once, subsequent calls to [`keyboard.down`](#keyboarddownkey-options) will have [repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key, use [`keyboard.up`](#keyboardupkey).

> **NOTE** Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

#### keyboard.press(key[, options])

- `key` <[string]> Name of key to press, such as `ArrowLeft`. See [USKeyboardLayout] for a list of all key names.
- `options` <[Object]>
  - `text` <[string]> If specified, generates an input event with this text.
  - `delay` <[number]> Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
- returns: <[Promise]>

If `key` is a single character and no modifier keys besides `Shift` are being held down, a `keypress`/`input` event will also be generated. The `text` option can be specified to force an input event to be generated.

> **NOTE** Modifier keys DO affect `keyboard.press`. Holding down `Shift` will type the text in upper case.

Shortcut for [`keyboard.down`](#keyboarddownkey-options) and [`keyboard.up`](#keyboardupkey).

#### keyboard.sendCharacter(char)

- `char` <[string]> Character to send into the page.
- returns: <[Promise]>

Dispatches a `keypress` and `input` event. This does not send a `keydown` or `keyup` event.

```js
page.keyboard.sendCharacter('嗨');
```

> **NOTE** Modifier keys DO NOT affect `keyboard.sendCharacter`. Holding down `Shift` will not type the text in upper case.

#### keyboard.type(text[, options])

- `text` <[string]> A text to type into a focused element.
- `options` <[Object]>
  - `delay` <[number]> Time to wait between key presses in milliseconds. Defaults to 0.
- returns: <[Promise]>

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use [`keyboard.press`](#keyboardpresskey-options).

```js
await page.keyboard.type('Hello'); // Types instantly
await page.keyboard.type('World', { delay: 100 }); // Types slower, like a user
```

> **NOTE** Modifier keys DO NOT affect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

#### keyboard.up(key)

- `key` <[string]> Name of key to release, such as `ArrowLeft`. See [USKeyboardLayout] for a list of all key names.
- returns: <[Promise]>

Dispatches a `keyup` event.

### class: Mouse

The Mouse class operates in main-frame CSS pixels relative to the top-left corner of the viewport.

Every `page` object has its own Mouse, accessible with [`page.mouse`](#pagemouse).

```js
// Using ‘page.mouse’ to trace a 100x100 square.
await page.mouse.move(0, 0);
await page.mouse.down();
await page.mouse.move(0, 100);
await page.mouse.move(100, 100);
await page.mouse.move(100, 0);
await page.mouse.move(0, 0);
await page.mouse.up();
```

Note that the mouse events trigger synthetic `MouseEvent`s.
This means that it does not fully replicate the functionality of what a normal user would be able to do with their mouse.


#### mouse.click(x, y[, options])

- `x` <[number]>
- `y` <[number]>
- `options` <[Object]>
  - `button` <"left"|"right"|"middle"> Defaults to `left`.
  - `clickCount` <[number]> defaults to 1. See [UIEvent.detail].
  - `delay` <[number]> Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
- returns: <[Promise]>

Shortcut for [`mouse.move`](#mousemovex-y-options), [`mouse.down`](#mousedownoptions) and [`mouse.up`](#mouseupoptions).

#### mouse.down([options])

- `options` <[Object]>
  - `button` <"left"|"right"|"middle"> Defaults to `left`.
  - `clickCount` <[number]> defaults to 1. See [UIEvent.detail].
- returns: <[Promise]>

Dispatches a `mousedown` event.

#### mouse.move(x, y[, options])

- `x` <[number]>
- `y` <[number]>
- `options` <[Object]>
  - `steps` <[number]> defaults to 1. Sends intermediate `mousemove` events.
- returns: <[Promise]>

Dispatches a `mousemove` event.

#### mouse.up([options])

- `options` <[Object]>
  - `button` <"left"|"right"|"middle"> Defaults to `left`.
  - `clickCount` <[number]> defaults to 1. See [UIEvent.detail].
- returns: <[Promise]>

Dispatches a `mouseup` event.

#### mouse.wheel([options])

- `options` <[Object]>
  - `deltaX` X delta in CSS pixels for mouse wheel event (default: 0). Positive values emulate a scroll right and negative values a scroll left event.
  - `deltaY` Y delta in CSS pixels for mouse wheel event (default: 0). Positive values emulate a scroll down and negative values a scroll up event.
- returns: <[Promise]>

Dispatches a `mousewheel` event.

Examples:

```js
await page.goto(
  'https://mdn.mozillademos.org/en-US/docs/Web/API/Element/wheel_event$samples/Scaling_an_element_via_the_wheel?revision=1587366'
);

const elem = await page.$('div');
const boundingBox = await elem.boundingBox();
await page.mouse.move(
  boundingBox.x + boundingBox.width / 2,
  boundingBox.y + boundingBox.height / 2
);

await page.mouse.wheel({ deltaY: -100 });
```



### class: Store

Scrapex stores data in collections and serves it to the user through the script or API as required. Store is an outer level store that shares its inventory with other scripts in the same Project. This store is to be used when multiple script may be extracting data from different websites but the data accessed from one store for uniformity.

Script store is the default store and the snippet below is a sample store interaction:


```js
  await store.saveOne('random-store', {id: 'some', data: 'other'});
  const data = await store.getOne('random-store', 'some');
```

#### store.getOne(collection, id)

Retrieves a single record from the store. 

- collection <[string]> Name of the collection in the store that has the data
- id <[string]> id of the data item that the user wishes to fetch
- return <[Promise]<[Object]>> Promise that resolves to the data item that was fetched as per user request

#### store.getAll(collection [, options])

Retrieves multiple records from the store. 

- collection <[string]> Name of the collection in the store that has the data
- options <[Object]> : 
 - limit <[string]> Limit of the amount of records fetched. Default is 50
 - offset <[string]> Offset of data origin. Default is 0
 - only <[Array]<[string]>> only fetch the following columns from the DB and not entire records. 
- return <[Promise]<[Array]<[Object]>>> Promise that resolves to all data items that was fetched as per user request

```js
  await store.getAll('store', {
    limit: 100,
    offset: 500,
    only:  ['id']
  })
```

#### store.saveOne(collection, data[, metadata, idFn])

Saves one data item into the store. 

- collection <[string]> Name of the collection in the store that has the data
- data <[Object]>: 
 - id <[string]> the unique identification keyword for the datum. It is required to store the data. Method throws if not passed.
 - [key] <[string]> data to be stored. 
- metadata <[Object]> the metadata of the object being stored
- idFn <[function]> An id generating function if required
- return <[Promise]> Promise that resolves to the data item being saved

Sample function: 
```js
  await store.saveOne('store', {data: "val"}, {metadata: 'json'}, () => {return 1;})
```

#### store.saveMany(collection, records)

Saves several data items into the store. 

- collection <[string]> Name of the collection in the store that has the data
- records <[Array]<[Object]>>: each record will be a data item with the following fields
 - id <[string]> the unique identification keyword for the datum. It is required to store the data. Method throws if not passed.
 - [key] <[string]> data to be stored. 
- idFn <[function]> An id generating function if required
- return <[Promise]> Promise that resolves to the data items being saved

### class: runStore

Scrapex stores data in collections and serves it to the user through the script or API as required. runStore is an inner level store that supposedly stores run-specific data. Although capable of storing all data, it is advised to use said store for debugging purposes as the use script has no access to stored data other than manually fetching the data by UI. It lacks the fetch APIs..

Run store lacks the get APIs but retains both save APIs the other stores have. 
The snippet below is a sample store interaction:


```js
  await runstore.saveOne('random-store', {id: 'some', data: 'other'});
  await runstore.saveMany('random-store', [{id: 'some2', data: 'other'}]);
```

#### runStore.saveOne(collection, data[, metadata, idFn])

Saves one data item into the run store. 

- collection <[string]> Name of the collection in the store that has the data
- data <[Object]>: 
 - id <[string]> the unique identification keyword for the datum. It is required to store the data. Method throws if not passed.
 - [key] <[string]> data to be stored. 
- metadata <[Object]> the metadata of the object being stored
- idFn <[function]> An id generating function if required
- return <[Promise]> Promise that resolves to the data item being saved

Sample function: 
```js
  await runstore.saveOne('store', {data: "val"}, {metadata: 'json'}, () => {return 1;})
```

#### runStore.saveMany(collection, records)

Saves several data items into the run store. 

- collection <[string]> Name of the collection in the store that has the data
- records <[Array]<[Object]>>: each record will be a data item with the following fields
 - id <[string]> the unique identification keyword for the datum. It is required to store the data. Method throws if not passed.
 - [key] <[string]> data to be stored. 
- idFn <[function]> An id generating function if required
- return <[Promise]> Promise that resolves to the data items being saved
