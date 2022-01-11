# Puppeteer API <!-- GEN:version -->Tip-Of-Tree<!-- GEN:stop-->

<!-- GEN:empty-if-release --><!-- GEN:stop -->

- Interactive Documentation: https://pptr.dev
- API Translations: [中文|Chinese](https://zhaoqize.github.io/puppeteer-api-zh_CN/#/)
- Troubleshooting: [troubleshooting.md](https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md)

<!-- prettier-ignore-start -->

<!-- GEN:versions-per-release -->
- Releases per Chromium version:
  * Chromium 97.0.4692.0 - [Puppeteer v12.0.0](https://github.com/puppeteer/puppeteer/blob/v12.0.0/docs/api.md)
  * Chromium 93.0.4577.0 - [Puppeteer v10.2.0](https://github.com/puppeteer/puppeteer/blob/v10.2.0/docs/api.md)
  * Chromium 92.0.4512.0 - [Puppeteer v10.0.0](https://github.com/puppeteer/puppeteer/blob/v10.0.0/docs/api.md)
  * Chromium 91.0.4469.0 - [Puppeteer v9.0.0](https://github.com/puppeteer/puppeteer/blob/v9.0.0/docs/api.md)
  * Chromium 90.0.4427.0 - [Puppeteer v8.0.0](https://github.com/puppeteer/puppeteer/blob/v8.0.0/docs/api.md)
  * Chromium 90.0.4403.0 - [Puppeteer v7.0.0](https://github.com/puppeteer/puppeteer/blob/v7.0.0/docs/api.md)
  * Chromium 89.0.4389.0 - [Puppeteer v6.0.0](https://github.com/puppeteer/puppeteer/blob/v6.0.0/docs/api.md)
  * Chromium 88.0.4298.0 - [Puppeteer v5.5.0](https://github.com/puppeteer/puppeteer/blob/v5.5.0/docs/api.md)
  * Chromium 87.0.4272.0 - [Puppeteer v5.4.0](https://github.com/puppeteer/puppeteer/blob/v5.4.0/docs/api.md)
  * Chromium 86.0.4240.0 - [Puppeteer v5.3.0](https://github.com/puppeteer/puppeteer/blob/v5.3.0/docs/api.md)
  * Chromium 85.0.4182.0 - [Puppeteer v5.2.1](https://github.com/puppeteer/puppeteer/blob/v5.2.1/docs/api.md)
  * Chromium 84.0.4147.0 - [Puppeteer v5.1.0](https://github.com/puppeteer/puppeteer/blob/v5.1.0/docs/api.md)
  * Chromium 83.0.4103.0 - [Puppeteer v3.1.0](https://github.com/puppeteer/puppeteer/blob/v3.1.0/docs/api.md)
  * Chromium 81.0.4044.0 - [Puppeteer v3.0.0](https://github.com/puppeteer/puppeteer/blob/v3.0.0/docs/api.md)
  * Chromium 80.0.3987.0 - [Puppeteer v2.1.0](https://github.com/puppeteer/puppeteer/blob/v2.1.0/docs/api.md)
  * Chromium 79.0.3942.0 - [Puppeteer v2.0.0](https://github.com/puppeteer/puppeteer/blob/v2.0.0/docs/api.md)
  * Chromium 78.0.3882.0 - [Puppeteer v1.20.0](https://github.com/puppeteer/puppeteer/blob/v1.20.0/docs/api.md)
  * Chromium 77.0.3803.0 - [Puppeteer v1.19.0](https://github.com/puppeteer/puppeteer/blob/v1.19.0/docs/api.md)
  * Chromium 76.0.3803.0 - [Puppeteer v1.17.0](https://github.com/puppeteer/puppeteer/blob/v1.17.0/docs/api.md)
  * Chromium 75.0.3765.0 - [Puppeteer v1.15.0](https://github.com/puppeteer/puppeteer/blob/v1.15.0/docs/api.md)
  * Chromium 74.0.3723.0 - [Puppeteer v1.13.0](https://github.com/puppeteer/puppeteer/blob/v1.13.0/docs/api.md)
  * Chromium 73.0.3679.0 - [Puppeteer v1.12.2](https://github.com/puppeteer/puppeteer/blob/v1.12.2/docs/api.md)
  * [All releases](https://github.com/puppeteer/puppeteer/releases)
<!-- GEN:stop -->

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
  * [page.screenshot([options])](#pagescreenshotoptions)
  * [page.select(selector, ...values)](#pageselectselector-values)
  * [page.setBypassCSP(enabled)](#pagesetbypasscspenabled)
  * [page.setCacheEnabled([enabled])](#pagesetcacheenabledenabled)
  * [page.setContent(html[, options])](#pagesetcontenthtml-options)
  * [page.setCookie(...cookies)](#pagesetcookiecookies)
  * [page.setDefaultNavigationTimeout(timeout)](#pagesetdefaultnavigationtimeouttimeout)
  * [page.setDefaultTimeout(timeout)](#pagesetdefaulttimeouttimeout)
  * [page.setDragInterception(enabled)](#pagesetdraginterceptionenabled)
  * [page.setExtraHTTPHeaders(headers)](#pagesetextrahttpheadersheaders)
  * [page.setGeolocation(options)](#pagesetgeolocationoptions)
  * [page.setJavaScriptEnabled(enabled)](#pagesetjavascriptenabledenabled)
  * [page.setOfflineMode(enabled)](#pagesetofflinemodeenabled)
  * [page.setRequestInterception(value)](#pagesetrequestinterceptionvalue)
    - [Multiple Intercept Handlers and Asynchronous Resolutions](#multiple-intercept-handlers-and-asynchronous-resolutions)
    - [Cooperative Intercept Mode](#cooperative-intercept-mode)
    - [Cooperative Request Continuation](#cooperative-request-continuation)
    - [Upgrading to Cooperative Intercept Mode for package maintainers](#upgrading-to-cooperative-intercept-mode-for-package-maintainers)
  * [page.setUserAgent(userAgent[, userAgentMetadata])](#pagesetuseragentuseragent-useragentmetadata)
  * [page.setViewport(viewport)](#pagesetviewportviewport)
  * [page.tap(selector)](#pagetapselector)
  * [page.target()](#pagetarget)
  * [page.title()](#pagetitle)
  * [page.touchscreen](#pagetouchscreen)
  * [page.tracing](#pagetracing)
  * [page.type(selector, text[, options])](#pagetypeselector-text-options)
  * [page.url()](#pageurl)
  * [page.viewport()](#pageviewport)
  * [page.waitFor(selectorOrFunctionOrTimeout[, options[, ...args]])](#pagewaitforselectororfunctionortimeout-options-args)
  * [page.waitForFileChooser([options])](#pagewaitforfilechooseroptions)
  * [page.waitForFrame(urlOrPredicate[, options])](#pagewaitforframeurlorpredicate-options)
  * [page.waitForFunction(pageFunction[, options[, ...args]])](#pagewaitforfunctionpagefunction-options-args)
  * [page.waitForNavigation([options])](#pagewaitfornavigationoptions)
  * [page.waitForNetworkIdle([options])](#pagewaitfornetworkidleoptions)
  * [page.waitForRequest(urlOrPredicate[, options])](#pagewaitforrequesturlorpredicate-options)
  * [page.waitForResponse(urlOrPredicate[, options])](#pagewaitforresponseurlorpredicate-options)
  * [page.waitForSelector(selector[, options])](#pagewaitforselectorselector-options)
  * [page.waitForTimeout(milliseconds)](#pagewaitfortimeoutmilliseconds)
  * [page.waitForXPath(xpath[, options])](#pagewaitforxpathxpath-options)
  * [page.workers()](#pageworkers)
  * [GeolocationOptions](#geolocationoptions)
  * [WaitTimeoutOptions](#waittimeoutoptions)
- [class: WebWorker](#class-webworker)
  * [webWorker.evaluate(pageFunction[, ...args])](#webworkerevaluatepagefunction-args)
  * [webWorker.evaluateHandle(pageFunction[, ...args])](#webworkerevaluatehandlepagefunction-args)
  * [webWorker.executionContext()](#webworkerexecutioncontext)
  * [webWorker.url()](#webworkerurl)
- [class: Accessibility](#class-accessibility)
  * [accessibility.snapshot([options])](#accessibilitysnapshotoptions)
- [class: Keyboard](#class-keyboard)
  * [keyboard.down(key[, options])](#keyboarddownkey-options)
  * [keyboard.press(key[, options])](#keyboardpresskey-options)
  * [keyboard.sendCharacter(char)](#keyboardsendcharacterchar)
  * [keyboard.type(text[, options])](#keyboardtypetext-options)
  * [keyboard.up(key)](#keyboardupkey)
- [class: Mouse](#class-mouse)
  * [mouse.click(x, y[, options])](#mouseclickx-y-options)
  * [mouse.down([options])](#mousedownoptions)
  * [mouse.drag(start, target)](#mousedragstart-target)
  * [mouse.dragAndDrop(start, target[, options])](#mousedraganddropstart-target-options)
  * [mouse.dragEnter(target, data)](#mousedragentertarget-data)
  * [mouse.dragOver(target, data)](#mousedragovertarget-data)
  * [mouse.drop(target, data)](#mousedroptarget-data)
  * [mouse.move(x, y[, options])](#mousemovex-y-options)
  * [mouse.up([options])](#mouseupoptions)
  * [mouse.wheel([options])](#mousewheeloptions)
- [class: Touchscreen](#class-touchscreen)
  * [touchscreen.tap(x, y)](#touchscreentapx-y)
- [class: Tracing](#class-tracing)
  * [tracing.start([options])](#tracingstartoptions)
  * [tracing.stop()](#tracingstop)
- [class: FileChooser](#class-filechooser)
  * [fileChooser.accept(filePaths)](#filechooseracceptfilepaths)
  * [fileChooser.cancel()](#filechoosercancel)
  * [fileChooser.isMultiple()](#filechooserismultiple)
- [class: Dialog](#class-dialog)
  * [dialog.accept([promptText])](#dialogacceptprompttext)
  * [dialog.defaultValue()](#dialogdefaultvalue)
  * [dialog.dismiss()](#dialogdismiss)
  * [dialog.message()](#dialogmessage)
  * [dialog.type()](#dialogtype)
- [class: ConsoleMessage](#class-consolemessage)
  * [consoleMessage.args()](#consolemessageargs)
  * [consoleMessage.location()](#consolemessagelocation)
  * [consoleMessage.stackTrace()](#consolemessagestacktrace)
  * [consoleMessage.text()](#consolemessagetext)
  * [consoleMessage.type()](#consolemessagetype)
- [class: Frame](#class-frame)
  * [frame.$(selector)](#frameselector)
  * [frame.$$(selector)](#frameselector-1)
  * [frame.$$eval(selector, pageFunction[, ...args])](#frameevalselector-pagefunction-args)
  * [frame.$eval(selector, pageFunction[, ...args])](#frameevalselector-pagefunction-args-1)
  * [frame.$x(expression)](#framexexpression)
  * [frame.addScriptTag(options)](#frameaddscripttagoptions)
  * [frame.addStyleTag(options)](#frameaddstyletagoptions)
  * [frame.childFrames()](#framechildframes)
  * [frame.click(selector[, options])](#frameclickselector-options)
  * [frame.content()](#framecontent)
  * [frame.evaluate(pageFunction[, ...args])](#frameevaluatepagefunction-args)
  * [frame.evaluateHandle(pageFunction[, ...args])](#frameevaluatehandlepagefunction-args)
  * [frame.executionContext()](#frameexecutioncontext)
  * [frame.focus(selector)](#framefocusselector)
  * [frame.goto(url[, options])](#framegotourl-options)
  * [frame.hover(selector)](#framehoverselector)
  * [frame.isDetached()](#frameisdetached)
  * [frame.isOOPFrame()](#frameisoopframe)
  * [frame.name()](#framename)
  * [frame.parentFrame()](#frameparentframe)
  * [frame.select(selector, ...values)](#frameselectselector-values)
  * [frame.setContent(html[, options])](#framesetcontenthtml-options)
  * [frame.tap(selector)](#frametapselector)
  * [frame.title()](#frametitle)
  * [frame.type(selector, text[, options])](#frametypeselector-text-options)
  * [frame.url()](#frameurl)
  * [frame.waitFor(selectorOrFunctionOrTimeout[, options[, ...args]])](#framewaitforselectororfunctionortimeout-options-args)
  * [frame.waitForFunction(pageFunction[, options[, ...args]])](#framewaitforfunctionpagefunction-options-args)
  * [frame.waitForNavigation([options])](#framewaitfornavigationoptions)
  * [frame.waitForSelector(selector[, options])](#framewaitforselectorselector-options)
  * [frame.waitForTimeout(milliseconds)](#framewaitfortimeoutmilliseconds)
  * [frame.waitForXPath(xpath[, options])](#framewaitforxpathxpath-options)
- [class: ExecutionContext](#class-executioncontext)
  * [executionContext.evaluate(pageFunction[, ...args])](#executioncontextevaluatepagefunction-args)
  * [executionContext.evaluateHandle(pageFunction[, ...args])](#executioncontextevaluatehandlepagefunction-args)
  * [executionContext.frame()](#executioncontextframe)
  * [executionContext.queryObjects(prototypeHandle)](#executioncontextqueryobjectsprototypehandle)
- [class: JSHandle](#class-jshandle)
  * [jsHandle.asElement()](#jshandleaselement)
  * [jsHandle.dispose()](#jshandledispose)
  * [jsHandle.evaluate(pageFunction[, ...args])](#jshandleevaluatepagefunction-args)
  * [jsHandle.evaluateHandle(pageFunction[, ...args])](#jshandleevaluatehandlepagefunction-args)
  * [jsHandle.executionContext()](#jshandleexecutioncontext)
  * [jsHandle.getProperties()](#jshandlegetproperties)
  * [jsHandle.getProperty(propertyName)](#jshandlegetpropertypropertyname)
  * [jsHandle.jsonValue()](#jshandlejsonvalue)
- [class: ElementHandle](#class-elementhandle)
  * [elementHandle.$(selector)](#elementhandleselector)
  * [elementHandle.$$(selector)](#elementhandleselector-1)
  * [elementHandle.$$eval(selector, pageFunction[, ...args])](#elementhandleevalselector-pagefunction-args)
  * [elementHandle.$eval(selector, pageFunction[, ...args])](#elementhandleevalselector-pagefunction-args-1)
  * [elementHandle.$x(expression)](#elementhandlexexpression)
  * [elementHandle.asElement()](#elementhandleaselement)
  * [elementHandle.boundingBox()](#elementhandleboundingbox)
  * [elementHandle.boxModel()](#elementhandleboxmodel)
  * [elementHandle.click([options])](#elementhandleclickoptions)
  * [elementHandle.clickablePoint([offset])](#elementhandleclickablepointoffset)
  * [elementHandle.contentFrame()](#elementhandlecontentframe)
  * [elementHandle.dispose()](#elementhandledispose)
  * [elementHandle.drag(target)](#elementhandledragtarget)
  * [elementHandle.dragAndDrop(target[, options])](#elementhandledraganddroptarget-options)
  * [elementHandle.dragEnter([data])](#elementhandledragenterdata)
  * [elementHandle.dragOver([data])](#elementhandledragoverdata)
  * [elementHandle.drop([data])](#elementhandledropdata)
  * [elementHandle.evaluate(pageFunction[, ...args])](#elementhandleevaluatepagefunction-args)
  * [elementHandle.evaluateHandle(pageFunction[, ...args])](#elementhandleevaluatehandlepagefunction-args)
  * [elementHandle.executionContext()](#elementhandleexecutioncontext)
  * [elementHandle.focus()](#elementhandlefocus)
  * [elementHandle.getProperties()](#elementhandlegetproperties)
  * [elementHandle.getProperty(propertyName)](#elementhandlegetpropertypropertyname)
  * [elementHandle.hover()](#elementhandlehover)
  * [elementHandle.isIntersectingViewport([options])](#elementhandleisintersectingviewportoptions)
  * [elementHandle.jsonValue()](#elementhandlejsonvalue)
  * [elementHandle.press(key[, options])](#elementhandlepresskey-options)
  * [elementHandle.screenshot([options])](#elementhandlescreenshotoptions)
  * [elementHandle.select(...values)](#elementhandleselectvalues)
  * [elementHandle.tap()](#elementhandletap)
  * [elementHandle.toString()](#elementhandletostring)
  * [elementHandle.type(text[, options])](#elementhandletypetext-options)
  * [elementHandle.uploadFile(...filePaths)](#elementhandleuploadfilefilepaths)
  * [elementHandle.waitForSelector(selector[, options])](#elementhandlewaitforselectorselector-options)
- [class: HTTPRequest](#class-httprequest)
  * [httpRequest.abort([errorCode], [priority])](#httprequestaborterrorcode-priority)
  * [httpRequest.abortErrorReason()](#httprequestaborterrorreason)
  * [httpRequest.continue([overrides], [priority])](#httprequestcontinueoverrides-priority)
  * [httpRequest.continueRequestOverrides()](#httprequestcontinuerequestoverrides)
  * [httpRequest.enqueueInterceptAction(pendingHandler)](#httprequestenqueueinterceptactionpendinghandler)
  * [httpRequest.failure()](#httprequestfailure)
  * [httpRequest.finalizeInterceptions()](#httprequestfinalizeinterceptions)
  * [httpRequest.frame()](#httprequestframe)
  * [httpRequest.headers()](#httprequestheaders)
  * [httpRequest.initiator()](#httprequestinitiator)
  * [httpRequest.interceptResolutionState()](#httprequestinterceptresolutionstate)
  * [httpRequest.isInterceptResolutionHandled()](#httprequestisinterceptresolutionhandled)
  * [httpRequest.isNavigationRequest()](#httprequestisnavigationrequest)
  * [httpRequest.method()](#httprequestmethod)
  * [httpRequest.postData()](#httprequestpostdata)
  * [httpRequest.redirectChain()](#httprequestredirectchain)
  * [httpRequest.resourceType()](#httprequestresourcetype)
  * [httpRequest.respond(response, [priority])](#httprequestrespondresponse-priority)
  * [httpRequest.response()](#httprequestresponse)
  * [httpRequest.responseForRequest()](#httprequestresponseforrequest)
  * [httpRequest.url()](#httprequesturl)
- [class: HTTPResponse](#class-httpresponse)
  * [httpResponse.buffer()](#httpresponsebuffer)
  * [httpResponse.frame()](#httpresponseframe)
  * [httpResponse.fromCache()](#httpresponsefromcache)
  * [httpResponse.fromServiceWorker()](#httpresponsefromserviceworker)
  * [httpResponse.headers()](#httpresponseheaders)
  * [httpResponse.json()](#httpresponsejson)
  * [httpResponse.ok()](#httpresponseok)
  * [httpResponse.remoteAddress()](#httpresponseremoteaddress)
  * [httpResponse.request()](#httpresponserequest)
  * [httpResponse.securityDetails()](#httpresponsesecuritydetails)
  * [httpResponse.status()](#httpresponsestatus)
  * [httpResponse.statusText()](#httpresponsestatustext)
  * [httpResponse.text()](#httpresponsetext)
  * [httpResponse.url()](#httpresponseurl)
- [class: SecurityDetails](#class-securitydetails)
  * [securityDetails.issuer()](#securitydetailsissuer)
  * [securityDetails.protocol()](#securitydetailsprotocol)
  * [securityDetails.subjectAlternativeNames()](#securitydetailssubjectalternativenames)
  * [securityDetails.subjectName()](#securitydetailssubjectname)
  * [securityDetails.validFrom()](#securitydetailsvalidfrom)
  * [securityDetails.validTo()](#securitydetailsvalidto)
- [class: Target](#class-target)
  * [target.browser()](#targetbrowser)
  * [target.browserContext()](#targetbrowsercontext)
  * [target.createCDPSession()](#targetcreatecdpsession)
  * [target.opener()](#targetopener)
  * [target.page()](#targetpage)
  * [target.type()](#targettype)
  * [target.url()](#targeturl)
  * [target.worker()](#targetworker)
- [class: CDPSession](#class-cdpsession)
  * [cdpSession.connection()](#cdpsessionconnection)
  * [cdpSession.detach()](#cdpsessiondetach)
  * [cdpSession.id()](#cdpsessionid)
  * [cdpSession.send(method[, ...paramArgs])](#cdpsessionsendmethod-paramargs)
- [class: Coverage](#class-coverage)
  * [coverage.startCSSCoverage([options])](#coveragestartcsscoverageoptions)
  * [coverage.startJSCoverage([options])](#coveragestartjscoverageoptions)
  * [coverage.stopCSSCoverage()](#coveragestopcsscoverage)
  * [coverage.stopJSCoverage()](#coveragestopjscoverage)
- [class: TimeoutError](#class-timeouterror)
- [class: EventEmitter](#class-eventemitter)
  * [eventEmitter.addListener(event, handler)](#eventemitteraddlistenerevent-handler)
  * [eventEmitter.emit(event, [eventData])](#eventemitteremitevent-eventdata)
  * [eventEmitter.listenerCount(event)](#eventemitterlistenercountevent)
  * [eventEmitter.off(event, handler)](#eventemitteroffevent-handler)
  * [eventEmitter.on(event, handler)](#eventemitteronevent-handler)
  * [eventEmitter.once(event, handler)](#eventemitteronceevent-handler)
  * [eventEmitter.removeAllListeners([event])](#eventemitterremovealllistenersevent)
  * [eventEmitter.removeListener(event, handler)](#eventemitterremovelistenerevent-handler)
- [interface: CustomQueryHandler](#interface-customqueryhandler)
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
```
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

> **NOTE** Additional configuration of references and params are required in some cases, which can be overridden in runtime.


### Script Objects

- page: A page object is returned by invoking an awaited newPage() function. This object loads a webpage as well as interacts with it.
- references: A external reference to a scraper defined in scrapex so as to make use of the existing tag-based APIs.
- store: An outer level store that shares its inventory with other scripts in the same Project. This store is to be used when multiple script may be extracting data from different websites but the data accessed from one store for uniformity. Stores script specific data. This is the primary store choice.
- runStore: An inner level store that supposedly stores run-specific data. Although capable of storing all data, it is advised to use said store for debugging purposes as the use script has no access to stored data other than manually fetching the data by UI. It lacks the fetch APIs. 
- params: User parameters passed to the script that can be used to access passed values. This can be overridden in runtime to use non-default values.

### General functions

- waitFor(timeout:number) - returns a promise waiting until timeout ms has passed. (Not page.waitFor)
- newPage() - returns a promise returning the page object. This spawns a new page object. The page will be a chromium tab instance. 
- end() [Not to be awaited] - terminates script.

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

#### page.clickTag(scraper, tag[, options])

Click an element on the page specified by its CSS selector.

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
  page.click(selector, clickOptions),
]);
```

#### page.close([options])

Closes the specified tab.

- `options` <[Object]>
  - `runBeforeUnload` <[boolean]> Defaults to `false`. Whether to run the
    [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload)
    page handlers.
- returns: <[Promise]>

By default, `page.close()` **does not** run beforeunload handlers.

> **NOTE** if `runBeforeUnload` is passed as true, a `beforeunload` dialog might be summoned

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

- `name` <[string]> Name of the snapshot
- returns: <[Promise]<[void]>> Promise which resolves to saving snapshot.


#### page.select(selector, ...values)

- `selector` <[string]> A [selector] to query page for
- `...values` <...[string]> Values of options to select. If the `<select>` has the `multiple` attribute, all values are considered, otherwise only the first one is taken into account.
- returns: <[Promise]<[Array]<[string]>>> An array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.
If there's no `<select>` element matching `selector`, the method throws an error.

```js
page.select('select#colors', 'blue'); // single selection
page.select('select#colors', 'red', 'green', 'blue'); // multiple selections
```

Shortcut for [page.mainFrame().select()](#frameselectselector-values)

#### page.waitForNavigation([options])

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
