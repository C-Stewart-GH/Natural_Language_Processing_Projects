#Site wouldn't let me scrape so I copied all the outer html
amazon="""<html lang="en-us" class="a-js a-audio a-video a-canvas a-svg a-drag-drop a-geolocation a-history a-webworker a-autofocus a-input-placeholder a-textarea-placeholder a-local-storage a-gradients a-hires a-transform3d a-touch-scrolling a-text-shadow a-text-stroke a-box-shadow a-border-radius a-border-image a-opacity a-transform a-transition a-ember" data-19ax5a9jf="dingo" data-aui-build-date="3.21.9-2022-03-01"><!-- sp:feature:head-start --><head><script async="" src="https://images-na.ssl-images-amazon.com/images/I/31YXrY93hfL.js" crossorigin="anonymous"></script><script>var aPageStart = (new Date()).getTime();</script><meta charset="utf-8">
<!-- sp:end-feature:head-start -->

<script type="text/javascript">var ue_t0=ue_t0||+new Date();</script>
<!-- sp:feature:cs-optimization -->
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="https://images-na.ssl-images-amazon.com">
<link rel="dns-prefetch" href="https://m.media-amazon.com">
<link rel="dns-prefetch" href="https://completion.amazon.com">
<!-- sp:end-feature:cs-optimization -->
<script type="text/javascript">
window.ue_ihb = (window.ue_ihb || window.ueinit || 0) + 1;
if (window.ue_ihb === 1) {

var ue_csm = window,
    ue_hob = +new Date();
(function(d){var e=d.ue=d.ue||{},f=Date.now||function(){return+new Date};e.d=function(b){return f()-(b?0:d.ue_t0)};e.stub=function(b,a){if(!b[a]){var c=[];b[a]=function(){c.push([c.slice.call(arguments),e.d(),d.ue_id])};b[a].replay=function(b){for(var a;a=c.shift();)b(a[0],a[1],a[2])};b[a].isStub=1}};e.exec=function(b,a){return function(){try{return b.apply(this,arguments)}catch(c){ueLogError(c,{attribution:a||"undefined",logLevel:"WARN"})}}}})(ue_csm);


    var ue_err_chan = 'jserr-rw';
(function(d,e){function h(f,b){if(!(a.ec>a.mxe)&&f){a.ter.push(f);b=b||{};var c=f.logLevel||b.logLevel;c&&c!==k&&c!==m&&c!==n&&c!==p||a.ec++;c&&c!=k||a.ecf++;b.pageURL=""+(e.location?e.location.href:"");b.logLevel=c;b.attribution=f.attribution||b.attribution;a.erl.push({ex:f,info:b})}}function l(a,b,c,e,g){d.ueLogError({m:a,f:b,l:c,c:""+e,err:g,fromOnError:1,args:arguments},g?{attribution:g.attribution,logLevel:g.logLevel}:void 0);return!1}var k="FATAL",m="ERROR",n="WARN",p="DOWNGRADED",a={ec:0,ecf:0,
pec:0,ts:0,erl:[],ter:[],mxe:50,startTimer:function(){a.ts++;setInterval(function(){d.ue&&a.pec<a.ec&&d.uex("at");a.pec=a.ec},1E4)}};l.skipTrace=1;h.skipTrace=1;h.isStub=1;d.ueLogError=h;d.ue_err=a;e.onerror=l})(ue_csm,window);


var ue_id = 'Z0KMT1JTKBYN6W6QW6GJ',
    ue_url = '/rd/uedata',
    ue_navtiming = 1,
    ue_mid = 'ATVPDKIKX0DER',
    ue_sid = '130-0450696-1458362',
    ue_sn = 'www.amazon.com',
    ue_furl = 'fls-na.amazon.com',
    ue_surl = 'https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.prod',
    ue_int = 0,
    ue_fcsn = 1,
    ue_urt = 3,
    ue_rpl_ns = 'cel-rpl',
    ue_ddq = 1,
    ue_fpf = '//fls-na.amazon.com/1/batch/1/OP/ATVPDKIKX0DER:130-0450696-1458362:Z0KMT1JTKBYN6W6QW6GJ$uedata=s:',
    ue_sbuimp = 1,
    ue_cel_lclia = 1,
    ue_f_paint = 1,
    ue_ibft = 0,
    ue_sswmts = 0,
    ue_jsmtf = 0,
    ue_fnt = 0,

    ue_swi = 1;
var ue_viz=function(){(function(b,e,a){function k(c){if(b.ue.viz.length<p&&!l){var a=c.type;c=c.originalEvent;/^focus./.test(a)&&c&&(c.toElement||c.fromElement||c.relatedTarget)||(a=e[m]||("blur"==a||"focusout"==a?"hidden":"visible"),b.ue.viz.push(a+":"+(+new Date-b.ue.t0)),"visible"==a&&(b.ue.isl&&q("at"),l=1))}}for(var l=0,q=b.uex,f,g,m,n=["","webkit","o","ms","moz"],d=0,p=20,h=0;h<n.length&&!d;h++)if(a=n[h],f=(a?a+"H":"h")+"idden",d="boolean"==typeof e[f])g=a+"visibilitychange",m=(a?a+"V":"v")+
"isibilityState";k({});d&&e.addEventListener(g,k,0);b.ue&&d&&(b.ue.pageViz={event:g,propHid:f})})(ue_csm,ue_csm.document,ue_csm.window)};

(function(d,h,N){function H(a){return a&&a.replace&&a.replace(/^\s+|\s+$/g,"")}function u(a){return"undefined"===typeof a}function B(a,b){for(var c in b)b[v](c)&&(a[c]=b[c])}function I(a){try{var b=N.cookie.match(RegExp("(^| )"+a+"=([^;]+)"));if(b)return b[2].trim()}catch(c){}}function O(m,b,c){var q=(x||{}).type;if("device"!==c||2!==q&&1!==q)m&&(d.ue_id=a.id=a.rid=m,w&&(w=w.replace(/((.*?:){2})(\w+)/,function(a,b){return b+m})),D&&(e("id",D,m),D=0)),b&&(w&&(w=w.replace(/(.*?:)(\w|-)+/,function(a,
c){return c+b})),d.ue_sid=b),c&&a.tag("page-source:"+c),d.ue_fpf=w}function P(){var a={};return function(b){b&&(a[b]=1);b=[];for(var c in a)a[v](c)&&b.push(c);return b}}function y(d,b,c,q){q=q||+new E;var f,l;if(b||u(c)){if(d)for(l in f=b?e("t",b)||e("t",b,{}):a.t,f[d]=q,c)c[v](l)&&e(l,b,c[l]);return q}}function e(d,b,c){var e=b&&b!=a.id?a.sc[b]:a;e||(e=a.sc[b]={});"id"===d&&c&&(Q=1);return e[d]=c||e[d]}function R(d,b,c,e,f){c="on"+c;var l=b[c];"function"===typeof l?d&&(a.h[d]=l):l=function(){};b[c]=
function(a){f?(e(a),l(a)):(l(a),e(a))};b[c]&&(b[c].isUeh=1)}function S(m,b,c,q){function p(b,c){var d=[b],g=0,f={},l,h;c?(d.push("m=1"),f[c]=1):f=a.sc;for(h in f)if(f[v](h)){var q=e("wb",h),p=e("t",h)||{},n=e("t0",h)||a.t0,k;if(c||2==q){q=q?g++:"";d.push("sc"+q+"="+h);for(k in p)u(p[k])||null===p[k]||d.push(k+q+"="+(p[k]-n));d.push("t"+q+"="+p[m]);if(e("ctb",h)||e("wb",h))l=1}}!J&&l&&d.push("ctb=1");return d.join("&")}function l(b,c,g,e){if(b){var f=d.ue_err;d.ue_url&&!e&&b&&0<b.length&&(e=new Image,
a.iel.push(e),e.src=b,a.count&&a.count("postbackImageSize",b.length));if(w){var m=h.encodeURIComponent;m&&b&&(e=new Image,b=""+d.ue_fpf+m(b)+":"+(+new E-d.ue_t0),a.iel.push(e),e.src=b)}else a.log&&(a.log(b,"uedata",{n:1}),a.ielf.push(b));f&&!f.ts&&f.startTimer();a.b&&(f=a.b,a.b="",l(f,c,g,1))}}function A(b){var c=x?x.type:F,d=2==c||a.isBFonMshop,c=c&&!d,e=a.bfini;Q||(e&&1<e&&(b+="&bfform=1",c||(a.isBFT=e-1)),d&&(b+="&bfnt=1",a.isBFT=a.isBFT||1),a.ssw&&a.isBFT&&(a.isBFonMshop&&(a.isNRBF=0),u(a.isNRBF)&&
(d=a.ssw(a.oid),d.e||u(d.val)||(a.isNRBF=1<d.val?0:1)),u(a.isNRBF)||(b+="&nrbf="+a.isNRBF)),a.isBFT&&!a.isNRBF&&(b+="&bft="+a.isBFT));return b}if(!a.paused&&(b||u(c))){for(var k in c)c[v](k)&&e(k,b,c[k]);a.isBFonMshop||y("pc",b,c);k="ld"===m&&b&&e("wb",b);var s=e("id",b)||a.id;k||s===a.oid||(D=b,ba(s,(e("t",b)||{}).tc||+e("t0",b),+e("t0",b)));var s=e("id",b)||a.id,t=e("id2",b),g=a.url+"?"+m+"&v="+a.v+"&id="+s,J=e("ctb",b)||e("wb",b),z;J&&(g+="&ctb="+J);t&&(g+="&id2="+t);1<d.ueinit&&(g+="&ic="+d.ueinit);
if(!("ld"!=m&&"ul"!=m||b&&b!=s)){if("ld"==m){try{h[K]&&h[K].isUeh&&(h[K]=null)}catch(I){}if(h.chrome)for(t=0;t<L.length;t++)T(G,L[t]);(t=N.ue_backdetect)&&t.ue_back&&t.ue_back.value++;d._uess&&(z=d._uess());a.isl=1}a._bf&&(g+="&bf="+a._bf());d.ue_navtiming&&f&&(e("ctb",s,"1"),a.isBFonMshop||y("tc",F,F,M));!C||a.isBFonMshop||U||(f&&B(a.t,{na_:f.navigationStart,ul_:f.unloadEventStart,_ul:f.unloadEventEnd,rd_:f.redirectStart,_rd:f.redirectEnd,fe_:f.fetchStart,lk_:f.domainLookupStart,_lk:f.domainLookupEnd,
co_:f.connectStart,_co:f.connectEnd,sc_:f.secureConnectionStart,rq_:f.requestStart,rs_:f.responseStart,_rs:f.responseEnd,dl_:f.domLoading,di_:f.domInteractive,de_:f.domContentLoadedEventStart,_de:f.domContentLoadedEventEnd,_dc:f.domComplete,ld_:f.loadEventStart,_ld:f.loadEventEnd,ntd:("function"!==typeof C.now||u(M)?0:new E(M+C.now())-new E)+a.t0}),x&&B(a.t,{ty:x.type+a.t0,rc:x.redirectCount+a.t0}),U=1);a.isBFonMshop||B(a.t,{hob:d.ue_hob,hoe:d.ue_hoe});a.ifr&&(g+="&ifr=1")}y(m,b,c,q);var r,n;k||b&&
b!==s||ca(b);(c=d.ue_mbl)&&c.cnt&&!k&&(g+=c.cnt());k?e("wb",b,2):"ld"==m&&(a.lid=H(s));for(r in a.sc)if(1==e("wb",r))break;if(k){if(a.s)return;g=p(g,null)}else c=p(g,null),c!=g&&(c=A(c),a.b=c),z&&(g+=z),g=p(g,b||a.id);g=A(g);if(a.b||k)for(r in a.sc)2==e("wb",r)&&delete a.sc[r];z=0;a._rt&&(g+="&rt="+a._rt());c=h.csa;if(!k&&c)for(n in r=e("t",b)||{},c=c("PageTiming"),r)r[v](n)&&c("mark",da[n]||n,r[n]);k||(a.s=0,(n=d.ue_err)&&0<n.ec&&n.pec<n.ec&&(n.pec=n.ec,g+="&ec="+n.ec+"&ecf="+n.ecf),z=e("ctb",b),
"ld"!==m||b||a.markers?a.markers&&a.isl&&!k&&b&&B(a.markers,e("t",b)):(a.markers={},B(a.markers,e("t",b))),e("t",b,{}));a.tag&&a.tag().length&&(g+="&csmtags="+a.tag().join("|"),a.tag=P());n=a.viz||[];(r=n.length)&&(g+="&viz="+n.splice(0,r).join("|"));u(d.ue_pty)||(g+="&pty="+d.ue_pty+"&spty="+d.ue_spty+"&pti="+d.ue_pti);a.tabid&&(g+="&tid="+a.tabid);a.aftb&&(g+="&aftb=1");!a._ui||b&&b!=s||(g+=a._ui());a.a=g;l(g,m,z,k)}}function ca(a){var b=h.ue_csm_markers||{},c;for(c in b)b[v](c)&&y(c,a,F,b[c])}
function A(a,b,c){c=c||h;if(c[V])c[V](a,b,!1);else if(c[W])c[W]("on"+a,b)}function T(a,b,c){c=c||h;if(c[X])c[X](a,b,!1);else if(c[Y])c[Y]("on"+a,b)}function Z(){function a(){d.onUl()}function b(a){return function(){c[a]||(c[a]=1,S(a))}}var c={},e,f;d.onLd=b("ld");d.onLdEnd=b("ld");d.onUl=b("ul");e={stop:b("os")};h.chrome?(A(G,a),L.push(a)):e[G]=d.onUl;for(f in e)e[v](f)&&R(0,h,f,e[f]);d.ue_viz&&ue_viz();A("load",d.onLd);y("ue")}function ba(e,b,c){var f=d.ue_mbl,p=h.csa,l=p&&p("SPA"),p=p&&p("PageTiming");
f&&f.ajax&&f.ajax(b,c);l&&p&&(l("newPage",{requestId:e,transitionType:"soft"}),p("mark","transitionStart",b));a.tag("ajax-transition")}d.ueinit=(d.ueinit||0)+1;var a=d.ue=d.ue||{};a.t0=h.aPageStart||d.ue_t0;a.id=d.ue_id;a.url=d.ue_url;a.rid=d.ue_id;a.a="";a.b="";a.h={};a.s=1;a.t={};a.sc={};a.iel=[];a.ielf=[];a.viz=[];a.v="0.223038.0";a.paused=!1;var v="hasOwnProperty",G="beforeunload",K="on"+G,V="addEventListener",X="removeEventListener",W="attachEvent",Y="detachEvent",da={cf:"criticalFeature",af:"aboveTheFold",
fn:"functional",fp:"firstPaint",fcp:"firstContentfulPaint",bb:"bodyBegin",be:"bodyEnd",ld:"loaded"},E=h.Date,C=h.performance||h.webkitPerformance,f=(C||{}).timing,x=(C||{}).navigation,M=(f||{}).navigationStart,w=d.ue_fpf,Q=0,U=0,L=[],D=0,F;a.oid=H(a.id);a.lid=H(a.id);a._t0=a.t0;a.tag=P();a.ifr=h.top!==h.self||h.frameElement?1:0;a.markers=null;a.attach=A;a.detach=T;if("000-0000000-8675309"===d.ue_sid){var $=I("cdn-rid"),aa=I("session-id");$&&aa&&O($,aa,"cdn")}d.uei=Z;d.ueh=R;d.ues=e;d.uet=y;d.uex=
S;a.reset=O;a.pause=function(d){a.paused=d};Z()})(ue_csm,ue_csm.window,ue_csm.document);


ue.stub(ue,"event");ue.stub(ue,"onSushiUnload");ue.stub(ue,"onSushiFlush");

ue.stub(ue,"log");ue.stub(ue,"onunload");ue.stub(ue,"onflush");
(function(c){var a=c.ue;a.cv={};a.cv.scopes={};a.count=function(d,c,b){var e={},f=a.cv,g=b&&0===b.c;e.counter=d;e.value=c;e.t=a.d();b&&b.scope&&(f=a.cv.scopes[b.scope]=a.cv.scopes[b.scope]||{},e.scope=b.scope);if(void 0===c)return f[d];f[d]=c;d=0;b&&b.bf&&(d=1);ue_csm.ue_sclog||!a.clog||0!==d||g?a.log&&a.log(e,"csmcount",{c:1,bf:d}):a.clog(e,"csmcount",{bf:d})};a.count("baselineCounter2",1);a&&a.event&&(a.event({requestId:c.ue_id||"rid",server:c.ue_sn||"sn",obfuscatedMarketplaceId:c.ue_mid||"mid"},
"csm","csm.CSMBaselineEvent.4"),a.count("nexusBaselineCounter",1,{bf:1}))})(ue_csm);



var ue_hoe = +new Date();
}
window.ueinit = window.ue_ihb;
</script>

<!-- 18zb7zh4nvq64vzrj1xsysfs14z3nyvcve8avr76vgm3q2 -->
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 9723)</script>
<!-- sp:feature:aui-assets -->
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/11EIQ5IGqaL._RC|01ZTHTZObnL.css,41wZkyTaWoL.css,31Y8m1dzTdL.css,013z33uKh2L.css,017DsKjNQJL.css,0131vqwP5UL.css,41EWOOlBJ9L.css,11TIuySqr6L.css,01ElnPiDxWL.css,11bGSgD5pDL.css,01Dm5eKVxwL.css,01IdKcBuAdL.css,01y-XAlI+2L.css,21N4kUH7pxL.css,01oDR3IULNL.css,41CYNGpGlrL.css,01XPHJk60-L.css,114y0SIP+yL.css,21aPhFy+riL.css,11gneA3MtJL.css,21fecG8pUzL.css,01ulGzBW88L.css,01CFUgsA-YL.css,31C80IiXalL.css,11qour3ND0L.css,11gKCCKQV+L.css,11061HxnEvL.css,11oHt2HYxnL.css,013RDhw9hoL.css,11JQtnL-6eL.css,116v6uYvN6L.css,11jtXRmppwL.css,01QrWuRrZ-L.css,21zuRztKjtL.css,11QyqG8yiqL.css,11K24eOJg4L.css,11F2+OBzLyL.css,01890+Vwk8L.css,11Y05DTEL6L.css,01cbS3UK11L.css,21F85am0yFL.css,01giMEP+djL.css_.css?AUIClients/AmazonUI#us.not-trident">
<script>
(function(f,h,Q,F){function z(a){v&&v.tag&&v.tag(q(":","aui",a))}function t(a,b){v&&v.count&&v.count("aui:"+a,0===b?0:b||(v.count("aui:"+a)||0)+1)}function p(a){try{return a.test(navigator.userAgent)}catch(b){return!1}}function y(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function q(a,b,c,e){b=b&&c?b+a+c:b||c;return e?q(a,b,e):b}function G(a,b,c){try{Object.defineProperty(a,b,{value:c,writable:!1})}catch(e){a[b]=c}return c}function ua(a,b,c){var e=
c=a.length,g=function(){e--||(R.push(b),S||(setTimeout(ca,0),S=!0))};for(g();c--;)da[a[c]]?g():(A[a[c]]=A[a[c]]||[]).push(g)}function va(a,b,c,e,g){var d=h.createElement(a?"script":"link");y(d,"error",e);g&&y(d,"load",g);a?(d.type="text/javascript",d.async=!0,c&&/AUIClients|images[/]I/.test(b)&&d.setAttribute("crossorigin","anonymous"),d.src=b):(d.rel="stylesheet",d.href=b);h.getElementsByTagName("head")[0].appendChild(d)}function ea(a,b){return function(c,e){function g(){va(b,c,d,function(b){T?t("resource_unload"):
d?(d=!1,t("resource_retry"),g()):(t("resource_error"),a.log("Asset failed to load: "+c));b&&b.stopPropagation?b.stopPropagation():f.event&&(f.event.cancelBubble=!0)},e)}if(fa[c])return!1;fa[c]=!0;t("resource_count");var d=!0;return!g()}}function wa(a,b,c){for(var e={name:a,guard:function(c){return b.guardFatal(a,c)},guardTime:function(a){return b.guardTime(a)},logError:function(c,d,e){b.logError(c,d,e,a)}},g=[],d=0;d<c.length;d++)H.hasOwnProperty(c[d])&&(g[d]=U.hasOwnProperty(c[d])?U[c[d]](H[c[d]],
e):H[c[d]]);return g}function B(a,b,c,e,g){return function(d,h){function n(){var a=null;e?a=h:"function"===typeof h&&(p.start=w(),a=h.apply(f,wa(d,k,l)),p.end=w());if(b){H[d]=a;a=d;for(da[a]=!0;(A[a]||[]).length;)A[a].shift()();delete A[a]}p.done=!0}var k=g||this;"function"===typeof d&&(h=d,d=F);b&&(d=d?d.replace(ha,""):"__NONAME__",V.hasOwnProperty(d)&&k.error(q(", reregistered by ",q(" by ",d+" already registered",V[d]),k.attribution),d),V[d]=k.attribution);for(var l=[],m=0;m<a.length;m++)l[m]=
a[m].replace(ha,"");var p=C[d||"anon"+ ++xa]={depend:l,registered:w(),namespace:k.namespace};d&&ya.hasOwnProperty(d);c?n():ua(l,k.guardFatal(d,n),d);return{decorate:function(a){U[d]=k.guardFatal(d,a)}}}}function ia(a){return function(){var b=Array.prototype.slice.call(arguments);return{execute:B(b,!1,a,!1,this),register:B(b,!0,a,!1,this)}}}function W(a,b){return function(c,e){e||(e=c,c=F);var g=this.attribution;return function(){u.push(b||{attribution:g,name:c,logLevel:a});var d=e.apply(this,arguments);
u.pop();return d}}}function I(a,b){this.load={js:ea(this,!0),css:ea(this)};G(this,"namespace",b);G(this,"attribution",a)}function ja(){h.body?r.trigger("a-bodyBegin"):setTimeout(ja,20)}function D(a,b){a.className=X(a,b)+" "+b}function X(a,b){return(" "+a.className+" ").split(" "+b+" ").join(" ").replace(/^ | $/g,"")}function ka(a){try{return a()}catch(b){return!1}}function J(){if(K){var a={w:f.innerWidth||n.clientWidth,h:f.innerHeight||n.clientHeight};5<Math.abs(a.w-Y.w)||50<a.h-Y.h?(Y=a,L=4,(a=k.mobile||
k.tablet?450<a.w&&a.w>a.h:1250<=a.w)?D(n,"a-ws"):n.className=X(n,"a-ws")):0<L&&(L--,la=setTimeout(J,16))}}function za(a){(K=a===F?!K:!!a)&&J()}function Aa(){return K}function ma(){E.forEach(function(a){z(a)})}function na(a,b,c){if(b){a=p(/Chrome/i)&&!p(/Edge/i)&&!p(/OPR/i)&&!a.capabilities.isAmazonApp&&!p(new RegExp(Z+"bwv"+Z+"b"));var e="sw:browser:"+c+":";b.browser&&a&&(E.push(e+"supported"),b.browser.action(e,c));!a&&b.browser&&E.push(e+"unsupported")}}"use strict";var M=Q.now=Q.now||function(){return+new Q},
w=function(a){return a&&a.now?a.now.bind(a):M}(f.performance),N=w(),ya={},l=f.AmazonUIPageJS||f.P;if(l&&l.when&&l.register){N=[];for(var m=h.currentScript;m;m=m.parentElement)m.id&&N.push(m.id);return l.log("A copy of P has already been loaded on this page.","FATAL",N.join(" "))}var v=f.ue;z();z("aui_build_date:3.21.9-2022-03-01");var R=[],Ba=[],S=!1;var ca=function(){for(var a=setTimeout(ca,0),b=M();Ba.length||R.length;)if(R.shift()(),50<M()-b)return;clearTimeout(a);S=!1};var da={},A={},fa={},T=
!1;y(f,"beforeunload",function(){T=!0;setTimeout(function(){T=!1},1E4)});var ha=/^prv:/,V={},H={},U={},C={},xa=0,Z=String.fromCharCode(92),u=[],oa=!0,pa=f.onerror;f.onerror=function(a,b,c,e,g){g&&"object"===typeof g||(g=Error(a,b,c),g.columnNumber=e,g.stack=b||c||e?q(Z,g.message,"at "+q(":",b,c,e)):F);var d=u.pop()||{};g.attribution=q(":",g.attribution||d.attribution,d.name);g.logLevel=d.logLevel;g.attribution&&console&&console.log&&console.log([g.logLevel||"ERROR",a,"thrown by",g.attribution].join(" "));
u=[];pa&&(d=[].slice.call(arguments),d[4]=g,pa.apply(f,d))};I.prototype={logError:function(a,b,c,e){b={message:b,logLevel:c||"ERROR",attribution:q(":",this.attribution,e)};if(f.ueLogError)return f.ueLogError(a||b,a?b:null),!0;console&&console.error&&(console.log(b),console.error(a));return!1},error:function(a,b,c,e){a=Error(q(":",e,a,c));a.attribution=q(":",this.attribution,b);throw a;},guardError:W(),guardFatal:W("FATAL"),guardCurrent:function(a){var b=u[u.length-1];return b?W(b.logLevel,b).call(this,
a):a},guardTime:function(a){var b=u[u.length-1],c=b&&b.name;return c&&c in C?function(){var b=w(),g=a.apply(this,arguments);C[c].async=(C[c].async||0)+w()-b;return g}:a},log:function(a,b,c){return this.logError(null,a,b,c)},declare:B([],!0,!0,!0),register:B([],!0),execute:B([]),AUI_BUILD_DATE:"3.21.9-2022-03-01",when:ia(),now:ia(!0),trigger:function(a,b,c){var e=M();this.declare(a,{data:b,pageElapsedTime:e-(f.aPageStart||NaN),triggerTime:e});c&&c.instrument&&O.when("prv:a-logTrigger").execute(function(b){b(a)})},
handleTriggers:function(){this.log("handleTriggers deprecated")},attributeErrors:function(a){return new I(a)},_namespace:function(a,b){return new I(a,b)},setPriority:function(a){oa?oa=!1:this.log("setPriority only accept the first call.")}};var r=G(f,"AmazonUIPageJS",new I);var O=r._namespace("PageJS","AmazonUI");O.declare("prv:p-debug",C);r.declare("p-recorder-events",[]);r.declare("p-recorder-stop",function(){});G(f,"P",r);ja();if(h.addEventListener){var qa;h.addEventListener("DOMContentLoaded",
qa=function(){r.trigger("a-domready");h.removeEventListener("DOMContentLoaded",qa,!1)},!1)}var n=h.documentElement,aa=function(){var a=["O","ms","Moz","Webkit"],b=h.createElement("div");return{testGradients:function(){return!0},test:function(c){var e=c.charAt(0).toUpperCase()+c.substr(1);c=(a.join(e+" ")+e+" "+c).split(" ");for(e=c.length;e--;)if(""===b.style[c[e]])return!0;return!1},testTransform3d:function(){return!0}}}();l=n.className;var ra=/(^| )a-mobile( |$)/.test(l),sa=/(^| )a-tablet( |$)/.test(l),
k={audio:function(){return!!h.createElement("audio").canPlayType},video:function(){return!!h.createElement("video").canPlayType},canvas:function(){return!!h.createElement("canvas").getContext},svg:function(){return!!h.createElementNS&&!!h.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect},offline:function(){return navigator.hasOwnProperty&&navigator.hasOwnProperty("onLine")&&navigator.onLine},dragDrop:function(){return"draggable"in h.createElement("span")},geolocation:function(){return!!navigator.geolocation},
history:function(){return!(!f.history||!f.history.pushState)},webworker:function(){return!!f.Worker},autofocus:function(){return"autofocus"in h.createElement("input")},inputPlaceholder:function(){return"placeholder"in h.createElement("input")},textareaPlaceholder:function(){return"placeholder"in h.createElement("textarea")},localStorage:function(){return"localStorage"in f&&null!==f.localStorage},orientation:function(){return"orientation"in f},touch:function(){return"ontouchend"in h},gradients:function(){return aa.testGradients()},
hires:function(){var a=f.devicePixelRatio&&1.5<=f.devicePixelRatio||f.matchMedia&&f.matchMedia("(min-resolution:144dpi)").matches;t("hiRes"+(ra?"Mobile":sa?"Tablet":"Desktop"),a?1:0);return a},transform3d:function(){return aa.testTransform3d()},touchScrolling:function(){return p(/Windowshop|android|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|SOFTWARE=([5-9]|[1-9][0-9]+)(.[0-9]{1,2})+.*DEVICE=iPhone|Chrome|Silk|Firefox|Trident.+?; Touch/i)},ios:function(){return p(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)&&
!p(/trident|Edge/i)},android:function(){return p(/android.([1-9]|[L-Z])/i)&&!p(/trident|Edge/i)},mobile:function(){return ra},tablet:function(){return sa},rtl:function(){return"rtl"===n.dir}};for(m in k)k.hasOwnProperty(m)&&(k[m]=ka(k[m]));for(var ba="textShadow textStroke boxShadow borderRadius borderImage opacity transform transition".split(" "),P=0;P<ba.length;P++)k[ba[P]]=ka(function(){return aa.test(ba[P])});var K=!0,la=0,Y={w:0,h:0},L=4;J();y(f,"resize",function(){clearTimeout(la);L=4;J()});
var ta={getItem:function(a){try{return f.localStorage.getItem(a)}catch(b){}},setItem:function(a,b){try{return f.localStorage.setItem(a,b)}catch(c){}}};n.className=X(n,"a-no-js");D(n,"a-js");!p(/OS [1-8](_[0-9]*)+ like Mac OS X/i)||f.navigator.standalone||p(/safari/i)||D(n,"a-ember");l=[];for(m in k)k.hasOwnProperty(m)&&k[m]&&l.push("a-"+m.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()}));D(n,l.join(" "));n.setAttribute("data-aui-build-date","3.21.9-2022-03-01");r.register("p-detect",function(){return{capabilities:k,
localStorage:k.localStorage&&ta,toggleResponsiveGrid:za,responsiveGridEnabled:Aa}});p(/UCBrowser/i)||k.localStorage&&D(n,ta.getItem("a-font-class"));r.declare("a-event-revised-handling",!1);try{var x=navigator.serviceWorker}catch(a){z("sw:nav_err")}x&&(y(x,"message",function(a){a&&a.data&&t(a.data.k,a.data.v)}),x.controller&&x.controller.postMessage("MSG-RDY"));var E=[];l={reg:{},unreg:{}};l.unreg.browser={action:function(a,b){try{x.getRegistrations().then(function(c){c.forEach(function(c){c.unregister().then(function(){t(a+
"success")}).catch(function(c){r.logError(c,"[AUI SW] Failed to "+b+" service worker: ");t(a+"failure")})})})}catch(c){z("sw:api_error")}}};(function(a){var b=a.reg,c=a.unreg;x&&x.getRegistrations?(O.when("A").execute(function(a){na(a,c,"unregister")}),y(f,"load",function(){O.when("A").execute(function(a){na(a,b,"register");ma()})})):(b&&b.browser&&E.push("sw:browser:register:unsupported"),c&&c.browser&&E.push("sw:browser:unregister:unsupported"),ma())})(l);r.declare("a-fix-event-off",!1);t("pagejs:pkgExecTime",
w()-N)})(window,document,Date);
(function(b){function q(a,f,d){function e(a,b,c){var e=Array(f.length);~l&&(e[l]={});~m&&(e[m]=c);for(c=0;c<n.length;c++){var g=n[c],r=a[c];e[g]=r}for(c=0;c<p.length;c++)g=p[c],r=b[c],e[g]=r;a=d.apply(null,e);return~l?e[l]:a}"string"!==typeof a&&b.P.error("C001");-1===a.indexOf("@")&&-1<a.indexOf("/")&&(-1<a.indexOf("es3")||-1<a.indexOf("evergreen"))&&(a=a.substring(0,a.lastIndexOf("/")));if(!t[a]){t[a]=!0;d||(d=f,f=[]);a=a.split(":",2);var c=a[1]?a[0]:void 0,g=(a[1]||a[0]).replace(/@capability\//,
"@c/"),k=c?b.P._namespace(c):b.P,u=!g.lastIndexOf("@c/",0),n=[];a=[];var p=[],v=[],m=-1,l=-1;for(c=0;c<f.length;c++){var h=f[c];"module"===h&&k.error("C002");"exports"===h?l=c:"require"===h?m=c:h.lastIndexOf("@p/",0)?h.lastIndexOf("@c/",0)?(n.push(c),a.push("mix:"+h)):(p.push(c),v.push(h)):(n.push(c),a.push(h.substr(3)))}k.when.apply(k,a).register("mix:"+g,function(){var a=[].slice.call(arguments);return u||~m||p.length?{capabilities:v,cardModuleFactory:function(b,c){b=e(a,b,c);b.P=k;return b},require:~m?
q:void 0}:e(a,[],function(){})});u&&k.when("mix:@amzn/mix.client-runtime","mix:"+g).execute(function(a,b){a.registerCapabilityModule(g,b)});k.when("mix:"+g).register("xcp:"+g,function(a){return a});var q=function(a,b,c){try{var f=-1<g.indexOf("/")?g.split("/")[0]:g,d=a[0],e=d.lastIndexOf("./",0)?d:f+"/"+d.substr(2),h=e.lastIndexOf("@p/",0)?"mix:"+e:e.substr(3);k.when(h).execute(function(a){try{b(a)}catch(x){c(x)}})}catch(w){c(w)}}}}"use strict";var t={};b.mix_d||((b.Promise?P:P.when("3p-promise")).register("@p/promise-is-ready",
function(a){b.Promise=b.Promise||a}),(Array.prototype.includes?P:P.when("a-polyfill")).register("@p/polyfill-is-ready",function(){}),b.mix_d=function(a,b,d){P.when("@p/promise-is-ready","@p/polyfill-is-ready").execute("@p/mix-d-deps",function(){q(a,b,d)})},b.xcp_d=b.mix_d,P.when("mix:@amzn/mix.client-runtime").execute(function(a){P.declare("xcp:@xcp/runtime",a)}));b.mixTimeout||(b.mixTimeout=function(a,f,d){b.mixCardInitTimeouts||(b.mixCardInitTimeouts={});b.mixCardInitTimeouts[f]&&clearTimeout(b.mixCardInitTimeouts[f]);
b.mixCardInitTimeouts[f]=setTimeout(function(){P.log("Client-side initialization timeout","WARN",a)},d)});b.mix_csa_map=b.mix_csa_map||{};b.mix_csa_internal=b.mix_csa_internal||function(a,f,d){return b.mix_csa_map[f]=b.mix_csa_map[f]||b.csa(a,d)};b.mix_csa_internal_key=b.mix_csa_internal_key||function(a,b){for(var d="",e=0;e<b.length;e++){var c=b[e];void 0!==a[c]&&"object"!==typeof a[c]&&(d+=c+":"+a[c]+",")}if(!d)throw Error("bad mix-csa key gen.");return d};b.mix_csa_event=b.mix_csa_event||function(a){try{var f=
b.mix_csa_internal_key(a,["producerId"])}catch(d){return P.logError(d,"MIX C005","ERROR",void 0),function(){}}try{return b.mix_csa_internal("Events",f,a)}catch(d){return P.logError(d,"MIX C004","ERROR",f),function(){}}};b.mix_csa=b.mix_csa||function(a,f){try{f=f||"";var d=document.querySelectorAll(a);if(1<d.length)for(var e=0;e<d.length;e++){if(d[e].querySelector(f)){var c=d[e];break}}else 1===d.length&&(c=d[0]);if(!c)throw Error(" ");return b.mix_csa_internal("Content",a,{element:c})}catch(g){return P.logError(g,
"MIX C004","ERROR",a),function(){}}}})(window);
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('sp.load.js').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/61XKxrBtDVL.js?AUIClients/AmazonUIjQuery');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/11Y+5x+kkTL._RC|51106gSDnJL.js,11yKORv-GTL.js,11giXtZCwVL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,51H19hJRYrL.js,11kWu3cNjYL.js,11tMohjWmVL.js,11OREnu1epL.js,11wcWdhrnDL.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31R9m8rig5L.js,01ezj5Rkz1L.js,11+RxVdhNcL.js,31o2NGTXThL.js,01rpauTep4L.js,01KFkXJxMTL.js_.js?AUIClients/AmazonUI');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/51Vsv+W3nKL.js?AUIClients/CardJsRuntimeBuzzCopyBuild');
});
</script>
<!-- sp:end-feature:aui-assets -->
<!-- sp:feature:nav-inline-css -->
<!-- NAVYAAN CSS -->

<style type="text/css">
.nav-sprite-v1 .nav-sprite, .nav-sprite-v1 .nav-icon {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png);
  background-position: 0 1000px;
  background-repeat: repeat-x;
}
.nav-spinner {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/01/javascripts/lib/popover/images/snake._CB485935611_.gif);
  background-position: center center;
  background-repeat: no-repeat;
}
.nav-timeline-icon, .nav-access-image, .nav-timeline-prime-icon {
  background-image: url(https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/timeline_sprite_1x._CB485945973_.png);
  background-repeat: no-repeat;
}
</style>
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41H4XraWzVL._RC|01RUIx5x4lL.css,71FRdI300gL.css,41HWK3u-jrL.css,31SIZofZ3OL.css,31YZpDCYJPL.css,21MKjoYL8wL.css,41wK0C031bL.css,01yCq3WXEcL.css,11kO7yAgiQL.css,31OvHRW+XiL.css,01XHMOHpK1L.css,11iUHDm4--L.css,41yKpEQVJkL.css_.css?AUIClients/NavDesktopUberAsset&amp;/tL3+TmD#desktop.408005-T1.400404-T1.310484-T1.392230-T1.269915-T2">
<!-- sp:end-feature:nav-inline-css -->
<!-- sp:feature:host-assets -->
<script type="text/javascript">
     window.P && P.register('sp.load.js');
</script>

<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/21ZkfeOo7vL.css?AUIClients/OctopusBrowsePageAssets">
<script>
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/0152SLDk8CL.js?AUIClients/OctopusBrowsePageAssets');
</script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/0152SLDk8CL.js?AUIClients/OctopusBrowsePageAssets"></script>
<title>Amazon.com: Books</title>
<meta name="keywords" content="Books, Amazon.com"><meta name="description" content="Online shopping from a great selection at Books Store."><link rel="canonical" href="https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&amp;node=283155"><!--&&&Portal&Delimiter&&&--><!-- sp:end-feature:host-assets -->
<script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/61XKxrBtDVL.js?AUIClients/AmazonUIjQuery"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/11Y+5x+kkTL._RC|51106gSDnJL.js,11yKORv-GTL.js,11giXtZCwVL.js,01+z+uIeJ-L.js,01VRMV3FBdL.js,21SDJtBU-PL.js,012FVc3131L.js,11rRjDLdAVL.js,51H19hJRYrL.js,11kWu3cNjYL.js,11tMohjWmVL.js,11OREnu1epL.js,11wcWdhrnDL.js,21ssiLNIZvL.js,0190vxtlzcL.js,51+N26vFcBL.js,01JYHc2oIlL.js,31R9m8rig5L.js,01ezj5Rkz1L.js,11+RxVdhNcL.js,31o2NGTXThL.js,01rpauTep4L.js,01KFkXJxMTL.js_.js?AUIClients/AmazonUI"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/51Vsv+W3nKL.js?AUIClients/CardJsRuntimeBuzzCopyBuild"></script><script type="text/javascript">
window.ue_ihe = (window.ue_ihe || 0) + 1;
if (window.ue_ihe === 1) {
(function(c){c&&1===c.ue_jsmtf&&"object"===typeof c.P&&"function"===typeof c.P.when&&c.P.when("mshop-interactions").execute(function(e){"object"===typeof e&&"function"===typeof e.addListener&&e.addListener(function(b){"object"===typeof b&&"ORIGIN"===b.dataSource&&"number"===typeof b.clickTime&&"object"===typeof b.events&&"number"===typeof b.events.pageVisible&&(c.ue_jsmtf_interaction={pv:b.events.pageVisible,ct:b.clickTime})})})})(ue_csm);
(function(c,e,b){function m(a){f||(f=d[a.type].id,"undefined"===typeof a.clientX?(h=a.pageX,k=a.pageY):(h=a.clientX,k=a.clientY),2!=f||l&&(l!=h||n!=k)?(r(),g.isl&&e.setTimeout(function(){p("at",g.id)},0)):(l=h,n=k,f=0))}function r(){for(var a in d)d.hasOwnProperty(a)&&g.detach(a,m,d[a].parent)}function s(){for(var a in d)d.hasOwnProperty(a)&&g.attach(a,m,d[a].parent)}function t(){var a="";!q&&f&&(q=1,a+="&ui="+f);return a}var g=c.ue,p=c.uex,q=0,f=0,l,n,h,k,d={click:{id:1,parent:b},mousemove:{id:2,
parent:b},scroll:{id:3,parent:e},keydown:{id:4,parent:b}};g&&p&&(s(),g._ui=t)})(ue_csm,window,document);


(function(s,l){function m(b,e,c){c=c||new Date(+new Date+t);c="expires="+c.toUTCString();n.cookie=b+"="+e+";"+c+";path=/"}function p(b){b+="=";for(var e=n.cookie.split(";"),c=0;c<e.length;c++){for(var a=e[c];" "==a.charAt(0);)a=a.substring(1);if(0===a.indexOf(b))return decodeURIComponent(a.substring(b.length,a.length))}return""}function q(b,e,c){if(!e)return b;-1<b.indexOf("{")&&(b="");for(var a=b.split("&"),f,d=!1,h=!1,g=0;g<a.length;g++)f=a[g].split(":"),f[0]==e?(!c||d?a.splice(g,1):(f[1]=c,a[g]=
f.join(":")),h=d=!0):2>f.length&&(a.splice(g,1),h=!0);h&&(b=a.join("&"));!d&&c&&(0<b.length&&(b+="&"),b+=e+":"+c);return b}var k=s.ue||{},t=3024E7,n=ue_csm.document||l.document,r=null,d;a:{try{d=l.localStorage;break a}catch(u){}d=void 0}k.count&&k.count("csm.cookieSize",document.cookie.length);k.cookie={get:p,set:m,updateCsmHit:function(b,e,c){try{var a;if(!(a=r)){var f;a:{try{if(d&&d.getItem){f=d.getItem("csm-hit");break a}}catch(k){}f=void 0}a=f||p("csm-hit")||"{}"}a=q(a,b,e);r=a=q(a,"t",+new Date);
try{d&&d.setItem&&d.setItem("csm-hit",a)}catch(h){}m("csm-hit",a,c)}catch(g){"function"==typeof l.ueLogError&&ueLogError(Error("Cookie manager: "+g.message),{logLevel:"WARN"})}}}})(ue_csm,window);


(function(l,e){function c(b){b="";var c=a.isBFT?"b":"s",d=""+a.oid,g=""+a.lid,h=d;d!=g&&20==g.length&&(c+="a",h+="-"+g);a.tabid&&(b=a.tabid+"+");b+=c+"-"+h;b!=f&&100>b.length&&(f=b,a.cookie?a.cookie.updateCsmHit(m,b+("|"+ +new Date)):e.cookie="csm-hit="+b+("|"+ +new Date)+n+"; path=/")}function p(){f=0}function d(b){!0===e[a.pageViz.propHid]?f=0:!1===e[a.pageViz.propHid]&&c({type:"visible"})}var n="; expires="+(new Date(+new Date+6048E5)).toGMTString(),m="tb",f,a=l.ue||{},k=a.pageViz&&a.pageViz.event&&
a.pageViz.propHid;a.attach&&(a.attach("click",c),a.attach("keyup",c),k||(a.attach("focus",c),a.attach("blur",p)),k&&(a.attach(a.pageViz.event,d,e),d({})));a.aftb=1})(ue_csm,ue_csm.document);


ue_csm.ue.stub(ue,"impression");


ue.stub(ue,"trigger");



if(window.ue&&uet) { uet('bb'); }

}
</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 3173)</script>
<!-- sp:feature:head-close -->
<script>
window.P && P.register('bb');
if (typeof ues === 'function') {
  ues('t0', 'portal-bb', new Date());
  ues('ctb', 'portal-bb', 1);
}
</script>
<script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/41TavVAsNFL.js?xcp"></script><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/41uLOOuUMJL._RC|01LEzWzrPZL.js,71BDiB9DHjL.js,01QvReFeJyL.js,016tgkOMMNL.js,616P4MHT7yL.js,41gNKoK0s7L.js,115pV8Rl02L.js,21QA-szxgvL.js,11k47yUMOjL.js,41SZNgvX4oL.js,51-xVUkFLqL.js,31sq3pfde4L.js,11lEMI5MhIL.js,31DbmIB-3JL.js_.js?AUIClients/NavDesktopUberAsset&amp;dRzb8qTH#desktop.language-en.us.375680-T1.387765-T1.365419-T1.366740-T1.310484-T1.392230-T1.403991-T1.395433-T1"></script><style></style><script type="text/javascript" async="" crossorigin="anonymous" src="https://images-na.ssl-images-amazon.com/images/I/71iqUL2aEuL.js?AUIClients/FWCIMAssets"></script></head><!-- sp:end-feature:head-close -->
<!-- sp:feature:start-body -->
<body class="a-m-us a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_killswitch_csa_logger_372963-c a-aui_launch_2021_ally_fixes_392482-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate"><div id="a-page"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;a-wlab-states&quot;}">{"AUI_TNR_V2_180836":"C","AUI_ACCORDION_A11Y_ROLE_354025":"C","AUI_PRELOAD_261698":"C","AUI_LAUNCH_2021_ALLY_FIXES_392482":"C","AUI_TEMPLATE_WEBLAB_CACHE_333406":"C","AUI_72554":"C","AUI_KILLSWITCH_CSA_LOGGER_372963":"C","AUI_REL_NOREFERRER_NOOPENER_309527":"C","AUI_PCI_RISK_BANNER_210084":"C"}</script><script>typeof uex === 'function' && uex('ld', 'portal-bb', {wb: 1})</script><!-- sp:end-feature:start-body -->


<script>
!function(){function n(n,t){var r=i(n);return t&&(r=r("instance",t)),r}var r=[],c=0,i=function(t){return function(){var n=c++;return r.push([t,[].slice.call(arguments,0),n,{time:Date.now()}]),i(n)}};n._s=r,this.csa=n}();;
csa('Config', {"Content.EnableContentRenders":true});
if (window.csa) {
    csa("Config", {
        'Application': 'Retail:Prod:www.amazon.com',
        'Events.Namespace': 'csa',
        'ObfuscatedMarketplaceId': 'ATVPDKIKX0DER',
        'Events.SushiEndpoint': 'https://unagi.amazon.com/1/events/com.amazon.csm.csa.prod',
        'CacheDetection.RequestID': "Z0KMT1JTKBYN6W6QW6GJ",
        'CacheDetection.Callback': window.ue && ue.reset,
        'LCP.elementDedup': 1
    });

    csa("Events")("setEntity", {
        page: {requestId: "Z0KMT1JTKBYN6W6QW6GJ", meaningful: "interactive"},
        session: {id: "130-0450696-1458362"}
    });
}
!function(i){var r,e,o="splice",u=i.csa,f={},c={},a=i.csa._s,s=0,l=0,g=-1,h={},d={},v={},n=Object.keys,p=function(){};function t(n,t){return u(n,t)}function m(n,t){var i=c[n]||{};O(i,t),c[n]=i,l++,S(U,0)}function w(n,t,i){var r=!0;return t=D(t),i&&i.buffered&&(r=(v[n]||[]).every(function(n){return!1!==t(n)})),r?(h[n]||(h[n]=[]),h[n].push(t),function(){!function(n,t){var i=h[n];i&&i[o](i.indexOf(t),1)}(n,t)}):p}function b(n,t){if(t=D(t),n in d)return t(d[n]),p;return w(n,function(n){return t(n),!1})}function E(n,t){if(u("Errors")("logError",n),f.DEBUG)throw t||n}function y(){return Math.abs(4294967295*Math.random()|0).toString(36)}function D(n,t){return function(){try{return n.apply(this,arguments)}catch(n){E(n.message||n,n)}}}function S(n,t){return i.setTimeout(D(n),t)}function U(){for(var n=0;n<a.length;){var t=a[n],i=t[0]in c;if(!i&&!e)return void(s=f.AddMissingPluginsToEnd?a.length:t.length);i?(a[o](s=n,1),I(t)):n++}g=l}function I(n){var arguments,t=c[n[0]],i=(arguments=n[1])[0];if(!t||!t[i])return E("Undefined function: "+t+"/"+i);r=n[3],c[n[2]]=t[i].apply(t,arguments.slice(1))||{},r=0}function M(){e=1,U()}function O(t,i){n(i).forEach(function(n){t[n]=i[n]})}b("$beforeunload",M),m("Config",{instance:function(n){O(f,n)}}),u.plugin=D(function(n){n(t)}),t.config=f,t.register=m,t.on=w,t.once=b,t.blank=p,t.emit=function(n,t,i){for(var r=h[n]||[],e=0;e<r.length;)!1===r[e](t)?r[o](e,1):e++;d[n]=t||{},i&&i.buffered&&(v[n]||(v[n]=[]),100<=v[n].length&&v[n].shift(),v[n].push(t||{}))},t.UUID=function(){return[y(),y(),y(),y()].join("-")},t.time=function(n){var t=r?new Date(r.time):new Date;return"ISO"===n?t.toISOString():t.getTime()},t.error=E,t.warn=function(n,t){if(u("Errors")("logWarn",n),f.DEBUG)throw t||n},t.exec=D,t.timeout=S,t.interval=function(n,t){return i.setInterval(D(n),t)},(t.global=i).csa._s.push=function(n){n[0]in c&&(!a.length||e)?(I(n),a.length&&g!==l&&U()):a[o](s++,0,n)},U(),S(function(){S(M,f.SkipMissingPluginsTimeout||5e3)},1)}("undefined"!=typeof window?window:global);csa.plugin(function(o){var f="addEventListener",e="requestAnimationFrame",t=o.exec,r=o.global,u=o.on;o.raf=function(n){if(r[e])return r[e](t(n))},o.on=function(n,e,t,r){if(n&&"function"==typeof n[f]){var i=o.exec(t);return n[f](e,i,r),function(){n.removeEventListener(e,i,r)}}return"string"==typeof n?u(n,e,t,r):o.blank}});csa.plugin(function(o){var t,n,r={},e="localStorage",c="sessionStorage",a="local",i="session",u=o.exec;function s(e,t){var n;try{r[t]=!!(n=o.global[e]),n=n||{}}catch(e){r[t]=!(n={})}return n}function f(){t=t||s(e,a),n=n||s(c,i)}function l(e){return e&&e[i]?n:t}o.store=u(function(e,t,n){f();var o=l(n);return e?t?void(o[e]=t):o[e]:Object.keys(o)}),o.storageSupport=u(function(){return f(),r}),o.deleteStored=u(function(e,t){f();var n=l(t);if("function"==typeof e)for(var o in n)n.hasOwnProperty(o)&&e(o,n[o])&&delete n[o];else delete n[e]})});csa.plugin(function(o){function r(n){return function(r){o("Metrics",{producerId:"csa",dimensions:{message:r}})("recordMetric",n,1)}}o.register("Errors",{logError:r("jsError"),logWarn:r("jsWarn")})});csa.plugin(function(r){var o,e,a,n,t,i="willDisappear",f=r.global,p=r.exec,u=r("Events"),c=f.location,d=f.document,l=((f.performance||{}).navigation||{}).type,s=r.on,g=r.emit,$={};c&&d&&(s(f,"beforeunload",b),s(f,"pagehide",b),e=f.app||{},a=p(b),t="function"==typeof(n=e[i]),e[i]=p(function(){a(),t&&n()}),f.app||(f.app=e),"complete"===d.readyState?y():s(f,"load",y),r.register("SPA",{newPage:h}),h({transitionType:{0:"hard",1:"refresh",2:"back-button"}[l]||"unknown"}));function h(a,e){var n=!!o,t=(e=e||{}).keepPageAttributes;n&&(g("$beforePageTransition"),g("$pageTransition")),n&&!t&&u("removeEntity","page"),o=r.UUID(),t?$.id=o:$={schemaId:"<ns>.PageEntity.1",id:o,url:c.href,server:c.hostname,path:c.pathname,referrer:d.referrer,title:d.title},Object.keys(a||{}).forEach(function(e){$[e]=a[e]}),u("setEntity",{page:$}),g("$pageChange",$,{buffered:1}),n&&g("$afterPageTransition")}function y(){g("$load"),g("$ready"),g("$afterload")}function b(){g("$ready"),g("$beforeunload"),g("$unload"),g("$afterunload")}});csa.plugin(function(c){var t="Events",e="UNKNOWN",a="id",u="all",n="messageId",i="timestamp",f="producerId",o="application",r="obfuscatedMarketplaceId",s="entities",d="schemaId",l="version",p="attributes",v="<ns>",g=c.config,h=(c.global.location||{}).host,m=g[t+".Namespace"]||"csa_other",I=g.Application||"Other"+(h?":"+h:""),b=c("Transport"),y={},O=function(t,e){Object.keys(t).forEach(e)};function E(n,i,o){O(i,function(t){var e=o===u||(o||{})[t];t in n||(n[t]={version:1,id:i[t][a]||c.UUID()}),U(n[t],i[t],e)})}function U(e,n,i){O(n,function(t){!function(t,e,n){return"string"!=typeof e&&t!==l?c.error("Attribute is not of type string: "+t):!0===n||1===n||(t===a||!!~(n||[]).indexOf(t))}(t,n[t],i)||(e[t]=n[t])})}function N(o,t,r){O(t,function(t){var e=o[t];if(e[d]){var n={},i={};n[a]=e[a],n[f]=e[f]||r,n[d]=e[d],n[l]=e[l]++,n[p]=i,S(n),U(i,e,1),k(i),b("log",n)}})}function S(t){t[i]=function(t){return"number"==typeof t&&(t=new Date(t).toISOString()),t||c.time("ISO")}(t[i]),t[n]=t[n]||c.UUID(),t[o]=I,t[r]=g.ObfuscatedMarketplaceId||e,t[d]=t[d].replace(v,m)}function k(t){delete t[l],delete t[d],delete t[f]}function w(o){var r={};this.log=function(t,e){var n={},i=(e||{}).ent;return t?"string"!=typeof t[d]?c.error("A valid schema id is required for the event"):(S(t),E(n,y,i),E(n,r,i),E(n,t[s]||{},i),O(n,function(t){k(n[t])}),t[f]=o[f],t[s]=n,void b("log",t,e)):c.error("The event cannot be undefined")},this.setEntity=function(t){E(r,t,u),N(r,t,o[f])}}g["KillSwitch."+t]||c.register(t,{setEntity:function(t){E(y,t,u),N(y,t,"csa")},removeEntity:function(t){delete y[t]},instance:function(t){return new w(t)}})});csa.plugin(function(s){var c,g="Transport",l="post",f="preflight",r="csa.cajun.",i="store",a="deleteStored",u="sendBeacon",t="__merge",e="messageId",n=".FlushInterval",o=0,d=s.config[g+".BufferSize"]||2e3,h=s.config[g+".RetryDelay"]||1500,p={},v=0,y=[],m=s.global,E=m.document,b=s.timeout,k=m.Object.keys,w=s.config[g+n]||5e3,I=w,O=s.config[g+n+".BackoffFactor"]||1,R=s.config[g+n+".BackoffLimit"]||3e4,S=0;function B(n){if(864e5<s.time()-+new Date(n.timestamp))return s.warn("Event is too old: "+n);v<d&&(n[e]in p||(p[n[e]]=n,v++),"function"==typeof n[t]&&n[t](p[n[e]]),!S&&o&&(S=b(T,function(){var n=I;return I=Math.min(n*O,R),n}())))}function T(){y.forEach(function(e){var o=[];k(p).forEach(function(n){var t=p[n];e.accepts(t)&&o.push(t)}),o.length&&(e.chunks?e.chunks(o).forEach(function(n){D(e,n)}):D(e,o))}),p={},S=0}function D(t,e){function o(){s[a](r+n)}var n=s.UUID();s[i](r+n,JSON.stringify(e)),[function(n,t,e){var o=m.navigator||{},r=m.cordova||{};if(!o[u]||!n[l])return 0;n[f]&&r&&"ios"===r.platformId&&!c&&((new Image).src=n[f]().url,c=1);var i=n[l](t);if(!i.type&&o[u](i.url,i.body))return e(),1},function(n,t,e){if(!n[l])return 0;var o=n[l](t),r=o.url,i=o.body,c=o.type,f=new XMLHttpRequest,a=0;function u(n,t,e){f.open("POST",n),f.withCredentials=!0,e&&f.setRequestHeader("Content-Type",e),f.send(t)}return f.onload=function(){f.status<299?e():s.config[g+".XHRRetries"]&&a<3&&b(function(){u(r,i,c)},++a*h)},u(r,i,c),1}].some(function(n){try{return n(t,e,o)}catch(n){}})}k&&(s.once("$afterload",function(){o=1,function(e){(s[i]()||[]).forEach(function(n){if(!n.indexOf(r))try{var t=s[i](n);s[a](n),JSON.parse(t).forEach(e)}catch(n){s.error(n)}})}(B),s.on(E,"visibilitychange",T,!1),T()}),s.once("$afterunload",function(){o=1,T()}),s.on("$afterPageTransition",function(){v=0,I=w}),s.register(g,{log:B,register:function(n){y.push(n)}}))});csa.plugin(function(n){var r=n.config["Events.SushiEndpoint"];n("Transport")("register",{accepts:function(n){return n.schemaId},post:function(n){var t=n.map(function(n){return{data:n}});return{url:r,body:JSON.stringify({events:t})}},preflight:function(){var n,t=/\/\/(.*?)\//.exec(r);return t&&t[1]&&(n="https://"+t[1]+"/ping"),{url:n}},chunks:function(n){for(var t=[];500<n.length;)t.push(n.splice(0,500));return t.push(n),t}})});csa.plugin(function(n){var t,a,o,r,e=n.config,i="PageViews",d=e[i+".ImpressionMinimumTime"]||1e3,s="hidden",c="innerHeight",g="innerWidth",l="renderedTo",f=l+"Viewed",m=l+"Meaningful",u=l+"Impressed",p=1,v=2,h=3,w=4,y=5,P="loaded",I=7,T=8,b=n.global,E=n.on,V=n("Events",{producerId:"csa"}),$=b.document,M={},S={},H=y;function K(e){if(!M[I]){var i;if(M[e]=n.time(),e!==h&&e!==P||(t=t||M[e]),t&&H===w)a=a||M[e],(i={})[m]=t-o,i[f]=a-o,R("PageView.4",i),r=r||n.timeout(j,d);if(e!==y&&e!==p&&e!==v||(clearTimeout(r),r=0),e!==p&&e!==v||R("PageRender.3",{transitionType:e===p?"hard":"soft"}),e===I)(i={})[m]=t-o,i[f]=a-o,i[u]=M[e]-o,R("PageImpressed.2",i)}}function R(e,i){S[e]||(i.schemaId="<ns>."+e,V("log",i,{ent:"all"}),S[e]=1)}function W(){0===b[c]&&0===b[g]?(H=T,n("Events")("setEntity",{page:{viewport:"hidden-iframe"}})):H=$[s]?y:w,K(H)}function j(){K(I),r=0}function k(){var e=o?v:p;M={},S={},a=t=0,o=n.time(),K(e),W()}function q(){var e=$.readyState;"interactive"===e&&K(h),"complete"===e&&K(P)}e["KillSwitch."+i]||($&&void 0!==$[s]?(k(),E($,"visibilitychange",W,!1),E($,"readystatechange",q,!1),E("$afterPageTransition",k),E("$timing:loaded",q),n.once("$load",q)):n.warn("Page visibility not supported"))});csa.plugin(function(c){var s=c.config["Interactions.ParentChainLength"]||15,e="click",r="touches",f="timeStamp",o="length",u="pageX",g="pageY",p="pageXOffset",h="pageYOffset",m=250,v=5,d=200,l=.5,t={capture:!0,passive:!0},X=c.global,Y=c.emit,n=c.on,x=X.Math.abs,a=(X.document||{}).documentElement||{},y={x:0,y:0,t:0,sX:0,sY:0},N={x:0,y:0,t:0,sX:0,sY:0};function b(t){if(t.id)return"//*[@id='"+t.id+"']";var e=function(t){var e,n=1;for(e=t.previousSibling;e;e=e.previousSibling)e.nodeName===t.nodeName&&(n+=1);return n}(t),n=t.nodeName;return 1!==e&&(n+="["+e+"]"),t.parentNode&&(n=b(t.parentNode)+"/"+n),n}function I(t,e,n){var a=c("Content",{target:n}),i={schemaId:"<ns>.ContentInteraction.1",interaction:t,interactionData:e,messageId:c.UUID()};if(n){var r=b(n);r&&(i.attribution=r);var o=function(t){for(var e=t,n=e.tagName,a=!1,i=t?t.href:null,r=0;r<s;r++){if(!e||!e.parentElement){a=!0;break}n=(e=e.parentElement).tagName+"/"+n,i=i||e.href}return a||(n=".../"+n),{pc:n,hr:i}}(n);o.pc&&(i.interactionData.parentChain=o.pc),o.hr&&(i.interactionData.href=o.hr)}a("log",i),Y("$content.interaction",i)}function i(t){I(e,{interactionX:""+t.pageX,interactionY:""+t.pageY},t.target)}function C(t){if(t&&t[r]&&1===t[r][o]){var e=t[r][0];N=y={e:t.target,x:e[u],y:e[g],t:t[f],sX:X[p],sY:X[h]}}}function D(t){if(t&&t[r]&&1===t[r][o]&&y&&N){var e=t[r][0],n=t[f],a=n-N.t,i={e:t.target,x:e[u],y:e[g],t:n,sX:X[p],sY:X[h]};N=i,d<=a&&(y=i)}}function E(t){if(t){var e=x(y.x-N.x),n=x(y.y-N.y),a=x(y.sX-N.sX),i=x(y.sY-N.sY),r=t[f]-y.t;if(m<1e3*e/r&&v<e||m<1e3*n/r&&v<n){var o=n<e;o&&a&&e*l<=a||!o&&i&&n*l<=i||I((o?"horizontal":"vertical")+"-swipe",{interactionX:""+y.x,interactionY:""+y.y,endX:""+N.x,endY:""+N.y},y.e)}}}n(a,e,i,t),n(a,"touchstart",C,t),n(a,"touchmove",D,t),n(a,"touchend",E,t)});csa.plugin(function(t){var n,s,i,r="MutationObserver",e="PerformanceObserver",u="observe",o="disconnect",a="scroll",f="mutObs",c=t.global,l=t.config["VisualReady.CollectAfterPaint"],b=c.document,d=b.body||b.documentElement,p=Date.now,g=[],m=[],y=[],v=0,O=0,h=0,w=t.blank,T={buffered:1},E=0;function _(e){t.global.ue_csa_ss_tag||t.emit("$csmTag:"+e,0,T)}function x(e){g.push({t:p(),m:e})}function A(e){m.push({t:p(),m:e}),E||_(f+"Active"),E=h=1,n&&n()}function B(){h&&(y.push({t:p(),y:O}),O=c.pageYOffset,h=0)}function L(e){v=e,(s=new c[r](A))[u](d,{childList:!0,subtree:!0}),(i=new c[r](x))[u](d,{attributes:!0,subtree:!0,attributeFilter:["src"],attributeOldValue:!0}),w=t.on(c,a,B,{passive:!0})}p&&c[r]?(_(f+"Yes"),l?c[e]&&~(c[e].supportedEntryTypes||[]).indexOf("paint")?new c[e](function(e){L(((e.getEntries()||[])[0]||{}).startTime||p())})[u]({entryTypes:["paint"],buffered:!0}):t.raf(L):L(0),t.register("SpeedIndexBuffers",{getBuffers:function(e){e&&(B(),e(v,g,m,y),s&&s[o](),i&&i[o](),w())},registerListener:function(e){n=e}})):_(f+"No")});

var ue_csa_ss_tag = false;
csa.plugin(function(b){var a=b.global,e=a.uet,f=a.uex,c=a.ue,d=a.Object,g={largestContentfulPaint:"lcp",speedIndex:"si",atfSpeedIndex:"atfsi",visuallyLoaded50:"vl50",visuallyLoaded90:"vl90",visuallyLoaded100:"vl100"},k="perfNo perfYes browserQuiteFn browserQuiteUd browserQuiteLd browserQuiteMut mutObsNo mutObsYes mutObsActive startVL endVL".split(" ");b&&e&&f&&d.keys&&c&&(d.keys(g).forEach(function(h){b.on("$timing:"+h,function(a){var b=g[h];if(c.isl){var d="csa:"+b;e(b,d,void 0,a);f("at",d)}else e(b,
void 0,void 0,a)})}),a.ue_csa_ss_tag||k.forEach(function(a){b.on("$csmTag:"+a,function(){c.tag&&c.tag(a);c.isl&&f("at","csa:"+a)},{buffered:1})}))});

</script>
<script>window.ue && ue.count && ue.count('CSMLibrarySize', 13617)</script>
<!-- sp:feature:nav-inline-js -->
<!-- NAVYAAN JS -->

<script type="text/javascript">!function(n){function e(n,e){return{m:n,a:function(n){return[].slice.call(n)}(e)}}document.createElement("header");var r=function(n){function u(n,r,u){n[u]=function(){a._replay.push(r.concat(e(u,arguments)))}}var a={};return a._sourceName=n,a._replay=[],a.getNow=function(n,e){return e},a.when=function(){var n=[e("when",arguments)],r={};return u(r,n,"run"),u(r,n,"declare"),u(r,n,"publish"),u(r,n,"build"),r.depends=n,r.iff=function(){var r=n.concat([e("iff",arguments)]),a={};return u(a,r,"run"),u(a,r,"declare"),u(a,r,"publish"),u(a,r,"build"),a},r},u(a,[],"declare"),u(a,[],"build"),u(a,[],"publish"),u(a,[],"importEvent"),r._shims.push(a),a};r._shims=[],n.$Nav||(n.$Nav=r("rcx-nav")),n.$Nav.make||(n.$Nav.make=r)}(window)</script><script type="text/javascript">
$Nav.importEvent('navbarJS-beaconbelt');
$Nav.declare('img.sprite', {
  'png32': 'https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png',
  'png32-2x': 'https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/nav-sprite-global-2x-hm-dsk-reorg._CB405937547_.png'
});
$Nav.declare('img.timeline', {
  'timeline-icon-2x': 'https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/timeline_sprite_2x._CB443581191_.png'
});
window._navbarSpriteUrl = 'https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png';
$Nav.declare('img.pixel', 'https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._CB485935036_.gif');
</script>
<img src="https://images-na.ssl-images-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-hm-dsk-reorg._CB405937547_.png" style="display:none" alt="">
<script type="text/javascript">var nav_t_after_preload_sprite = + new Date();</script>
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/41uLOOuUMJL._RC|01LEzWzrPZL.js,71BDiB9DHjL.js,01QvReFeJyL.js,016tgkOMMNL.js,616P4MHT7yL.js,41gNKoK0s7L.js,115pV8Rl02L.js,21QA-szxgvL.js,11k47yUMOjL.js,41SZNgvX4oL.js,51-xVUkFLqL.js,31sq3pfde4L.js,11lEMI5MhIL.js,31DbmIB-3JL.js_.js?AUIClients/NavDesktopUberAsset&dRzb8qTH#desktop.language-en.us.375680-T1.387765-T1.365419-T1.366740-T1.310484-T1.392230-T1.403991-T1.395433-T1');
});
</script>
<!-- sp:end-feature:nav-inline-js -->
<!-- sp:feature:nav-skeleton -->
<!-- sp:end-feature:nav-skeleton -->
<!-- sp:feature:navbar -->

<!--Pilu -->


  <!-- NAVYAAN -->











<!-- navmet initial definition -->



<script type="text/javascript">
    if(window.navmet===undefined) {
      window.navmet=[];
      if (window.performance && window.performance.timing && window.ue_t0) {
        var t = window.performance.timing;
        var now = + new Date();
        window.navmet.basic = {
          'networkLatency': (t.responseStart - t.fetchStart),
          'navFirstPaint': (now - t.responseStart),
          'NavStart': (now - window.ue_t0)
        };
        window.navmet.push({key:"NavFirstPaintStart",end:+new Date(),begin:window.ue_t0});
      }
    }
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainStart",end:+new Date(),begin:window.ue_t0});
    }
</script>




<script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <script type="text/javascript">
    // Nav start should be logged at this place only if request is NOT progressively loaded.
    // For progressive loading case this metric is logged as part of skeleton.
    // Presence of skeleton signals that request is progressively loaded.
    if(!document.getElementById("navbar-skeleton")) {
      window.uet && uet('ns');
    }
    window._navbar = (function (o) {
      o.componentLoaded = o.loading = function(){};
      o.browsepromos = {};
      o.issPromos = [];
      return o;
    }(window._navbar || {}));
    window._navbar.declareOnLoad = function () { window.$Nav && $Nav.declare('page.load'); };
    if (window.addEventListener) {
      window.addEventListener("load", window._navbar.declareOnLoad, false);
    } else if (window.attachEvent) {
      window.attachEvent("onload", window._navbar.declareOnLoad);
    } else if (window.$Nav) {
      $Nav.when('page.domReady').run("OnloadFallbackSetup", function () {
        window._navbar.declareOnLoad();
      });
    }
    window.$Nav && $Nav.declare('logEvent.enabled',
      'false');

    window.$Nav && $Nav.declare('config.lightningDeals', {"activeItems":[],"marketplaceID":"ATVPDKIKX0DER","customerID":"A124BGP0M70XCG"});
  </script>

    <style mark="aboveNavInjectionCSS" type="text/css">
       #nav-flyout-searchAjax .nav-flyout-buffer-top { display: none; } div#navSwmHoliday.nav-focus {border: none;margin: 0;}
    </style>
    <script mark="aboveNavInjectionJS" type="text/javascript">
      try {
        if(window.navmet===undefined)window.navmet=[]; if(window.$Nav) { $Nav.when('$', 'config', 'flyout.accountList', 'SignInRedirect', 'dataPanel').run('accountListRedirectFix', function ($, config, flyout, SignInRedirect, dataPanel) { if (!config.accountList) { return; } flyout.getPanel().onData(function (data) { if (SignInRedirect) { var $anchors = $('[data-nav-role=signin]', flyout.elem()); $.each($anchors, function(i, anchorEl) {SignInRedirect.setRedirectUrl($(anchorEl), null, null);});}});}); $Nav.when('$').run('defineIsArray', function(jQuery) { if(jQuery.isArray===undefined) { jQuery.isArray=function(param) { if(param.length===undefined) { return false; } return true; }; } }); $Nav.declare('config.cartFlyoutDisabled', 'true'); $Nav.when('$','$F','config','logEvent','panels','phoneHome','dataPanel','flyouts.renderPromo','flyouts.sloppyTrigger','flyouts.accessibility','util.mouseOut','util.onKey','debug.param').build('flyouts.buildSubPanels',function($,$F,config,logEvent,panels,phoneHome,dataPanel,renderPromo,createSloppyTrigger,a11yHandler,mouseOutUtility,onKey,debugParam){var flyoutDebug=debugParam('navFlyoutClick');return function(flyout,event){var linkKeys=[];$('.nav-item',flyout.elem()).each(function(){var $item=$(this);linkKeys.push({link:$item,panelKey:$item.attr('data-nav-panelkey')});});if(linkKeys.length===0){return;} var visible=false;var $parent=$('<div class=\'nav-subcats\'></div>').appendTo(flyout.elem());var panelGroup=flyout.getName()+'SubCats';var hideTimeout=null;var sloppyTrigger=createSloppyTrigger($parent);var showParent=function(){if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} if(visible){return;} var height=$('#nav-flyout-shopAll').height(); $parent.css({'height': height});$parent.animate({width:'show'},{duration:200,complete:function(){$parent.css({overflow:'visible'});}});visible=true;};var hideParentNow=function(){$parent.stop().css({overflow:'hidden',display:'none',width:'auto',height:'auto'});panels.hideAll({group:panelGroup});visible=false;if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;}};var hideParent=function(){if(!visible){return;} if(hideTimeout){clearTimeout(hideTimeout);hideTimeout=null;} hideTimeout=setTimeout(hideParentNow,10);};flyout.onHide(function(){sloppyTrigger.disable();hideParentNow();this.elem().hide();});var addPanel=function($link,panelKey){var panel=dataPanel({className:'nav-subcat',dataKey:panelKey,groups:[panelGroup],spinner:false,visible:false});if(!flyoutDebug){var mouseout=mouseOutUtility();mouseout.add(flyout.elem());mouseout.action(function(){panel.hide();});mouseout.enable();} var a11y=a11yHandler({link:$link,onEscape:function(){panel.hide();$link.focus();}});var logPanelInteraction=function(promoID,wlTriggers){var logNow=$F.once().on(function(){var panelEvent=$.extend({},event,{id:promoID});if(config.browsePromos&&!!config.browsePromos[promoID]){panelEvent.bp=1;} logEvent(panelEvent);phoneHome.trigger(wlTriggers);});if(panel.isVisible()&&panel.hasInteracted()){logNow();}else{panel.onInteract(logNow);}};panel.onData(function(data){renderPromo(data.promoID,panel.elem());logPanelInteraction(data.promoID,data.wlTriggers);});panel.onShow(function(){var columnCount=$('.nav-column',panel.elem()).length;panel.elem().addClass('nav-colcount-'+columnCount);showParent();var $subCatLinks=$('.nav-subcat-links > a',panel.elem());var length=$subCatLinks.length;if(length>0){var firstElementLeftPos=$subCatLinks.eq(0).offset().left;for(var i=1;i<length;i++){if(firstElementLeftPos===$subCatLinks.eq(i).offset().left){$subCatLinks.eq(i).addClass('nav_linestart');}} if($('span.nav-title.nav-item',panel.elem()).length===0){var catTitle=$.trim($link.html());catTitle=catTitle.replace(/ref=sa_menu_top/g,'ref=sa_menu');var $subPanelTitle=$('<span class=\'nav-title nav-item\'>'+ catTitle+'</span>');panel.elem().prepend($subPanelTitle);}} $link.addClass('nav-active');});panel.onHide(function(){$link.removeClass('nav-active');hideParent();a11y.disable();sloppyTrigger.disable();});panel.onShow(function(){a11y.elems($('a, area',panel.elem()));});sloppyTrigger.register($link,panel);if(flyoutDebug){$link.click(function(){if(panel.isVisible()){panel.hide();}else{panel.show();}});} var panelKeyHandler=onKey($link,function(){if(this.isEnter()||this.isSpace()){panel.show();}},'keydown',false);$link.focus(function(){panelKeyHandler.bind();}).blur(function(){panelKeyHandler.unbind();});panel.elem().appendTo($parent);};var hideParentAndResetTrigger=function(){hideParent();sloppyTrigger.disable();};for(var i=0;i<linkKeys.length;i++){var item=linkKeys[i];if(item.panelKey){addPanel(item.link,item.panelKey);}else{item.link.mouseover(hideParentAndResetTrigger);}}};});};
      } catch ( err ) {
        if ( window.$Nav ) {
          window.$Nav.when('metrics', 'logUeError').run(function(metrics, log) {
            metrics.increment('NavJS:AboveNavInjection:error');
            log(err.toString(), {
              'attribution': 'rcx-nav',
              'logLevel': 'FATAL'
            });
          });
        }
      }
    </script>

  <noscript>
    <style type="text/css"><!--
      #navbar #nav-shop .nav-a:hover {
        color: #ff9900;
        text-decoration: underline;
      }
      #navbar #nav-search .nav-search-facade,
      #navbar #nav-tools .nav-icon,
      #navbar #nav-shop .nav-icon,
      #navbar #nav-subnav .nav-hasArrow .nav-arrow {
        display: none;
      }
      #navbar #nav-search .nav-search-submit,
      #navbar #nav-search .nav-search-scope {
        display: block;
      }
      #nav-search .nav-search-scope {
        padding: 0 5px;
      }
      #navbar #nav-search .nav-search-dropdown {
        position: relative;
        top: 5px;
        height: 23px;
        font-size: 14px;
        opacity: 1;
        filter: alpha(opacity = 100);
      }
    --></style>
 </noscript>
<script type="text/javascript">window.navmet.push({key:'PreNav',end:+new Date(),begin:window.navmet.tmp});</script>

<a id="nav-top"></a>







<a id="skiplink" tabindex="0" class="skip-link">Skip to main content</a>

<script type="text/javascript">window.navmet.tmp=+new Date();</script>
<!-- Navyaan Upnav -->
    <div id="nav-upnav" aria-hidden="true">
      <!-- unw1 failed -->
      
    </div>
<script type="text/javascript">window.navmet.push({key:'UpNav',end:+new Date(),begin:window.navmet.tmp});</script>


<script type="text/javascript">window.navmet.main=+new Date();</script>



<header id="navbar-main" class="nav-opt-sprite nav-flex nav-locale-us nav-lang-en nav-ssl nav-rec nav-progressive-attribute">

   
  <div id="navbar" cel_widget_id="Navigation-desktop-navbar" role="navigation" class="nav-sprite-v1 celwidget nav-bluebeacon nav-a11y-t1 bold-focus-hover layout2 nav-flex layout3 layout3-alt nav-fresh nav-packard-glow hamburger nav-progressive-attribute using-mouse" data-csa-c-id="au7qur-31tvjj-w2qm64-r1j8dt" data-cel-widget="Navigation-desktop-navbar">
    
    <div id="nav-belt">
      <div class="nav-left">
        <script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <div id="nav-logo" class="nav-prime-1 nav-progressive-attribute">
    <a href="/ref=nav_logo" id="nav-logo-sprites" class="nav-logo-link nav-progressive-attribute" aria-label="Amazon">
      <span class="nav-sprite nav-logo-base"></span>
      <span id="logo-ext" class="nav-sprite nav-logo-ext nav-progressive-content"></span>
      <span class="nav-logo-locale">.us</span>
    </a>
 <div id="nav-tagline" class="nav-progressive-content">
  <a href="/ref=nav_logo_prime" aria-label="Prime" class="nav-sprite nav-logo-tagline">
    
  </a>
</div>
  </div>
<script type="text/javascript">window.navmet.push({key:'Logo',end:+new Date(),begin:window.navmet.tmp});</script>
        
<div id="nav-global-location-slot">
    <span id="nav-global-location-data-modal-action" class="a-declarative nav-progressive-attribute" data-a-modal="{&quot;width&quot;:375, &quot;closeButton&quot;:&quot;false&quot;,&quot;popoverLabel&quot;:&quot;Choose your location&quot;, &quot;ajaxHeaders&quot;:{&quot;anti-csrftoken-a2z&quot;:&quot;gMRZ/Y+P8Diacj9ZwkJ3Z9rKdgSnDU6wtEaIBxcAAAAMAAAAAGImjOFyYXcAAAAA;hNAInQG9m+vnB6XTp5B4jPHwIHfEqe06OsKodFqNHYVuAAAAAGImjOEAAAAB&quot;}, &quot;name&quot;:&quot;glow-modal&quot;, &quot;url&quot;:&quot;/portal-migration/hz/glow/get-rendered-address-selections?deviceType=desktop&amp;pageType=Landing&amp;storeContext=books&amp;actionSource=desktop-modal&quot;, &quot;footer&quot;:&quot;<span class=\&quot;a-declarative\&quot; data-action=\&quot;a-popover-close\&quot; data-a-popover-close=\&quot;{}\&quot;><span class=\&quot;a-button a-button-primary\&quot;><span class=\&quot;a-button-inner\&quot;><button name=\&quot;glowDoneButton\&quot; class=\&quot;a-button-text\&quot; type=\&quot;button\&quot;>Done</button></span></span></span>&quot;,&quot;header&quot;:&quot;Choose your location&quot;}" data-action="a-modal">
        <a id="nav-global-location-popover-link" class="nav-a nav-a-2 a-popover-trigger a-declarative nav-progressive-attribute" tabindex="0">
            <div class="nav-sprite nav-progressive-attribute" id="nav-packard-glow-loc-icon"></div>
            <div id="glow-ingress-block">
                <span class="nav-line-1 nav-progressive-content" id="glow-ingress-line1">
                   Deliver to Ana
                </span>
                <span class="nav-line-2 nav-progressive-content" id="glow-ingress-line2">
                   Seattle 98107‌
                </span>
            </div>
        </a>
        </span>
        <input data-addnewaddress="add-new" id="unifiedLocation1ClickAddress" name="dropdown-selection" type="hidden" value="kkjjoumllpkq" class="nav-progressive-attribute">
        <input data-addnewaddress="add-new" id="ubbShipTo" name="dropdown-selection-ubb" type="hidden" value="kkjjoumllpkq" class="nav-progressive-attribute">
        <input id="glowValidationToken" name="glow-validation-token" type="hidden" value="gMRZ/Y+P8Diacj9ZwkJ3Z9rKdgSnDU6wtEaIBxcAAAAMAAAAAGImjOFyYXcAAAAA;hNAInQG9m+vnB6XTp5B4jPHwIHfEqe06OsKodFqNHYVuAAAAAGImjOEAAAAB" class="nav-progressive-attribute">
</div>

<div id="nav-global-location-toaster-script-container" class="nav-progressive-content">
</div>

      </div>
          <div class="nav-fill">
            <script type="text/javascript">window.navmet.tmp=+new Date();</script>
<div id="nav-search">
  <div id="nav-bar-left"></div>
  <form id="nav-search-bar-form" accept-charset="utf-8" action="/s/ref=nb_sb_noss" class="nav-searchbar nav-progressive-attribute" method="GET" name="site-search" role="search">

    <div class="nav-left">
      <div id="nav-search-dropdown-card">
        
  <div class="nav-search-scope nav-sprite">
    <div class="nav-search-facade" data-value="search-alias=aps">
      <span id="nav-search-label-id" class="nav-search-label nav-progressive-content" style="width: auto;">Books</span>
      <i class="nav-icon"></i>
    </div>
    <span id="searchDropdownDescription" class="nav-progressive-attribute" style="display:none">Select the department you want to search in</span>
    <select aria-describedby="searchDropdownDescription" class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown" data-nav-digest="47FT/CSgacNvYbeET+YSzLNPKsk=" data-nav-selected="17" id="searchDropdownBox" name="url" style="display: block; top: 2.5px;" tabindex="0" title="Search in">
        <option value="search-alias=aps">All Departments</option>
        <option value="search-alias=alexa-skills">Alexa Skills</option>
        <option value="search-alias=allthebestpets">All The Best Pets</option>
        <option value="search-alias=amazon-devices">Amazon Devices</option>
        <option value="search-alias=live-explorations">Amazon Explore</option>
        <option value="search-alias=amazonfresh">Amazon Fresh</option>
        <option value="search-alias=amazon-pharmacy">Amazon Pharmacy</option>
        <option value="search-alias=warehouse-deals">Amazon Warehouse</option>
        <option value="search-alias=appliances">Appliances</option>
        <option value="search-alias=mobile-apps">Apps &amp; Games</option>
        <option value="search-alias=arts-crafts">Arts, Crafts &amp; Sewing</option>
        <option value="search-alias=audible">Audible Books &amp; Originals</option>
        <option value="search-alias=automotive">Automotive Parts &amp; Accessories</option>
        <option value="search-alias=courses">AWS Courses</option>
        <option value="search-alias=baby-products">Baby</option>
        <option value="search-alias=bartelldrugs">Bartell Drugs</option>
        <option value="search-alias=beauty">Beauty &amp; Personal Care</option>
        <option selected="selected" current="parent" value="search-alias=stripbooks">Books</option>
        <option value="search-alias=popular">CDs &amp; Vinyl</option>
        <option value="search-alias=mobile">Cell Phones &amp; Accessories</option>
        <option value="search-alias=fashion">Clothing, Shoes &amp; Jewelry</option>
        <option value="search-alias=fashion-womens">&nbsp;&nbsp;&nbsp;Women</option>
        <option value="search-alias=fashion-mens">&nbsp;&nbsp;&nbsp;Men</option>
        <option value="search-alias=fashion-girls">&nbsp;&nbsp;&nbsp;Girls</option>
        <option value="search-alias=fashion-boys">&nbsp;&nbsp;&nbsp;Boys</option>
        <option value="search-alias=fashion-baby">&nbsp;&nbsp;&nbsp;Baby</option>
        <option value="search-alias=collectibles">Collectibles &amp; Fine Art</option>
        <option value="search-alias=computers">Computers</option>
        <option value="search-alias=financial">Credit and Payment Cards</option>
        <option value="search-alias=edu-alt-content">Digital Educational Resources</option>
        <option value="search-alias=digital-music">Digital Music</option>
        <option value="search-alias=electronics">Electronics</option>
        <option value="search-alias=lawngarden">Garden &amp; Outdoor</option>
        <option value="search-alias=gift-cards">Gift Cards</option>
        <option value="search-alias=grocery">Grocery &amp; Gourmet Food</option>
        <option value="search-alias=handmade">Handmade</option>
        <option value="search-alias=hpc">Health, Household &amp; Baby Care</option>
        <option value="search-alias=local-services">Home &amp; Business Services</option>
        <option value="search-alias=garden">Home &amp; Kitchen</option>
        <option value="search-alias=industrial">Industrial &amp; Scientific</option>
        <option value="search-alias=prime-exclusive">Just for Prime</option>
        <option value="search-alias=digital-text">Kindle Store</option>
        <option value="search-alias=fashion-luggage">Luggage &amp; Travel Gear</option>
        <option value="search-alias=luxury">Luxury Stores</option>
        <option value="search-alias=magazines">Magazine Subscriptions</option>
        <option value="search-alias=movies-tv">Movies &amp; TV</option>
        <option value="search-alias=mi">Musical Instruments</option>
        <option value="search-alias=office-products">Office Products</option>
        <option value="search-alias=pets">Pet Supplies</option>
        <option value="search-alias=luxury-beauty">Premium Beauty</option>
        <option value="search-alias=instant-video">Prime Video</option>
        <option value="search-alias=smart-home">Smart Home</option>
        <option value="search-alias=software">Software</option>
        <option value="search-alias=sporting">Sports &amp; Outdoors</option>
        <option value="search-alias=specialty-aps-sns">Subscribe &amp; Save</option>
        <option value="search-alias=subscribe-with-amazon">Subscription Boxes</option>
        <option value="search-alias=tools">Tools &amp; Home Improvement</option>
        <option value="search-alias=toys-and-games">Toys &amp; Games</option>
        <option value="search-alias=under-ten-dollars">Under $10</option>
        <option value="search-alias=videogames">Video Games</option>
        <option value="search-alias=wholefoods">Whole Foods Market</option>
    </select>
  </div>

      </div>
    </div>
    <div class="nav-fill">
      <div class="nav-search-field ">
        <input type="text" id="twotabsearchtextbox" value="" name="field-keywords" autocomplete="off" placeholder="" class="nav-input nav-progressive-attribute" dir="auto" tabindex="0" aria-label="Search">
      </div>
      <div id="nav-iss-attach"></div>
    </div>
    <div class="nav-right">
      <div class="nav-search-submit nav-sprite">
        <span id="nav-search-submit-text" class="nav-search-submit-text nav-sprite nav-progressive-attribute" aria-label="Go">
          <input id="nav-search-submit-button" type="submit" class="nav-input nav-progressive-attribute" value="Go" tabindex="0">
        </span>
      </div>
    </div>
  </form>
</div>
<script type="text/javascript">window.navmet.push({key:'Search',end:+new Date(),begin:window.navmet.tmp});</script>
          </div>
      <div class="nav-right">
          <script type="text/javascript">window.navmet.tmp=+new Date();</script>
          <div id="nav-tools" class="layoutToolbarPadding">
              
              
              
              
  <a href="/gp/customer-preferences/select-language/ref=topnav_lang?ie=UTF8&amp;preferencesReturnUrl=%2Fb%3Fnode%3D283155%26ref_%3Dnav_ya_signin%26" id="icp-nav-flyout" class="nav-a nav-a-2 icp-link-style-2" aria-label="Choose a language for shopping.">
    <span class="icp-nav-link-inner">
      <span class="nav-line-1">
      </span>
      <span class="nav-line-2">
        <span class="icp-nav-flag icp-nav-flag-us"></span>
        <span class="nav-icon nav-arrow" style="visibility: visible;"></span>
      </span>
    </span>
  </a>

              
  <a href="https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_btn" class="nav-a nav-a-2 nav-truncate   nav-progressive-attribute" data-nav-ref="nav_youraccount_btn" data-nav-role="signin" data-ux-jq-mouseenter="true" id="nav-link-accountList" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-accountList" data-csa-c-content-id="nav_youraccount_btn" data-csa-c-id="7q9xf8-9jc1u-4rfj6z-ys6tk8">
  <div class="nav-line-1-container"><span id="nav-link-accountList-nav-line-1" class="nav-line-1 nav-progressive-content">Hello, Ana</span></div>
  <span class="nav-line-2 ">Account &amp; Lists<span class="nav-icon nav-arrow" style="visibility: visible;"></span>
  </span>
</a>

<a href="/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&amp;signIn=1&amp;useRedirectOnSuccess=1&amp;action=sign-out&amp;ref_=nav_signout" class="nav-hidden-aria  " tabindex="0">
  Not Ana? Sign Out
</a>

              
<a href="/gp/css/order-history?ref_=nav_orders_first" class="nav-a nav-a-2   nav-progressive-attribute" id="nav-orders" tabindex="0">
  <span class="nav-line-1">Returns</span>
  <span class="nav-line-2">&amp; Orders</span>
</a>

              
              
  <a href="/gp/cart/view.html?ref_=nav_cart" aria-label="0 items in cart" class="nav-a nav-a-2 nav-progressive-attribute" id="nav-cart">
    <div id="nav-cart-count-container">
      <span id="nav-cart-count" aria-hidden="true" class="nav-cart-count nav-cart-0 nav-progressive-attribute nav-progressive-content">0</span>
      <span class="nav-cart-icon nav-sprite"></span>
    </div>
    <div id="nav-cart-text-container" class=" nav-progressive-attribute">
      <span aria-hidden="true" class="nav-line-1">
        
      </span>
      <span aria-hidden="true" class="nav-line-2">
        Cart
        <span class="nav-icon nav-arrow"></span>
      </span>
    </div>
  </a>

          </div>
          <script type="text/javascript">window.navmet.push({key:'Tools',end:+new Date(),begin:window.navmet.tmp});</script>

      </div>
    </div><div id="nav-flyout-iss-anchor"><div id="nav-flyout-searchAjax" class="nav-issFlyout nav-flyout"><div class="nav-template nav-flyout-content"></div><div class="autocomplete-results-container"></div></div></div><div id="nav-flyout-anchor"><div class="nav-ewc-arrow"></div><div id="nav-flyout-prime" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-amazonprime" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-accountList" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content"><div id="nav-al-container"><div id="nav-al-wishlist" class="nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility"><div class="nav-title" id="nav-al-title">Your Lists</div><div class="nav-template have-bot-border nav-spinner" id="nav-flyout-wl-items" style="display: none;"></div><a href="/hz/wishlist/ls?triggerElementID=createList&amp;ref_=nav_ListFlyout_navFlyout_createList_lv_redirect" class="nav-link nav-item"><span class="nav-text">Create a List</span></a> <a href="/registries?ref_=nav_ListFlyout_find" class="nav-link nav-item"><span class="nav-text">Find a List or Registry</span></a> <a href="/gp/clpf?ref_=nav_ListFlyout_smi_se_ya_lll_ll" class="nav-link nav-item"><span class="nav-text">AmazonSmile Charity Lists</span></a><div class="nav-template" id="nav-flyout-wl-alexa" style="display: none;"></div></div><div id="nav-al-your-account" class="nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility"><div class="nav-title">Your Account</div><a href="/gp/css/homepage.html?ref_=nav_AccountFlyout_ya" class="nav-link nav-item"><span class="nav-text">Account</span></a> <a id="nav_prefetch_yourorders" href="/gp/css/order-history?ref_=nav_AccountFlyout_orders" class="nav-link nav-item"><span class="nav-text">Orders</span></a> <a href="/gp/yourstore?ref_=nav_AccountFlyout_recs" class="nav-link nav-item"><span class="nav-text">Recommendations</span></a> <a href="/gp/history?ref_=nav_AccountFlyout_browsinghistory" class="nav-link nav-item"><span class="nav-text">Browsing History</span></a> <a href="/gp/video/watchlist?ref_=nav_AccountFlyout_ywl" class="nav-link nav-item"><span class="nav-text">Watchlist</span></a> <a href="/gp/video/library?ref_=nav_AccountFlyout_yvl" class="nav-link nav-item"><span class="nav-text">Video Purchases &amp; Rentals</span></a> <a href="/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku" class="nav-link nav-item"><span class="nav-text">Kindle Unlimited</span></a> <a href="/hz/mycd/myx?pageType=content&amp;ref_=nav_AccountFlyout_myk" class="nav-link nav-item"><span class="nav-text">Content &amp; Devices</span></a> <a href="/gp/subscribe-and-save/manager/viewsubscriptions?ref_=nav_AccountFlyout_sns" class="nav-link nav-item"><span class="nav-text">Subscribe &amp; Save Items</span></a> <a href="/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions" class="nav-link nav-item"><span class="nav-text">Memberships &amp; Subscriptions</span></a> <a href="/gp/gc/balance?ref_=nav_item_yourgcbalance" class="nav-link nav-item"><span class="nav-text">Gift Card Balance</span></a> <a href="/gp/subs/primeclub/account/homepage.html?ref_=nav_AccountFlyout_prime" class="nav-link nav-item"><span class="nav-text">Prime Membership</span></a> <a href="https://www.amazon.com/credit/landing?ref_=nav_AccountFlyout_ya_amazon_cc_landing_ms" class="nav-link nav-item"><span class="nav-text">Amazon Credit Cards</span></a> <a href="https://music.amazon.com?ref=nav_youraccount_cldplyr" class="nav-link nav-item"><span class="nav-text">Music Library</span></a> <a href="/b/?node=12766669011&amp;ld=AZUSSOA-yaflyout&amp;ref_=nav_AccountFlyout_cs_sell" class="nav-link nav-item"><span class="nav-text">Start a Selling Account</span></a> <a href="/gp/browse.html?node=11261610011&amp;ref_=nav_AccountFlyout_b2b_reg" class="nav-link nav-item"><span class="nav-text">Register for a Business Account</span></a> <a id="nav-item-switch-account" href="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%2F%3Fie%3DUTF8%26node%3D283155%26ref_%3Dnav_youraccount_switchacct&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=usflex&amp;openid.mode=checkid_setup&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;switch_account=picker&amp;ignoreAuthState=1&amp;_encoding=UTF8" class="nav-link nav-item"><span class="nav-text">Switch Accounts</span></a> <a id="nav-item-signout" href="/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&amp;useRedirectOnSuccess=1&amp;signIn=1&amp;action=sign-out&amp;ref_=nav_AccountFlyout_signout" class="nav-link nav-item"><span class="nav-text">Sign Out</span></a></div></div></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-amazonfresh" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-groceries" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-transientFlyout" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abAcquisition" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abActivation" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abAccountLink" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatAcquisition" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatActivation" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-abCatAccountLink" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-timeline" class="nav-coreFlyout nav-fullWidthFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-icp" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div><div id="nav-flyout-icp-footer-flyout" class="nav-coreFlyout nav-flyout"><div class="nav-arrow"><div class="nav-arrow-inner"></div></div><div class="nav-template nav-flyout-content nav-spinner"></div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div></div>
    <div id="nav-main" class="nav-sprite">
      <div class="nav-left">
        <script type="text/javascript">window.navmet.tmp=+new Date();</script>
  <a href="javascript: void(0)" id="nav-hamburger-menu" role="button" aria-label="Open Menu" data-csa-c-type="widget" data-csa-c-slot-id="HamburgerMenuDesktop" data-csa-c-interaction-events="click" data-csa-c-id="svkt86-lqwdor-9v1s6t-v9q5oc">
    <i class="hm-icon nav-sprite"></i>
    <span class="hm-icon-label">All</span>
  </a>
  
<script type="text/javascript">
  var hmenu = document.getElementById("nav-hamburger-menu");
  hmenu.setAttribute("href", "javascript: void(0)");
  window.navHamburgerMetricLogger = function() {
    if (window.ue && window.ue.count) {
      var metricName = "Nav:Hmenu:IconClickActionPending";
      window.ue.count(metricName, (ue.count(metricName) || 0) + 1);
    }
    window.$Nav && $Nav.declare("navHMenuIconClicked",!0);
    window.$Nav && $Nav.declare("navHMenuIconClickedNotReadyTimeStamp", Date.now());
  };
  hmenu.addEventListener("click", window.navHamburgerMetricLogger);
  window.$Nav && $Nav.declare('hamburgerMenuIconAvailableOnLoad', false);
</script>  
<script type="text/javascript">window.navmet.push({key:'HamburgerMenuIcon',end:+new Date(),begin:window.navmet.tmp});</script>
        
        
        
        
      </div>
      <div class="nav-fill">
        
          
 <div id="nav-shop">
 </div>
          <div id="nav-xshop-container">
            <div id="nav-xshop" class="nav-progressive-content">
              <script type="text/javascript">window.navmet.tmp=+new Date();</script>
<a href="/Amazon-Video/b/?ie=UTF8&amp;node=2858778011&amp;ref_=nav_cs_prime_video" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_0" data-csa-c-content-id="nav_cs_prime_video" data-csa-c-id="4a8bs-207301-crw9qs-r70dcm">Prime Video</a>

<a href="/deals?ref_=nav_cs_gb" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_1" data-csa-c-content-id="nav_cs_gb" data-csa-c-id="fwbvo7-pby77l-qncow3-z99qwo">Today's Deals</a>

<a href="/gp/browse.html?node=16115931011&amp;ref_=nav_cs_registry" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_2" data-csa-c-content-id="nav_cs_registry" data-csa-c-id="p8njar-ca9ur0-ygf7ys-rx96y1">Registry</a>

<a href="/gcx/Gifts-for-Everyone/gfhz/?ref_=nav_cs_giftfinder" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_3" data-csa-c-content-id="nav_cs_giftfinder" data-csa-c-id="9879md-dny8ly-5a2dq3-vzy5i7">Find a Gift</a>

<a href="/b/?node=17867753011&amp;ref_=nav_cs_shoppertoolkit" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_4" data-csa-c-content-id="nav_cs_shoppertoolkit" data-csa-c-id="yoip8a-104d96-qemjwi-hbcw5h">Shopper Toolkit</a>

<a href="/gp/buyagain?ie=UTF8&amp;ref_=nav_cs_buy_again" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_5" data-csa-c-content-id="nav_cs_buy_again" data-csa-c-id="mr3laz-12hsm8-1jz9sn-1n5jbd">Buy Again</a>

<a href="/Coupons/b/?_encoding=UTF8&amp;node=2231352011&amp;ref_=nav_cs_coupons" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_6" data-csa-c-content-id="nav_cs_coupons" data-csa-c-id="14keev-m250f8-bj6n23-71bif5">Coupons</a>

<a href="/fmc/learn-more?ref_=nav_cs_groceries" class="nav-a  " data-ux-jq-mouseenter="true" id="nav-link-groceries" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-groceries" data-csa-c-content-id="nav_cs_groceries" data-csa-c-id="lgf1to-dzrho4-gxfurq-rs3weu"><span>Groceries</span><span class="nav-icon nav-arrow" style="visibility: visible;"></span></a>

<a href="/health-personal-care-nutrition-fitness/b/?ie=UTF8&amp;node=3760901&amp;ref_=nav_cs_hpc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_8" data-csa-c-content-id="nav_cs_hpc" data-csa-c-id="uabr13-2uz3eu-4fwtm8-p8gr4">Health &amp; Household</a>

<a href="/gift-cards/b/?ie=UTF8&amp;node=2238192011&amp;ref_=nav_cs_gc" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_9" data-csa-c-content-id="nav_cs_gc" data-csa-c-id="34nwhh-34ruo5-qm303l-p5qdwl">Gift Cards</a>

<a href="https://pharmacy.amazon.com/?ref_=nav_cs_pharmacy" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_10" data-csa-c-content-id="nav_cs_pharmacy" data-csa-c-id="5bbw30-4ey7ar-o5f7h5-3l93kp">Pharmacy</a>

<a href="/live?ref_=nav_cs_amazonlive" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_11" data-csa-c-content-id="nav_cs_amazonlive" data-csa-c-id="vate1j-cekq02-1xogxh-cyfkz9">Livestreams</a>

<a href="/Beauty-Makeup-Skin-Hair-Products/b/?ie=UTF8&amp;node=3760911&amp;ref_=nav_cs_beauty" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_12" data-csa-c-content-id="nav_cs_beauty" data-csa-c-id="579egn-3uk8f2-2jynfy-j7oy9v">Beauty &amp; Personal Care</a>

<a href="/gp/help/customer/display.html?nodeId=508510&amp;ref_=nav_cs_help" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_13" data-csa-c-content-id="nav_cs_help" data-csa-c-id="zcabm0-v68u4u-uaft4t-fz35x2">Customer Service</a>

<a href="/Launchpad/b/?ie=UTF8&amp;node=12034488011&amp;ref_=nav_cs_launchpad" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_14" data-csa-c-content-id="nav_cs_launchpad" data-csa-c-id="gy4je6-fe41p5-9qqtlg-9qc700">Amazon Launchpad</a>

<a id="nav-your-amazon" href="/gp/yourstore/home?ref_=nav_cs_ys" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_15" data-csa-c-content-id="nav_cs_ys" data-csa-c-id="xbouep-7eg4ub-79r85s-pi9r2i"><span id="nav-your-amazon-text"><span class="nav-shortened-name">Ana</span>'s Amazon.com</span></a>

<a href="/stores/node/20648519011?channel=discovbar?field-lbr_brands_browse-bin=AmazonBasics&amp;ref_=nav_cs_amazonbasics" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_16" data-csa-c-content-id="nav_cs_amazonbasics" data-csa-c-id="m4mo7x-xcg449-47qfld-n815fc">Amazon Basics</a>

<a href="/gp/history?ref_=nav_cs_timeline" class="nav-a  " data-ux-jq-mouseenter="true" id="nav-recently-viewed" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-recently-viewed" data-csa-c-content-id="nav_cs_timeline" data-csa-c-id="x0taqw-a3gwlc-n5bfgh-4t30lo"><span>Browsing History</span><span class="nav-icon nav-arrow" style="visibility: visible;"></span></a>

<a href="/luxurystores?ref_=nav_cs_luxury" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_18" data-csa-c-content-id="nav_cs_luxury" data-csa-c-id="blc9bd-69sg4l-cpuzvo-v4dap4">Luxury Stores</a>

<a href="/Tools-and-Home-Improvement/b/?ie=UTF8&amp;node=228013&amp;ref_=nav_cs_hi" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_19" data-csa-c-content-id="nav_cs_hi" data-csa-c-id="h6ruf3-hrbl0b-acn2k3-7efxfk">Home Improvement</a>

<a href="/pet-shops-dogs-cats-hamsters-kittens/b/?ie=UTF8&amp;node=2619533011&amp;ref_=nav_cs_pets" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_20" data-csa-c-content-id="nav_cs_pets" data-csa-c-id="25uljj-t1crfx-f34fnx-3ulqhl">Pet Supplies</a>

<a href="/Smart-Home/b/?ie=UTF8&amp;node=6563140011&amp;ref_=nav_cs_smart_home" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_21" data-csa-c-content-id="nav_cs_smart_home" data-csa-c-id="61ejby-ur251v-uyupey-niincb">Smart Home</a>

<a href="/amazon-fashion/b/?ie=UTF8&amp;node=7141123011&amp;ref_=nav_cs_fashion" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_22" data-csa-c-content-id="nav_cs_fashion" data-csa-c-id="d97avs-klbusd-s3g4jk-5rgbyg">Fashion</a>

<a href="/auto-deliveries/landing?ref_=nav_cs_sns" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_23" data-csa-c-content-id="nav_cs_sns" data-csa-c-id="m44cqr-71mvlw-ilan1n-tjqxr5">Subscribe &amp; Save</a>

<a href="/books-used-books-textbooks/b/?ie=UTF8&amp;node=283155&amp;ref_=nav_cs_books" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_24" data-csa-c-content-id="nav_cs_books" data-csa-c-id="2mypx9-4ow7q1-qlya32-nf9rrc">Books</a>

<a href="/prime?ref_=nav_cs_primelink_member" class="nav-a  " data-ux-jq-mouseenter="true" id="nav-link-prime" tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav-link-prime" data-csa-c-content-id="nav_cs_primelink_member" data-csa-c-id="rl3zu7-akz9b3-ynxe2a-itgw5r"><span>Prime</span><span class="nav-icon nav-arrow" style="visibility: visible;"></span></a>

<a href="/home-garden-kitchen-furniture-bedding/b/?ie=UTF8&amp;node=1055398&amp;ref_=nav_cs_home" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_26" data-csa-c-content-id="nav_cs_home" data-csa-c-id="638xpm-wzo6gv-1u8ieu-542tac">Amazon Home</a>

<a href="/Handmade/b/?ie=UTF8&amp;node=11260432011&amp;ref_=nav_cs_handmade" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_27" data-csa-c-content-id="nav_cs_handmade" data-csa-c-id="vwo4kz-8ra48t-xg9163-rnu1hk">Handmade</a>

<a href="/tv-video/b/?ie=UTF8&amp;node=1266092011&amp;ref_=nav_cs_tv" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_28" data-csa-c-content-id="nav_cs_tv" data-csa-c-id="dwg4eq-7jteaf-4ybf68-douruh">TV &amp; Video</a>

<a href="/automotive-auto-truck-replacements-parts/b/?ie=UTF8&amp;node=15684181&amp;ref_=nav_cs_automotive" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_29" data-csa-c-content-id="nav_cs_automotive" data-csa-c-id="ghgl53-kvi0dq-64du0j-xjpn05">Automotive</a>

<a href="/computer-video-games-hardware-accessories/b/?ie=UTF8&amp;node=468642&amp;ref_=nav_cs_video_games" class="nav-a  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_30" data-csa-c-content-id="nav_cs_video_games" data-csa-c-id="dm4ta9-lamvpm-hvwz9g-yr2x2c">Video Games</a>

<a href="/gp/help/customer/accessibility" aria-label="Click to call our Disability Customer Support line, or reach us directly at 1-888-283-1678" class="nav-hidden-aria  " tabindex="0" data-csa-c-type="link" data-csa-c-slot-id="nav_cs_31" data-csa-c-id="qkdt8b-jlrf7s-rzhlok-gv2m9p">Disability Customer Support</a>
<script type="text/javascript">window.navmet.push({key:'CrossShop',end:+new Date(),begin:window.navmet.tmp});</script>
            </div>
          </div>
        
      </div>
      <div class="nav-right">
          <script type="text/javascript">window.navmet.tmp=+new Date();</script><!-- Navyaan SWM -->
<div id="nav-swmslot" class="nav-swm-text-widget">
  <a href="/b/w/?_encoding=UTF8&amp;node=17964635011&amp;ref_=nav_swm_SBE_WHM22_SWM1&amp;pf_rd_p=6b5ce80f-017f-4b33-9896-168b6489b661&amp;pf_rd_s=nav-sitewide-msg-text&amp;pf_rd_t=4201&amp;pf_rd_i=navbar-4201&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ" id="swm-link" class="nav_a nav-swm-text nav-progressive-attribute nav-progressive-content" tabindex="0">Celebrate Women's History Month</a>
</div><script type="text/javascript">window.navmet.push({key:'SWM',end:+new Date(),begin:window.navmet.tmp});</script>
      </div>
    </div>

    <div id="nav-subnav-toaster"></div>

    
    <div id="nav-progressive-subnav">
      <script type="text/javascript">window.navmet.tmp=+new Date();</script>
<div id="nav-subnav" data-category="books">
  <a href="/books-used-books-textbooks/b/?ie=UTF8&amp;node=283155&amp;ref_=topnav_storetab_b" class="nav-a nav-b" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Books
      
    </span>
  </a>
  <a href="/Advanced-Search-Books/b/?ie=UTF8&amp;node=241582011&amp;ref_=sv_b_1" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Advanced Search
      
    </span>
  </a>
  <a href="/gp/new-releases/books/?ie=UTF8&amp;ref_=sv_b_2" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      New Releases
      
    </span>
  </a>
  <a href="/b/?ie=UTF8&amp;node=16857165011&amp;ref_=sv_b_3" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Best Sellers &amp; More
      
    </span>
  </a>
  <a href="/Childrens-Books/b/?ie=UTF8&amp;node=4&amp;ref_=sv_b_4" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Children's Books
      
    </span>
  </a>
  <a href="/New-Used-Textbooks-Books/b/?ie=UTF8&amp;node=465600&amp;ref_=sv_b_5" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Textbooks
      
    </span>
  </a>
  <a href="/rentals/b/?ie=UTF8&amp;node=17853655011&amp;ref_=sv_b_6" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Textbook Rentals
      
    </span>
  </a>
  <a href="/b/?ie=UTF8&amp;node=390919011&amp;ref_=sv_b_7" class="nav-a" data-nav-link-bold="1" data-nav-link-highlight="1" data-nav-link-color="#e47911" tabindex="0">
    <span class="nav-a-content">
      Best Books of the Month
      
    </span>
  </a>
<!-- nav-linktree-subnav - 'books' -->
</div>

<script type="text/javascript">window.navmet.push({key:'Subnav',end:+new Date(),begin:window.navmet.tmp});</script>
    </div>

    <script type="text/javascript">
(function() {
  var viewportWidth = function() {
    return window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;
  };

  if (typeof uet === 'function') {  uet('x1', 'ewc', {wb: 1}); }

  window.$Nav && $Nav.declare('config.ewc', (function() {
    var config = {"enablePersistent":true,"viewportWidthForPersistent":1400,"isEWCLogging":1,"isEWCStateExpanded":true,"EWCStateReason":"fixed","isSmallScreenEnabled":true,"isFreshCustomer":false,"errorContent":{"html":"<div class='nav-ewc-error'><span class='nav-title'>Oops!</span><p class='nav-paragraph'>There's a problem loading your cart right now.</p><a href='/gp/cart/view.html?ref_=nav_err_ewc_timeout' class='nav-action-button'><span class='nav-action-inner'>Your Cart</span></a></div>"},"url":"/cart/ewc/compact?hostPageType=Landing&hostSubPageType=BrowsePage&hostPageRID=Z0KMT1JTKBYN6W6QW6GJ&prerender=0&storeName=books","cartCount":0,"freshCartCount":0,"almCartCount":0,"primeWardrobeCartCount":0,"isCompactViewEnabled":true,"isCompactEWCRendered":true,"isWiderCompactEWCRendered":true};
    var hasAui = window.P && window.P.AUI_BUILD_DATE;
    var isRTLEnabled = (document.dir === 'rtl');
    config.pinnable = config.pinnable && hasAui;
    config.isMigrationTreatment = true;

    config.flyout = (function() {
      var navbelt = document.getElementById('nav-belt');
      var navCart = document.getElementById('nav-cart');
      var ewcFlyout = document.getElementById('nav-flyout-ewc');
      var persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-full-height-persistent-hover';
      var flyout = {};

      var getDocumentScrollTop = function() {
        return (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
      };

      var isWindow = function(obj) {
        return obj != null && obj === obj.window;
      };

      var getWindow = function(elem) {
        return isWindow(elem) ? elem : elem.nodeType === 9 && elem.defaultView;
      };

      var getOffset = function(elem) {
        if (elem.getClientRects && !elem.getClientRects().length) {
          return {top: 0};
        }

        var rect = elem.getBoundingClientRect
          ? elem.getBoundingClientRect()
          : {top: 0};

        if (rect.width || rect.height) {
          var doc = elem.ownerDocument;
          var win = getWindow(doc);
          return {
            top: rect.top + win.pageYOffset - doc.documentElement.clientTop
          };
        }
        return rect;
      };

      flyout.align = function() {
        var newTop = getOffset(navbelt).top - getDocumentScrollTop();
        ewcFlyout.style.top = (newTop > 0 ? newTop + 'px' : 0);
      };

      flyout.hide = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = '')
          : (ewcFlyout.style.right = '');
      };

      if(typeof config.isCompactEWCRendered === 'undefined') {
        if (
          (config.isSmallScreenEnabled && viewportWidth() < 1400) ||
          (config.isCompactViewEnabled && viewportWidth() >= 1400)
        ) {
          config.isCompactEWCRendered = true;
          config.isEWCStateExpanded = true;
          config.url = config.url.replace("/gp/navcart/sidebar", "/cart/ewc/compact");
        } else {
          config.isCompactEWCRendered = false;
        }
      }

      var viewportQualifyForPersistent = function () {
        return (config.isCompactEWCRendered)
          ? true
          : viewportWidth() >= 1400;
      }

      flyout.hasQualifiedViewportForPersistent = viewportQualifyForPersistent;

      var getEWCRightOffset = function() {
        if (!config.isCompactEWCRendered) {
          return 0;
        }

        var $navbelt = document.getElementById('nav-belt');
        if ($navbelt === undefined || $navbelt === null) {
          return 0;
        }

        var EWCCompactViewWidth = (config.isWiderCompactEWCRendered  && viewportWidth() >= 1280) ? 130 : 100;
        var scrollLeft = (window.pageXOffset !== undefined)
          ? window.pageXOffset
          : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
        var scrollXAxis = Math.abs(scrollLeft);
        var windowWidth = document.documentElement.clientWidth;
        var navbeltWidth = $navbelt.offsetWidth;
        var isPartOfNavbarNotVisible = (navbeltWidth + EWCCompactViewWidth) > windowWidth;

        if (isPartOfNavbarNotVisible) {
          return 0 - (navbeltWidth - scrollXAxis - windowWidth + EWCCompactViewWidth);
        } else {
          return 0;
        }
      }

      flyout.getEWCRightOffsetCssProperty = function () {
        return getEWCRightOffset() + 'px';
      }

      if (config.isCompactEWCRendered) {
        persistentClassOnBody = 'nav-ewc-persistent-hover nav-ewc-compact-view';
        if (config.isWiderCompactEWCRendered) { persistentClassOnBody += ' nav-ewc-wider-compact-view'; }
      }

      flyout.show = function() {
        isRTLEnabled
          ? (ewcFlyout.style.left = flyout.getEWCRightOffsetCssProperty())
          : (ewcFlyout.style.right = flyout.getEWCRightOffsetCssProperty());
      };

      var isIOSDevice = function() {
        return (/iPad|iPhone|iPod/.test(navigator.platform) ||
                (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) &&
                !window.MSStream;
      }

      var checkForPersistent = function() {
        if (!hasAui) {
          return { result: false, reason: 'noAui' };
        }
        if (!config.enablePersistent) {
          return { result: false, reason: 'config' };
        }
        if (!viewportQualifyForPersistent()) {
          return { result: false, reason: 'viewport' };
        }
        if (isIOSDevice()) {
          return { result: false, reason: 'iOS' };
        }
        if (!config.cartCount > 0) {
          return { result: false, reason: 'emptycart' };
        }

        return { result: true };
      };

      flyout.ableToPersist = function() {
        return checkForPersistent().result;
      };

      var persistentClassRegExp = '(?:^|\\s)' + persistentClassOnBody + '(?!\\S)';
      flyout.applyPageLayoutForPersistent = function() {
        if (!document.documentElement.className.match( new RegExp(persistentClassRegExp) )) {
          document.documentElement.className += ' ' + persistentClassOnBody;
        }
      };

      flyout.unapplyPageLayoutForPersistent = function() {
        document.documentElement.className = document.documentElement.className.replace( new RegExp(persistentClassRegExp, 'g'), '');
      };

      flyout.persist = function() {
        flyout.applyPageLayoutForPersistent();
        flyout.show();
        if (config.isCompactEWCRendered) {
          flyout.align();
        }
      };

      flyout.unpersist = function() {
        flyout.unapplyPageLayoutForPersistent();
        flyout.hide();
      };

      var resizeCallback = function() {
        if (flyout.ableToPersist()) {
          flyout.persist();
        }
        else {
          flyout.unpersist();
        }
      };

      flyout.bindEvents = function() {
        if (window.addEventListener) {
          window.addEventListener('resize', resizeCallback, false);
          if (config.isCompactEWCRendered) {
            window.addEventListener('scroll', flyout.align, false);
          }
        }
      };

      flyout.unbindEvents = function() {
        if (window.removeEventListener) {
          window.removeEventListener('resize', resizeCallback, false);
          if (config.isCompactEWCRendered) {
            window.removeEventListener('scroll', flyout.align, false);
          }
        }
      };

      var persistentCheck = checkForPersistent();

      if (persistentCheck.result) {
        flyout.persist();
        if (window.ue && ue.tag) {
          ue.tag('ewc:persist');
        }
      } else {
        if (window.ue && ue.tag) {
          ue.tag('ewc:unpersist');
          if (persistentCheck.reason === 'noAui') {
            ue.tag('ewc:unpersist:noAui');
          }
          if (persistentCheck.reason === 'viewport') {
            ue.tag('ewc:unpersist:viewport');
          }
          if (persistentCheck.reason === 'emptycart') {
            ue.tag('ewc:unpersist:emptycart');
          }
          if (persistentCheck.reason === 'iOS') {
            ue.tag('ewc:unpersist:iOS');
          }
        }
      }

      if (window.ue && ue.tag)  {
        if (flyout.hasQualifiedViewportForPersistent()) {
          ue.tag('ewc:bview');
        }
        else {
          ue.tag('ewc:sview');
        }
      }
      flyout.bindEvents();

      return flyout;
    }());

    return config;
  }()));

  if (typeof uet === 'function') {
    uet('x2', 'ewc', {wb: 1});
    (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('navCF').execute(function() {
      uet('bb', 'ewc', {wb: 1});
    });
  }

  if (window.ue && ue.tag) {
    ue.tag('ewc');
    ue.tag('ewc:prime');
    ue.tag('ewc:cartsize:0');

    if ( window.P && window.P.AUI_BUILD_DATE ) {
      ue.tag('ewc:aui');
    } else {
      ue.tag('ewc:noAui');
    }
  }
}());
</script>
  <div id="nav-flyout-ewc" aria-hidden="true" tabindex="-1" class="nav-ewc-lazy-align nav-ewcFlyout nav-flyout nav-locked" style="top: 0px; height: 821px;"><div class="nav-flyout-body ewc-beacon"><div class="nav-ewc-content"></div></div><div class="nav-template nav-flyout-content" style="display: none;"> </div><div class="nav-flyout-buffer-left"></div><div class="nav-flyout-buffer-right"></div><div class="nav-flyout-buffer-top"></div><div class="nav-flyout-buffer-bottom"></div></div></div>

  
  

</header>


<script type="text/javascript">window.navmet.push({key:'NavBar',end:+new Date(),begin:window.navmet.main});</script>


<script type="text/javascript">
  if (window.ue_t0) {
    window.navmet.push({key:"NavMainPaintEnd",end:+new Date(),begin:window.ue_t0});
    window.navmet.push({key:"NavFirstPaintEnd",end:+new Date(),begin:window.ue_t0});
  }
</script>


<script type="text/javascript">
    <!--
    
    window.$Nav && $Nav.when("data").run(function(data) { data({"freshTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<style>#nav-flyout-fresh{width:269px;padding:0;}#nav-flyout-fresh .nav-flyout-content{padding:0;}</style><a href='/amazonfresh'><img src='https://images-na.ssl-images-amazon.com/images/G/01/omaha/images/yoda/flyout_72dpi._V270255989_.png' /></a>"}}}},"cartTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_cart_timeout"},"title":"Oops!","paragraph":"Unable to retrieve your cart."}}}},"primeTimeout":{"template":{"name":"flyoutError","data":{"error":{"title":"<a href='/gp/prime'><img src='https://images-na.ssl-images-amazon.com/images/G/01/prime/piv/YourPrimePIV_fallback_CTA._V327346943_.jpg' /></a>"}}}},"ewcTimeout":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Cart","url":"/gp/cart/view.html?ref_=nav_err_ewc_timeout"},"title":"Oops!","paragraph":"There's a problem loading your cart right now."}}}},"errorWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wishlist","url":"/gp/registry/wishlist/?ref_=nav_err_wishlist"},"title":"Oops!","paragraph":"Unable to retrieve your wishlist"}}}},"emptyWishlist":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Wishlist","url":"/gp/registry/wishlist/?ref_=nav_err_empty_wishlist"},"title":"Oops!","paragraph":"Your list is empty"}}}},"yourAccountContent":{"template":{"name":"flyoutError","data":{"error":{"button":{"text":"Your Account","url":"/gp/css/homepage.html?ref_=nav_err_youraccount"},"title":"Oops!","paragraph":"Unable to retrieve your account"}}}},"shopAllTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"Unable to retrieve departments, please try again later"}}}},"kindleTimeout":{"template":{"name":"flyoutError","data":{"error":{"paragraph":"Unable to retrieve list, please try again later"}}}}}); });
window.$Nav && $Nav.when("util.templates").run("FlyoutErrorTemplate", function(templates) {
      templates.add("flyoutError", "<# if(error.title) { #><span class='nav-title'><#=error.title #></span><# } #><# if(error.paragraph) { #><p class='nav-paragraph'><#=error.paragraph #></p><# } #><# if(error.button) { #><a href='<#=error.button.url #>' class='nav-action-button' ><span class='nav-action-inner'><#=error.button.text #></span></a><# } #>");
    });
window.$Nav && $Nav.when("data").run(function(data) { data({"timelineTimeout":{"html":"<div id='nav-timeline'><div id='nav-timeline-error-content'><span class='nav-title'>There’s a problem showing your shopping history right now</span><p class='nav-paragraph'>Please check your network connection or come back in a few minutes.</p></div></div>"}}); });
    if (typeof uet == 'function') {
    uet('bb', 'iss-init-pc', {wb: 1});
  }
  if (!window.$SearchJS && window.$Nav) {
    window.$SearchJS = $Nav.make('sx');
  }

  var opts = {
    host: "completion.amazon.com/search/complete"
  , marketId: "1"
  , obfuscatedMarketId: "ATVPDKIKX0DER"
  , searchAliases: ["aps","amazon-custom-products","amazon-devices","amazonbasics","amazonfresh","amazon-pharmacy","wholefoods","allthebestpets","bartelldrugs","bristolfarms","cardenas","familyfare","freshthyme","kegnbottle","missionwinespirits","petfoodexpress","savemart","sousaswineliquors","surdyksliquorcheeseshop","weis","stripbooks","popular","apparel","electronics","sporting","sports-and-fitness","outdoor-recreation","fan-shop","garden","videogames","toys-and-games","jewelry","digital-text","digital-music","prime-digital-music","watches","grocery","hpc","instant-video","handmade","handmade-jewelry","handmade-home-and-kitchen","prime-instant-video","shop-instant-video","baby-products","office-products","software","smart-home","magazines","tools","automotive","misc","industrial","mi","pet-supplies","digital-music-track","digital-music-album","mobile","mobile-apps","movies-tv","music-artist","music-album","music-song","stripbooks-spanish","electronics-accessories","photo","audio-video","computers","furniture","kitchen","audible","audiobooks","beauty","shoes","arts-crafts","appliances","gift-cards","pets","outdoor","lawngarden","collectibles","replacement-parts","financial","fine-art","fashion","fashion-womens","fashion-womens-clothing","fashion-womens-jewelry","fashion-womens-shoes","fashion-womens-watches","fashion-womens-handbags","fashion-mens","fashion-mens-clothing","fashion-mens-jewelry","fashion-mens-shoes","fashion-mens-watches","fashion-girls","fashion-girls-clothing","fashion-girls-jewelry","fashion-girls-shoes","fashion-girls-watches","fashion-boys","fashion-boys-clothing","fashion-boys-jewelry","fashion-boys-shoes","fashion-boys-watches","fashion-baby","fashion-baby-boys","fashion-baby-girls","fashion-luggage","3d-printing","tradein-aps","todays-deals","live-explorations","local-services","vehicles","video-shorts","warehouse-deals","luxury-beauty","banjo-apps","black-friday","cyber-monday","alexa-skills","subscribe-with-amazon","courses","edu-alt-content","amazon-global-store","prime-wardrobe","under-ten-dollars","tempo","specialty-aps-sns","luxury"]
  , filterAliases: []
  , pageType: "Landing"
  , requestId: "Z0KMT1JTKBYN6W6QW6GJ"
  , sessionId: "130-0450696-1458362"
  , language: "en_US"
  , customerId: "A124BGP0M70XCG"
  , b2b: 0
  , fresh: 0
  , isJpOrCn: 0
  , isUseAuiIss: 1
};

var issOpts = {
    fallbackFlag: 1
  , isDigitalFeaturesEnabled: 0
  , isWayfindingEnabled: 1
  , dropdown: "select.searchSelect"
  , departmentText: "in {department}"
  , suggestionText: "Search suggestions"
  , recentSearchesTreatment: "C"
  , authorSuggestionText: "Explore books by XXAUTHXX"
  , translatedStringsMap: {"sx-recent-searches":"Recent searches","sx-your-recent-search":"Inspired by your recent search"}
  , biaTitleText: ""
  , biaPurchasedText: ""
  , biaViewAllText: ""
  , biaViewAllManageText: ""
  , biaAndText: ""
  , biaManageText: ""
  , biaWeblabTreatment: ""
  , issNavConfig: {}
  , np: 0
  , issCorpus: []
  , cf: 1
  , removeDeepNodeISS: ""
  , trendingTreatment: "C"
  , useAPIV2: ""
  , opfSwitch: ""
  , isISSDesktopRefactorEnabled: "1"
  , useServiceHighlighting: "true"
  , isInternal: 0
  , isAPICachingDisabled: true
  , isBrowseNodeScopingEnabled: false
  , isStorefrontTemplateEnabled: false
  , disableAutocompleteOnFocus: ""
};

  if (opts.isUseAuiIss === 1 && window.$Nav) {
  window.$Nav.when('sx.iss').run('iss-mason-init', function(iss){
    var issInitObj = buildIssInitObject(opts, issOpts, true);

    new iss.IssParentCoordinator(issInitObj);

    $SearchJS.declare('canCreateAutocomplete', issInitObj);
  });
} else if (window.$SearchJS) {
  var iss;

  // BEGIN Deprecated globals
  var issHost = opts.host
    , issMktid = opts.marketId
    , issSearchAliases = opts.searchAliases
    , updateISSCompletion = function() { iss.updateAutoCompletion(); };
  // END deprecated globals


  $SearchJS.when('jQuery', 'search-js-autocomplete-lib').run('autocomplete-init', initializeAutocomplete);
  $SearchJS.when('canCreateAutocomplete').run('createAutocomplete', createAutocomplete);

} // END conditional for window.$SearchJS
  function initializeAutocomplete(jQuery) {
  var issInitObj = buildIssInitObject(opts, issOpts);
  $SearchJS.declare("canCreateAutocomplete", issInitObj);
} // END initializeAutocomplete
  function initSearchCsl(searchCSL, issInitObject) {
  searchCSL.init(
    opts.pageType,
    (window.ue && window.ue.rid) || opts.requestId
  );
  $SearchJS.declare("canCreateAutocomplete", issInitObject);
} // END initSearchCsl
  function createAutocomplete(issObject) {
  iss = new AutoComplete(issObject);

  $SearchJS.publish("search-js-autocomplete", iss);

  logMetrics();
} // END createAutocomplete
  function buildIssInitObject(opts, issOpts, isNewIss) {
    var issInitObj = {
        src: opts.host
      , sessionId: opts.sessionId
      , requestId: opts.requestId
      , mkt: opts.marketId
      , obfMkt: opts.obfuscatedMarketId
      , pageType: opts.pageType
      , language: opts.language
      , customerId: opts.customerId
      , fresh: opts.fresh
      , b2b: opts.b2b
      , aliases: opts.searchAliases
      , fb: issOpts.fallbackFlag
      , isDigitalFeaturesEnabled: issOpts.isDigitalFeaturesEnabled
      , isWayfindingEnabled: issOpts.isWayfindingEnabled
      , issPrimeEligible: issOpts.issPrimeEligible
      , deptText: issOpts.departmentText
      , sugText: issOpts.suggestionText
      , filterAliases: opts.filterAliases
      , biaWidgetUrl: opts.biaWidgetUrl
      , recentSearchesTreatment: issOpts.recentSearchesTreatment
      , authorSuggestionText: issOpts.authorSuggestionText
      , translatedStringsMap: issOpts.translatedStringsMap
      , biaTitleText: ""
      , biaPurchasedText: ""
      , biaViewAllText: ""
      , biaViewAllManageText: ""
      , biaAndText: ""
      , biaManageText: ""
      , biaWeblabTreatment: ""
      , issNavConfig: issOpts.issNavConfig
      , cf: issOpts.cf
      , ime: opts.isJpOrCn
      , mktid: opts.marketId
      , qs: opts.isJpOrCn
      , issCorpus: issOpts.issCorpus
      , deepNodeISS: {
          searchAliasAccessor: function($) {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAlias()) ||
                   $('select.searchSelect').children().attr('data-root-alias');
          },
          searchAliasDisplayNameAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAliasDisplayName());
          }
        }
      , removeDeepNodeISS: issOpts.removeDeepNodeISS
      , trendingTreatment: issOpts.trendingTreatment
      , useAPIV2: issOpts.useAPIV2
      , opfSwitch: issOpts.opfSwitch
      , isISSDesktopRefactorEnabled: issOpts.isISSDesktopRefactorEnabled
      , useServiceHighlighting: issOpts.useServiceHighlighting
      , isInternal: issOpts.isInternal
      , isAPICachingDisabled: issOpts.isAPICachingDisabled
      , isBrowseNodeScopingEnabled: issOpts.isBrowseNodeScopingEnabled
      , isStorefrontTemplateEnabled: issOpts.isStorefrontTemplateEnabled
      , disableAutocompleteOnFocus: issOpts.disableAutocompleteOnFocus
    };
  
    // If we aren't using the new ISS then we need to add these properties
    
    if (!isNewIss) {
      issInitObj.dd = issOpts.dropdown; // The element with id searchDropdownBox doesn't exist in C.
      issInitObj.imeSpacing = issOpts.imeSpacing;
      issInitObj.isNavInline = 1;
      issInitObj.triggerISSOnClick = 0;
      issInitObj.sc = 1;
      issInitObj.np = issOpts.np;
    }
  
    return issInitObj;
  } // END buildIssInitObject
  function logMetrics() {
  if (typeof uet == 'function' && typeof uex == 'function') {
      uet('be', 'iss-init-pc',
          {
              wb: 1
          });
      uex('ld', 'iss-init-pc',
          {
              wb: 1
          });
  }
} // END logMetrics
  
    
window.$Nav && $Nav.declare('config.navDeviceType','desktop');

window.$Nav && $Nav.declare('config.navDebugHighres',false);

window.$Nav && $Nav.declare('config.pageType','Landing');
window.$Nav && $Nav.declare('config.subPageType','BrowsePage');

window.$Nav && $Nav.declare('config.dynamicMenuUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdynamic\x2Dmenu.html');

window.$Nav && $Nav.declare('config.dismissNotificationUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fdismissnotification.html');

window.$Nav && $Nav.declare('config.enableDynamicMenus',true);

window.$Nav && $Nav.declare('config.isInternal',false);

window.$Nav && $Nav.declare('config.isBackup',false);

window.$Nav && $Nav.declare('config.isRecognized',true);

window.$Nav && $Nav.declare('config.transientFlyoutTrigger','\x23nav\x2Dtransient\x2Dflyout\x2Dtrigger');

window.$Nav && $Nav.declare('config.subnavFlyoutUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Fgeneric.html');
window.$Nav && $Nav.declare('config.isSubnavFlyoutMigrationEnabled',true);

window.$Nav && $Nav.declare('config.recordEvUrl','\x2Fgp\x2Fnavigation\x2Fajax\x2Frecordevent.html');
window.$Nav && $Nav.declare('config.recordEvInterval',15000);
window.$Nav && $Nav.declare('config.sessionId','130\x2D0450696\x2D1458362');
window.$Nav && $Nav.declare('config.requestId','Z0KMT1JTKBYN6W6QW6GJ');

window.$Nav && $Nav.declare('config.alexaListEnabled',true);

window.$Nav && $Nav.declare('config.readyOnATF',false);

window.$Nav && $Nav.declare('config.dynamicMenuArgs',{"rid":"Z0KMT1JTKBYN6W6QW6GJ","isFullWidthPrime":0,"isPrime":1,"dynamicRequest":1,"weblabs":"","isFreshRegionAndCustomer":"","primeMenuWidth":450});

window.$Nav && $Nav.declare('config.customerName','Ana');

window.$Nav && $Nav.declare('config.yourAccountPrimeURL','https\x3A\x2F\x2Fwww.amazon.com\x2Fgp\x2Fcss\x2Forder\x2Dhistory\x2Futils\x2Ffirst\x2Dorder\x2Dfor\x2Dcustomer.html\x2Fref\x3Dya_prefetch_beacon\x3Fie\x3DUTF8\x26s\x3D130\x2D0450696\x2D1458362');

window.$Nav && $Nav.declare('config.yourAccountPrimeHover',true);

window.$Nav && $Nav.declare('config.searchBackState',{});

window.$Nav && $Nav.declare('nav.inline');

(function (i) {
  if(window._navbarSpriteUrl) {
    i.onload = function() {window.uet && uet('ne')};
    i.src = window._navbarSpriteUrl;
  }
}(new Image()));

window.$Nav && $Nav.declare('config.autoFocus',false);

window.$Nav && $Nav.declare('config.responsiveTouchAgents',["ieTouch"]);

window.$Nav && $Nav.declare('config.responsiveGW',false);

window.$Nav && $Nav.declare('config.pageHideEnabled',false);

window.$Nav && $Nav.declare('config.sslTriggerType','flyoutProximityLarge');
window.$Nav && $Nav.declare('config.sslTriggerRetry',0);

window.$Nav && $Nav.declare('config.doubleCart',false);

window.$Nav && $Nav.declare('config.signInOverride',false);

window.$Nav && $Nav.declare('config.signInTooltip',false);

window.$Nav && $Nav.declare('config.isPrimeMember',true);

window.$Nav && $Nav.declare('config.packardGlowTooltip',false);

window.$Nav && $Nav.declare('config.packardGlowFlyout',false);

window.$Nav && $Nav.declare('config.rightMarginAlignEnabled',true);

window.$Nav && $Nav.declare('config.flyoutAnimation',false);

window.$Nav && $Nav.declare('config.campusActivation','CAMPUS_ZSE');

window.$Nav && $Nav.declare('config.primeTooltip',{"url":"/gp/prime/digital-adoption/navigation-bar"});

window.$Nav && $Nav.declare('config.primeDay',false);

window.$Nav && $Nav.declare('config.disableBuyItAgain',false);

window.$Nav && $Nav.declare('config.enableCrossShopBiaFlyout',false);

window.$Nav && $Nav.declare('config.pseudoPrimeFirstBrowse',null);

window.$Nav && $Nav.declare('config.sdaYourAccount',{"url":"/ma/api/notification"});

window.$Nav && $Nav.declare('config.csYourAccount',{"url":"/gp/youraccount/navigation/sidepanel"});

window.$Nav && $Nav.declare('config.cartFlyoutDisabled',true);

window.$Nav && $Nav.declare('config.isTabletBrowser',false);

window.$Nav && $Nav.declare('config.HmenuProximityArea',[200,200,200,200]);

window.$Nav && $Nav.declare('config.HMenuIsProximity',true);

window.$Nav && $Nav.declare('config.isPureAjaxALF',false);

window.$Nav && $Nav.declare('config.accountListFlyoutRedesign',false);

window.$Nav && $Nav.declare('config.navfresh',false);

window.$Nav && $Nav.declare('config.isFreshRegion',true);

if (window.ue && ue.tag) { ue.tag('navbar'); };

window.$Nav && $Nav.declare('config.blackbelt',true);

window.$Nav && $Nav.declare('config.beaconbelt',true);

window.$Nav && $Nav.declare('config.accountList',true);

window.$Nav && $Nav.declare('config.iPadTablet',false);

window.$Nav && $Nav.declare('config.searchapiEndpoint',false);

window.$Nav && $Nav.declare('config.timeline',true);

window.$Nav && $Nav.declare('config.timelineAsinPriceEnabled',false);

window.$Nav && $Nav.declare('config.timelineDeleteEnabled',true);

window.$Nav && $Nav.declare('config.dynamicTimelineDeleteArgs','0');

window.$Nav && $Nav.declare('config.extendedFlyout',false);

window.$Nav && $Nav.declare('config.flyoutCloseDelay',600);

window.$Nav && $Nav.declare('config.pssFlag',0);

window.$Nav && $Nav.declare('config.isPrimeTooltipMigrated',false);

window.$Nav && $Nav.declare('config.isDynamicWishListMigrationEnabled',true);

window.$Nav && $Nav.declare('config.hashCustomerAndSessionId','756dd04cabd064fd7e51b03cf981d8a24487193c');

window.$Nav && $Nav.declare('config.isExportMode',false);

window.$Nav && $Nav.declare('config.languageCode','en_US');

window.$Nav && $Nav.declare('config.environmentVFI','AmazonNavigationCards\x2Fdevelopment\x40B6073151372\x2DAL2_x86_64');



window.$Nav && $Nav.declare('config.isHMenuBrowserCacheDisable',false);

window.$Nav && $Nav.declare('config.signInUrlWithRefTag','null');

window.$Nav && $Nav.declare('config.isSmile',false);

window.$Nav && $Nav.declare('config.regionalStores',["QW1hem9uIEZyZXNo","VUZHIFdob2xlIEZvb2Rz","QmFydGVsbCBEcnVncw","QWxsIFRoZSBCZXN0IFBldCBDYXJl","QW1hem9uIEZyZXNo","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","QW1hem9uIEZyZXNo","QW1hem9uIEZyZXNo","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz","QW1hem9uIEZyZXNo","VUZHIFdob2xlIEZvb2Rz","VUZHIFdob2xlIEZvb2Rz"]);

window.$Nav && $Nav.declare('config.isALFRedesignPT2',true);

window.$Nav && $Nav.declare('config.isNavALFRegistryGiftList',false);

window.$Nav && $Nav.declare('config.marketplaceId','ATVPDKIKX0DER');

window.$Nav && $Nav.declare('config.exportTransitionState','none');

window.$Nav && $Nav.declare('config.enableAeeXopFlyout',false);

window.$Nav && $Nav.declare('config.isPrimeFlyoutMigrationEnabled',false);

if (window.P && typeof window.P.declare === "function" && typeof window.P.now === "function") {
  window.P.now('packardGlowIngressJsEnabled').execute(function(glowEnabled) {
    if (!glowEnabled) {
      window.P.declare('packardGlowIngressJsEnabled', true);
    }
  });
  window.P.now('packardGlowStoreName').execute(function(storeName) {
    if (!storeName) {
      window.P.declare('packardGlowStoreName','books');
    }
  });
}

window.$Nav && $Nav.declare('configComplete');

    -->
</script>


<a id="skippedLink" tabindex="-1"></a>

<script type="text/javascript">window.navmet.MainEnd = new Date();</script>
<script type="text/javascript">
    if (window.ue_t0) {
      window.navmet.push({key:"NavMainEnd",end:+new Date(),begin:window.ue_t0});
    }
</script>
<!-- sp:end-feature:navbar -->
<!-- sp:feature:host-atf -->








  <div class="a-container">
    
    
      <div class="a-row">
        
            <div class="a-column a-span12">
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-6fcd1358-727d-439a-ab08-469978c717aa pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="cf45e0fd-11e2-3544-9d03-e54260bdef99" data-csa-c-content-id="amzn1.sym.6fcd1358-727d-439a-ab08-469978c717aa" data-csa-c-slot-id="cf45e0fd-11e2-3544-9d03-e54260bdef99-1" data-csa-c-type="widget" data-csa-c-painter="xslt:__application_Amabot_StaticContentXSLTs_ilm.xsl" data-csa-c-id="p9rvjh-vssp77-9j11cn-qyfgyl" data-cel-widget="cf45e0fd-11e2-3544-9d03-e54260bdef99"><!--wlilm--><table border="0" width="100%" cellspacing="0" cellpadding="0"><tbody><tr><td align="center"><table border="0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF"><tbody><tr><td align="center"><img src="https://m.media-amazon.com/images/G/01/img16/books/content-grid/header/34111_books_us_type_title_840x54_ember._CB485948830_.png" rw_name="img16/books/content-grid/header/34111_books_us_type_title_840x54_ember.png" border="0" alt="Books%20at%20Amazon"></td></tr></tbody></table></td></tr></tbody></table></div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
              
            </div>
        
      </div>
    
      <div class="a-row apb-browse-two-col-center-pad">
        
            <div class="a-column a-span12 aok-float-right apb-browse-col-pad-left apb-browse-two-col-center-margin-right">
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-5ff26949-e314-4d87-9dc5-9973a02c9eb3 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="228714bb-8c0a-4404-b40a-ce3f71e18065" data-csa-c-content-id="amzn1.sym.5ff26949-e314-4d87-9dc5-9973a02c9eb3" data-csa-c-slot-id="228714bb-8c0a-4404-b40a-ce3f71e18065-6" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="bnlctq-w95bwf-eioa1g-8qrgaq" data-cel-widget="228714bb-8c0a-4404-b40a-ce3f71e18065">
























































    







<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41y7o03hqHL.css?AUIClients/ACSWidgetAssets-contentGrid">



<div class="acsUxWidget">
    <div id="contentGrid_634541" class="acswidget acswidget-content-grid celwidget US bxw-content-grid bxw-content-grid--ember bxc-grid--padding bxc-grid--spacing-large  bxc-grid--light" cel_widget_id="acsux-widgets_content-grid_merchandised-search-1" data-is-mobile="false" data-csa-c-id="y5f4gv-j22x4w-kqgg0n-wtwsgg" data-cel-widget="acsux-widgets_content-grid_merchandised-search-1">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_content-grid_merchandised-search-1', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"contentGrid","type":"initialize"}, 'acsux-widgets', null);
}</script>


        
        














        <div class="bxc-grid__container bxc-grid__container--width-1500" data-cel-widget="osa_browse_banner_0">
            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--12-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-1_row1-col1" data-csa-c-id="t54td7-a6tlsa-j0x8ml-estnbq" data-cel-widget="acsux-widgets_content-grid_merchandised-search-1_row1-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/gp/product/0593358279/ref=s9_acss_bw_cg_mab5sbhp_1a1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-1&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=5ff26949-e314-4d87-9dc5-9973a02c9eb3&amp;pf_rd_i=283155" aria-label="The Unsinkable Greta James by Jennifer E. Smith">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/kindle/MaB/JenniferSmith/Mab5_BHP_Desktop.png" alt="The Unsinkable Greta James by Jennifer E. Smith">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            
        </div>

    
<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_content-grid_merchandised-search-1', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_content-grid_merchandised-search-1', {wb: 1});  // timestamp body-end</script>
</div>

</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-e60a10d0-198b-47e1-9e80-9b1b4261c663 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="eac5aae6-265c-48d4-8368-6596c1857b2d" data-csa-c-content-id="amzn1.sym.e60a10d0-198b-47e1-9e80-9b1b4261c663" data-csa-c-slot-id="eac5aae6-265c-48d4-8368-6596c1857b2d-7" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="7n760d-6igf3p-f6jddi-ar5x59" data-cel-widget="eac5aae6-265c-48d4-8368-6596c1857b2d">
























































    







<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41y7o03hqHL.css?AUIClients/ACSWidgetAssets-contentGrid">



<div class="acsUxWidget">
    <div id="contentGrid_108441" class="acswidget acswidget-content-grid celwidget US bxw-content-grid bxw-content-grid--ember bxc-grid--padding bxc-grid--spacing-large  bxc-grid--light" cel_widget_id="acsux-widgets_content-grid_merchandised-search-2" data-is-mobile="false" data-csa-c-id="wmcvn7-3sm9q5-ooppoj-5o21dr" data-cel-widget="acsux-widgets_content-grid_merchandised-search-2">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_content-grid_merchandised-search-2', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"contentGrid","type":"initialize"}, 'acsux-widgets', null);
}</script>


        
        














        <div class="bxc-grid__container bxc-grid__container--width-1500" data-cel-widget="osa_browse_banner_1">
            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-2_row1-col1" data-csa-c-id="tbsxox-k9l0bg-14dfhy-7izq24" data-cel-widget="acsux-widgets_content-grid_merchandised-search-2_row1-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/b/ref=s9_acss_bw_cg_BHPNOV20_1a1_w?node=17143709011&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-2&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=e60a10d0-198b-47e1-9e80-9b1b4261c663&amp;pf_rd_i=283155" aria-label="Best books of the month">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/XCM_Manual_ORIGIN_1263269_1341942_US_us_books_botm_tile_3338833_440x344_en_US.jpg" alt="Best books of the month">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-2_row1-col2" data-csa-c-id="cjt751-s00v2z-izmsrg-9kf1mv" data-cel-widget="acsux-widgets_content-grid_merchandised-search-2_row1-col2">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/amazonbookreview/celebritypicks.html/ref=s9_acss_bw_cg_BHPNOV20_1b1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-2&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=e60a10d0-198b-47e1-9e80-9b1b4261c663&amp;pf_rd_i=283155" aria-label="Celebrity Picks">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/Books/Kids/BOTM/2021/cp_CelebPicks_BOTY_2021_Porter_Barrymore_440x334.jpg" alt="Celebrity Picks">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-2_row1-col3" data-csa-c-id="2ta47s-a5sq20-jntzcg-g1kn1y" data-cel-widget="acsux-widgets_content-grid_merchandised-search-2_row1-col3">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/b/ref=s9_acss_bw_cg_BHPNOV20_1c1_w?node=17276794011&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-2&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=e60a10d0-198b-47e1-9e80-9b1b4261c663&amp;pf_rd_i=283155" aria-label="Best kids' books of the month">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/Books/Kids/BOTM/NewBOTM_KIDS_tile_2021_440-x334.jpg" alt="Best kids' books of the month">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-2_row1-col4" data-csa-c-id="x4bnji-x4e5bn-q6a8qm-zci0k4" data-cel-widget="acsux-widgets_content-grid_merchandised-search-2_row1-col4">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/amazonbookreview/ref=s9_acss_bw_cg_BHPNOV20_1d1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-2&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=e60a10d0-198b-47e1-9e80-9b1b4261c663&amp;pf_rd_i=283155" aria-label="Amazon Book Review">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/books/editorial/content_grid_amazon_book_review_2_440x344.jpg" alt="Amazon Book Review">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            
        </div>

    
<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_content-grid_merchandised-search-2', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_content-grid_merchandised-search-2', {wb: 1});  // timestamp body-end</script>
</div>

</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pd_rd_w-MKR9O pf_rd_p-ab907333-063a-4de1-b403-0a312c047f32 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ pd_rd_r-5b8365d8-6016-4fe0-8bc3-20ffea8edfc6 pd_rd_wg-caAzT c-f" cel_widget_id="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0" data-csa-c-content-id="amzn1.sym.ab907333-063a-4de1-b403-0a312c047f32" data-csa-c-slot-id="pbook-storefront-infinite-scroll-1" data-csa-c-type="widget" data-csa-c-painter="p13n-desktop-ysh-cards" data-csa-c-id="ai8ft5-kfgmah-uf43k3-5x8k10" data-cel-widget="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0"><script>if(window.mix_csa){window.mix_csa('[cel_widget_id="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0"]', 'CardInstanceFOByMFw_L28FsdSKGGpNQw')('mark', 'bb')}</script>
<script>if(window.uet){window.uet('bb','p13n-desktop-ysh_pbook-storefront-infinite-scroll_0',{wb: 1})}</script>
<style>._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-2__EWgCb{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-5__2l-dX{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-6__28daG{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-7__1k_Mc{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-8__1yvsR{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-9__3Pofd{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-10__mY8_7{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ{margin-bottom:20px;margin-left:0;overflow:auto;white-space:nowrap}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ::-webkit-scrollbar{background:transparent;width:0}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ li{-webkit-box-pack:center;-ms-flex-pack:center;background-color:#f0f0f0;border:1px solid #f0f0f0;border-radius:8px;box-shadow:0 1px 2px 0 rgba(15,17,17,.2);color:#111;cursor:pointer;display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;font-weight:500;justify-content:center;list-style-type:none;margin:1px 8px 2px 1px;min-width:44px;padding:8px;text-align:center;white-space:normal}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ li button{background:none;border:none}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ li.p13n-selected-pill{background-color:#e7f4f5;border-color:#c7e4e8;color:#007185}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ li:hover.p13n-selected-pill{background-color:#daf1f3;border-color:#c7e4e8;color:#007185}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ li:hover{background-color:#eee;border-color:#eee}._p13n-desktop-ysh_pillContainerStyle_p13nscPills__1KzwZ ._p13n-desktop-ysh_pillContainerStyle_unselected__q8wvT{background-color:#f4f4f4}._p13n-desktop-ysh_pillContainerStyle_spinnerContainer__Llfcc{min-height:100px;width:100%}._p13n-desktop-ysh_pillContainerStyle_spinnerContainer__Llfcc ._p13n-desktop-ysh_pillContainerStyle_p13nScSpinner__3lJFM{margin:20px auto auto}._p13n-desktop-ysh_pillContainerStyle_refinementPillCss__1fYG0{max-width:200px}
._p13n-desktop-ysh_style_grid-cell__zFYyO{-webkit-box-pack:center;-ms-flex-pack:center;background-color:#fff;cursor:pointer;display:-webkit-box;display:-ms-flexbox;display:flex;justify-content:center;margin:10px;position:relative}._p13n-desktop-ysh_style_grid-row__3VsqC{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-bottom:22px;margin-left:25px;min-width:900px}._p13n-desktop-ysh_style_grid-column__UjCjt{-ms-flex-preferred-size:210px;flex-basis:210px;max-width:300px;min-width:210px}._p13n-desktop-ysh_style_grid-column__UjCjt,._p13n-desktop-ysh_style_grid-detail-column__2AJfX{border-bottom:1px solid #d5dbdb;border-top:1px solid #d5dbdb;border-color:#d5dbdb;border-style:solid;border-width:.5px 1px;margin-bottom:-1px;margin-left:-1px;margin-right:0!important;margin-top:0}._p13n-desktop-ysh_style_grid-detail-column__2AJfX{width:100%}._p13n-desktop-ysh_style_card__2VZFf,._p13n-desktop-ysh_style_expandedGridCell__15bML{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-flow:column;flex-flow:column;height:100%;margin-bottom:0;margin-top:0;padding:10px;position:relative;text-align:center}._p13n-desktop-ysh_style_expandedGridCell__15bML{cursor:pointer}._p13n-desktop-ysh_style_gridExpansion__2aNlg{-webkit-box-pack:center;-ms-flex-pack:center;-ms-flex-preferred-size:210px;-webkit-box-flex:1;-ms-flex-positive:1;background-color:#fff;display:-webkit-box;display:-ms-flexbox;display:flex;flex-basis:210px;flex-grow:1;justify-content:center;margin:10px}._p13n-desktop-ysh_style_overlayTitle__E6uXy{position:absolute;top:35%}._p13n-desktop-ysh_style_notInterestedMessage__2bIn5{position:absolute;top:50%}._p13n-desktop-ysh_style_image__rSmhM{opacity:.1}._p13n-desktop-ysh_style_feedbackRow__23bqz{margin-right:0!important}
._p13n-desktop-ysh_style_column__2x05O{grid-column:auto/span 1;margin-right:0!important}._p13n-desktop-ysh_style_grid-row__3daT_{display:grid;grid-template-columns:repeat(auto-fit,50%)}._p13n-desktop-ysh_style_card__3H7qC{margin-bottom:0;margin-top:0;padding:10px;position:relative;text-align:center}._p13n-desktop-ysh_style_card__3H7qC,._p13n-desktop-ysh_style_expandedColumn__1-66H{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-flow:column;flex-flow:column;height:100%;outline:.5px solid #d5dbdb}._p13n-desktop-ysh_style_expandedColumn__1-66H{-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;grid-column:auto/span 2;margin-right:0!important}._p13n-desktop-ysh_style_overlayTitle__2XUqy{position:absolute;top:35%}._p13n-desktop-ysh_style_notInterestedMessage__2-bO3{position:absolute;top:50%}._p13n-desktop-ysh_style_image__2eEq7{opacity:.1}._p13n-desktop-ysh_style_feedbackRow__17KjU{margin-right:0!important}
.p13n-kebab-button-edit-recs-bottom-sheet{padding-left:10px}.p13n-edit-recs-kebab-wrapper{-ms-flex-negative:0;flex-shrink:0}.p13n-edit-your-recs-button{margin:17px 10px 0}.p13n-flex-container-edit-recs-bottom-sheet{-webkit-box-pack:justify;-ms-flex-pack:justify;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;justify-content:space-between}
.report-flag-hide{cursor:none;display:none}.report-flag{background-image:url(https://m.media-amazon.com/images/S/sash/vh8ofoqOd7XyRsk.png);background-repeat:no-repeat;background-size:15px 16px;cursor:pointer;height:16px;position:absolute;right:20px;top:35px;width:15px}.report-flag:hover{background-image:url(https://m.media-amazon.com/images/S/sash/WXxFP-k55X6KCh2.png)}.report-problem-modal-root{padding:14px 18px}
._p13n-desktop-ysh_panelStyle_panel-text__3TtlT{width:220px}._p13n-desktop-ysh_panelStyle_panel-container__3ZNzh{float:left;width:238px}._p13n-desktop-ysh_panelStyle_panel-subsection__19oyW{padding-left:15px;padding-right:18px}._p13n-desktop-ysh_panelStyle_panel-logo-container__ucYMM{height:33px;margin-bottom:5px;width:220px}._p13n-desktop-ysh_panelStyle_panel-button__GP7zd{width:auto}
._p13n-desktop-ysh_style_asin-title__2KJ6_{font-size:14px;font-weight:bolder;margin-left:20px;margin-top:10px;text-align:left}._p13n-desktop-ysh_style_asin-row__3PozI{display:block}._p13n-desktop-ysh_style_asin-detail-row__T7Jm0{margin-bottom:-12px}._p13n-desktop-ysh_style_image__11f2t{height:90px;width:90px}._p13n-desktop-ysh_style_feedback-switch__2zE08{cursor:pointer;display:inline-block;height:50px;margin-top:5px;vertical-align:top;width:50px}
._p13n-desktop-ysh_style_card__2yY06{width:95%}._p13n-desktop-ysh_style_image-and-offer__XQEhq{display:-webkit-box;display:-ms-flexbox;display:flex;margin-bottom:0;margin-top:10px}._p13n-desktop-ysh_style_review-row__1d5Qn{padding-right:10px;width:100%}._p13n-desktop-ysh_style_row__1eL-2{width:100%}._p13n-desktop-ysh_style_icon__3kTmk{background-position:-310px -5px;height:1.6rem;width:1.6rem}
._p13n-desktop-ysh_style_card__3UH71{text-align:left;width:95%}._p13n-desktop-ysh_style_close-icon-row__1UiN7{height:5px;padding-right:10px;text-align:right;width:100%}._p13n-desktop-ysh_style_close-icon-column__33S0b{height:inherit}._p13n-desktop-ysh_style_row__NdY00{width:100%}._p13n-desktop-ysh_style_icon___PtFG{background-position:-310px -5px;cursor:pointer;height:1.6rem;width:1.6rem}._p13n-desktop-ysh_style_feedbackText__1z8PE{cursor:pointer}
._p13n-desktop-ysh_maskStyle_maskStyling__1IlBq{background-color:#000;height:100%;left:0;opacity:.04;position:absolute;top:0;width:100%}._p13n-desktop-ysh_maskStyle_positionRelativeCss__ZwMqj{position:relative}._p13n-desktop-ysh_maskStyle_noop__3Xbw5{-webkit-perspective:none;perspective:none}
._p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z{word-wrap:normal}
._p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h{position:relative;top:2px}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__1-yh1{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__1-yh1:before{border-bottom-color:#c45500!important}._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__1-yh1:after{border-top-color:#c45500!important}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-body__3nkHf{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-text__3apKt{color:#fff;line-height:18px}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2Z3cK{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-ysh_amazonsChoiceStyles_p13n-amazons-choice-badge-image__14WY0{margin-right:2px}
._p13n-desktop-ysh_climatePledgeFriendlyBadgeStyles_p13n-sc-climatepledgefriendly-badge-text__1Plzn{color:#168342}
._p13n-desktop-ysh_curationStyles_curation__13VGx{margin-bottom:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}._p13n-desktop-ysh_curationStyles_curation__13VGx ._p13n-desktop-ysh_curationStyles_icon__3_dKr{width:20px}
._p13n-desktop-ysh_dealInfo_p13nDealOfTheDay__cVlwZ{background:#b12704;color:#fff;float:right;padding:2px 4px;position:relative}._p13n-desktop-ysh_dealInfo_dealsCardDealTimer__2oYBO{display:inline-block}._p13n-desktop-ysh_dealInfo_dealsCardPercentClaimed__1GTDI{float:right;padding-top:3px}
._p13n-desktop-ysh_dealBadge_p13nDealOfTheDayBadge__2Nn7x{background:#b12704;color:#fff;padding:2px 4px}
._p13n-desktop-ysh_quantityPricingTable_qdPricingTableContainer__29w2z ._p13n-desktop-ysh_quantityPricingTable_qdPricingTable__1_iY1{border:none;border-collapse:separate;border-top:1px solid #e7e7e7}._p13n-desktop-ysh_quantityPricingTable_qdPlaceholderRow__1ry1S ._p13n-desktop-ysh_quantityPricingTable_quantityColumn__2sfjE{border-left:3px solid #d77d32}._p13n-desktop-ysh_quantityPricingTable_qdPricingTableContainer__29w2z ._p13n-desktop-ysh_quantityPricingTable_qdPricingTable__1_iY1 ._p13n-desktop-ysh_quantityPricingTable_qdRow__2WzQJ{background-color:#fff;cursor:pointer}._p13n-desktop-ysh_quantityPricingTable_mobile__2LnqI._p13n-desktop-ysh_quantityPricingTable_qdTableInput__1Z2G6{width:95%}._p13n-desktop-ysh_quantityPricingTable_qdTableInput__1Z2G6{float:left;margin:10px}._p13n-desktop-ysh_quantityPricingTable_closeButton__3sVAs{background-color:#eee;border-radius:5px;cursor:pointer;float:right;font-weight:100;height:30px;line-height:.85;margin:10px 10px 10px 0;text-align:center;width:30px}
._p13n-desktop-ysh_quantityDiscounts_qdMessage__3xK5j{color:#007185}._p13n-desktop-ysh_quantityDiscounts_qdMessage__3xK5j:hover{color:#c45000}
._p13n-desktop-ysh_sponsoredLabel_sponsoredLabel__2UvSK{color:#555;font-size:11px}
._p13n-desktop-ysh_couponStyles_p13n-coupon-badge__3d5NR{background:#7fda69;color:#111;display:inline-block;padding:0 6px;position:relative}
._p13n-desktop-ysh_delightPricingStyles_p13n-delight-pricing-badge__26S9Q{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
._p13n-desktop-ysh_style_card-title__1EuRU{margin-left:25px;margin-top:20px}._p13n-desktop-ysh_style_card__2os3u{padding:2px}._p13n-desktop-ysh_style_widgetDivider__2cOPG{border-top:5px solid #e7e7e7}
._p13n-desktop-ysh_style_grid-cell__3AyvM{-webkit-box-pack:center;-ms-flex-pack:center;background-color:#fff;cursor:pointer;display:-webkit-box;display:-ms-flexbox;display:flex;justify-content:center;margin:10px;position:relative}._p13n-desktop-ysh_style_grid-row__2R6S9{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-bottom:22px;margin-left:25px;min-width:900px}._p13n-desktop-ysh_style_grid-column__3iMdw{-ms-flex-preferred-size:210px;flex-basis:210px;max-width:300px;min-width:210px}._p13n-desktop-ysh_style_grid-column__3iMdw,._p13n-desktop-ysh_style_grid-detail-column__S6U61{border-bottom:1px solid #d5dbdb;border-top:1px solid #d5dbdb;border-color:#d5dbdb;border-style:solid;border-width:.5px 1px;margin-bottom:-1px;margin-left:-1px;margin-right:0!important;margin-top:0}._p13n-desktop-ysh_style_grid-detail-column__S6U61{width:100%}._p13n-desktop-ysh_style_card__3OySw,._p13n-desktop-ysh_style_expandedGridCell__2dH0D{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-flow:column;flex-flow:column;height:100%;margin-bottom:0;margin-top:0;padding:10px;position:relative;text-align:center}._p13n-desktop-ysh_style_expandedGridCell__2dH0D{cursor:pointer}._p13n-desktop-ysh_style_gridExpansion__vuxFX{-webkit-box-pack:center;-ms-flex-pack:center;-ms-flex-preferred-size:210px;-webkit-box-flex:1;-ms-flex-positive:1;background-color:#fff;display:-webkit-box;display:-ms-flexbox;display:flex;flex-basis:210px;flex-grow:1;justify-content:center;margin:10px}._p13n-desktop-ysh_style_overlayTitle__3i-n9{position:absolute;top:35%}._p13n-desktop-ysh_style_notInterestedMessage__3Vy5z{position:absolute;top:50%}._p13n-desktop-ysh_style_image__3QFmU{opacity:.1}._p13n-desktop-ysh_style_feedbackRow__ZcBSK{margin-right:0!important}
._p13n-desktop-ysh_style_card__1u-hH{width:95%}._p13n-desktop-ysh_style_image-and-offer__ttP6r{display:-webkit-box;display:-ms-flexbox;display:flex;margin-bottom:0;margin-top:10px}._p13n-desktop-ysh_style_review-row__3GjsU{padding-right:10px;width:100%}._p13n-desktop-ysh_style_row__3mza_{width:100%}._p13n-desktop-ysh_style_icon__2LLzM{background-position:-310px -5px;height:1.6rem;width:1.6rem}
._p13n-desktop-ysh_style_card__24Skw{text-align:left;width:95%}._p13n-desktop-ysh_style_close-icon-row__2Y0Qb{height:5px;padding-right:10px;text-align:right;width:100%}._p13n-desktop-ysh_style_close-icon-column__1v3OL{height:inherit}._p13n-desktop-ysh_style_row__1eIop{width:100%}._p13n-desktop-ysh_style_icon__2Xd8T{background-position:-310px -5px;cursor:pointer;height:1.6rem;width:1.6rem}._p13n-desktop-ysh_style_feedbackText__3e5Du{cursor:pointer}
._p13n-desktop-ysh_style_asin-title__3n1UB{font-size:14px;font-weight:bolder;margin-left:20px;margin-top:10px;text-align:left}._p13n-desktop-ysh_style_asin-row__3DVqG{display:block}._p13n-desktop-ysh_style_asin-detail-row__2Lpno{margin-bottom:-12px}._p13n-desktop-ysh_style_image__2lQoz{height:90px;width:90px}._p13n-desktop-ysh_style_feedback-switch__VCHeh{cursor:pointer;display:inline-block;height:50px;margin-top:5px;vertical-align:top;width:50px}
._p13n-desktop-ysh_maskStyle_maskStyling__12j_X{background-color:#000;height:100%;left:0;opacity:.04;position:absolute;top:0;width:100%}._p13n-desktop-ysh_maskStyle_positionRelativeCss__1GDAD{position:relative}._p13n-desktop-ysh_maskStyle_noop__1oBjC{-webkit-perspective:none;perspective:none}
._p13n-desktop-ysh_prime_p13n-prime-badge__wRb4G{position:relative;top:2px}
._p13n-desktop-ysh_price_p13n-sc-price__bCZQt{word-wrap:normal}
._p13n-desktop-ysh_delightPricingStyles_p13n-delight-pricing-badge__3R9NU{background:#b12704;color:#fff;display:inline-block;padding:2px 10px;position:relative}
input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}input[type=number]{-moz-appearance:textfield}
._p13n-desktop-ysh_couponStyles_p13n-coupon-badge__2YGiH{background:#7fda69;color:#111;display:inline-block;padding:0 6px;position:relative}
._p13n-desktop-ysh_sponsoredLabel_sponsoredLabel__122-w{color:#555;font-size:11px}
._p13n-desktop-ysh_curationStyles_curation__327u1{margin-bottom:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}._p13n-desktop-ysh_curationStyles_curation__327u1 ._p13n-desktop-ysh_curationStyles_icon__3JMTe{width:20px}
._p13n-desktop-ysh_dealInfo_p13nDealOfTheDay__10RZg{background:#b12704;color:#fff;float:right;padding:2px 4px;position:relative}._p13n-desktop-ysh_dealInfo_dealsCardDealTimer__1Em5d{display:inline-block}._p13n-desktop-ysh_dealInfo_dealsCardPercentClaimed__1s7Ha{float:right;padding-top:3px}
._p13n-desktop-ysh_dealBadge_p13nDealOfTheDayBadge__3WWAr{background:#b12704;color:#fff;padding:2px 4px}
._p13n-desktop-ysh_climatePledgeFriendlyBadgeStyles_p13n-sc-climatepledgefriendly-badge-text__a4pTj{color:#168342}
._p13n-desktop-ysh_quantityDiscounts_qdMessage__13ejZ{color:#007185}._p13n-desktop-ysh_quantityDiscounts_qdMessage__13ejZ:hover{color:#c45000}
._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__3hEN7{background-color:#c45500!important;font-size:12px;margin-right:8px;padding-bottom:2px;padding-top:2px}._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__3hEN7:before{border-bottom-color:#c45500!important}._p13n-desktop-ysh_bestsellerStyles_p13n-best-seller-badge__3hEN7:after{border-top-color:#c45500!important}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-body__3iDBy{background-color:#c45500;float:left;line-height:18px;padding-left:6px;padding-right:3px}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-text__1i9QT{color:#fff;line-height:18px}._p13n-desktop-ysh_bestsellerStyles_p13n-sc-bestseller-badge-triangle__2HApm{border-right:9px solid transparent;border-top:18px solid;color:#c45500;float:left;height:0;width:0}
._p13n-desktop-ysh_amazonsChoiceStyles_p13n-amazons-choice-badge-image__1ZZjv{margin-right:2px}
._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-1__2o7X6{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-2__YmMc7{-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-3__3xIkK{-webkit-line-clamp:3;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-4__2oUlo{-webkit-line-clamp:4;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-5__1Hi04{-webkit-line-clamp:5;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-6__3fNYL{-webkit-line-clamp:6;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-7__q6tIz{-webkit-line-clamp:7;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-8__3HH-S{-webkit-line-clamp:8;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-9__jEGnm{-webkit-line-clamp:9;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}._p13n-desktop-ysh_truncationStyles_p13n-sc-css-line-clamp-10__28Uvv{-webkit-line-clamp:10;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}
._p13n-desktop-ysh_quantityPricingTable_qdPricingTableContainer__xRhp5 ._p13n-desktop-ysh_quantityPricingTable_qdPricingTable__19st0{border:none;border-collapse:separate;border-top:1px solid #e7e7e7}._p13n-desktop-ysh_quantityPricingTable_qdPlaceholderRow__etljl ._p13n-desktop-ysh_quantityPricingTable_quantityColumn__3t9Qy{border-left:3px solid #d77d32}._p13n-desktop-ysh_quantityPricingTable_qdPricingTableContainer__xRhp5 ._p13n-desktop-ysh_quantityPricingTable_qdPricingTable__19st0 ._p13n-desktop-ysh_quantityPricingTable_qdRow__247cy{background-color:#fff;cursor:pointer}._p13n-desktop-ysh_quantityPricingTable_mobile__2qg3-._p13n-desktop-ysh_quantityPricingTable_qdTableInput__3-g8q{width:95%}._p13n-desktop-ysh_quantityPricingTable_qdTableInput__3-g8q{float:left;margin:10px}._p13n-desktop-ysh_quantityPricingTable_closeButton__1s3Di{background-color:#eee;border-radius:5px;cursor:pointer;float:right;font-weight:100;height:30px;line-height:.85;margin:10px 10px 10px 0;text-align:center;width:30px}</style>
<!--CardsClient--><div id="CardInstanceFOByMFw_L28FsdSKGGpNQw" data-card-metrics-id="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0" data-acp-tracking="{&quot;pd_rd_w&quot;:&quot;MKR9O&quot;,&quot;pf_rd_p&quot;:&quot;ab907333-063a-4de1-b403-0a312c047f32&quot;,&quot;pf_rd_r&quot;:&quot;Z0KMT1JTKBYN6W6QW6GJ&quot;,&quot;pd_rd_r&quot;:&quot;5b8365d8-6016-4fe0-8bc3-20ffea8edfc6&quot;,&quot;pd_rd_wg&quot;:&quot;caAzT&quot;,&quot;ref_&quot;:&quot;rtpb&quot;}" data-mix-claimed="true"><div class="_p13n-desktop-ysh_style_card-title__1EuRU"><h2 class="a-size-large a-spacing-base">Top picks for you</h2></div><div class="p13n-grid-feedbackTitle-translation aok-hidden">Removed</div><div class="p13n-grid-feedbackMessage-translation aok-hidden">You said you are not interested in this</div><div class="p13n-grid-removeRecsText-translation aok-hidden">Remove this recommendation</div><div class="a-cardui _p13n-desktop-ysh_style_card__2os3u" data-a-card-type="basic"><div class="p13n-desktop-grid" data-client-recs-list="[{&quot;id&quot;:&quot;B09QZVYPD1&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09QZVYPD1&quot;}},{&quot;id&quot;:&quot;0593336844&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;0593336844&quot;}},{&quot;id&quot;:&quot;607315089X&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;607315089X&quot;}},{&quot;id&quot;:&quot;B07QQDQMKV&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B07QQDQMKV&quot;}},{&quot;id&quot;:&quot;0684815524&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;0684815524&quot;}},{&quot;id&quot;:&quot;B077THHK5Z&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B077THHK5Z&quot;}},{&quot;id&quot;:&quot;1484243536&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1484243536&quot;}},{&quot;id&quot;:&quot;1491910399&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1491910399&quot;}},{&quot;id&quot;:&quot;0062959921&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;0062959921&quot;}},{&quot;id&quot;:&quot;1916404359&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1916404359&quot;}},{&quot;id&quot;:&quot;B07RYGHRTS&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B07RYGHRTS&quot;}},{&quot;id&quot;:&quot;B08FJKT2H9&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08FJKT2H9&quot;}},{&quot;id&quot;:&quot;B08LDYBGJD&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08LDYBGJD&quot;}},{&quot;id&quot;:&quot;B08QGLNSFK&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08QGLNSFK&quot;}},{&quot;id&quot;:&quot;1449373321&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1449373321&quot;}},{&quot;id&quot;:&quot;1593279280&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1593279280&quot;}},{&quot;id&quot;:&quot;1119002257&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1119002257&quot;}},{&quot;id&quot;:&quot;B01CXO4VRI&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B01CXO4VRI&quot;}},{&quot;id&quot;:&quot;B09RTRGKJL&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09RTRGKJL&quot;}},{&quot;id&quot;:&quot;B09BTQ9HW6&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09BTQ9HW6&quot;}},{&quot;id&quot;:&quot;1501190113&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1501190113&quot;}},{&quot;id&quot;:&quot;B07CLFYBCT&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B07CLFYBCT&quot;}},{&quot;id&quot;:&quot;B09FYT6JMR&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09FYT6JMR&quot;}},{&quot;id&quot;:&quot;0451490827&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;0451490827&quot;}},{&quot;id&quot;:&quot;B072V27QMZ&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B072V27QMZ&quot;}},{&quot;id&quot;:&quot;B07QN8SRR3&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B07QN8SRR3&quot;}},{&quot;id&quot;:&quot;B082J3XTCD&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B082J3XTCD&quot;}},{&quot;id&quot;:&quot;B09PC7WTRG&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09PC7WTRG&quot;}},{&quot;id&quot;:&quot;B09JPHNC1R&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B09JPHNC1R&quot;}},{&quot;id&quot;:&quot;B07L7RYYF7&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B07L7RYYF7&quot;}},{&quot;id&quot;:&quot;006295850X&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;006295850X&quot;}},{&quot;id&quot;:&quot;B08FTF3D2M&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08FTF3D2M&quot;}},{&quot;id&quot;:&quot;B083SN82NQ&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B083SN82NQ&quot;}},{&quot;id&quot;:&quot;B092RXXJDM&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B092RXXJDM&quot;}},{&quot;id&quot;:&quot;1982123915&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1982123915&quot;}},{&quot;id&quot;:&quot;B097JJS74S&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B097JJS74S&quot;}},{&quot;id&quot;:&quot;1491957662&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1491957662&quot;}},{&quot;id&quot;:&quot;B08RZ56MF3&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08RZ56MF3&quot;}},{&quot;id&quot;:&quot;1491912057&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1491912057&quot;}},{&quot;id&quot;:&quot;1538733366&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1538733366&quot;}},{&quot;id&quot;:&quot;000748805X&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;000748805X&quot;}},{&quot;id&quot;:&quot;B08PG6CKZJ&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08PG6CKZJ&quot;}},{&quot;id&quot;:&quot;1617296864&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1617296864&quot;}},{&quot;id&quot;:&quot;B08BZNQN7X&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08BZNQN7X&quot;}},{&quot;id&quot;:&quot;0062941232&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;0062941232&quot;}},{&quot;id&quot;:&quot;B08ZSQLZBS&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B08ZSQLZBS&quot;}},{&quot;id&quot;:&quot;1617294438&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;1617294438&quot;}},{&quot;id&quot;:&quot;B097QRBQZ3&quot;,&quot;linkParameters&quot;:{&quot;pd_rd_i&quot;:&quot;B097QRBQZ3&quot;}}]" data-index-offset="4" data-reftag="rtpb" data-linkparameters="{&quot;pd_rd_w&quot;:&quot;MKR9O&quot;,&quot;pf_rd_p&quot;:&quot;ab907333-063a-4de1-b403-0a312c047f32&quot;,&quot;pf_rd_r&quot;:&quot;Z0KMT1JTKBYN6W6QW6GJ&quot;,&quot;pd_rd_r&quot;:&quot;5b8365d8-6016-4fe0-8bc3-20ffea8edfc6&quot;,&quot;pd_rd_wg&quot;:&quot;caAzT&quot;}" data-offset="48" data-faceoutkataname="GeneralFaceout"><div class="p13n-gridRow _p13n-desktop-ysh_style_grid-row__3VsqC"><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML p13n-grid-image-only aok-hidden" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="My Killer Vacation" src="https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width: none; max-height: none; height: 172px; width: auto;"></div></div><div id="p13n-asin-index-0" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="My Killer Vacation" src="https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">My Killer Vacation</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$4.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="My Killer Vacation" src="https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71iFHfrEy1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Love on the Brain" src="https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-1" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Love on the Brain" src="https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Love on the Brain</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$14.99</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE Delivery</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Love on the Brain" src="https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81XS0eEa6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Los niños de Irena / Irena's Children: The extraordinary Story of the Woman Who Saved 2.500 Children from the Warsaw Ghetto (" src="https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-2" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Los niños de Irena / Irena's Children: The extraordinary Story of the Woman Who Saved 2.500 Children from the Warsaw Ghetto (" src="https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="Los niños de Irena / Irena's Children: The extraordinary Story of the Woman Who Saved 2.500 Children from the Warsaw Ghetto (Spanish Edition)">Los niños de Irena / Irena's Children: The extraordinary…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">341</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$17.95</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Los niños de Irena / Irena's Children: The extraordinary Story of the Woman Who Saved 2.500 Children from the Warsaw Ghetto (" src="https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wQTajvbhL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Las montañas de Buda (OTROS LIB. EN EXISTENCIAS S.BARRAL) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-3" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Las montañas de Buda (OTROS LIB. EN EXISTENCIAS S.BARRAL) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Las montañas de Buda (OTROS LIB. EN EXISTENCIAS S.BARRAL) (Spanish Edition)</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.6 out of 5 stars</span></i> <span class="a-size-small">348</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$6.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Las montañas de Buda (OTROS LIB. EN EXISTENCIAS S.BARRAL) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91q3TFLNlpL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Muchas vidas, muchos sabios" src="https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-4" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Muchas vidas, muchos sabios" src="https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2">Muchas vidas, muchos sabios</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">550</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$13.99</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Muchas vidas, muchos sabios" src="https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71CbVO9zD+L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="La bailarina de Auschwitz: Una inspiradora historia de valentía y supervivencia (No Ficción) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-5" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="La bailarina de Auschwitz: Una inspiradora historia de valentía y supervivencia (No Ficción) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3" title="La bailarina de Auschwitz: Una inspiradora historia de valentía y supervivencia (No Ficción) (Spanish Edition)">La bailarina de Auschwitz: Una inspiradora historia de valentía y supervivencia (No Ficción)…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">3,929</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$5.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="La bailarina de Auschwitz: Una inspiradora historia de valentía y supervivencia (No Ficción) (Spanish Edition)" src="https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81+so3KlD8L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Text Analytics with Python: A Practitioner's Guide to Natural Language Processing" src="https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-6" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Text Analytics with Python: A Practitioner's Guide to Natural Language Processing" src="https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="Text Analytics with Python: A Practitioner's Guide to Natural Language Processing">Text Analytics with Python: A Practitioner's Guide to Natural…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.5 out of 5 stars</span></i> <span class="a-size-small">48</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$23.49</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE Delivery</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Text Analytics with Python: A Practitioner's Guide to Natural Language Processing" src="https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/61n3Z6lt3qL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="R for Data Science: Import, Tidy, Transform, Visualize, and Model Data" src="https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-7" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="R for Data Science: Import, Tidy, Transform, Visualize, and Model Data" src="https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="R for Data Science: Import, Tidy, Transform, Visualize, and Model Data">R for Data Science: Import, Tidy, Transform, Visualize, and Model…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">1,170</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$32.06</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="R for Data Science: Import, Tidy, Transform, Visualize, and Model Data" src="https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81YPoJkJafS._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="You Had Me at Hola: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-8" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="You Had Me at Hola: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2">You Had Me at Hola: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.3 out of 5 stars</span></i> <span class="a-size-small">1,391</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$12.00</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="You Had Me at Hola: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81HTf+30KHL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Wanna Bet?: An Interracial Romance (Dirty British Romance)" src="https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-9" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Wanna Bet?: An Interracial Romance (Dirty British Romance)" src="https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">Wanna Bet?: An Interracial Romance (Dirty British Romance)</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.3 out of 5 stars</span></i> <span class="a-size-small">709</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Wanna Bet?: An Interracial Romance (Dirty British Romance)" src="https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71ant7Ts6EL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="His &amp; Hers: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-10" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="His &amp; Hers: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">His &amp; Hers: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.3 out of 5 stars</span></i> <span class="a-size-small">4,625</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$9.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="His &amp; Hers: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91Ods7iErCL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Just Last Night: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-11" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Just Last Night: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Just Last Night: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.4 out of 5 stars</span></i> <span class="a-size-small">1,299</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$10.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Just Last Night: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71+wuqxzYqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="The Soulmate Equation" src="https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-12" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="The Soulmate Equation" src="https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">The Soulmate Equation</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.4 out of 5 stars</span></i> <span class="a-size-small">6,513</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$1.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="The Soulmate Equation" src="https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/815BFYciADL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Rock Paper Scissors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-13" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Rock Paper Scissors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Rock Paper Scissors: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-top"><span class="a-icon-alt">4.2 out of 5 stars</span></i> <span class="a-size-small">7,106</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$14.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Rock Paper Scissors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91CktmxU6dL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems" src="https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-14" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems" src="https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems">Designing Data-Intensive Applications: The Big Ideas…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-top"><span class="a-icon-alt">4.8 out of 5 stars</span></i> <span class="a-size-small">2,349</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$35.00</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE Delivery</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems" src="https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91JAIKQUkYL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming" src="https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-15" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming" src="https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming">Python Crash Course, 2nd Edition: A Hands-On, Project-Based…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.7 out of 5 stars</span></i> <span class="a-size-small">5,952</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$21.49</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto"><b>Today by 10:00 PM</b></span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming" src="https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Storytelling with Data: A Data Visualization Guide for Business Professionals" src="https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-16" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Storytelling with Data: A Data Visualization Guide for Business Professionals" src="https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2" title="Storytelling with Data: A Data Visualization Guide for Business Professionals">Storytelling with Data: A Data Visualization Guide for Business…</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.6 out of 5 stars</span></i> <span class="a-size-small">2,618</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$19.25</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto"><b>Today by 10:00 PM</b></span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Storytelling with Data: A Data Visualization Guide for Business Professionals" src="https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/41M8UKaaO1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Behind Closed Doors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-17" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Behind Closed Doors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Behind Closed Doors: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.3 out of 5 stars</span></i> <span class="a-size-small">28,439</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$9.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Behind Closed Doors: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/91wi9P3fGSL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Everything for You (Bergman Brothers Book 5)" src="https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-18" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Everything for You (Bergman Brothers Book 5)" src="https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">Everything for You (Bergman Brothers Book 5)</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$3.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Everything for You (Bergman Brothers Book 5)" src="https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/715hR8Ko+5L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Book Lovers" src="https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-19" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Book Lovers" src="https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">Book Lovers</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$9.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Book Lovers" src="https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71duwitbLBL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="The Family Upstairs: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-20" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="The Family Upstairs: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2">The Family Upstairs: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.4 out of 5 stars</span></i> <span class="a-size-small">30,593</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$11.38</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="The Family Upstairs: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71xz3rSG2pL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="My Favorite Half-Night Stand" src="https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-21" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="My Favorite Half-Night Stand" src="https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">My Favorite Half-Night Stand</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.4 out of 5 stars</span></i> <span class="a-size-small">1,997</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$10.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="My Favorite Half-Night Stand" src="https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71KbI8StdqL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="The Missed Connection" src="https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-22" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="The Missed Connection" src="https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">The Missed Connection</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$1.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="The Missed Connection" src="https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71dyo5mptML._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="The Bride Test" src="https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-23" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="The Bride Test" src="https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL254_SR254,254_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="2">The Bride Test</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.4 out of 5 stars</span></i> <span class="a-size-small">3,391</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$9.94</span></span><div class="a-row"><span class="_p13n-desktop-ysh_prime_p13n-prime-badge__GVM4h"><i class="a-icon a-icon-prime a-icon-small" role="presentation"></i></span>&nbsp;<span class="a-size-mini a-color-base" dir="auto">FREE One-Day</span></div></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="The Bride Test" src="https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81++qN-RI1L._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="The Wife Between Us: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-24" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="The Wife Between Us: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">The Wife Between Us: A Novel</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-top"><span class="a-icon-alt">4.3 out of 5 stars</span></i> <span class="a-size-small">12,655</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$9.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="The Wife Between Us: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71hNf6V8I0L._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Love Her or Lose Her: A Novel (Hot and Hammered Book 2)" src="https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-25" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Love Her or Lose Her: A Novel (Hot and Hammered Book 2)" src="https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Love Her or Lose Her: A Novel (Hot and Hammered Book 2)</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-top"><span class="a-icon-alt">4.2 out of 5 stars</span></i> <span class="a-size-small">1,389</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$10.49</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Love Her or Lose Her: A Novel (Hot and Hammered Book 2)" src="https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71VD1HsM5ZL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Tools of Engagement: A Novel (Hot &amp; Hammered Book 3)" src="https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-26" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Tools of Engagement: A Novel (Hot &amp; Hammered Book 3)" src="https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="3">Tools of Engagement: A Novel (Hot &amp; Hammered Book 3)</div></span><div class="a-row"><div class="a-icon-row"><i class="a-icon a-icon-star-small a-star-small-4 aok-align-top"><span class="a-icon-alt">4.2 out of 5 stars</span></i> <span class="a-size-small">1,728</span></div></div><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$10.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Tools of Engagement: A Novel (Hot &amp; Hammered Book 3)" src="https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/71HT2yRgPUL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div><div id="gridItemRoot" class="a-column a-span12 a-text-center _p13n-desktop-ysh_style_grid-column__UjCjt p13n-grid-column-root"><div class="a-cardui _p13n-desktop-ysh_style_expandedGridCell__15bML aok-hidden p13n-grid-image-only" data-a-card-type="basic"><div class="a-section a-spacing-mini" style=""><img alt="Ten Trends to Seduce Your Bestfriend" src="https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div></div><div id="p13n-asin-index-27" class="a-cardui _p13n-desktop-ysh_style_grid-cell__zFYyO p13n-grid-content" data-a-card-type="basic"><div><div class="a-section a-spacing-mini _p13n-desktop-ysh_maskStyle_noop__3Xbw5"><img alt="Ten Trends to Seduce Your Bestfriend" src="https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL381_SR381,381_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><span class="a-size-small"><div class="p13n-sc-truncate-desktop-type2  p13n-sc-truncated" aria-hidden="true" data-rows="4">Ten Trends to Seduce Your Bestfriend</div></span><div class="a-row"><span class="a-size-base a-color-price"><span class="_p13n-desktop-ysh_price_p13n-sc-price__3mJ9Z">$5.99</span></span></div></div></div><div class="a-cardui _p13n-desktop-ysh_style_card__2VZFf aok-hidden p13n-grid-overlay" data-a-card-type="basic"><div class="a-section _p13n-desktop-ysh_style_image__rSmhM" style=""><img alt="Ten Trends to Seduce Your Bestfriend" src="https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL127_SR127,127_.jpg" class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image" height="127px" data-a-dynamic-image="{&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL127_SR127,127_.jpg&quot;:[127,127],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL254_SR254,254_.jpg&quot;:[254,254],&quot;https://images-na.ssl-images-amazon.com/images/I/81Ywr15HXcL._AC_UL381_SR381,381_.jpg&quot;:[381,381]}" style="max-width:127px;max-height:127px"></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_overlayTitle__E6uXy"><span class="a-size-medium p13n-grid-RemovedMessage a-text-bold">Removed</span></div></div><div class="a-row a-grid-vertical-align a-grid-center _p13n-desktop-ysh_style_feedbackRow__23bqz"><div class="a-column a-span11 a-text-center _p13n-desktop-ysh_style_notInterestedMessage__2bIn5"><span class="a-size-base p13n-grid-RemovedDescription">You said you are not interested in this</span></div></div></div></div></div><div id="endOfList"></div></div></div><hr aria-hidden="true" class="a-divider-normal _p13n-desktop-ysh_style_widgetDivider__2cOPG"></div><script>if(window.mix_csa){window.mix_csa('[cel_widget_id="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0"]', 'CardInstanceFOByMFw_L28FsdSKGGpNQw')('mark', 'be')}</script>
<script>if(window.uet){window.uet('be','p13n-desktop-ysh_pbook-storefront-infinite-scroll_0',{wb: 1})}</script>
<script>if(window.mixTimeout){window.mixTimeout('p13n-desktop-ysh', 'CardInstanceFOByMFw_L28FsdSKGGpNQw', 90000)};
P.when('mix:@amzn/mix.client-runtime', 'mix:p13n-desktop-ysh__iazZoN5U').execute(function (runtime, cardModule) {runtime.registerCardFactory('CardInstanceFOByMFw_L28FsdSKGGpNQw', cardModule).then(function(){if(window.mix_csa){window.mix_csa('[cel_widget_id="p13n-desktop-ysh_pbook-storefront-infinite-scroll_0"]', 'CardInstanceFOByMFw_L28FsdSKGGpNQw')('mark', 'functional')}if(window.uex){window.uex('ld','p13n-desktop-ysh_pbook-storefront-infinite-scroll_0',{wb: 1})}});});
</script>
<script>P.load.js('https://images-na.ssl-images-amazon.com/images/I/41TavVAsNFL.js?xcp');
</script>
</div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-912614e3-2b52-463a-bdbb-07c9749935a7 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="9d2b061c-9a78-38b1-a678-3ed75b4a10f6" data-csa-c-content-id="amzn1.sym.912614e3-2b52-463a-bdbb-07c9749935a7" data-csa-c-slot-id="9d2b061c-9a78-38b1-a678-3ed75b4a10f6-16" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="kr4ot9-ruqzxz-5abvra-fag874" data-cel-widget="9d2b061c-9a78-38b1-a678-3ed75b4a10f6">

























<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01CsPicJWpL.css?AUIClients/ACSWidgetAssets-carousel">




<div id="carousel_932790" class="acswidget acswidget-carousel celwidget a-spacing-base acswidget-carousel--shoveler acswidget-carousel--default" cel_widget_id="acsux-widgets_carousel_merchandised-search-12" data-csa-c-id="g7qr0e-asx74m-r2u9s5-1rmnb8" data-cel-widget="acsux-widgets_carousel_merchandised-search-12">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_carousel_merchandised-search-12', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"carousel","type":"initialize"}, 'acsux-widgets', null);
}</script>


    
    
    
        
        
            <h2 class="a-spacing-mini acswidget-carousel__header">
                <span class="acswidget-carousel__title">
                    Most wished for in Books
                </span>

                
                

                
                    
                    <a aria-label="See more Most wished for in Books" class="a-size-base a-spacing-top-small a-link-emphasis aok-float-right acswidget-carousel__seemore a-text-normal" href="/gp/most-wished-for/books/283155/ref=s9_acsd_ri_bw_clnk/ref=s9_acsd_ri_bw_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
                        
                            See more
                        
                    </a>
                

                
                

                <hr aria-hidden="true" class="a-spacing-base a-spacing-top-mini a-divider-normal acswidget-carousel__divider">
            </h2>
        
    


    <div class="a-box-group acswidget-carousel__carousel-container">
        

















<div id="carousel" data-a-carousel-options="{&quot;set_size&quot;:39,&quot;minimum_gutter_width&quot;:15,&quot;maintain_state&quot;:false,&quot;show_partial_next&quot;:false,&quot;name&quot;:&quot;carousel&quot;,&quot;mobile&quot;:false,&quot;single_page_align&quot;:&quot;stretch&quot;,&quot;first_item_flush_left&quot;:true,&quot;hide_off_screen&quot;:false}" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="none" class="a-begin a-carousel-container a-carousel-display-swap a-carousel-transition-swap a-spacing-top-small min-items--3"><input autocomplete="on" type="hidden" class="a-carousel-firstvisibleitem">
    <div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#" id="a-autoid-0"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list">
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-0" data-asin="0399226907" data-default-order="0" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0399226907/ref=s9_acsd_ri_bw_c2_x_0_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Very Hungry Caterpillar" src="https://images-na.ssl-images-amazon.com/images/I/41w4B0f21VL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41w4B0f21VL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0399226907/ref=s9_acsd_ri_bw_c2_x_0_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Very Hungry Caterpillar</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Very Hungry Cater…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Eric Carle
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Eric Carle
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$5.06</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">5<span class="a-price-decimal">.</span></span><span class="a-price-fraction">06</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(46,449)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-1" data-asin="0375851569" data-default-order="1" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0375851569/ref=s9_acsd_ri_bw_c2_x_1_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Dr. Seuss's Beginner Book Collection (Cat in the Hat, One Fish Two Fish, Green Eggs and Ham, Hop on Pop, F" src="https://images-na.ssl-images-amazon.com/images/I/51PWDGLykIL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51PWDGLykIL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0375851569/ref=s9_acsd_ri_bw_c2_x_1_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Dr. Seuss's Beginner Book Collection (Cat in the Hat, One Fish Two Fish, Green Eggs and Ham, Hop on Pop, Fox in Socks)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Dr. Seuss's Beginner Bo…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Dr. Seuss
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Dr. Seuss
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$26.47</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">26<span class="a-price-decimal">.</span></span><span class="a-price-fraction">47</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$49.95</span><span aria-hidden="true">$49.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(18,858)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-2" data-asin="0805047905" data-default-order="2" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0805047905/ref=s9_acsd_ri_bw_c2_x_2_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Brown Bear, Brown Bear, What Do You See?" src="https://images-na.ssl-images-amazon.com/images/I/51430n+9jlL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51430n+9jlL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0805047905/ref=s9_acsd_ri_bw_c2_x_2_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Brown Bear, Brown Bear, What Do You See?</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Brown Bear, Brown Be…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Bill Martin Jr., Eric Carle
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Bill Martin Jr., Eric Carle
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$5.36</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">5<span class="a-price-decimal">.</span></span><span class="a-price-fraction">36</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(38,387)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-3" data-asin="1589255518" data-default-order="3" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1589255518/ref=s9_acsd_ri_bw_c2_x_3_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="I Love You to the Moon and Back" src="https://images-na.ssl-images-amazon.com/images/I/51p2SDOCV9L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51p2SDOCV9L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1589255518/ref=s9_acsd_ri_bw_c2_x_3_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">I Love You to the Moon and Back</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">I Love You to the Moo…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Amelia Hepworth, Tim Warnes
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Amelia Hepworth, Tim…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.31</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">31</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$7.99</span><span aria-hidden="true">$7.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(50,036)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-4" data-asin="0694003611" data-default-order="4" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0694003611/ref=s9_acsd_ri_bw_c2_x_4_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Goodnight Moon" src="https://images-na.ssl-images-amazon.com/images/I/51Ix49rxgtL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51Ix49rxgtL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0694003611/ref=s9_acsd_ri_bw_c2_x_4_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Goodnight Moon</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Goodnight Moon</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Margaret Wise Brown, Clement Hurd
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Margaret Wise Brown,…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$5.36</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">5<span class="a-price-decimal">.</span></span><span class="a-price-fraction">36</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$8.99</span><span aria-hidden="true">$8.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(21,854)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-5" data-asin="0312527594" data-default-order="5" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0312527594/ref=s9_acsd_ri_bw_c2_x_5_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="See, Touch, Feel: A First Sensory Book" src="https://images-na.ssl-images-amazon.com/images/I/51dhuBJNmNL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51dhuBJNmNL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0312527594/ref=s9_acsd_ri_bw_c2_x_5_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">See, Touch, Feel: A First Sensory Book</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">See, Touch, Feel: A Firs…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Roger Priddy
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Roger Priddy
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$7.58</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">7<span class="a-price-decimal">.</span></span><span class="a-price-fraction">58</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$12.99</span><span aria-hidden="true">$12.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(7,256)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-6" data-asin="1442450703" data-default-order="6" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1442450703/ref=s9_acsd_ri_bw_c2_x_6_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Chicka Chicka Boom Boom (Board Book)" src="https://images-na.ssl-images-amazon.com/images/I/51wfzW0QnXL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51wfzW0QnXL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1442450703/ref=s9_acsd_ri_bw_c2_x_6_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Chicka Chicka Boom Boom (Board Book)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Chicka Chicka Boom B…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Bill Martin Jr., John Archambault, Lois Ehlert
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Bill Martin Jr., John Arc…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.59</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">59</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$7.99</span><span aria-hidden="true">$7.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(29,788)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-7" data-asin="0451470796" data-default-order="7" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0451470796/ref=s9_acsd_ri_bw_c2_x_7_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Corduroy" src="https://images-na.ssl-images-amazon.com/images/I/51CSQG-vbuL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51CSQG-vbuL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0451470796/ref=s9_acsd_ri_bw_c2_x_7_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Corduroy</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Corduroy</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Don Freeman
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Don Freeman
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.53</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">53</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$7.99</span><span aria-hidden="true">$7.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(13,662)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-8" data-asin="0399240462" data-default-order="8" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0399240462/ref=s9_acsd_ri_bw_c2_x_8_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Where's S" src="https://images-na.ssl-images-amazon.com/images/I/51o4b5AdNLL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51o4b5AdNLL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0399240462/ref=s9_acsd_ri_bw_c2_x_8_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Where's Spot?</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Where's Spot?</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Eric Hill
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Eric Hill
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.97</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">97</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$7.99</span><span aria-hidden="true">$7.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(25,213)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-9" data-asin="0920668372" data-default-order="9" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0920668372/ref=s9_acsd_ri_bw_c2_x_9_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Love You Forever" src="https://images-na.ssl-images-amazon.com/images/I/61k5YUaOrZL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/61k5YUaOrZL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0920668372/ref=s9_acsd_ri_bw_c2_x_9_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Love You Forever</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Love You Forever</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Robert Munsch, Sheila McGraw
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Robert Munsch, Sheila…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.98</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">98</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$5.95</span><span aria-hidden="true">$5.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(45,703)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-10" data-asin="0060254920" data-default-order="10" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0060254920/ref=s9_acsd_ri_bw_c2_x_10_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Where the Wild Things Are" src="https://images-na.ssl-images-amazon.com/images/I/61zGOvBSgAL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/61zGOvBSgAL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0060254920/ref=s9_acsd_ri_bw_c2_x_10_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Where the Wild Things Are</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Where the Wild Things…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Maurice Sendak
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Maurice Sendak
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$13.20</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">20</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$19.95</span><span aria-hidden="true">$19.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(28,785)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-11" data-asin="1400233321" data-default-order="11" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1400233321/ref=s9_acsd_ri_bw_c2_x_11_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="You Can Count on God: 100 Devotions for Kids" src="https://images-na.ssl-images-amazon.com/images/I/412KPjSbCnL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/412KPjSbCnL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1400233321/ref=s9_acsd_ri_bw_c2_x_11_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">You Can Count on God: 100 Devotions for Kids</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">You Can Count on God…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Max Lucado
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Max Lucado
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$15.29</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">15<span class="a-price-decimal">.</span></span><span class="a-price-fraction">29</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.99</span><span aria-hidden="true">$16.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(10)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-12" data-asin="0374300216" data-default-order="12" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0374300216/ref=s9_acsd_ri_bw_c2_x_12_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="If Animals Kissed Good Night" src="https://images-na.ssl-images-amazon.com/images/I/51PRQuO-xjL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51PRQuO-xjL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0374300216/ref=s9_acsd_ri_bw_c2_x_12_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">If Animals Kissed Good Night</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">If Animals Kissed Good…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Ann Whitford Paul, David Walker
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Ann Whitford Paul, Da…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.14</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">14</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$7.99</span><span aria-hidden="true">$7.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(62,831)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-13" data-asin="0735211299" data-default-order="13" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0735211299/ref=s9_acsd_ri_bw_c2_x_13_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Atomic Habits: An Easy &amp; Proven Way to Build Good Habits &amp; Break " src="https://images-na.ssl-images-amazon.com/images/I/515mvgd0pXL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/515mvgd0pXL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0735211299/ref=s9_acsd_ri_bw_c2_x_13_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Atomic Habits: An Easy &amp; Proven Way to Build Good Habits &amp; Break Bad Ones</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Atomic Habits: An Easy…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        James Clear
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        James Clear
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.98</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">98</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$27.00</span><span aria-hidden="true">$27.00</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(69,845)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-14" data-asin="1542025605" data-default-order="14" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1542025605/ref=s9_acsd_ri_bw_c2_x_14_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Reminders of Him: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/41n9-p6-PpL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41n9-p6-PpL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1542025605/ref=s9_acsd_ri_bw_c2_x_14_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Reminders of Him: A Novel</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Reminders of Him: A N…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Colleen Hoover
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Colleen Hoover
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.95</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">95</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$15.95</span><span aria-hidden="true">$15.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(46,083)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-15" data-asin="0679406417" data-default-order="15" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0679406417/ref=s9_acsd_ri_bw_c2_x_15_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Complete Maus: A Survivor's Tale (Pantheon Graphic Libr" src="https://images-na.ssl-images-amazon.com/images/I/51bX7G6BgXL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51bX7G6BgXL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0679406417/ref=s9_acsd_ri_bw_c2_x_15_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Complete Maus: A Survivor's Tale (Pantheon Graphic Library)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Complete Maus: A…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Art Spiegelman
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Art Spiegelman
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$23.29</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">23<span class="a-price-decimal">.</span></span><span class="a-price-fraction">29</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$35.00</span><span aria-hidden="true">$35.00</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(4,770)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-16" data-asin="052557221X" data-default-order="16" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/052557221X/ref=s9_acsd_ri_bw_c2_x_16_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Dr. Seuss Workbook: Grade 1: 260+ Fun Activities with Stickers and More! (Spelling, Phonics, Sight Words, Writ" src="https://images-na.ssl-images-amazon.com/images/I/51v8yD0yPNL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51v8yD0yPNL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/052557221X/ref=s9_acsd_ri_bw_c2_x_16_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Dr. Seuss Workbook: Grade 1: 260+ Fun Activities with Stickers and More! (Spelling, Phonics, Sight Words, Writing, Reading Comprehension, Math, ... Science, SEL) (Dr. Seuss Workbooks)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Dr. Seuss Workbook: G…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Dr. Seuss
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Dr. Seuss
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.62</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">62</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$12.99</span><span aria-hidden="true">$12.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">


        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-17" data-asin="0679805273" data-default-order="17" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0679805273/ref=s9_acsd_ri_bw_c2_x_17_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Oh, the Places You'll G" src="https://images-na.ssl-images-amazon.com/images/I/51x8pmqjY0L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51x8pmqjY0L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0679805273/ref=s9_acsd_ri_bw_c2_x_17_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Oh, the Places You'll Go!&nbsp;&nbsp;</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Oh, the Places You'll G…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Dr. Seuss
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Dr. Seuss
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$8.98</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">8<span class="a-price-decimal">.</span></span><span class="a-price-fraction">98</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$18.99</span><span aria-hidden="true">$18.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(34,901)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-18" data-asin="0312521065" data-default-order="18" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0312521065/ref=s9_acsd_ri_bw_c2_x_18_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="First 100 Board Book Box Set (3 books): First 100 Words, Numbers Colors Shapes, and First 100 Animals" src="https://images-na.ssl-images-amazon.com/images/I/514CZz2fN-L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/514CZz2fN-L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0312521065/ref=s9_acsd_ri_bw_c2_x_18_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">First 100 Board Book Box Set (3 books): First 100 Words, Numbers Colors Shapes, and First 100 Animals</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">First 100 Board Book B…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Roger Priddy
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Roger Priddy
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$13.17</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">17</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$17.97</span><span aria-hidden="true">$17.97</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(12,430)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-19" data-asin="9387779262" data-default-order="19" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/9387779262/ref=s9_acsd_ri_bw_c2_x_19_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="My First Library : Boxset of 10 Board Books for Kids" src="https://images-na.ssl-images-amazon.com/images/I/51bR0PX1y9L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51bR0PX1y9L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/9387779262/ref=s9_acsd_ri_bw_c2_x_19_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">My First Library : Boxset of 10 Board Books for Kids</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">My First Library : Boxse…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Wonder House Books
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Wonder House Books
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$17.19</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">17<span class="a-price-decimal">.</span></span><span class="a-price-fraction">19</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$19.99</span><span aria-hidden="true">$19.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(38,619)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-20" data-asin="1542029910" data-default-order="20" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1542029910/ref=s9_acsd_ri_bw_c2_x_20_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Silent Sisters (Charles Jenkins)" src="https://images-na.ssl-images-amazon.com/images/I/51rWyrdtxdL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51rWyrdtxdL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1542029910/ref=s9_acsd_ri_bw_c2_x_20_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Silent Sisters (Charles Jenkins)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Silent Sisters (Char…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Robert Dugoni
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Robert Dugoni
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$17.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">17<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$24.95</span><span aria-hidden="true">$24.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(1,203)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-21" data-asin="0671449028" data-default-order="21" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0671449028/ref=s9_acsd_ri_bw_c2_x_21_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Going-To-Bed Book" src="https://images-na.ssl-images-amazon.com/images/I/512kHsHZHNL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/512kHsHZHNL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0671449028/ref=s9_acsd_ri_bw_c2_x_21_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Going-To-Bed Book</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">The Going-To-Bed Book</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Sandra Boynton
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Sandra Boynton
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$3.59</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">3<span class="a-price-decimal">.</span></span><span class="a-price-fraction">59</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$5.99</span><span aria-hidden="true">$5.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(13,337)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-22" data-asin="0385376715" data-default-order="22" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0385376715/ref=s9_acsd_ri_bw_c2_x_22_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Wonderful Things You Will Be" src="https://images-na.ssl-images-amazon.com/images/I/51gEY86ijML._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51gEY86ijML._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0385376715/ref=s9_acsd_ri_bw_c2_x_22_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Wonderful Things You Will Be</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Wonderful Things…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Emily Winfield Martin
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Emily Winfield Martin
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$8.55</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">8<span class="a-price-decimal">.</span></span><span class="a-price-fraction">55</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$17.99</span><span aria-hidden="true">$17.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(20,480)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-23" data-asin="0312498586" data-default-order="23" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0312498586/ref=s9_acsd_ri_bw_c2_x_23_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Bright Baby Touch &amp; Feel Baby Animals (Bright Baby Touch and F" src="https://images-na.ssl-images-amazon.com/images/I/51h-N7R8QHL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51h-N7R8QHL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0312498586/ref=s9_acsd_ri_bw_c2_x_23_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Bright Baby Touch &amp; Feel Baby Animals (Bright Baby Touch and Feel)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Bright Baby Touch &amp; F…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Roger Priddy
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Roger Priddy
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$4.70</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">4<span class="a-price-decimal">.</span></span><span class="a-price-fraction">70</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(10,707)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-24" data-asin="0060256656" data-default-order="24" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0060256656/ref=s9_acsd_ri_bw_c2_x_24_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Giving Tree" src="https://images-na.ssl-images-amazon.com/images/I/41m-Tm2wAqL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41m-Tm2wAqL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0060256656/ref=s9_acsd_ri_bw_c2_x_24_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Giving Tree</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">The Giving Tree</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Shel Silverstein
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Shel Silverstein
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$9.09</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">09</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$17.99</span><span aria-hidden="true">$17.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(24,220)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-25" data-asin="1450805752" data-default-order="25" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1450805752/ref=s9_acsd_ri_bw_c2_x_25_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="World of Eric Carle, Around the Farm Animal 30-Button Sound Book - Great for First Words - PI Kids" src="https://images-na.ssl-images-amazon.com/images/I/51ddcXBCmcS._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51ddcXBCmcS._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1450805752/ref=s9_acsd_ri_bw_c2_x_25_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">World of Eric Carle, Around the Farm Animal 30-Button Sound Book - Great for First Words - PI Kids</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">World of Eric Carle, Ar…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        PI Kids, Editors of Publications International, Eric Carle
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        PI Kids, Editors of Publ…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$12.49</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">49</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.98</span><span aria-hidden="true">$16.98</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(15,511)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-26" data-asin="1949759229" data-default-order="26" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1949759229/ref=s9_acsd_ri_bw_c2_x_26_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Mountain Is You: Transforming Self-Sabotage Into Self-Mastery" src="https://images-na.ssl-images-amazon.com/images/I/31OB9IQdNaL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/31OB9IQdNaL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1949759229/ref=s9_acsd_ri_bw_c2_x_26_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Mountain Is You: Transforming Self-Sabotage Into Self-Mastery</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Mountain Is You: T…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Brianna Wiest
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Brianna Wiest
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$17.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">17<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(4,023)</span>

        
        
        




    




    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-27" data-asin="1452179611" data-default-order="27" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1452179611/ref=s9_acsd_ri_bw_c2_x_27_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="From Crook to Cook: Platinum Recipes from Tha Boss Dogg's Kitchen (Snoop Dogg Cookbook, Celebrity Cookbook" src="https://images-na.ssl-images-amazon.com/images/I/51Ycj8SiNkL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51Ycj8SiNkL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1452179611/ref=s9_acsd_ri_bw_c2_x_27_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">From Crook to Cook: Platinum Recipes from Tha Boss Dogg's Kitchen (Snoop Dogg Cookbook, Celebrity Cookbook with Soul Food Recipes) (Snoop Dog x Chronicle Books)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">From Crook to Cook: P…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Snoop Dogg, Ryan Ford
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Snoop Dogg, Ryan Ford
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$12.74</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">74</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$24.95</span><span aria-hidden="true">$24.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(23,132)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-28" data-asin="1936493837" data-default-order="28" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1936493837/ref=s9_acsd_ri_bw_c2_x_28_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Complete Cooking for Two Cookbook: 650 Recipes for Everything You'll Ever Want to Make (The Complete A" src="https://images-na.ssl-images-amazon.com/images/I/51LkSIFTHlL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51LkSIFTHlL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1936493837/ref=s9_acsd_ri_bw_c2_x_28_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Complete Cooking for Two Cookbook: 650 Recipes for Everything You'll Ever Want to Make (The Complete ATK Cookbook Series)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Complete Cooking…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        America's Test Kitchen
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        America's Test Kitchen
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$20.32</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">20<span class="a-price-decimal">.</span></span><span class="a-price-fraction">32</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$34.99</span><span aria-hidden="true">$34.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(7,595)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-29" data-asin="1523504676" data-default-order="29" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1523504676/ref=s9_acsd_ri_bw_c2_x_29_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Indestructibles: Hello, Farm!: Chew Proof · Rip Proof · Nontoxic · 100% Washable (Book for Babies, Newborn Boo" src="https://images-na.ssl-images-amazon.com/images/I/51+BqNwkLWL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51+BqNwkLWL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1523504676/ref=s9_acsd_ri_bw_c2_x_29_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Indestructibles: Hello, Farm!: Chew Proof · Rip Proof · Nontoxic · 100% Washable (Book for Babies, Newborn Books, Safe to Chew)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Indestructibles: Hello,…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Amy Pixton, Maddie Frost
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Amy Pixton, Maddie Fr…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$5.95</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">5<span class="a-price-decimal">.</span></span><span class="a-price-fraction">95</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(5,311)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-30" data-asin="1938093682" data-default-order="30" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1938093682/ref=s9_acsd_ri_bw_c2_x_30_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Hello, Baby Animals: A High-Contrast Book (High-Contrast Books)" src="https://images-na.ssl-images-amazon.com/images/I/51zBQcDaAvL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51zBQcDaAvL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1938093682/ref=s9_acsd_ri_bw_c2_x_30_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Hello, Baby Animals: A High-Contrast Book (High-Contrast Books)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Hello, Baby Animals: A…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        duopress, Julissa Mora
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        duopress, Julissa Mora
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$7.95</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">7<span class="a-price-decimal">.</span></span><span class="a-price-fraction">95</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(3,574)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-31" data-asin="1641520779" data-default-order="31" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1641520779/ref=s9_acsd_ri_bw_c2_x_31_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Baby Sign Language Made Easy: 101 Signs to Start Communicating with Your Child Now (Baby Sign Language Guides)" src="https://images-na.ssl-images-amazon.com/images/I/51mzZZBgapL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51mzZZBgapL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1641520779/ref=s9_acsd_ri_bw_c2_x_31_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Baby Sign Language Made Easy: 101 Signs to Start Communicating with Your Child Now (Baby Sign Language Guides)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Baby Sign Language M…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Lane Rebelo
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Lane Rebelo
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$12.37</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">37</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$14.99</span><span aria-hidden="true">$14.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(8,011)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-32" data-asin="0143127748" data-default-order="32" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0143127748/ref=s9_acsd_ri_bw_c2_x_32_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma" src="https://images-na.ssl-images-amazon.com/images/I/41D3enj6JVS._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41D3enj6JVS._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0143127748/ref=s9_acsd_ri_bw_c2_x_32_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Body Keeps the Sc…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Bessel van der Kolk M.D.
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Bessel van der Kolk M.D.
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.40</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">40</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$19.00</span><span aria-hidden="true">$19.00</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(43,613)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-33" data-asin="1681888238" data-default-order="33" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1681888238/ref=s9_acsd_ri_bw_c2_x_33_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Ultimate Reading Challenge: Complete a Goal, Open an Envelope, and Reveal Your Bookish Prize!" src="https://images-na.ssl-images-amazon.com/images/I/51ifWM99+OL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51ifWM99+OL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1681888238/ref=s9_acsd_ri_bw_c2_x_33_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Ultimate Reading Challenge: Complete a Goal, Open an Envelope, and Reveal Your Bookish Prize!</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">The Ultimate Reading…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Weldon Owen
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Weldon Owen
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Novelty Book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$26.54</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">26<span class="a-price-decimal">.</span></span><span class="a-price-fraction">54</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$29.99</span><span aria-hidden="true">$29.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(12)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-34" data-asin="006282015X" data-default-order="34" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/006282015X/ref=s9_acsd_ri_bw_c2_x_34_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Magnolia Table" src="https://images-na.ssl-images-amazon.com/images/I/51iDWMHbdhL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51iDWMHbdhL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/006282015X/ref=s9_acsd_ri_bw_c2_x_34_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Magnolia Table</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Magnolia Table</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Joanna Gaines, Marah Stets
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Joanna Gaines, Marah…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$16.59</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">16<span class="a-price-decimal">.</span></span><span class="a-price-fraction">59</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$29.99</span><span aria-hidden="true">$29.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(29,323)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-35" data-asin="1501128019" data-default-order="35" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1501128019/ref=s9_acsd_ri_bw_c2_x_35_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Love and Other Words" src="https://images-na.ssl-images-amazon.com/images/I/41AjSHCZiOL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41AjSHCZiOL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1501128019/ref=s9_acsd_ri_bw_c2_x_35_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Love and Other Words</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Love and Other Words</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Christina Lauren
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Christina Lauren
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$10.43</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">10<span class="a-price-decimal">.</span></span><span class="a-price-fraction">43</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.99</span><span aria-hidden="true">$16.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(4,358)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-36" data-asin="0544938097" data-default-order="36" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0544938097/ref=s9_acsd_ri_bw_c2_x_36_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Little Blue Truck's Spring" src="https://images-na.ssl-images-amazon.com/images/I/51VQB3uWu+L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51VQB3uWu+L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0544938097/ref=s9_acsd_ri_bw_c2_x_36_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Little Blue Truck's Springtime</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Little Blue Truck's Spri…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Alice Schertle, Jill McElmurry
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Alice Schertle, Jill McEl…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Board book</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$7.66</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">7<span class="a-price-decimal">.</span></span><span class="a-price-fraction">66</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$13.99</span><span aria-hidden="true">$13.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(11,303)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-37" data-asin="1476753180" data-default-order="37" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1476753180/ref=s9_acsd_ri_bw_c2_x_37_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Ugly Love: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/41g9RfNVZBL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41g9RfNVZBL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1476753180/ref=s9_acsd_ri_bw_c2_x_37_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Ugly Love: A Novel</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Ugly Love: A Novel</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Colleen Hoover
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Colleen Hoover
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$14.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.99</span><span aria-hidden="true">$16.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(30,627)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="39">
                






















<div id="acs-product-block-38" data-asin="0062997424" data-default-order="38" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0062997424/ref=s9_acsd_ri_bw_c2_x_38_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="The Club: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/41VorGI5jKL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41VorGI5jKL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0062997424/ref=s9_acsd_ri_bw_c2_x_38_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-12&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=912614e3-2b52-463a-bdbb-07c9749935a7&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">The Club: A Novel</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">The Club: A Novel</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Ellery Lloyd
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Ellery Lloyd
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$18.13</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">18<span class="a-price-decimal">.</span></span><span class="a-price-fraction">13</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$26.99</span><span aria-hidden="true">$26.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4"></i>            <span class="acs-product-block__rating__review-count">(72)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
    </ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#" id="a-autoid-1"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page</span></i></span></a></div></div></div>
<span class="a-end aok-hidden"></span></div>
    </div>

<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_carousel_merchandised-search-12', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_carousel_merchandised-search-12', {wb: 1});  // timestamp body-end</script>
</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-219d6bf0-72fe-4d91-86b9-9d1607f9c1f5 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="7fb59504-f5bb-4fdc-8aef-2cc0a8f8375b" data-csa-c-content-id="amzn1.sym.219d6bf0-72fe-4d91-86b9-9d1607f9c1f5" data-csa-c-slot-id="7fb59504-f5bb-4fdc-8aef-2cc0a8f8375b-18" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="onjxxf-ekhnf9-fnimqw-250icp" data-cel-widget="7fb59504-f5bb-4fdc-8aef-2cc0a8f8375b">

























<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/01CsPicJWpL.css?AUIClients/ACSWidgetAssets-carousel">




<div id="carousel_460809" class="acswidget acswidget-carousel celwidget a-spacing-base acswidget-carousel--shoveler acswidget-carousel--default" cel_widget_id="acsux-widgets_carousel_merchandised-search-14" data-csa-c-id="4t0ti5-onql5q-wqewsm-exd13j" data-cel-widget="acsux-widgets_carousel_merchandised-search-14">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_carousel_merchandised-search-14', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"carousel","type":"initialize"}, 'acsux-widgets', null);
}</script>


    
    
    
        
        
            <h2 class="a-spacing-mini acswidget-carousel__header">
                <span class="acswidget-carousel__title">
                    Page to Screen Adaptations
                </span>

                
                

                
                    
                    <a aria-label="See more Page to Screen Adaptations" class="a-size-base a-spacing-top-small a-link-emphasis aok-float-right acswidget-carousel__seemore a-text-normal" href="/kindle-dbs/search/ref=s9_acsd_al_bw_clnk/ref=s9_acsd_al_bw_c2_x_c2cl?
k=1250862809|1506714811|1789097312|1506721737|1641292970|059343837X|0593468074|059347130X&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
                        
                            See more
                        
                    </a>
                

                
                

                <hr aria-hidden="true" class="a-spacing-base a-spacing-top-mini a-divider-normal acswidget-carousel__divider">
            </h2>
        
    


    <div class="a-box-group acswidget-carousel__carousel-container">
        

















<div id="carousel" data-a-carousel-options="{&quot;set_size&quot;:8,&quot;minimum_gutter_width&quot;:15,&quot;maintain_state&quot;:false,&quot;show_partial_next&quot;:false,&quot;name&quot;:&quot;carousel&quot;,&quot;mobile&quot;:false,&quot;single_page_align&quot;:&quot;stretch&quot;,&quot;first_item_flush_left&quot;:true,&quot;hide_off_screen&quot;:false}" data-a-display-strategy="swap" data-a-transition-strategy="swap" data-a-ajax-strategy="none" class="a-begin a-carousel-container a-carousel-display-swap a-carousel-transition-swap a-spacing-top-small min-items--3"><input autocomplete="on" type="hidden" class="a-carousel-firstvisibleitem">
    <div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left"><a class="a-button a-button-image a-carousel-button a-carousel-goto-prevpage" tabindex="0" href="#" id="a-autoid-2"><span class="a-button-inner"><i class="a-icon a-icon-previous"><span class="a-icon-alt">Previous page</span></i></span></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport"><ol class="a-carousel" role="list">
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-0" data-asin="1250862809" data-default-order="0" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1250862809/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="All the Old Knives: A Novel" src="https://images-na.ssl-images-amazon.com/images/I/41HAQVjnTYL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41HAQVjnTYL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1250862809/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">All the Old Knives: A Novel</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">All the Old Knives: A N…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Olen Steinhauer
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Olen Steinhauer
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$17.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">17<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4"></i>            <span class="acs-product-block__rating__review-count">(498)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-1" data-asin="1506714811" data-default-order="1" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1506714811/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Critical Role Vox Machina: Origins Volume I" src="https://images-na.ssl-images-amazon.com/images/I/51RVq2uTZ4L._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51RVq2uTZ4L._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1506714811/ref=s9_acsd_al_bw_c2_x_1_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Critical Role Vox Machina: Origins Volume I</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Critical Role Vox Machi…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Critical Role, Matthew Mercer, Matthew Colville, Olivia Samson, Chris Northrop
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Critical Role, Matthew…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.59</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">59</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$19.99</span><span aria-hidden="true">$19.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(2,619)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-2" data-asin="1789097312" data-default-order="2" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1789097312/ref=s9_acsd_al_bw_c2_x_2_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Uncharted: The Official Movie Novelization" src="https://images-na.ssl-images-amazon.com/images/I/41cxX86XjTL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41cxX86XjTL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1789097312/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Uncharted: The Official Movie Novelization</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Uncharted: The Officia…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        S.D. Perry
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        S.D. Perry
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Mass Market Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$8.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">8<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>
                
                

                

                

                
                    

                    
    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(6)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-3" data-asin="1506721737" data-default-order="3" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1506721737/ref=s9_acsd_al_bw_c2_x_3_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Critical Role: Vox Machina Origins Library Edition: Series I &amp; II Collec" src="https://images-na.ssl-images-amazon.com/images/I/5172MLQ6alL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/5172MLQ6alL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1506721737/ref=s9_acsd_al_bw_c2_x_3_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Critical Role: Vox Machina Origins Library Edition: Series I &amp; II Collection</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Critical Role: Vox Mach…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Critical Role, Matthew Colville, Jody Houser, Olivia Samson, Chris Northrop
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">
        Critical Role, Matthew…</span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Hardcover</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$21.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">21<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$39.99</span><span aria-hidden="true">$39.99</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-5"></i>            <span class="acs-product-block__rating__review-count">(1,849)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-4" data-asin="1641292970" data-default-order="4" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/1641292970/ref=s9_acsd_al_bw_c2_x_4_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Slow Horses (Deluxe Edition) (Slough House)" src="https://images-na.ssl-images-amazon.com/images/I/51vf4bluOgL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/51vf4bluOgL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/1641292970/ref=s9_acsd_al_bw_c2_x_4_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Slow Horses (Deluxe Edition) (Slough House)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Slow Horses (Deluxe E…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Mick Herron
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Mick Herron
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$11.69</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">11<span class="a-price-decimal">.</span></span><span class="a-price-fraction">69</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.95</span><span aria-hidden="true">$16.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4"></i>            <span class="acs-product-block__rating__review-count">(3,544)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-5" data-asin="059343837X" data-default-order="5" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/059343837X/ref=s9_acsd_al_bw_c2_x_5_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Dune (Movie Tie-In)" src="https://images-na.ssl-images-amazon.com/images/I/41zSCBO3FOL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41zSCBO3FOL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/059343837X/ref=s9_acsd_al_bw_c2_x_5_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Dune (Movie Tie-In)</span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">Dune (Movie Tie-In)</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Frank Herbert
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Frank Herbert
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$13.86</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">86</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$18.00</span><span aria-hidden="true">$18.00</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(51,039)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-6" data-asin="0593468074" data-default-order="6" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/0593468074/ref=s9_acsd_al_bw_c2_x_6_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Station Eleven (Television Tie-in)" src="https://images-na.ssl-images-amazon.com/images/I/41512eumNzL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41512eumNzL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/0593468074/ref=s9_acsd_al_bw_c2_x_6_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Station Eleven (Television Tie-in)</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Station Eleven (Televis…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Emily St. John Mandel
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Emily St. John Mandel
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$12.85</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">12<span class="a-price-decimal">.</span></span><span class="a-price-fraction">85</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$16.95</span><span aria-hidden="true">$16.95</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(15,925)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
            <li class="a-carousel-card acswidget-carousel__card" role="listitem" aria-setsize="8">
                






















<div id="acs-product-block-7" data-asin="059347130X" data-default-order="7" class="a-section acs-product-block acs-product-block--default">

    
    












    
    
        
<div class="a-section a-spacing-mini a-spacing-top-micro acs-product-block__product-image">
    <a class="a-color-base a-link-normal" href="/dp/059347130X/ref=s9_acsd_al_bw_c2_x_7_i?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">

        
        
        



    













        
            <div class="acs-product-block__empty-badge" style="display: inline-block;"></div>

        <img alt="Stay Close (Movie Tie-In): A Novel" src="https://images-na.ssl-images-amazon.com/images/I/41yKy7z0zFL._AC_SX184_.jpg" data-a-hires="https://images-na.ssl-images-amazon.com/images/I/41yKy7z0zFL._AC_SX368_.jpg">
    </a>
</div>

    
    
    



    
    
    









<a class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title" href="/dp/059347130X/ref=s9_acsd_al_bw_c2_x_7_t?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-14&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=219d6bf0-72fe-4d91-86b9-9d1607f9c1f5&amp;pf_rd_i=283155">
    <span class="a-truncate a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">Stay Close (Movie Tie-In): A Novel</span><span class="a-truncate-cut" aria-hidden="true" style="height: 2.6em;">Stay Close (Movie Tie-I…</span></span>
</a>

    
    
        
        
            
            
                




<span class="a-truncate acs-product-block__contributor a-size-base" data-a-word-break="normal" data-a-max-rows="2" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 2.6em;" data-a-recalculate="false" data-a-updated="true"><span class="a-truncate-full a-offscreen">
        Harlan Coben
    </span><span class="a-truncate-cut" aria-hidden="true" style="height: auto;">
        Harlan Coben
    </span></span>
            
        
    

    
    
        



<div class="a-section a-spacing-micro acs-product-block__binding">
    
                                                                        <span class="acs-product-block__binding-value">Paperback</span>        
</div>
    

    
    
        







                









    <div class="a-section a-spacing-micro acs-product-block__price">




        

            
            

            

            

            
                


                
                


                        
                        

                    
<span class="a-price acs-product-block__price--buying" data-a-size="l" data-a-color="base"><span class="a-offscreen">$13.08</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">08</span></span></span>
                
                

                

                

                
                    

                    


                        

<span class="a-price a-text-price acs-product-block__price--strikethrough" data-a-size="b" data-a-strike="true"><span class="a-offscreen">$17.00</span><span aria-hidden="true">$17.00</span></span>    </div>

    

    
    




<div class="a-section a-spacing-micro acs-product-block__review">

    <div class="a-section a-spacing-micro acs-product-block__rating">

<i class="a-icon a-icon-star-medium a-star-medium-4-5"></i>            <span class="acs-product-block__rating__review-count">(3,814)</span>

        
        
        




    




    <i class="a-icon a-icon-prime a-icon-small" role="img" aria-label="Acs amazonPrime"></i>
    </div>
</div>


</div>
            </li>
        
    </ol></div></div><div class="a-carousel-col a-carousel-right"><a class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage" tabindex="0" href="#" id="a-autoid-3"><span class="a-button-inner"><i class="a-icon a-icon-next"><span class="a-icon-alt">Next page</span></i></span></a></div></div></div>
<span class="a-end aok-hidden"></span></div>
    </div>

<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_carousel_merchandised-search-14', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_carousel_merchandised-search-14', {wb: 1});  // timestamp body-end</script>
</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-09081ddd-8340-4873-a2f0-c5dec74d1c81 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="43d73413-5b2a-458b-bd0a-6a0db424f213" data-csa-c-content-id="amzn1.sym.09081ddd-8340-4873-a2f0-c5dec74d1c81" data-csa-c-slot-id="43d73413-5b2a-458b-bd0a-6a0db424f213-19" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="crp7vp-a0k4n5-wgtudb-tunib8" data-cel-widget="43d73413-5b2a-458b-bd0a-6a0db424f213">
























































    







<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41y7o03hqHL.css?AUIClients/ACSWidgetAssets-contentGrid">



<div class="acsUxWidget">
    <div id="contentGrid_962993" class="acswidget acswidget-content-grid celwidget US bxw-content-grid bxw-content-grid--ember bxc-grid--padding bxc-grid--spacing-large  bxc-grid--light" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15" data-is-mobile="false" data-csa-c-id="630dm0-s4hlpx-54hy2v-wyidq3" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_content-grid_merchandised-search-15', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"contentGrid","type":"initialize"}, 'acsux-widgets', null);
}</script>


        
        














        <div class="bxc-grid__container bxc-grid__container--width-1500" data-cel-widget="osa_browse_banner_2">
            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--12-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row1-col1" data-csa-c-id="bcejc9-jki2mm-71tedt-fyf5qm" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row1-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <img src="https://images-na.ssl-images-amazon.com/images/G/01/img16/books/content-grid/header/34111_books_us_type_title2_840x54_ember.png" alt="Popular authors &amp; series">
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row2-col1" data-csa-c-id="h19pdw-7xq7ym-ezh99r-db0efe" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row2-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Barack-Obama/e/B001H6OA8E/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_2a1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Barack Obama">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q4-2021/1524763160.jpg" alt="Barack Obama">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row2-col2" data-csa-c-id="zgsudn-wrhavf-wbnuuy-ojmk6r" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row2-col2">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/David-Chang/e/B002HQFV68/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_2b1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="David Chang">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/david_chang.jpg" alt="David Chang">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row2-col3" data-csa-c-id="j5i1u9-tkwg1-mvc6ae-d0hq7y" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row2-col3">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Shalane-Flanagan/e/B01KP145Q8/ref=s9_acss_bw_cg_CFQ122_2c1_w?ref=sr_ntt_srch_lnk_2&amp;qid=1638987522&amp;sr=1-2&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Shalane Flanagan">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/shalane_flagnan.jpg" alt="Shalane Flanagan">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row2-col4" data-csa-c-id="4fcru0-v2hq59-soyxv6-z53n6d" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row2-col4">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Gina-Homolka/e/B00JXTXG00/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_2d1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Gina Homolka">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/Gina_homolka.jpg" alt="Gina Homolka">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row3-col1" data-csa-c-id="swkb7d-xcmr85-9paizg-lfjaof" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row3-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/stores/page/21D51F4C-D500-42CC-93D2-AA9EA8C23D1C/ref=s9_acss_bw_cg_CFQ122_3a1_w?ingress=0&amp;visitId=e68c8be9-d515-48c3-bddc-34d62fc11077&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="The Plant Paradox">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/plant_paradox.jpg" alt="The Plant Paradox">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row3-col2" data-csa-c-id="mti8ar-4y88pp-oveura-rqhdpk" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row3-col2">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Bren%25C3%25A9-Brown/e/B001JP45BA/ref=s9_acss_bw_cg_CFQ122_3b1_w?ref=sr_ntt_srch_lnk_1&amp;qid=1638988232&amp;sr=1-1&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Brené Brown">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/brenebrown.jpg" alt="Brené Brown">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row3-col3" data-csa-c-id="rhqz4d-ha4ynz-z4o1iv-d4e68w" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row3-col3">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/stores/page/5C2DF4D0-DA22-47BC-BF27-1211F8B17D39/ref=s9_acss_bw_cg_CFQ122_3c1_w?ingress=0&amp;visitId=e68c8be9-d515-48c3-bddc-34d62fc11077&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Zora Neale Hurston">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/zora_neale_hurstob.jpg" alt="Zora Neale Hurston">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row3-col4" data-csa-c-id="9ixsyw-ev9mz4-806djs-am2pzx" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row3-col4">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/stores/page/4847E7CB-07C3-4263-9694-1BB2A292F0D7/ref=s9_acss_bw_cg_CFQ122_3d1_w?channel=HTP_SweetMags_CFQP_Jan2022&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Sweet Magnolias">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/sweetmagnolias.jpg" alt="Sweet Magnolias">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row4-col1" data-csa-c-id="40anx2-cr7hmz-hj13cr-hshg0q" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row4-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Danielle-Steel/e/B000APK2GC/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_4a1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Danielle Steel">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q4-2021/1984821520.jpg" alt="Danielle Steel">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row4-col2" data-csa-c-id="bzotax-tynapr-osa2b8-q9ebx5" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row4-col2">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/stores/page/7729D50D-E61F-4E70-B175-E565A70315BC/ref=s9_acss_bw_cg_CFQ122_4b1_w?ingress=0&amp;visitId=e68c8be9-d515-48c3-bddc-34d62fc11077&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Agatha Christie">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/agatha_christie.jpg" alt="Agatha Christie">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row4-col3" data-csa-c-id="1h8idh-jm7cnb-gz3e2q-dqbcru" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row4-col3">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/stores/page/EEB8FB0D-1031-4325-BC87-24CFB63B9692/ref=s9_acss_bw_cg_CFQ122_4c1_w?ingress=0&amp;visitId=e68c8be9-d515-48c3-bddc-34d62fc11077&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Bridgerton">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q3-2021/bridgerton.jpg" alt="Bridgerton">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row4-col4" data-csa-c-id="e1s399-pb9t4h-c6hfgk-cjunct" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row4-col4">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Diana-Gabaldon/e/B000APXMEG/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_4d1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Diana Gabaldon">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q4-2021/0385319959.jpg" alt="Diana Gabaldon">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row5-col1" data-csa-c-id="cz2ppt-yuwet8-qw76ag-9s1rb0" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row5-col1">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/V-E-Schwab/e/B00MLKA3WM/ref=s9_acss_bw_cg_CFQ122_5a1_w?ref=sr_ntt_srch_lnk_8&amp;qid=1638139298&amp;sr=1-8&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="V. E. Schwab">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/ve_schawab.jpg" alt="V. E. Schwab">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row5-col2" data-csa-c-id="x6qd0q-k8l76-k0gjnq-yd70kd" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row5-col2">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Sabaa-Tahir/e/B00OK3OY6O/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_5b1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Sabaa Tahir">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/sabaa_tahir.jpg" alt="Sabaa Tahir">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row5-col3" data-csa-c-id="u8b5j3-35gmrc-apn98f-f3gnuy" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row5-col3">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Ruta-Sepetys/e/B003NWP99Y/ref=dp_byline_cont_pop_book_1/ref=s9_acss_bw_cg_CFQ122_5c1_w?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Ruta Sepetys">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/ruta_septeys.jpg" alt="Ruta Sepetys">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--3-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-15_row5-col4" data-csa-c-id="h4i2qk-qpvcns-dqgtsq-z73crh" data-cel-widget="acsux-widgets_content-grid_merchandised-search-15_row5-col4">

            








    
    
        













    


    






































    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>






<div class="bxc-grid__image   bxc-grid__image--light">
    <a href="/Karen-M-McManus/e/B01M4HOSP5/ref=s9_acss_bw_cg_CFQ122_5d1_w?ref=sr_ntt_srch_lnk_3&amp;qid=1638988109&amp;sr=1-3&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=merchandised-search-15&amp;pf_rd_r=Z0KMT1JTKBYN6W6QW6GJ&amp;pf_rd_t=101&amp;pf_rd_p=09081ddd-8340-4873-a2f0-c5dec74d1c81&amp;pf_rd_i=283155" aria-label="Karen M. McManus">
                            <img src="https://images-na.ssl-images-amazon.com/images/G/01/US-hq/2020/img/Books/CatFav/Q1-2022/karen_m.jpg" alt="Karen M. McManus">
                    </a>
</div>


























    
    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            
        </div>

    
<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_content-grid_merchandised-search-15', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_content-grid_merchandised-search-15', {wb: 1});  // timestamp body-end</script>
</div>

</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-124d0d5d-4aa8-4ebf-99b6-cc1d39d13755 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="fd88df52-c128-4a0d-81f4-f21790d497a1" data-csa-c-content-id="amzn1.sym.124d0d5d-4aa8-4ebf-99b6-cc1d39d13755" data-csa-c-slot-id="fd88df52-c128-4a0d-81f4-f21790d497a1-22" data-csa-c-type="widget" data-csa-c-painter="raw:__NA_leo-widget_1.0" data-csa-c-id="en9jpk-g6xvc2-pz1f17-kjkhgd" data-cel-widget="fd88df52-c128-4a0d-81f4-f21790d497a1">
























































    







<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/I/41y7o03hqHL.css?AUIClients/ACSWidgetAssets-contentGrid">



<div class="acsUxWidget">
    <div id="contentGrid_136068" class="acswidget acswidget-content-grid celwidget US bxw-content-grid bxw-content-grid--ember bxc-grid--padding bxc-grid--spacing-large  bxc-grid--light" cel_widget_id="acsux-widgets_content-grid_merchandised-search-18" data-is-mobile="false" data-csa-c-id="to9lh6-q7vg90-8rde3t-1wdoxf" data-cel-widget="acsux-widgets_content-grid_merchandised-search-18">
<script type="text/javascript">if (typeof uet == 'function') uet('bb', 'acsux-widgets_content-grid_merchandised-search-18', {wb: 1});  // timestamp body-begin</script>
<script type="text/javascript">if (typeof ue == 'function') {
	ue.log({"widget":"contentGrid","type":"initialize"}, 'acsux-widgets', null);
}</script>


        
        














        <div class="bxc-grid__container bxc-grid__container--width-1500" data-cel-widget="osa_browse_banner_3">
            

                
                
                

                
                
                

                














    







    










    
    

    

    

        
        
        

        
        

        <div class="bxc-grid__row   bxc-grid__row--light  ">

                
            

                
            

                
                

                
                
                
                

                
































    












    
    

    
        <div class="bxc-grid__column  bxc-grid__column--12-of-12   bxc-grid__column--light">

            
                
                

                

                
                
                

                














    







    










    
    

    
        
        

        <div class="bxc-grid__content   bxc-grid__content--light celwidget" cel_widget_id="acsux-widgets_content-grid_merchandised-search-18_row1-col1" data-csa-c-id="7zxu5w-eacm98-z72nxg-f9htl8" data-cel-widget="acsux-widgets_content-grid_merchandised-search-18_row1-col1">

            








    
    
    
        













    
    
    
    
        
    




    
    
    
    
        
        
    























    





















    

    

    


<script type="text/javascript">
    function handleIframeSize (obj) {

        observePopUpIframe(obj)

        function resizeIframe (obj) {
            if (obj && obj.contentWindow && obj.contentWindow.document && obj.contentWindow.document.body
                && obj.contentWindow.document.body.offsetHeight && obj.contentWindow.document.body.offsetHeight > 200) {
                obj.style.height = obj.contentWindow.document.body.offsetHeight + 'px';
            } else {
                obj.style.height = '200px';
            }
        };

        function observePopUpIframe (obj) {
            const iframeContent = obj.contentWindow.document.body;
            const config = { attributes: true, childList: true, subtree: true };

            const callback = function() {
                resizeIframe(obj);
            };

            const observer = new MutationObserver(callback);
            observer.observe(iframeContent, config);

            obj.contentWindow.onbeforeunload = function(e) {
                observer.disconnect();
            };
        }
    }
</script>





<div class="bxc-grid__text a-text-left   bxc-grid__text--light">
    
        
        
            <h2>Books at Amazon</h2>
<p>The Amazon.com Books homepage helps you explore Earth's Biggest Bookstore without ever leaving the comfort of your couch. Here you'll find current best sellers in books, new releases in books, deals in books, Kindle eBooks, Audible audiobooks, and so much more. We have popular genres like Literature &amp; Fiction, Children's Books, Mystery &amp; Thrillers, Cooking, Comics &amp; Graphic Novels, Romance, Science Fiction &amp; Fantasy, and Amazon programs such as Best Books of the Month, the Amazon Book Review, and Amazon Charts to help you discover your next great read.</p>
<p>In addition, you'll find great book recommendations that may be of interest to you based on your search and purchase history, as well as the most wished for and most gifted books. We hope you enjoy the Amazon.com Books homepage!</p>
        
    
</div>



    













    
    

        
</div>

    

    




                
                
            

        </div>
    



                
                

            
        </div>
    




            
        </div>

    
<script type="text/javascript">if (typeof uex == 'function') uex('ld', 'acsux-widgets_content-grid_merchandised-search-18', {wb: 1});  // timestamp page-loaded + send the metrics</script>
<script type="text/javascript">if (typeof uet == 'function') uet('be', 'acsux-widgets_content-grid_merchandised-search-18', {wb: 1});  // timestamp body-end</script>
</div>

</div>



</div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
            </div>
        
            <div class="a-column a-span12 apb-browse-left-nav apb-browse-col-pad-right a-span-last">
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-cede6ab2-c031-4edc-9216-2ac77c066f28 pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="6128b384-be6d-4583-b38a-be0bb25dd365" data-csa-c-content-id="amzn1.sym.cede6ab2-c031-4edc-9216-2ac77c066f28" data-csa-c-slot-id="6128b384-be6d-4583-b38a-be0bb25dd365-5" data-csa-c-type="widget" data-csa-c-painter="xslt:__application_Amabot_StaticContentXSLTs_browsebox.xsl" data-csa-c-id="l5nrii-bkhg0r-4n08b9-dm9tkf" data-cel-widget="6128b384-be6d-4583-b38a-be0bb25dd365"><!--wlbb--><style type="text/css">
        #a-page div.left_nav.browseBox {
            font-family: arial,helvetica,sans-serif;
        }
        #a-page div.left_nav.browseBox ul {
            margin: 0 0 10px 10px;
            padding: 0px;
        }
        #a-page div.left_nav.browseBox ul li {
            list-style-type: none;
            line-height: 17px;
        }
        #a-page div.left_nav.browseBox h3 {
            font-size: 13px;
            padding: 0;
            color: #000;
        }
        #a-page div.left_nav.browseBox h2 {
            display: none;
        }
        #a-page div.left_nav.browseBox p {
            margin-left: 8px;
        }
        #a-page div.left_nav.browseBox .carat {
            font-weight: bold;
            font-size: 120%;
            font-family: verdana,arial,helvetica,sans-serif;
            color: #E47911;
            margin-right: 0.2em;
        }
        #a-page div.left_nav.browseBox a, div.left_nav p a {
            color: #333;
            font-size: 12px;
            margin-left: 0;
            text-decoration: none;
        }
        #a-page div.left_nav.browseBox a:hover, div.left_nav p a:hover {
            text-decoration: none;
            background-color: transparent;
            color: #e47911;
        }
    </style><div class="left_nav browseBox"><h2 style=""></h2><h3>Popular in Books</h3><ul><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=21606498011&amp;ref_=bkevtwhm_bhp_nav">Celebrate Women's History Month</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=21227993011&amp;ref_=amb_link_YSizhL5tRYOzir4Lsl3TZQ_2">Amplify Black Voices</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=17143709011&amp;ref_=bhp_brws_botm">Best Books of the Month</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=17276804011&amp;ref_=bhp_brws_boty21">Best Books of 2021</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=16568978011&amp;ref_=bhp_brws_Esp">Books in Spanish</a></li><li><a href="/amazonbookreview/celebritypicks.html?rw_useCurrentProtocol=1&amp;ref_=abr_on_lp_n_bhp_sb">Celebrity Picks</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=4&amp;ref_=bhp_brws_chp">Children's Books</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=45&amp;ref_=bhp_brws_dibs">Deals in Books</a></li></ul><h3>More in Books</h3><ul><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=8192263011&amp;ref_=bhp_brws_100bks">100 Books to Read in a Lifetime</a></li><li><a href="/amazonbookreview?rw_useCurrentProtocol=1&amp;ref_=abr_on_lp_n_bhp_sb">Amazon Book Review</a></li><li><a href="https://www.facebook.com/Amazon.comBooks?rw_useCurrentProtocol=1&amp;ref_=bhp_brws_FB">Amazon Books on Facebook</a></li><li><a href="http://www.twitter.com/amazonbooks?rw_useCurrentProtocol=1&amp;ref_=bhp_brws_Twtr">Amazon Books on Twitter</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=13270229011&amp;ref_=bhp_ABS">Amazon Books Stores</a></li><li><a href="/firstreads?rw_useCurrentProtocol=1&amp;ref=afr_BHP%2F&amp;ref_=amb_link_YSizhL5tRYOzir4Lsl3TZQ_14">Amazon First Reads</a></li><li><a href="https://www.amazon.com/amazonbookclubs/amazonbookclubs?rw_useCurrentProtocol=1&amp;ref_=amb_link_YSizhL5tRYOzir4Lsl3TZQ_15">Book Club Picks</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=6574866011&amp;ref_=pts_BHP">From Page to Screen</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=6574835011&amp;ref_=sans_BHP">Start a New Series</a></li></ul><h3>Textbooks</h3><ul><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=465600&amp;ref_=bhp_brws_txt_stor">Textbooks Store</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=17853655011&amp;ref_=bhp_brws_txt_rent">Textbook Rentals</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=2223210011&amp;ref_=bhp_brws_txt_etxt">Kindle eTextbooks</a></li></ul><h3>Kindle &amp; Audible</h3><ul><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=18145289011&amp;ref_=audible_BHP">Audible Audiobooks</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=154606011&amp;ref_=bhp_brws_kin_ebk">Kindle eBooks</a></li><li><a href="/gp/browse.html?rw_useCurrentProtocol=1&amp;node=11552285011&amp;ref_=bhp_brws_kin_kdd">Kindle Deals</a></li><li><a href="/kindle-dbs/ku2/ui/rw/about?rw_useCurrentProtocol=1&amp;ref_=bhp_brws_kin_ku">Kindle Unlimited</a></li><li><a href="/kindle-Vella?rw_useCurrentProtocol=1&amp;ref_=amb_link_YSizhL5tRYOzir4Lsl3TZQ_25">Kindle Vella</a></li><li><a href="/kindle-dbs/fd/prime-pr?rw_useCurrentProtocol=1&amp;ref_=amb_link_YSizhL5tRYOzir4Lsl3TZQ_26">Prime Reading</a></li></ul></div><div class="left_nav_footer">&nbsp;</div></div>

                      
                      
                    
                  </div>
                
              
                
                
                  <div class="a-row">
                    
                      
                      
                        







<div id="s-refinements" class="a-section a-spacing-none apb-browse-refinements">
    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Prime Reading</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_eleven_browse-bin%3A23616628011&amp;dc&amp;qid=1646693600&amp;rnid=23616627011&amp;ref=lp_1000_nr_p_n_feature_eleven_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Prime Reading Eligible</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">New Releases</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_publication_date%3A1250226011&amp;dc&amp;qid=1646693600&amp;rnid=1250225011&amp;ref=lp_1000_nr_p_n_publication_date_0">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Last 30 days</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_publication_date%3A1250227011&amp;dc&amp;qid=1646693600&amp;rnid=1250225011&amp;ref=lp_1000_nr_p_n_publication_date_1">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Last 90 days</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_publication_date%3A1250228011&amp;dc&amp;qid=1646693600&amp;rnid=1250225011&amp;ref=lp_1000_nr_p_n_publication_date_2">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Coming Soon</span>

    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Department</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
        
        
        
        
            






    <li class="a-spacing-micro"><span class="a-list-item">
        
            

<span class="a-size-base a-color-base apb-browse-refinements-indent-1 a-text-bold" dir="auto">Books</span>

        
    </span></li>
    
        






    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A1&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_0">
    
        

<span dir="auto">Arts &amp; Photography</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A2&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_1">
    
        

<span dir="auto">Biographies &amp; Memoirs</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A3&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_2">
    
        

<span dir="auto">Business &amp; Money</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A3248857011&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_3">
    
        

<span dir="auto">Calendars</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A4&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_4">
    
        

<span dir="auto">Children's Books</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A12290&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_5">
    
        

<span dir="auto">Christian Books &amp; Bibles</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A4366&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_6">
    
        

<span dir="auto">Comics &amp; Graphic Novels</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A5&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_7">
    
        

<span dir="auto">Computers &amp; Technology</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A6&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_8">
    
        

<span dir="auto">Cookbooks, Food &amp; Wine</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A48&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_9">
    
        

<span dir="auto">Crafts, Hobbies &amp; Home</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A8975347011&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_10">
    
        

<span dir="auto">Education &amp; Teaching</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A173507&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_11">
    
        

<span dir="auto">Engineering &amp; Transportation</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A10&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_12">
    
        

<span dir="auto">Health, Fitness &amp; Dieting</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A9&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_13">
    
        

<span dir="auto">History</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A86&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_14">
    
        

<span dir="auto">Humor &amp; Entertainment</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A10777&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_15">
    
        

<span dir="auto">Law</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A301889&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_16">
    
        

<span dir="auto">LGBTQ+ Books</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A17&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_17">
    
        

<span dir="auto">Literature &amp; Fiction</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A173514&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_18">
    
        

<span dir="auto">Medical Books</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A18&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_19">
    
        

<span dir="auto">Mystery, Thriller &amp; Suspense</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A20&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_20">
    
        

<span dir="auto">Parenting &amp; Relationships</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A3377866011&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_21">
    
        

<span dir="auto">Politics &amp; Social Sciences</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A21&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_22">
    
        

<span dir="auto">Reference</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A22&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_23">
    
        

<span dir="auto">Religion &amp; Spirituality</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A23&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_24">
    
        

<span dir="auto">Romance</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A75&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_25">
    
        

<span dir="auto">Science &amp; Math</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A25&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_26">
    
        

<span dir="auto">Science Fiction &amp; Fantasy</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A4736&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_27">
    
        

<span dir="auto">Self-Help</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A26&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_28">
    
        

<span dir="auto">Sports &amp; Outdoors</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A28&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_29">
    
        

<span dir="auto">Teen &amp; Young Adult</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A5267710011&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_30">
    
        

<span dir="auto">Test Preparation</span>

    
</a>

        
    </span></li>
    

    <li class="a-spacing-micro apb-browse-refinements-indent-2"><span class="a-list-item">
        
            



<a class="a-color-base a-link-normal" href="/s?bbn=1000&amp;rh=n%3A283155%2Cn%3A27&amp;dc&amp;qid=1646693600&amp;rnid=1000&amp;ref=lp_1000_nr_n_31">
    
        

<span dir="auto">Travel</span>

    
</a>

        
    </span></li>
    




    




        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Format</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_0">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Paperback</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656020011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_1">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Hardcover</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A618073011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_2">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Kindle Edition</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A14725254011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_3">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Large Print</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A1240885011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_4">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Audible Audiobook</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A7114437011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_5">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Printed Access Code</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A9934628011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_6">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Digital Access Code</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A13411983011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_7">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Loose Leaf</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A2682077011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_8">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Audio CD</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656019011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_9">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Board Book</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_browse-bin%3A23488071011&amp;dc&amp;qid=1646693600&amp;rnid=618072011&amp;ref=lp_1000_nr_p_n_feature_browse-bin_10">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Spiral-bound</span>

    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Kindle Unlimited</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_twenty_browse-bin%3A13054657011&amp;dc&amp;qid=1646693600&amp;rnid=13054642011&amp;ref=lp_1000_nr_p_n_feature_twenty_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Kindle Unlimited Eligible</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Author</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3AJames+Clear&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_0">
            
    
        

<span class="a-size-base a-color-base" dir="auto">James Clear</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3AScholastic&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_1">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Scholastic</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3APeter+H.+Diamandis&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_2">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Peter H. Diamandis</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3ATony+Robbins&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_3">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Tony Robbins</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3AColleen+Hoover&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_4">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Colleen Hoover</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3AAdam+Wallace&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_5">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Adam Wallace</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_one_browse-bin%3AStephen+Perrine&amp;dc&amp;qid=1646693600&amp;rnid=2272759011&amp;ref=lp_1000_nr_p_lbr_one_browse-bin_6">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Stephen Perrine</span>

    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Book Series</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3AHow+to+Catch&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">How to Catch</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3ACrescent+City&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Crescent City</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3AToltec+Wisdom&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_2">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Toltec Wisdom</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3AMark+Manson+Collection&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_3">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Mark Manson Collection</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3ABellinger+Sisters&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_4">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Bellinger Sisters</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3AHarry+Potter&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_5">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Harry Potter</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_lbr_books_series_browse-bin%3ALittle+Blue+Truck&amp;dc&amp;qid=1646693600&amp;rnid=3275128011&amp;ref=lp_1000_nr_p_lbr_books_series_browse-bin_6">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Little Blue Truck</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Language</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291437011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">English</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291436011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">German</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291438011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_2">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">French</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291439011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_3">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Spanish</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291443011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_4">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Japanese</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291508011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_5">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Middle English</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_nine_browse-bin%3A3291479011&amp;dc&amp;qid=1646693600&amp;rnid=3291435011&amp;ref=lp_1000_nr_p_n_feature_nine_browse-bin_6">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Yiddish</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Climate Pledge Friendly</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_cpf_eligible%3A21512497011&amp;dc&amp;qid=1646693600&amp;rnid=21512496011&amp;ref=lp_1000_nr_p_n_cpf_eligible_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Climate Pledge Friendly</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Amazon Prime</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_85%3A2470955011&amp;dc&amp;qid=1646693600&amp;rnid=2470954011&amp;ref=lp_1000_nr_p_85_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        



<i class="a-icon a-icon-prime a-icon-medium apb-browse-refinements-icon" role="presentation"></i>


    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Eligible for Free Shipping</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_76%3A1250218011&amp;dc&amp;qid=1646693600&amp;rnid=1250216011&amp;ref=lp_1000_nr_p_76_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Free Shipping by Amazon</span>

    
    
        <div class="a-section a-spacing-none a-spacing-top-mini">
            
                

<span class="a-size-base a-color-base" dir="auto">All customers get FREE Shipping on orders over $25 shipped by Amazon</span>

            
        </div>
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Award Winners</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250579011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Booker Prize</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250578011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Caldecott Medal</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A7428544011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_2">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Eisner Award</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1251276011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_3">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Hugo &amp; Nebula Awards</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250580011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_4">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">National Book Award</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250582011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_5">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Newbery Medal</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250584011&amp;dc&amp;qid=1646693600&amp;rnid=1250577011&amp;ref=lp_1000_nr_p_n_feature_three_browse-bin_6">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Pulitzer Prize</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Packaging Option</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_is_ffp%3A7252855011&amp;dc&amp;qid=1646693600&amp;rnid=7252854011&amp;ref=lp_1000_nr_p_n_is_ffp_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Frustration-Free Packaging</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Promotion</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_special_merchandising_browse-bin%3A394172011&amp;dc&amp;qid=1646693600&amp;rnid=394171011&amp;ref=lp_1000_nr_p_n_special_merchandising_browse-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Bargain Books</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Avg. Customer Review</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_72%3A1250221011&amp;dc&amp;qid=1646693600&amp;rnid=1250219011&amp;ref=lp_1000_nr_p_72_0">
            
    <div aria-label="4 Stars &amp; Up" class="a-section">
        
            





    
    
        <i class="a-icon a-icon-star-medium a-star-medium-4"><span class="a-icon-alt">4 Stars &amp; Up</span></i>
    


        
            

<span class="a-size-small a-color-base" dir="auto">&amp; Up</span>

        
    </div>

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_72%3A1250222011&amp;dc&amp;qid=1646693600&amp;rnid=1250219011&amp;ref=lp_1000_nr_p_72_1">
            
    <div aria-label="3 Stars &amp; Up" class="a-section">
        
            





    
    
        <i class="a-icon a-icon-star-medium a-star-medium-3"><span class="a-icon-alt">3 Stars &amp; Up</span></i>
    


        
            

<span class="a-size-small a-color-base" dir="auto">&amp; Up</span>

        
    </div>

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_72%3A1250223011&amp;dc&amp;qid=1646693600&amp;rnid=1250219011&amp;ref=lp_1000_nr_p_72_2">
            
    <div aria-label="2 Stars &amp; Up" class="a-section">
        
            





    
    
        <i class="a-icon a-icon-star-medium a-star-medium-2"><span class="a-icon-alt">2 Stars &amp; Up</span></i>
    


        
            

<span class="a-size-small a-color-base" dir="auto">&amp; Up</span>

        
    </div>

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_72%3A1250224011&amp;dc&amp;qid=1646693600&amp;rnid=1250219011&amp;ref=lp_1000_nr_p_72_3">
            
    <div aria-label="1 Star &amp; Up" class="a-section">
        
            





    
    
        <i class="a-icon a-icon-star-medium a-star-medium-1"><span class="a-icon-alt">1 Star &amp; Up</span></i>
    


        
            

<span class="a-size-small a-color-base" dir="auto">&amp; Up</span>

        
    </div>

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Amazon Global Store</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_global_store_origin_marketplace%3A16354393011&amp;dc&amp;qid=1646693600&amp;rnid=16354392011&amp;ref=lp_1000_nr_p_n_global_store_origin_marketplace_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Amazon Global Store</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">International Shipping</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_shipping_option-bin%3A3242350011&amp;dc&amp;qid=1646693600&amp;rnid=2944662011&amp;ref=lp_1000_nr_p_n_shipping_option-bin_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">International Shipping Eligible</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Condition</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_condition-type%3A1294423011&amp;dc&amp;qid=1646693600&amp;rnid=1294421011&amp;ref=lp_1000_nr_p_n_condition-type_0">
            
    
        

<span class="a-size-base a-color-base" dir="auto">New</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_condition-type%3A1294425011&amp;dc&amp;qid=1646693600&amp;rnid=1294421011&amp;ref=lp_1000_nr_p_n_condition-type_1">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Used</span>

    

        </a>
    
    



                    </span></li>
                
            
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_condition-type%3A1294422011&amp;dc&amp;qid=1646693600&amp;rnid=1294421011&amp;ref=lp_1000_nr_p_n_condition-type_2">
            
    
        

<span class="a-size-base a-color-base" dir="auto">Collectible</span>

    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Deals</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_specials_match%3A21213697011&amp;dc&amp;qid=1646693600&amp;rnid=21213696011&amp;ref=lp_1000_nr_p_n_specials_match_0">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base" dir="auto">Today's Deals</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
        





<div class="a-section a-spacing-none">
    <div class="a-section a-spacing-small">
        
            

<span class="a-size-base a-color-base a-text-bold" dir="auto">Availability</span>

        
    </div>
    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-medium">
        
            
                
                
                    <li class="a-spacing-micro"><span class="a-list-item">
                        
















    
        <a class="a-link-normal" tabindex="-1" href="/s?bbn=283155&amp;rh=n%3A283155%2Cp_n_availability%3A2661600011&amp;dc&amp;qid=1646693600&amp;rnid=2661599011&amp;ref=lp_1000_nr_p_n_availability_1">
            
    
        



<div class="a-checkbox a-checkbox-fancy aok-float-left apb-browse-refinements-checkbox"><label><input type="checkbox" name="" value="" checked=""><i class="a-icon a-icon-checkbox"></i><span class="a-label a-checkbox-label"></span></label></div>

    
        

<span class="a-size-base a-color-base a-text-bold" dir="auto">Include Out of Stock</span>

    
    

        </a>
    
    



                    </span></li>
                
            
        
    </ul>
</div>

    
</div>


                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
                
                
              
            </div>
        
      </div>
    
      <div class="a-row">
        
            <div class="a-column a-span12">
              
                
                
                  <div class="a-row">
                    
                      
                        

<div class="celwidget pf_rd_p-9fc017f7-ce17-4762-a6b5-72ab4014314e pf_rd_r-Z0KMT1JTKBYN6W6QW6GJ" cel_widget_id="ebb57ba8-2c3c-3667-9bed-fd1470162cfc" data-csa-c-content-id="amzn1.sym.9fc017f7-ce17-4762-a6b5-72ab4014314e" data-csa-c-slot-id="ebb57ba8-2c3c-3667-9bed-fd1470162cfc-44" data-csa-c-type="widget" data-csa-c-painter="xslt:__application_Amabot_StaticContentXSLTs_RCM.xsl" data-csa-c-id="dpedr7-ygvz0n-aalcya-y87hru" data-cel-widget="ebb57ba8-2c3c-3667-9bed-fd1470162cfc"><!--wlrcm--><style type="text/css">
        #a-page div.unified_widget.rcmBody {
            font-size: 12px;
            font-family: arial,helvetica,sans-serif;
            line-height: 1.4 em;
        }
        #a-page div.unified_widget.rcmBody h2 {
            font-size:135%; 
            font-weight:bold;
            margin:0 0 0.35em 0px;
            color:#E47911; 
            padding:0;
        }
        #a-page div.unified_widget.rcmBody .headline {
            color: #E47911;
            font-size: .92em;
            display: block;
            font-weight: bold;
        }
        #a-page div.unified_widget.rcmBody p {
            margin:0 0 0.5em 0;
            line-height:1.4em;
        }
        #a-page div.unified_widget.rcmBody a {
            color: #004B91;
            text-decoration: underline;
        }
        #a-page div.unified_widget.rcmBody a:active {
            color: #FF9933;
        }
        #a-page div.unified_widget.rcmBody a:visited {
            color: #996633;
        }
        #a-page div.unified_widget.rcmBody hr {
            border-top: ridge;
            margin: 0px;
        }
        #a-page div.unified_widget.rcmBody ul {
            list-style-position: inside;
            margin: 1em 0;
            padding: 0 0 0 30px;
            color: #111;
        }
        #a-page div.unified_widget.rcmBody ul li {
            list-style: disc;
        }
        #a-page div.unified_widget.rcmBody div.bannerImage {
            text-align: center;
        }
        #a-page div.unified_widget.rcmBody .carat {
            font-weight: bold;
            font-size: 120%;
            color: #E47911;
            margin-right: 0.2em;
            font-family: verdana,arial,helvetica,sans-serif;
        }
        #a-page div.unified_widget.rcmBody div.prodImage {
            margin: 0 0.5em 0.25em 0;
            float: left;
        }
    </style><div class="unified_widget rcmBody"><p>
Amazon.com Books has the world’s largest selection of new and used titles to suit any reader's tastes.  Find best-selling books, new releases, and classics in every category, from Harper Lee's <i>To Kill a Mockingbird</i> to the latest by Stephen King or the next installment in the <i>Diary of a Wimpy Kid</i> children’s book series. Whatever you are looking for: popular fiction, cookbooks, mystery, romance, a new memoir, a look back at history, or books for kids and young adults, you can find it on Amazon.com Books.  Discover a new favorite author or book series, a debut novel or a best-seller in the making.  We have books to help you learn a new language, travel guides to take you on new adventures, and business books for entrepreneurs.  Let your inner detective run wild with our mystery, thriller &amp; suspense selection containing everything from hard-boiled sleuths to twisty psychological thrillers. Science fiction fans can start the <i>Game of Thrones</i> book series or see what's next from its author, George R.R. Martin. You’ll find the latest New York Times best-seller lists, and award winners in literature, mysteries, and children’s books.  Get reading recommendations from our Amazon book editors, who select the best new books each month and the best books of the year in our most popular genres. Read the books behind blockbuster movies like Suzanne Collins’ <i>The Hunger Games</i>,  John Green’s <i>The Fault in Our Stars</i>, Stephenie Meyers’ <i>Twilight</i> series, or E.L. James’ <i>50 Shades of Grey</i>. For new and returning students, we have textbooks to buy, rent or sell and teachers can find books for their classroom in our education store.   Whether you know which book you want or are looking for a recommendation, you’ll find it in the Amazon.com Books store.
</p><div class="h_rule"></div></div></div>

                      
                      
                    
                  </div>
                
              
                
                
              
                
                
              
                
                
              
            </div>
        
      </div>
    
    
  </div>

<!-- Registering CriticalFeatures to make sure our Nav JS is loaded. -->
<script>
    window.P.register('cf');
</script>
<!-- sp:end-feature:host-atf -->
<!-- sp:feature:nav-btf -->
<!-- NAVYAAN BTF START -->




  



  <script type="text/javascript">(function ($Nav) {
"use strict";

if (typeof $Nav === 'undefined' || $Nav === null || typeof $Nav.when !== 'function') {
    return;
}

$Nav.when('$', 'data', 'flyout.yourAccount', 'sidepanel.csYourAccount',
          'config')
    .run("BuyitAgain-YourAccount-SidePanel",
    function ($, data, yaFlyout, csYourAccount, config) {
        if (config.disableBuyItAgain) {
            return;
        }
        var render = function (data) {
            if (data.dramResult) {
                var widgetHtml = data.dramResult;
                navbar.sidePanel({
                    flyoutName: 'yourAccount',
                    data: {html: widgetHtml}
                });
            }
        };

        var renderBuyItAgain = function (biaData) {
            if (csYourAccount) {
                csYourAccount.register(render, biaData);
            } else {
                render(biaData);
            }
        };

        yaFlyout.sidePanel.onData(function() {
            if (window.P) {
                P.when('A', 'a-truncate').execute(function(A, truncate) {
                    var truncateElements = A.$('.a-truncate');
                    A.each(truncateElements, function(element) {
                        truncate.get(element).update();
                    });
                });
            }

        });

    yaFlyout.onRender(function() {
            $.ajax({
                url: '/gp/bia/external/bia-hcb-ajax-handler.html',
                data: { biaHcbRid: 'Z0KMT1JTKBYN6W6QW6GJ' },
                dataType: 'json',
                timeout: 4*1000,
                success: renderBuyItAgain,
                error: function (jqXHR, textStatus, errorThrown) {
                }
            });
        });
    });
})(window.$Nav);</script>


<script type="text/javascript">
  window.$Nav && $Nav.when("data").run(function (data) {
    data({
      "accountListContent": { "html": "<div id='nav-al-container'><div id='nav-al-wishlist' class='nav-al-column nav-tpl-itemList nav-flyout-content nav-flyout-accessibility'><div class='nav-title' id='nav-al-title'>Your Lists</div><a href='/hz/wishlist/ls?triggerElementID=createList&ref_=nav_ListFlyout_navFlyout_createList_lv_redirect' class='nav-link nav-item'><span class='nav-text'>Create a List</span></a> <a href='/registries?ref_=nav_ListFlyout_find' class='nav-link nav-item'><span class='nav-text'>Find a List or Registry</span></a> <a href='/gp/clpf?ref_=nav_ListFlyout_smi_se_ya_lll_ll' class='nav-link nav-item'><span class='nav-text'>AmazonSmile Charity Lists</span></a></div><div id='nav-al-your-account' class='nav-al-column nav-template nav-flyout-content nav-tpl-itemList nav-flyout-accessibility'><div class='nav-title'>Your Account</div><a href='/gp/css/homepage.html?ref_=nav_AccountFlyout_ya' class='nav-link nav-item'><span class='nav-text'>Account</span></a> <a id='nav_prefetch_yourorders' href='/gp/css/order-history?ref_=nav_AccountFlyout_orders' class='nav-link nav-item'><span class='nav-text'>Orders</span></a> <a href='/gp/yourstore?ref_=nav_AccountFlyout_recs' class='nav-link nav-item'><span class='nav-text'>Recommendations</span></a> <a href='/gp/history?ref_=nav_AccountFlyout_browsinghistory' class='nav-link nav-item'><span class='nav-text'>Browsing History</span></a> <a href='/gp/video/watchlist?ref_=nav_AccountFlyout_ywl' class='nav-link nav-item'><span class='nav-text'>Watchlist</span></a> <a href='/gp/video/library?ref_=nav_AccountFlyout_yvl' class='nav-link nav-item'><span class='nav-text'>Video Purchases & Rentals</span></a> <a href='/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku' class='nav-link nav-item'><span class='nav-text'>Kindle Unlimited</span></a> <a href='/hz/mycd/myx?pageType=content&ref_=nav_AccountFlyout_myk' class='nav-link nav-item'><span class='nav-text'>Content & Devices</span></a> <a href='/gp/subscribe-and-save/manager/viewsubscriptions?ref_=nav_AccountFlyout_sns' class='nav-link nav-item'><span class='nav-text'>Subscribe & Save Items</span></a> <a href='/hz5/yourmembershipsandsubscriptions?ref_=nav_AccountFlyout_digital_subscriptions' class='nav-link nav-item'><span class='nav-text'>Memberships & Subscriptions</span></a> <a href='/gp/gc/balance?ref_=nav_item_yourgcbalance' class='nav-link nav-item'><span class='nav-text'>Gift Card Balance</span></a> <a href='/gp/subs/primeclub/account/homepage.html?ref_=nav_AccountFlyout_prime' class='nav-link nav-item'><span class='nav-text'>Prime Membership</span></a> <a href='https://www.amazon.com/credit/landing?ref_=nav_AccountFlyout_ya_amazon_cc_landing_ms' class='nav-link nav-item'><span class='nav-text'>Amazon Credit Cards</span></a> <a href='https://music.amazon.com?ref=nav_youraccount_cldplyr' class='nav-link nav-item'><span class='nav-text'>Music Library</span></a> <a href='/b/?node=12766669011&ld=AZUSSOA-yaflyout&ref_=nav_AccountFlyout_cs_sell' class='nav-link nav-item'><span class='nav-text'>Start a Selling Account</span></a> <a href='/gp/browse.html?node=11261610011&ref_=nav_AccountFlyout_b2b_reg' class='nav-link nav-item'><span class='nav-text'>Register for a Business Account</span></a> <a id='nav-item-switch-account' href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%2F%3Fie%3DUTF8%26node%3D283155%26ref_%3Dnav_youraccount_switchacct&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=picker&ignoreAuthState=1&_encoding=UTF8' class='nav-link nav-item'><span class='nav-text'>Switch Accounts</span></a> <a id='nav-item-signout' href='/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&useRedirectOnSuccess=1&signIn=1&action=sign-out&ref_=nav_AccountFlyout_signout' class='nav-link nav-item'><span class='nav-text'>Sign Out</span></a></div></div>" },
      "signinContent": { "html": "<div id='nav-signin-tooltip'><a href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fb%2F%3F_encoding%3DUTF8%26node%3D283155%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-action-button' data-nav-role='signin' data-nav-ref='nav_custrec_signin'><span class='nav-action-inner'>Sign in</span></a><div class='nav-signin-tooltip-footer'>New customer? <a href='https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fb%2F%3F_encoding%3DUTF8%26node%3D283155%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&' class='nav-a'>Start here.</a></div></div>" },
      "templates": {"itemList":"<# var hasColumns = (function () {  var checkColumns = function (_items) {    if (!_items) {      return false;    }    for (var i=0; i<_items.length; i++) {      if (_items[i].columnBreak || (_items[i].items && checkColumns(_items[i].items))) {        return true;      }    }    return false;  };  return checkColumns(items);}()); #><# if(hasColumns) { #>  <# if(items[0].image && items[0].image.src) { #>    <div class='nav-column nav-column-first nav-column-image'>  <# } else if (items[0].greeting) { #>    <div class='nav-column nav-column-first nav-column-greeting'>  <# } else { #>    <div class='nav-column nav-column-first'>  <# } #><# } #><# var renderItems = function(items) { #>  <# jQuery.each(items, function (i, item) { #>    <# if(hasColumns && item.columnBreak) { #>      <# if(item.image && item.image.src) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-image'>      <# } else if (item.greeting) { #>        </div><div class='nav-column nav-column-notfirst nav-column-break nav-column-greeting'>      <# } else { #>        </div><div class='nav-column nav-column-notfirst nav-column-break'>      <# } #>    <# } #>    <# if(item.dividerBefore) { #>      <div class='nav-divider'></div>    <# } #>    <# if(item.text || item.content) { #>      <# if(item.url) { #>        <a href='<#=item.url #>' class='nav-link      <# } else {#>        <span class='      <# } #>      <# if(item.panelKey) { #>        nav-hasPanel      <# } #>      <# if(item.items) { #>        nav-title      <# } #>      <# if(item.decorate == 'carat') { #>        nav-carat      <# } #>      <# if(item.decorate == 'nav-action-button') { #>        nav-action-button      <# } #>      nav-item'      <# if(item.extra) { #>        <#=item.extra #>      <# } #>      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      <# if(item.dataNavRole) { #>        data-nav-role='<#=item.dataNavRole #>'      <# } #>      <# if(item.dataNavRef) { #>        data-nav-ref='<#=item.dataNavRef #>'      <# } #>      <# if(item.panelKey) { #>        data-nav-panelkey='<#=item.panelKey #>'        role='navigation'        aria-label='<#=item.text#>'      <# } #>      <# if(item.subtextKey) { #>        data-nav-subtextkey='<#=item.subtextKey #>'      <# } #>      <# if(item.image && item.image.height > 16) { #>        style='line-height:<#=item.image.height #>px;'      <# } #>      >      <# if(item.decorate == 'carat') { #>        <i class='nav-icon'></i>      <# } #>      <# if(item.image && item.image.src) { #>        <img class='nav-image' src='<#=item.image.src #>' style='height:<#=item.image.height #>px; width:<#=item.image.width #>px;' />      <# } #>      <# if(item.text) { #>        <span class='nav-text<# if(item.classname) { #> <#=item.classname #><# } #>'><#=item.text#><# if(item.badgeText) { #>          <span class='nav-badge'><#=item.badgeText#></span>        <# } #></span>      <# } else if (item.content) { #>        <span class='nav-content'><# jQuery.each(item.content, function (j, cItem) { #><# if(cItem.url && cItem.text) { #><a href='<#=cItem.url #>' class='nav-a'><#=cItem.text #></a><# } else if (cItem.text) { #><#=cItem.text#><# } #><# }); #></span>      <# } #>      <# if(item.subtext) { #>        <span class='nav-subtext'><#=item.subtext #></span>      <# } #>      <# if(item.url) { #>        </a>      <# } else {#>        </span>      <# } #>    <# } #>    <# if(item.image && item.image.src) { #>      <# if(item.url) { #>        <a href='<#=item.url #>'>       <# } #>      <img class='nav-image'      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      src='<#=item.image.src #>' <# if (item.alt) { #> alt='<#= item.alt #>'<# } #>/>      <# if(item.url) { #>        </a>       <# } #>    <# } #>    <# if(item.items) { #>      <div class='nav-panel'> <# renderItems(item.items); #> </div>    <# } #>  <# }); #><# }; #><# renderItems(items); #><# if(hasColumns) { #>  </div><# } #>","subnav":"<# if (obj && obj.type === 'vertical') { #>  <# jQuery.each(obj.rows, function (i, row) { #>    <# if (row.flyoutElement === 'button') { #>      <div class='nav_sv_fo_v_button'        <# if (row.elementStyle) { #>          style='<#= row.elementStyle #>'        <# } #>      >        <a href='<#=row.url #>' class='nav-action-button nav-sprite'>          <#=row.text #>        </a>      </div>    <# } else if (row.flyoutElement === 'list' && row.list) { #>      <# jQuery.each(row.list, function (j, list) { #>        <div class='nav_sv_fo_v_column <#=(j === 0) ? 'nav_sv_fo_v_first' : '' #>'>          <ul class='<#=list.elementClass #>'>          <# jQuery.each(list.linkList, function (k, link) { #>            <# if (k === 0) { link.elementClass += ' nav_sv_fo_v_first'; } #>            <li class='<#=link.elementClass #>'>              <# if (link.url) { #>                <a href='<#=link.url #>' class='nav_a'><#=link.text #></a>              <# } else { #>                <span class='nav_sv_fo_v_span'><#=link.text #></span>              <# } #>            </li>          <# }); #>          </ul>        </div>      <# }); #>    <# } else if (row.flyoutElement === 'link') { #>      <# if (row.topSpacer) { #>        <div class='nav_sv_fo_v_clear'></div>      <# } #>      <div class='<#=row.elementClass #>'>        <a href='<#=row.url #>' class='nav_sv_fo_v_lmargin nav_a'>          <#=row.text #>        </a>      </div>    <# } #>  <# }); #><# } else if (obj) { #>  <div class='nav_sv_fo_scheduled'>    <#= obj #>  </div><# } #>","htmlList":"<# jQuery.each(items, function (i, item) { #>  <div class='nav-item'>    <#=item #>  </div><# }); #>"}
    })
  })
</script>

<script type="text/javascript">
  window.$Nav && $Nav.declare('config.flyoutURL', null);
  window.$Nav && $Nav.declare('btf.lite');
  window.$Nav && $Nav.declare('btf.full');
  window.$Nav && $Nav.declare('btf.exists');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).register('navCF');
</script>













<script type="text/javascript">
  window.$Nav && window.$Nav.build('PldnLocalStorage', function() {
    var PldnLocalStorage = function() {};

    PldnLocalStorage.prototype.setItem = function(key, obj) {
      if (typeof obj !== 'string') {
        obj = window.JSON && window.JSON.stringify(obj);
      }

      try {
        window.localStorage && window.localStorage.setItem(key, obj);
        return true;
      } catch (exception) {
        return false;
      };
    };

    PldnLocalStorage.prototype.getItem = function(key) {
      try {
        return window.localStorage && window.localStorage.getItem(key);
      } catch(exception) {};
    };

    return new PldnLocalStorage();
  });

  window.$Nav && window.$Nav.when('PldnLocalStorage').run('PldnUcolCheck', function(storage) {
    if (!storage.getItem('amazonSmileCampaigns')) {
      storage.setItem('amazonSmileCampaigns', {
        "ucol": {
          "optOut": false,
          "hits": [
            {
              "date": new Date(),
              "redirect": false,
              "optOut": false
            }
          ]
        }
      });
    }
  });
</script>

<!-- NAVYAAN BTF END --><!-- sp:end-feature:nav-btf -->
<!-- sp:feature:host-btf -->
<!-- sp:end-feature:host-btf -->
<!-- sp:feature:aui-preload -->
<!-- sp:end-feature:aui-preload -->
<!-- sp:feature:nav-footer -->

  <!-- NAVYAAN FOOTER START -->
  <!-- WITH MOZART -->



<div class="navLeftFooter nav-sprite-v1" id="navFooter">
  
<a href="#nav-top" id="navBackToTop" aria-label="Back to top">
  <div class="navFooterBackToTop">
  <span class="navFooterBackToTopText">
    Back to top
  </span>
  </div>
</a>

  
<div class="navFooterVerticalColumn navAccessibility" role="presentation">
  <div class="navFooterVerticalRow navAccessibility" style="display: table-row;">
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Get to Know Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://www.amazon.jobs" class="nav_a">Careers</a>
            </li>
            <li>
              <a href="https://blog.aboutamazon.com/?utm_source=gateway&amp;utm_medium=footer&amp;token=about" class="nav_a">Blog</a>
            </li>
            <li>
              <a href="https://www.aboutamazon.com/?utm_source=gateway&amp;utm_medium=footer&amp;token=about" class="nav_a">About Amazon</a>
            </li>
            <li>
              <a href="https://sustainability.aboutamazon.com/?utm_source=gateway&amp;utm_medium=footer&amp;ref_=susty_footer" class="nav_a">Sustainability</a>
            </li>
            <li>
              <a href="https://www.amazon.com/pr" class="nav_a">Press Center</a>
            </li>
            <li>
              <a href="https://www.amazon.com/ir" class="nav_a">Investor Relations</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=2102313011&amp;ref_=footer_devices" class="nav_a">Amazon Devices</a>
            </li>
            <li class="nav_last ">
              <a href="https://www.amazon.science" class="nav_a">Amazon Science</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Make Money with Us</div>
        <ul>
            <li class="nav_first">
              <a href="https://sell.amazon.com/?ld=AZFSSOA&amp;ref_=footer_soa" class="nav_a">Sell products on Amazon</a>
            </li>
            <li>
              <a href="https://developer.amazon.com" class="nav_a">Sell apps on Amazon</a>
            </li>
            <li>
              <a href="https://affiliate-program.amazon.com/" class="nav_a">Become an Affiliate</a>
            </li>
            <li>
              <a href="https://www.fountain.com/jobs/amazon-delivery-service-partner?utm_source=amazon.com&amp;utm_medium=footer" class="nav_a">Become a Delivery Driver</a>
            </li>
            <li>
              <a href="https://logistics.amazon.com/marketing?utm_source=amzn&amp;utm_medium=footer&amp;utm_campaign=home" class="nav_a">Start a package delivery business</a>
            </li>
            <li>
              <a href="https://advertising.amazon.com/?ref=ext_amzn_ftr" class="nav_a">Advertise Your Products</a>
            </li>
            <li>
              <a href="/gp/seller-account/mm-summary-page.html?ld=AZFooterSelfPublish&amp;topic=200260520&amp;ref_=footer_publishing" class="nav_a">Self-Publish with Us</a>
            </li>
            <li>
              <a href="https://www.amazon.com/b/?node=13853235011" class="nav_a">Host an Amazon Hub</a>
            </li>
            <li class="nav_last nav_a_carat">
              <span class="nav_a_carat">›</span><a href="/b/?node=18190131011&amp;ld=AZUSSOA-seemore&amp;ref_=footer_seemore" class="nav_a">See More Ways to Make Money</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Amazon Payment Products</div>
        <ul>
            <li class="nav_first">
              <a href="/iss/credit/rewardscardmember?plattr=CBFOOT&amp;ref_=footer_cbcc" class="nav_a">Amazon Rewards Visa Signature Cards</a>
            </li>
            <li>
              <a href="/credit/storecard/member?plattr=PLCCFOOT&amp;ref_=footer_plcc" class="nav_a">Amazon.com Store Card</a>
            </li>
            <li>
              <a href="/gp/product/B084KP3NG6?plattr=SCFOOT&amp;ref_=footer_ACB" class="nav_a">Amazon Secured Card</a>
            </li>
            <li>
              <a href="/dp/B07984JN3L?plattr=ACOMFO&amp;ie=UTF-8" class="nav_a">Amazon Business Card</a>
            </li>
            <li>
              <a href="/dp/B07CBJQS16?pr=ibprox&amp;plattr=CCLFOOT&amp;place=camp&amp;ie=UTF-8&amp;ref_=footer_ccl" class="nav_a">Amazon Business Line of Credit</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=16218619011&amp;ref_=footer_swp" class="nav_a">Shop with Points</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=3561432011&amp;ref_=footer_ccmp" class="nav_a">Credit Card Marketplace</a>
            </li>
            <li>
              <a href="/gp/browse.html?node=10232440011&amp;ref_=footer_reload_us" class="nav_a">Reload Your Balance</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/browse.html?node=388305011&amp;ref_=footer_tfx" class="nav_a">Amazon Currency Converter</a>
            </li>
        </ul>
      </div>
        <div class="navFooterColSpacerInner navAccessibility"></div>
        <div class="navFooterLinkCol navAccessibility">
          <div class="navFooterColHead">Let Us Help You</div>
        <ul>
            <li class="nav_first">
              <a href="/gp/help/customer/display.html?nodeId=GDFU3JS5AL6SYHRD&amp;ref_=footer_covid" class="nav_a">Amazon and COVID-19</a>
            </li>
            <li>
              <a href="https://www.amazon.com/gp/css/homepage.html?ref_=footer_ya" class="nav_a">Your Account</a>
            </li>
            <li>
              <a href="https://www.amazon.com/gp/css/order-history?ref_=footer_yo" class="nav_a">Your Orders</a>
            </li>
            <li>
              <a href="/gp/help/customer/display.html?nodeId=468520&amp;ref_=footer_shiprates" class="nav_a">Shipping Rates &amp; Policies</a>
            </li>
            <li>
              <a href="/gp/prime?ref_=footer_prime" class="nav_a">Amazon Prime</a>
            </li>
            <li>
              <a href="/gp/css/returns/homepage.html?ref_=footer_hy_f_4" class="nav_a">Returns &amp; Replacements</a>
            </li>
            <li>
              <a href="/hz/mycd/myx?ref_=footer_myk" class="nav_a">Manage Your Content and Devices</a>
            </li>
            <li>
              <a href="/gp/BIT/ref=footer_bit_v2_us_A0029?bitCampaignCode=A0029" class="nav_a">Amazon Assistant</a>
            </li>
            <li class="nav_last ">
              <a href="/gp/help/customer/display.html?nodeId=508510&amp;ref_=footer_gw_m_b_he" class="nav_a">Help</a>
            </li>
        </ul>
      </div>
  </div>
</div>
<div class="nav-footer-line"></div>

  <div class="navFooterLine navFooterLinkLine navFooterPadItemLine">
    <span>
      <div class="navFooterLine navFooterLogoLine">
        <a href="/?ref_=footer_logo">
        <div class="nav-logo-base nav-sprite"></div>
        </a>
      </div>
</span>
    
      <span class="icp-container-desktop"><div class="navFooterLine">
<style type="text/css">
  #icp-touch-link-language { display: none; }
</style>


<a href="/gp/customer-preferences/select-language/ref=footer_lang?ie=UTF8&amp;preferencesReturnUrl=%2Fb%3Fnode%3D283155%26ref_%3Dnav_ya_signin%26" class="icp-button" id="icp-touch-link-language">
  <div class="icp-nav-globe-img-2 icp-button-globe-2"></div><span class="icp-color-base">English</span><span class="nav-arrow icp-up-down-arrow"></span><span class="aok-hidden" style="display:none">Choose a language for shopping.</span>
</a>



<style type="text/css">
#icp-touch-link-country { display: none; }
</style>
<a href="/customer-preferences/country?ie=UTF8&amp;preferencesReturnUrl=%2Fb%3Fnode%3D283155%26ref_%3Dnav_ya_signin%26&amp;ref_=footer_icp_cp" class="icp-button" id="icp-touch-link-country">
  <span class="icp-flag-3 icp-flag-3-us"></span><span class="icp-color-base">United States</span><span class="aok-hidden" style="display:none">Choose a country/region for shopping.</span>
</a>
</div></span>
    
  </div>
  
  
  <div class="navFooterLine navFooterLinkLine navFooterDescLine" role="navigation" aria-lable="More on Amazon.com">
    <table class="navFooterMoreOnAmazon" cellspacing="0">
      <tbody><tr>
<td class="navFooterDescItem"><a href="https://music.amazon.com?ref=dm_aff_amz_com" class="nav_a">Amazon Music<br><span class="navFooterDescText">Stream millions<br>of songs</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://advertising.amazon.com/?ref=footer_advtsing_amzn_com" class="nav_a">Amazon Advertising<br><span class="navFooterDescText">Find, attract, and<br>engage customers</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=15547130011&amp;ref_=_us_footer_drive" class="nav_a">Amazon Drive<br><span class="navFooterDescText">Cloud storage<br>from Amazon</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.6pm.com" class="nav_a">6pm<br><span class="navFooterDescText">Score deals<br>on fashion brands</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.abebooks.com" class="nav_a">AbeBooks<br><span class="navFooterDescText">Books, art<br>&amp; collectibles</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.acx.com/" class="nav_a">ACX <br><span class="navFooterDescText">Audiobook Publishing<br>Made Easy</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.alexa.com" class="nav_a">Alexa<br><span class="navFooterDescText">Actionable Analytics<br>for the Web</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://sell.amazon.com/?ld=AZUSSOA-footer-aff&amp;ref_=footer_sell" class="nav_a">Sell on Amazon<br><span class="navFooterDescText">Start a Selling Account</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/business?ref_=footer_retail_b2b" class="nav_a">Amazon Business<br><span class="navFooterDescText">Everything For<br>Your Business</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/alm/storefront?almBrandId=QW1hem9uIEZyZXNo&amp;ref_=footer_aff_fresh" class="nav_a">Amazon Fresh<br><span class="navFooterDescText">Groceries &amp; More<br>Right To Your Door</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=230659011&amp;ref_=footer_amazonglobal" class="nav_a">AmazonGlobal<br><span class="navFooterDescText">Ship Orders<br>Internationally</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/services?ref_=footer_services" class="nav_a">Home Services<br><span class="navFooterDescText">Experienced Pros<br>Happiness Guarantee</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://ignite.amazon.com/?ref=amazon_footer_ignite" class="nav_a">Amazon Ignite<br><span class="navFooterDescText">Sell your original<br>Digital Educational<br>Resources</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&amp;sc_campaign=amazonfooter" class="nav_a">Amazon Web Services<br><span class="navFooterDescText">Scalable Cloud<br>Computing Services</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://www.audible.com" class="nav_a">Audible<br><span class="navFooterDescText">Listen to Books &amp; Original<br>Audio Performances</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.bookdepository.com" class="nav_a">Book Depository<br><span class="navFooterDescText">Books With Free<br>Delivery Worldwide</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.boxofficemojo.com/?ref_=amzn_nav_ftr" class="nav_a">Box Office Mojo<br><span class="navFooterDescText">Find Movie<br>Box Office Data</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.comixology.com" class="nav_a">ComiXology<br><span class="navFooterDescText">Thousands of<br>Digital Comics</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.dpreview.com" class="nav_a">DPReview<br><span class="navFooterDescText">Digital<br>Photography</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.fabric.com" class="nav_a">Fabric<br><span class="navFooterDescText">Sewing, Quilting<br>&amp; Knitting</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.goodreads.com" class="nav_a">Goodreads<br><span class="navFooterDescText">Book reviews<br>&amp; recommendations</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://www.imdb.com" class="nav_a">IMDb<br><span class="navFooterDescText">Movies, TV<br>&amp; Celebrities</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://pro.imdb.com?ref_=amzn_nav_ftr" class="nav_a">IMDbPro<br><span class="navFooterDescText">Get Info Entertainment<br>Professionals Need</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://kdp.amazon.com" class="nav_a">Kindle Direct Publishing<br><span class="navFooterDescText">Indie Digital &amp; Print Publishing<br>Made Easy
</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=13234696011&amp;ref_=_gno_p_foot" class="nav_a">Amazon Photos<br><span class="navFooterDescText">Unlimited Photo Storage<br>Free With Prime</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://videodirect.amazon.com/home/landing" class="nav_a">Prime Video Direct<br><span class="navFooterDescText">Video Distribution<br>Made Easy</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.shopbop.com/welcome" class="nav_a">Shopbop<br><span class="navFooterDescText">Designer<br>Fashion Brands</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=10158976011&amp;ref_=footer_wrhsdls" class="nav_a">Amazon Warehouse<br><span class="navFooterDescText">Great Deals on<br>Quality Used Products </span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem"><a href="https://www.wholefoodsmarket.com" class="nav_a">Whole Foods Market<br><span class="navFooterDescText">America’s Healthiest<br>Grocery Store</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.woot.com/" class="nav_a">Woot!<br><span class="navFooterDescText">Deals and <br>Shenanigans</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.zappos.com" class="nav_a">Zappos<br><span class="navFooterDescText">Shoes &amp;<br>Clothing</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://ring.com" class="nav_a">Ring<br><span class="navFooterDescText">Smart Home<br>Security Systems
</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://eero.com/" class="nav_a">eero WiFi<br><span class="navFooterDescText">Stream 4K Video<br>in Every Room</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://blinkforhome.com/?ref=nav_footer" class="nav_a">Blink<br><span class="navFooterDescText">Smart Security<br>for Every Home
</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://shop.ring.com/pages/neighbors-app" class="nav_a">Neighbors App <br><span class="navFooterDescText"> Real-Time Crime<br>&amp; Safety Alerts
</span></a></td></tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=14498690011&amp;ref_=amzn_nav_ftr_swa" class="nav_a">Amazon Subscription Boxes<br><span class="navFooterDescText">Top subscription boxes – right to your door</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="https://www.pillpack.com" class="nav_a">PillPack<br><span class="navFooterDescText">Pharmacy Simplified</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/gp/browse.html?node=12653393011&amp;ref_=footer_usrenew" class="nav_a">Amazon Renewed<br><span class="navFooterDescText">Like-new products<br>you can trust</span></a></td><td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescItem">&nbsp;</td>
</tr>

    </tbody></table>
  </div>

  
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine navFooterCopyright">
  <ul><li class="nav_first"><a href="/gp/help/customer/display.html?nodeId=508088&amp;ref_=footer_cou" class="nav_a">Conditions of Use</a></li><li><a href="/gp/help/customer/display.html?nodeId=468496&amp;ref_=footer_privacy" class="nav_a">Privacy Notice</a></li><li class="nav_last"><a href="/interestbasedads/ref=footer_iba" class="nav_a">Interest-Based Ads</a></li></ul><span>© 1996-2022, Amazon.com, Inc. or its affiliates</span>
</div>

  
</div>

<div id="sis_pixel_r2" aria-hidden="true" style="height:1px; position: absolute; left: -1000000px; top: -1000000px;"><iframe id="DAsis" src="//s.amazon-adsystem.com/iu3?d=amazon.com&amp;slot=navFooter&amp;a1=0101e95961bce7abe73582a93cf25b084396fbd4b022f280e94b0b2257a00a436055&amp;a2=0101f14d5e4847c1de8c282778b91389f8bc8abd8caa62f568bc0a16917b33400898&amp;old_oo=0&amp;ts=1646693601373&amp;s=AY3UcX53SPNurRyJVW9Jiq5THfupOWGvsShxXtSA6IoL&amp;gdpr_consent=&amp;gdpr_consent_avl=&amp;cb=1646693601373" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" sandbox=""></iframe></div><script>(function(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.addEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=document.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="//s.amazon-adsystem.com/iu3?d=amazon.com&slot=navFooter&a1=0101e95961bce7abe73582a93cf25b084396fbd4b022f280e94b0b2257a00a436055&a2=0101f14d5e4847c1de8c282778b91389f8bc8abd8caa62f568bc0a16917b33400898&old_oo=0&ts=1646693601373&s=AY3UcX53SPNurRyJVW9Jiq5THfupOWGvsShxXtSA6IoL&gdpr_consent=&gdpr_consent_avl=&cb=1646693601373" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" sandbox></iframe>')},300)});</script>

  <!-- NAVYAAN FOOTER END -->

<!-- sp:end-feature:nav-footer -->
<!-- sp:feature:associate-tracker-pixel -->
<img src="https://assoc-na.associates-amazon.com/abid/um?c=A124BGP0M70XCG&amp;s=130-0450696-1458362&amp;m=ATVPDKIKX0DER" style="display:none" alt=""><!-- sp:end-feature:associate-tracker-pixel -->
<!-- sp:feature:configured-sitewide-assets -->
<!-- sp:end-feature:configured-sitewide-assets -->
<!-- sp:feature:customer-behavior-js -->
<script type="text/javascript">if (window.ue && ue.tag) { ue.tag('FWCIMEnabled'); }</script>
<script type="text/javascript">window.fwcimData = { customerId: 'A124BGP0M70XCG' };</script>
<script>
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('afterLoad').execute(function() {
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('https://images-na.ssl-images-amazon.com/images/I/71iqUL2aEuL.js?AUIClients/FWCIMAssets');
});
</script>
<!-- sp:end-feature:customer-behavior-js -->
<div id="be" style="display:none;visibility:hidden;"><form name="ue_backdetect" action="get"><input type="hidden" name="ue_back" value="2"></form>


<script type="text/javascript">
window.ue_ibe = (window.ue_ibe || 0) + 1;
if (window.ue_ibe === 1) {
(function(e,c){function h(b,a){f.push([b,a])}function g(b,a){if(b){var c=e.head||e.getElementsByTagName("head")[0]||e.documentElement,d=e.createElement("script");d.async="async";d.src=b;d.setAttribute("crossorigin","anonymous");a&&a.onerror&&(d.onerror=a.onerror);a&&a.onload&&(d.onload=a.onload);c.insertBefore(d,c.firstChild)}}function k(){ue.uels=g;for(var b=0;b<f.length;b++){var a=f[b];g(a[0],a[1])}ue.deffered=1}var f=[];c.ue&&(ue.uels=h,c.ue.attach&&c.ue.attach("load",k))})(document,window);


if (window.ue && window.ue.uels) {
        var cel_widgets = [ { "c":"celwidget" },{ "s":"#nav-swmslot > div", "id_gen":function(elem, index){ return 'nav_sitewide_msg'; } },{ "s":".acswidget.acswidget-content-grid.bxw-content-grid > .bxc-grid__container", "id_gen":function(elem, index){ return 'osa_browse_banner_' + index; } },{ "s":".GB-M-COMMON.GB-SUPPLE", "id_gen":function(elem, index){ return 'osa_browse_supple_' + index; } },{ "s":".GB-M-COMMON.GB-SHOVELER", "id_gen":function(elem, index){ return 'osa_browse_shoveler_' + index; } },{ "s":".a-section.coupon-shoveler", "id_gen":function(elem, index){ return 'osa_browse_coupon_' + index; } },{ "s":"#live-flagship-root", "id_gen":function(elem, index){ return 'osa_browse_amazon_live' + index; } },{ "s":".footerStripe", "id_gen":function(elem, index){ return 'osa_browse_footer_stripe_' + index; } },{ "s":".acswidget.acswidget-carousel.acswidget-carousel--shoveler.acswidget-carousel--softlines", "id_gen":function(elem, index){ return 'osa_browse_carousel_' + index; } },{ "s":"video", "id_gen":function(elem, index){ return 'osa_browse_video_' + index; } } ];

                ue.uels("https://images-na.ssl-images-amazon.com/images/I/31YXrY93hfL.js");
}
var ue_mbl=ue_csm.ue.exec(function(g,a){function p(c){b=c||{};a.AMZNPerformance=b;b.transition=b.transition||{};b.timing=b.timing||{};if(a.csa){var e;b.timing.transitionStart&&(e=b.timing.transitionStart);b.timing.processStart&&(e=b.timing.processStart);e&&(csa("PageTiming")("mark","nativeTransitionStart",e),csa("PageTiming")("mark","transitionStart",e))}g.ue.exec(q,"csm-android-check")()&&b.tags instanceof Array&&(c=-1!=b.tags.indexOf("usesAppStartTime")||b.transition.type?!b.transition.type&&-1<
b.tags.indexOf("usesAppStartTime")?"warm-start":void 0:"view-transition",c&&(b.transition.type=c));if("reload"===d._nt&&g.ue_orct||"intrapage-transition"===d._nt)a:{if(k&&(c=d.ssw(l),e=b.timing.transitionStart,c&&!c.e&&e&&c.val&&e!==+c.val))break a;f&&f.timing&&f.timing.navigationStart?b.timing.transitionStart=f.timing.navigationStart:delete b.timing.transitionStart}else"undefined"===typeof d._nt&&f&&f.timing&&f.timing.navigationStart&&a.history&&"function"===typeof a.History&&"object"===typeof a.history&&
a.history.length&&1!=a.history.length&&(b.timing.transitionStart=f.timing.navigationStart);k&&d.ssw(l,""+(b.timing.transitionStart||""));c=b.transition;e=d._nt?d._nt:void 0;c.subType=e;a.ue&&a.ue.tag&&a.ue.tag("has-AMZNPerformance");d.isl&&a.uex&&a.uex("at","csm-timing");r()}function s(b){a.ue&&a.ue.count&&a.ue.count("csm-cordova-plugin-failed",1)}function q(){return a.cordova&&a.cordova.platformId&&"android"==a.cordova.platformId}function r(){try{a.P.register("AMZNPerformance",function(){return b})}catch(c){}}
function m(){if(!b)return"";ue_mbl.cnt=null;for(var c=b.timing,a=b.transition,c=["mts",n(c.transitionStart),"mps",n(c.processStart),"mtt",a.type,"mtst",a.subType,"mtlt",a.launchType],a="",d=0;d<c.length;d+=2){var f=c[d],g=c[d+1];"undefined"!==typeof g&&(a+="&"+f+"="+g)}return a}function n(a){if("undefined"!==typeof a&&"undefined"!==typeof h)return a-h}function t(a,d){b&&(h=d,b.timing.transitionStart=a,b.transition.type="view-transition",b.transition.subType="ajax-transition",b.transition.launchType=
"normal",ue_mbl.cnt=m)}var d=g.ue||{},h=g.ue_t0,l="csm-last-mts",k=1===g.ue_sswmts,f=a.performance,b;if(a.P&&a.P.when&&a.P.register)return 1===a.ue_fnt&&(h=a.aPageStart||g.ue_t0),a.P.when("CSMPlugin").execute(function(a){a.buildAMZNPerformance&&a.buildAMZNPerformance({successCallback:p,failCallback:s})}),{cnt:m,ajax:t}},"mobile-timing")(ue_csm,ue_csm.window);

(function(d){d._uess=function(){var a="";screen&&screen.width&&screen.height&&(a+="&sw="+screen.width+"&sh="+screen.height);var b=function(a){var b=document.documentElement["client"+a];return"CSS1Compat"===document.compatMode&&b||document.body["client"+a]||b},c=b("Width"),b=b("Height");c&&b&&(a+="&vw="+c+"&vh="+b);return a}})(ue_csm);

(function(a){var b=document.ue_backdetect;b&&b.ue_back&&a.ue&&(a.ue.bfini=b.ue_back.value);a.uet&&a.uet("be");a.onLdEnd&&(window.addEventListener?window.addEventListener("load",a.onLdEnd,!1):window.attachEvent&&window.attachEvent("onload",a.onLdEnd));a.ueh&&a.ueh(0,window,"load",a.onLd,1);a.ue&&a.ue.tag&&(a.ue_furl?(b=a.ue_furl.replace(/\./g,"-"),a.ue.tag(b)):a.ue.tag("nofls"))})(ue_csm);

(function(g,h){function d(a,d){var b={};if(!e||!f)try{var c=h.sessionStorage;c?a&&("undefined"!==typeof d?c.setItem(a,d):b.val=c.getItem(a)):f=1}catch(g){e=1}e&&(b.e=1);return b}var b=g.ue||{},a="",f,e,c,a=d("csmtid");f?a="NA":a.e?a="ET":(a=a.val,a||(a=b.oid||"NI",d("csmtid",a)),c=d(b.oid),c.e||(c.val=c.val||0,d(b.oid,c.val+1)),b.ssw=d);b.tabid=a})(ue_csm,ue_csm.window);

ue_csm.ue.exec(function(e,f){var a=e.ue||{},b=a._wlo,d;if(a.ssw){d=a.ssw("CSM_previousURL").val;var c=f.location,b=b?b:c&&c.href?c.href.split("#")[0]:void 0;c=(b||"")===a.ssw("CSM_previousURL").val;!c&&b&&a.ssw("CSM_previousURL",b);d=c?"reload":d?"intrapage-transition":"first-view"}else d="unknown";a._nt=d},"NavTypeModule")(ue_csm,window);
ue_csm.ue.exec(function(c,a){function g(a){a.run(function(e){d.tag("csm-feature-"+a.name+":"+e);d.isl&&c.uex("at")})}if(a.addEventListener)for(var d=c.ue||{},f=[{name:"touch-enabled",run:function(b){var e=function(){a.removeEventListener("touchstart",c,!0);a.removeEventListener("mousemove",d,!0)},c=function(){b("true");e()},d=function(){b("false");e()};a.addEventListener("touchstart",c,!0);a.addEventListener("mousemove",d,!0)}}],b=0;b<f.length;b++)g(f[b])},"csm-features")(ue_csm,window);


(function(b,c){var a=c.images;a&&a.length&&b.ue.count("totalImages",a.length)})(ue_csm,document);
(function(b){function c(){var d=[];a.log&&a.log.isStub&&a.log.replay(function(a){e(d,a)});a.clog&&a.clog.isStub&&a.clog.replay(function(a){e(d,a)});d.length&&(a._flhs+=1,n(d),p(d))}function g(){a.log&&a.log.isStub&&(a.onflush&&a.onflush.replay&&a.onflush.replay(function(a){a[0]()}),a.onunload&&a.onunload.replay&&a.onunload.replay(function(a){a[0]()}),c())}function e(d,b){var c=b[1],f=b[0],e={};a._lpn[c]=(a._lpn[c]||0)+1;e[c]=f;d.push(e)}function n(b){q&&(a._lpn.csm=(a._lpn.csm||0)+1,b.push({csm:{k:"chk",
f:a._flhs,l:a._lpn,s:"inln"}}))}function p(a){if(h)a=k(a),b.navigator.sendBeacon(l,a);else{a=k(a);var c=new b[f];c.open("POST",l,!0);c.setRequestHeader&&c.setRequestHeader("Content-type","text/plain");c.send(a)}}function k(a){return JSON.stringify({rid:b.ue_id,sid:b.ue_sid,mid:b.ue_mid,mkt:b.ue_mkt,sn:b.ue_sn,reqs:a})}var f="XMLHttpRequest",q=1===b.ue_ddq,a=b.ue,r=b[f]&&"withCredentials"in new b[f],h=b.navigator&&b.navigator.sendBeacon,l="//"+b.ue_furl+"/1/batch/1/OE/",m=b.ue_fci_ft||5E3;a&&(r||h)&&
(a._flhs=a._flhs||0,a._lpn=a._lpn||{},a.attach&&(a.attach("beforeunload",a.exec(g,"fcli-bfu")),a.attach("pagehide",a.exec(g,"fcli-ph"))),m&&b.setTimeout(a.exec(c,"fcli-t"),m),a._ffci=a.exec(c))})(window);


(function(k,c){function l(a,b){return a.filter(function(a){return a.initiatorType==b})}function f(a,c){if(b.t[a]){var g=b.t[a]-b._t0,e=c.filter(function(a){return 0!==a.responseEnd&&m(a)<g}),f=l(e,"script"),h=l(e,"link"),k=l(e,"img"),n=e.map(function(a){return a.name.split("/")[2]}).filter(function(a,b,c){return a&&c.lastIndexOf(a)==b}),q=e.filter(function(a){return a.duration<p}),s=g-Math.max.apply(null,e.map(m))<r|0;"af"==a&&(b._afjs=f.length);return a+":"+[e[d],f[d],h[d],k[d],n[d],q[d],s].join("-")}}
function m(a){return a.responseEnd-(b._t0-c.timing.navigationStart)}function n(){var a=c[h]("resource"),d=f("cf",a),g=f("af",a),a=f("ld",a);delete b._rt;b._ld=b.t.ld-b._t0;b._art&&b._art();return[d,g,a].join("_")}var p=20,r=50,d="length",b=k.ue,h="getEntriesByType";b._rre=m;b._rt=c&&c.timing&&c[h]&&n})(ue_csm,window.performance);


(function(c,d){var b=c.ue,a=d.navigator;b&&b.tag&&a&&(a=a.connection||a.mozConnection||a.webkitConnection)&&a.type&&b.tag("netInfo:"+a.type)})(ue_csm,window);


(function(c,d){function h(a,b){for(var c=[],d=0;d<a.length;d++){var e=a[d],f=b.encode(e);if(e[k]){var g=b.metaSep,e=e[k],l=b.metaPairSep,h=[],m=void 0;for(m in e)e.hasOwnProperty(m)&&h.push(m+"="+e[m]);e=h.join(l);f+=g+e}c.push(f)}return c.join(b.resourceSep)}function s(a){var b=a[k]=a[k]||{};b[t]||(b[t]=c.ue_mid);b[u]||(b[u]=c.ue_sid);b[f]||(b[f]=c.ue_id);b.csm=1;a="//"+c.ue_furl+"/1/"+a[v]+"/1/OP/"+a[w]+"/"+a[x]+"/"+h([a],y);if(n)try{n.call(d[p],a)}catch(g){c.ue.sbf=1,(new Image).src=a}else(new Image).src=
a}function q(){g&&g.isStub&&g.replay(function(a,b,c){a=a[0];b=a[k]=a[k]||{};b[f]=b[f]||c;s(a)});l.impression=s;g=null}if(!(1<c.ueinit)){var k="metadata",x="impressionType",v="foresterChannel",w="programGroup",t="marketplaceId",u="session",f="requestId",p="navigator",l=c.ue||{},n=d[p]&&d[p].sendBeacon,r=function(a,b,c,d){return{encode:d,resourceSep:a,metaSep:b,metaPairSep:c}},y=r("","?","&",function(a){return h(a.impressionData,z)}),z=r("/",":",",",function(a){return a.featureName+":"+h(a.resources,
A)}),A=r(",","@","|",function(a){return a.id}),g=l.impression;n?q():(l.attach("load",q),l.attach("beforeunload",q));try{d.P&&d.P.register&&d.P.register("impression-client",function(){})}catch(B){c.ueLogError(B,{logLevel:"WARN"})}}})(ue_csm,window);



var ue_pty = "Landing";

var ue_spty = "BrowsePage";

var ue_pti = "283155";


var ue_adb = 4;
var ue_adb_rtla = 1;
ue_csm.ue.exec(function(y,a){function t(){if(d&&f){var a;a:{try{a=d.getItem(g);break a}catch(c){}a=void 0}if(a)return b=a,!0}return!1}function u(){if(a.fetch)fetch(m).then(function(a){if(!a.ok)throw Error(a.statusText);return a.text?a.text():null}).then(function(b){b?(-1<b.indexOf("window.ue_adb_chk = 1")&&(a.ue_adb_chk=1),n()):h()})["catch"](h);else e.uels(m,{onerror:h,onload:n})}function h(){b=k;l();if(f)try{d.setItem(g,b)}catch(a){}}function n(){b=1===a.ue_adb_chk?p:k;l();if(f)try{d.setItem(g,
b)}catch(c){}}function q(){a.ue_adb_rtla&&c&&0<c.ec&&!1===r&&(c.elh=null,ueLogError({m:"Hit Info",fromOnError:1},{logLevel:"INFO",adb:b}),r=!0)}function l(){e.tag(b);e.isl&&a.uex&&uex("at",b);s&&s.updateCsmHit("adb",b);c&&0<c.ec?q():a.ue_adb_rtla&&c&&(c.elh=q)}function v(){return b}if(a.ue_adb){a.ue_fadb=a.ue_fadb||10;var e=a.ue,k="adblk_yes",p="adblk_no",m="https://m.media-amazon.com/images/G/01/csm/showads.v2.js?adtag=csm&ad_box_",b="adblk_unk",d;a:{try{d=a.localStorage;break a}catch(z){}d=void 0}var g=
"csm:adb",c=a.ue_err,s=e.cookie,f=void 0!==a.localStorage,w=Math.random()>1-1/a.ue_fadb,r=!1,x=t();w||!x?u():l();a.ue_isAdb=v;a.ue_isAdb.unk="adblk_unk";a.ue_isAdb.no=p;a.ue_isAdb.yes=k}},"adb")(document,window);




(function(c,l,m){function h(a){if(a)try{if(a.id)return"//*[@id='"+a.id+"']";var b,d=1,e;for(e=a.previousSibling;e;e=e.previousSibling)e.nodeName===a.nodeName&&(d+=1);b=d;var c=a.nodeName;1!==b&&(c+="["+b+"]");a.parentNode&&(c=h(a.parentNode)+"/"+c);return c}catch(f){return"DETACHED"}}function f(a){if(a&&a.getAttribute)return a.getAttribute(k)?a.getAttribute(k):f(a.parentElement)}var k="data-cel-widget",g=!1,d=[];(c.ue||{}).isBF=function(){try{var a=JSON.parse(localStorage["csm-bf"]||"[]"),b=0<=a.indexOf(c.ue_id);
a.unshift(c.ue_id);a=a.slice(0,20);localStorage["csm-bf"]=JSON.stringify(a);return b}catch(d){return!1}}();c.ue_utils={getXPath:h,getFirstAscendingWidget:function(a,b){c.ue_cel&&c.ue_fem?!0===g?b(f(a)):d.push({element:a,callback:b}):b()},notifyWidgetsLabeled:function(){if(!1===g){g=!0;for(var a=f,b=0;b<d.length;b++)if(d[b].hasOwnProperty("callback")&&d[b].hasOwnProperty("element")){var c=d[b].callback,e=d[b].element;"function"===typeof c&&"function"===typeof a&&c(a(e))}d=null}},extractStringValue:function(a){if("string"===
typeof a)return a}}})(ue_csm,window,document);


(function(a){a.ue_cel||(a.ue_cel=function(){function f(a,c){c?c.r=v:c={r:v,c:1};!ue_csm.ue_sclog&&c.clog&&d.clog?d.clog(a,c.ns||q,c):c.glog&&d.glog?d.glog(a,c.ns||q,c):d.log(a,c.ns||q,c)}function m(a,d){"function"===typeof g&&g("log",{schemaId:s+".RdCSI.1",eventType:a,clientData:d},{ent:{page:["requestId"]}})}function c(){var a=n.length;if(0<a){for(var c=[],b=0;b<a;b++){var F=n[b].api;F.ready()?(F.on({ts:d.d,ns:q}),e.push(n[b]),f({k:"mso",n:n[b].name,t:d.d()})):c.push(n[b])}n=c}}function h(){if(!h.executed){for(var a=
0;a<e.length;a++)e[a].api.off&&e[a].api.off({ts:d.d,ns:q});A();f({k:"eod",t0:d.t0,t:d.d()},{c:1,il:1});h.executed=1;for(a=0;a<e.length;a++)n.push(e[a]);e=[];b(t);b(x)}}function A(a){f({k:"hrt",t:d.d()},{c:1,il:1,n:a});l=Math.min(w,r*l);y()}function y(){b(x);x=k(function(){A(!0)},l)}function u(){h.executed||A()}var p=a.window,k=p.setTimeout,b=p.clearTimeout,r=1.5,w=p.ue_cel_max_hrt||3E4,s="robotdetection",n=[],e=[],q=a.ue_cel_ns||"cel",t,x,d=a.ue,E=a.uet,B=a.uex,v=d.rid,C=p.csa,g,l=p.ue_cel_hrt_int||
3E3,z=p.requestAnimationFrame||function(a){a()};!a.ue_cel_lclia&&C&&(g=C("Events",{producerId:s}));if(d.isBF)f({k:"bft",t:d.d()});else{"function"==typeof E&&E("bb","csmCELLSframework",{wb:1});k(c,0);d.onunload(h);if(d.onflush)d.onflush(u);t=k(h,6E5);y();"function"==typeof B&&B("ld","csmCELLSframework",{wb:1});return{registerModule:function(a,b){n.push({name:a,api:b});f({k:"mrg",n:a,t:d.d()});c()},reset:function(a){f({k:"rst",t0:d.t0,t:d.d()});n=n.concat(e);e=[];for(var r=n.length,g=0;g<r;g++)n[g].api.off(),
n[g].api.reset();v=a||d.rid;c();b(t);t=k(h,6E5);h.executed=0},timeout:function(a,d){return k(function(){z(function(){h.executed||a()})},d)},log:f,csaEventLog:m,off:h}}}())})(ue_csm);
(function(a){a.ue_pdm||!a.ue_cel||a.ue.isBF||(a.ue_pdm=function(){function f(){try{var d=b.screen;if(d){var c={w:d.width,aw:d.availWidth,h:d.height,ah:d.availHeight,cd:d.colorDepth,pd:d.pixelDepth};e&&e.w===c.w&&e.h===c.h&&e.aw===c.aw&&e.ah===c.ah&&e.pd===c.pd&&e.cd===c.cd||(e=c,e.t=s(),e.k="sci",E(e),!C&&g&&l("sci",{h:(e.h||"0")+""}))}var k=r.body||{},h=r.documentElement||{},m={w:Math.max(k.scrollWidth||0,k.offsetWidth||0,h.clientWidth||0,h.scrollWidth||0,h.offsetWidth||0),h:Math.max(k.scrollHeight||
0,k.offsetHeight||0,h.clientHeight||0,h.scrollHeight||0,h.offsetHeight||0)};q&&q.w===m.w&&q.h===m.h||(q=m,q.t=s(),q.k="doi",E(q));w=a.ue_cel.timeout(f,n);x+=1}catch(p){b.ueLogError&&ueLogError(p,{attribution:"csm-cel-page-module",logLevel:"WARN"})}}function m(){u("ebl","default",!1)}function c(){u("efo","default",!0)}function h(){u("ebl","app",!1)}function A(){u("efo","app",!0)}function y(){b.setTimeout(function(){r[H]?u("ebl","pageviz",!1):u("efo","pageviz",!0)},0)}function u(a,d,c){t!==c&&(E({k:a,
t:s(),s:d},{ff:!0===c?0:1}),!C&&g&&l(a,{t:(s()||"0")+"",s:d}));t=c}function p(){d.attach&&(z&&d.attach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.addEventListener&&(a.addEventListener("appPause",h),a.addEventListener("appResume",A))}),d.attach("blur",m,b),d.attach("focus",c,b))}function k(){d.detach&&(z&&d.detach(D,y,r),I&&P.when("mash").execute(function(a){a&&a.removeEventListener&&(a.removeEventListener("appPause",h),a.removeEventListener("appResume",A))}),d.detach("blur",m,b),d.detach("focus",
c,b))}var b=a.window,r=a.document,w,s,n,e,q,t=null,x=0,d=a.ue,E=a.ue_cel.log,B=a.uet,v=a.uex,C=a.ue_cel_lclia,g=b.csa,l=a.ue_cel.csaEventLog,z=!!d.pageViz,D=z&&d.pageViz.event,H=z&&d.pageViz.propHid,I=b.P&&b.P.when;"function"==typeof B&&B("bb","csmCELLSpdm",{wb:1});return{on:function(a){n=a.timespan||500;s=a.ts;p();a=b.location;E({k:"pmd",o:a.origin,p:a.pathname,t:s()});f();"function"==typeof v&&v("ld","csmCELLSpdm",{wb:1})},off:function(a){clearTimeout(w);k();d.count&&d.count("cel.PDM.TotalExecutions",
x)},ready:function(){return r.body&&a.ue_cel&&a.ue_cel.log},reset:function(){e=q=null}}}(),a.ue_cel&&a.ue_cel.registerModule("page module",a.ue_pdm))})(ue_csm);
(function(a){a.ue_vpm||!a.ue_cel||a.ue.isBF||(a.ue_vpm=function(){function f(){var a=y(),b={w:k.innerWidth,h:k.innerHeight,x:k.pageXOffset,y:k.pageYOffset};c&&c.w==b.w&&c.h==b.h&&c.x==b.x&&c.y==b.y||(b.t=a,b.k="vpi",c=b,r(c,{clog:1}),!q&&t&&x("vpi",{t:(c.t||"0")+"",h:(c.h||"0")+"",y:(c.y||"0")+"",w:(c.w||"0")+"",x:(c.x||"0")+""}));h=0;u=y()-a;p+=1}function m(){h||(h=a.ue_cel.timeout(f,A))}var c,h,A,y,u=0,p=0,k=a.window,b=a.ue,r=a.ue_cel.log,w=a.uet,s=a.uex,n=b.attach,e=b.detach,q=a.ue_cel_lclia,t=
k.csa,x=a.ue_cel.csaEventLog;"function"==typeof w&&w("bb","csmCELLSvpm",{wb:1});return{on:function(a){y=a.ts;A=a.timespan||100;f();n&&(n("scroll",m),n("resize",m));"function"==typeof s&&s("ld","csmCELLSvpm",{wb:1})},off:function(a){clearTimeout(h);e&&(e("scroll",m),e("resize",m));b.count&&(b.count("cel.VPI.TotalExecutions",p),b.count("cel.VPI.TotalExecutionTime",u),b.count("cel.VPI.AverageExecutionTime",u/p))},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){c=void 0},getVpi:function(){return c}}}(),
a.ue_cel&&a.ue_cel.registerModule("viewport module",a.ue_vpm))})(ue_csm);
(function(a){if(!a.ue_fem&&a.ue_cel&&a.ue_utils){var f=a.ue||{},m=a.window,c=m.document;!f.isBF&&!a.ue_fem&&c.querySelector&&m.getComputedStyle&&[].forEach&&(a.ue_fem=function(){function h(a,d){return a>d?3>a-d:3>d-a}function A(a,d){var c=m.pageXOffset,b=m.pageYOffset,k;a:{try{if(a){var g=a.getBoundingClientRect(),e,r=0===a.offsetWidth&&0===a.offsetHeight;c:{for(var f=a.parentNode,w=g.left||0,n=g.top||0,p=g.width||0,q=g.height||0;f&&f!==document.body;){var l;d:{try{var s=void 0;if(f)var G=f.getBoundingClientRect(),
s={x:G.left||0,y:G.top||0,w:G.width||0,h:G.height||0};else s=void 0;l=s;break d}catch(v){}l=void 0}var t=window.getComputedStyle(f),u="hidden"===t.overflow,y=u||"hidden"===t.overflowX,z=u||"hidden"===t.overflowY,J=n+q-1<l.y+1||n+1>l.y+l.h-1;if((w+p-1<l.x+1||w+1>l.x+l.w-1)&&y||J&&z){e=!0;break c}f=f.parentNode}e=!1}k={x:g.left+c||0,y:g.top+b||0,w:g.width||0,h:g.height||0,d:(r||e)|0}}else k=void 0;break a}catch(A){}k=void 0}if(k&&!a.cel_b)a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,
x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi",cl:a.className},{clog:1});else{if(c=k)c=a.cel_b,b=k,c=b.d===c.d&&1===b.d?!1:!(h(c.x,b.x)&&h(c.y,b.y)&&h(c.w,b.w)&&h(c.h,b.h)&&c.d===b.d);c&&(a.cel_b=k,C({n:a.getAttribute(x),w:a.cel_b.w,h:a.cel_b.h,d:a.cel_b.d,x:a.cel_b.x,y:a.cel_b.y,t:d,k:"ewi"},{clog:1}))}}function y(b,g){var h;h=b.c?c.getElementsByClassName(b.c):b.id?[c.getElementById(b.id)]:c.querySelectorAll(b.s);b.w=[];for(var f=0;f<h.length;f++){var e=h[f];if(e){if(!e.getAttribute(x)){var r=e.getAttribute("cel_widget_id")||
(b.id_gen||v)(e,f)||e.id;e.setAttribute(x,r)}b.w.push(e);k(Q,e,g)}}!1===B&&(E++,E===d.length&&(B=!0,a.ue_utils.notifyWidgetsLabeled()))}function u(a,c){g.contains(a)||C({n:a.getAttribute(x),t:c,k:"ewd"},{clog:1})}function p(a){K.length&&ue_cel.timeout(function(){if(q){for(var c=R(),d=!1;R()-c<e&&!d;){for(d=S;0<d--&&0<K.length;){var b=K.shift();T[b.type](b.elem,b.time)}d=0===K.length}U++;p(a)}},0)}function k(a,c,d){K.push({type:a,elem:c,time:d})}function b(a,c){for(var b=0;b<d.length;b++)for(var e=
d[b].w||[],g=0;g<e.length;g++)k(a,e[g],c)}function r(){M||(M=a.ue_cel.timeout(function(){M=null;var c=t();b(W,c);for(var g=0;g<d.length;g++)k(X,d[g],c);0===d.length&&!1===B&&(B=!0,a.ue_utils.notifyWidgetsLabeled());p(c)},n))}function w(){M||N||(N=a.ue_cel.timeout(function(){N=null;var a=t();b(Q,a);p(a)},n))}function s(){return z&&D&&g&&g.contains&&g.getBoundingClientRect&&t}var n=50,e=4.5,q=!1,t,x="data-cel-widget",d=[],E=0,B=!1,v=function(){},C=a.ue_cel.log,g,l,z,D,H=m.MutationObserver||m.WebKitMutationObserver||
m.MozMutationObserver,I=!!H,F,G,O="DOMAttrModified",L="DOMNodeInserted",J="DOMNodeRemoved",N,M,K=[],U=0,S=null,W="removedWidget",X="updateWidgets",Q="processWidget",T,V=m.performance||{},R=V.now&&function(){return V.now()}||function(){return Date.now()};"function"==typeof uet&&uet("bb","csmCELLSfem",{wb:1});return{on:function(b){function e(){if(s()){T={removedWidget:u,updateWidgets:y,processWidget:A};if(I){var a={attributes:!0,subtree:!0};F=new H(w);G=new H(r);F.observe(g,a);G.observe(g,{childList:!0,
subtree:!0});G.observe(l,a)}else z.call(g,O,w),z.call(g,L,r),z.call(g,J,r),z.call(l,L,w),z.call(l,J,w);r()}}g=c.body;l=c.head;z=g.addEventListener;D=g.removeEventListener;t=b.ts;d=a.cel_widgets||[];S=b.bs||5;f.deffered?e():f.attach&&f.attach("load",e);"function"==typeof uex&&uex("ld","csmCELLSfem",{wb:1});q=!0},off:function(){s()&&(G&&(G.disconnect(),G=null),F&&(F.disconnect(),F=null),D.call(g,O,w),D.call(g,L,r),D.call(g,J,r),D.call(l,L,w),D.call(l,J,w));f.count&&f.count("cel.widgets.batchesProcessed",
U);q=!1},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){d=a.cel_widgets||[]}}}(),a.ue_cel&&a.ue_fem&&a.ue_cel.registerModule("features module",a.ue_fem))}})(ue_csm);
(function(a){!a.ue_mcm&&a.ue_cel&&a.ue_utils&&!a.ue.isBF&&(a.ue_mcm=function(){function f(a,b){var h=a.srcElement||a.target||{},f={k:m,w:(b||{}).ow||(A.body||{}).scrollWidth,h:(b||{}).oh||(A.body||{}).scrollHeight,t:(b||{}).ots||c(),x:a.pageX,y:a.pageY,p:p.getXPath(h),n:h.nodeName};y&&"function"===typeof y.now&&a.timeStamp&&(f.dt=(b||{}).odt||y.now()-a.timeStamp,f.dt=parseFloat(f.dt.toFixed(2)));a.button&&(f.b=a.button);h.href&&(f.r=p.extractStringValue(h.href));h.id&&(f.i=h.id);h.className&&h.className.split&&
(f.c=h.className.split(/\s+/));u(f,{c:1})}var m="mcm",c,h=a.window,A=h.document,y=h.performance,u=a.ue_cel.log,p=a.ue_utils;return{on:function(k){c=k.ts;a.ue_cel_stub&&a.ue_cel_stub.replayModule(m,f);h.addEventListener&&h.addEventListener("mousedown",f,!0)},off:function(a){h.addEventListener&&h.removeEventListener("mousedown",f,!0)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){}}}(),a.ue_cel&&a.ue_cel.registerModule("mouse click module",a.ue_mcm))})(ue_csm);
(function(a){a.ue_mmm||!a.ue_cel||a.ue.isBF||(a.ue_mmm=function(f){function m(a,c){var b={x:a.pageX||a.x||0,y:a.pageY||a.y||0,t:p()};!c&&l&&(b.t-l.t<A||b.x==l.x&&b.y==l.y)||(l=b,v.push(b))}function c(){if(v.length){E=F.now();for(var a=0;a<v.length;a++){var c=v[a],b=a;z=v[g];D=c;var e=void 0;if(!(e=2>b)){e=void 0;a:if(v[b].t-v[b-1].t>h)e=0;else{for(e=g+1;e<b;e++){var f=z,k=D,l=v[e];H=(k.x-f.x)*(f.y-l.y)-(f.x-l.x)*(k.y-f.y);if(H*H/((k.x-f.x)*(k.x-f.x)+(k.y-f.y)*(k.y-f.y))>y){e=0;break a}}e=1}e=!e}(I=
e)?g=b-1:C.pop();C.push(c)}B=F.now()-E;q=Math.min(q,B);t=Math.max(t,B);x=(x*d+B)/(d+1);d+=1;n({k:u,e:C,min:Math.floor(1E3*q),max:Math.floor(1E3*t),avg:Math.floor(1E3*x)},{c:1});v=[];C=[];g=0}}var h=100,A=20,y=25,u="mmm1",p,k,b=a.window,r=b.document,w=b.setInterval,s=a.ue,n=a.ue_cel.log,e,q=1E3,t=0,x=0,d=0,E,B,v=[],C=[],g=0,l,z,D,H,I,F=f&&f.now&&f||Date.now&&Date||{now:function(){return(new Date).getTime()}};return{on:function(a){p=a.ts;k=a.ns;s.attach&&s.attach("mousemove",m,r);e=w(c,3E3)},off:function(a){k&&
(l&&m(l,!0),c());clearInterval(e);s.detach&&s.detach("mousemove",m,r)},ready:function(){return a.ue_cel&&a.ue_cel.log},reset:function(){v=[];C=[];g=0;l=null}}}(window.performance),a.ue_cel&&a.ue_cel.registerModule("mouse move module",a.ue_mmm))})(ue_csm);



ue_csm.ue.exec(function(b,c){var e=function(){},f=function(){return{send:function(b,d){if(d&&b){var a;if(c.XDomainRequest)a=new XDomainRequest,a.onerror=e,a.ontimeout=e,a.onprogress=e,a.onload=e,a.timeout=0;else if(c.XMLHttpRequest){if(a=new XMLHttpRequest,!("withCredentials"in a))throw"";}else a=void 0;if(!a)throw"";a.open("POST",b,!0);a.setRequestHeader&&a.setRequestHeader("Content-type","text/plain");a.send(d)}},isSupported:!0}}(),g=function(){return{send:function(c,d){if(c&&d)if(navigator.sendBeacon(c,
d))b.ue_sbuimp&&b.ue&&b.ue.ssw&&b.ue.ssw("eelsts","scs");else throw"";},isSupported:!!navigator.sendBeacon&&!(c.cordova&&c.cordova.platformId&&"ios"==c.cordova.platformId)}}();b.ue._ajx=f;b.ue._sBcn=g},"Transportation-clients")(ue_csm,window);
ue_csm.ue.exec(function(b,k){function A(){for(var a=0;a<arguments.length;a++){var c=arguments[a];try{var h;if(c.isSupported){var b=t.buildPayload(l,e);h=c.send(J,b)}else throw dummyException;return h}catch(d){}}B({m:"All supported clients failed",attribution:"CSMSushiClient_TRANSPORTATION_FAIL",f:"sushi-client.js",logLevel:"ERROR"},k.ue_err_chan||"jserr")}function m(){if(e.length){for(var a=0;a<n.length;a++)n[a]();A(d._sBcn||{},d._ajx||{});e=[];f={};l={};u=v=q=w=0}}function K(){var a=new Date,c=function(a){return 10>
a?"0"+a:a};return Date.prototype.toISOString?a.toISOString():a.getUTCFullYear()+"-"+c(a.getUTCMonth()+1)+"-"+c(a.getUTCDate())+"T"+c(a.getUTCHours())+":"+c(a.getUTCMinutes())+":"+c(a.getUTCSeconds())+"."+String((a.getUTCMilliseconds()/1E3).toFixed(3)).slice(2,5)+"Z"}function x(a){try{return JSON.stringify(a)}catch(c){}return null}function C(a,c,h,g){var p=!1;g=g||{};r++;r==D&&B({m:"Max number of Sushi Logs exceeded",f:"sushi-client.js",logLevel:"ERROR",attribution:"CSMSushiClient_MAX_CALLS"},k.ue_err_chan||
"jserr");var f;if(f=!(r>=D))(f=a&&-1<a.constructor.toString().indexOf("Object")&&c&&-1<c.constructor.toString().indexOf("String")&&h&&-1<h.constructor.toString().indexOf("String"))||L++;f&&(d.count&&d.count("Event:"+h,1),a.producerId=a.producerId||c,a.schemaId=a.schemaId||h,a.timestamp=K(),c=Date.now?Date.now():+new Date,h=Math.random().toString().substring(2,12),a.messageId=b.ue_id+"-"+c+"-"+h,g&&!g.ssd&&(a.sessionId=a.sessionId||b.ue_sid,a.requestId=a.requestId||b.ue_id,a.obfuscatedMarketplaceId=
a.obfuscatedMarketplaceId||b.ue_mid),(c=x(a))?(c=c.length,(e.length==M||q+c>N)&&m(),q+=c,a={data:t.compressEvent(a)},e.push(a),(g||{}).n?0===E?m():u||(u=k.setTimeout(m,E)):v||(v=k.setTimeout(m,O)),p=!0):p=!1);!p&&b.ue_int&&console.error("Invalid JS Nexus API call");return p}function F(){if(!G){for(var a=0;a<y.length;a++)y[a]();for(a=0;a<n.length;a++)n[a]();e.length&&(b.ue_sbuimp&&b.ue&&b.ue.ssw&&(a=x({dct:l,evt:e}),b.ue.ssw("eeldata",a),b.ue.ssw("eelsts","unk")),A(d._sBcn||{}));G=!0}}function H(a){y.push(a)}
function I(a){n.push(a)}var D=1E3,M=499,N=524288,s=function(){},d=b.ue||{},B=d.log||s,P=b.uex||s;(b.uet||s)("bb","ue_sushi_v1",{wb:1});var J=b.ue_surl||"https://unagi-na.amazon.com/1/events/com.amazon.csm.nexusclient.gamma",Q=["messageId","timestamp"],z="#",e=[],f={},l={},q=0,w=0,L=0,r=0,y=[],n=[],G=!1,u,v,E=void 0===b.ue_hpsi?1E3:b.ue_hpsi,O=void 0===b.ue_lpsi?1E4:b.ue_lpsi,t=function(){function a(a){f[a]=z+w++;l[f[a]]=a;return f[a]}function c(b){if(!(b instanceof Function)){if(b instanceof Array){for(var g=
[],d=b.length,e=0;e<d;e++)g[e]=c(b[e]);return g}if(b instanceof Object){g={};for(d in b)b.hasOwnProperty(d)&&(g[f[d]?f[d]:a(d)]=-1===Q.indexOf(d)?c(b[d]):b[d]);return g}return"string"===typeof b&&(b.length>(z+w).length||b.charAt(0)===z)?f[b]?f[b]:a(b):b}}return{compressEvent:c,buildPayload:function(){return x({cs:{dct:l},events:e})}}}();(function(){if(d.event&&d.event.isStub){if(b.ue_sbuimp&&b.ue&&b.ue.ssw){var a=b.ue.ssw("eelsts").val;if(a&&"unk"===a&&(a=b.ue.ssw("eeldata").val)){var c;a:{try{c=
JSON.parse(a);break a}catch(f){}c=null}c&&c.evt instanceof Array&&c.dct instanceof Object&&(e=c.evt,l=c.dct,e&&l&&(m(),b.ue.ssw("eeldata","{}"),b.ue.ssw("eelsts","scs")))}}d.event.replay(function(a){a[3]=a[3]||{};a[3].n=1;C.apply(this,a)});d.onSushiUnload.replay(function(a){H(a[0])});d.onSushiFlush.replay(function(a){I(a[0])})}})();d.attach("beforeunload",F);d.attach("pagehide",F);d._cmps=t;d.event=C;d.event.reset=function(){r=0};d.onSushiUnload=H;d.onSushiFlush=I;try{k.P&&k.P.register&&k.P.register("sushi-client",
s)}catch(R){b.ueLogError(R,{logLevel:"WARN"})}P("ld","ue_sushi_v1",{wb:1})},"Nxs-JS-Client")(ue_csm,window);


ue_csm.ue_unrt = 1500;
(function(d,b,t){function u(a,g){var c=a.srcElement||a.target||{},b={k:v,t:g.t,dt:g.dt,x:a.pageX,y:a.pageY,p:e.getXPath(c),n:c.nodeName};a.button&&(b.b=a.button);c.type&&(b.ty=c.type);c.href&&(b.r=e.extractStringValue(c.href));c.id&&(b.i=c.id);c.className&&c.className.split&&(b.c=c.className.split(/\s+/));h+=1;e.getFirstAscendingWidget(c,function(a){b.wd=a;d.ue.log(b,r)})}function w(a){if(!x(a.srcElement||a.target)){m+=1;n=!0;var g=f=d.ue.d(),c;p&&"function"===typeof p.now&&a.timeStamp&&(c=p.now()-
a.timeStamp,c=parseFloat(c.toFixed(2)));s=b.setTimeout(function(){u(a,{t:g,dt:c})},y)}}function z(a){if(a){var b=a.filter(A);a.length!==b.length&&(q=!0,k=d.ue.d(),n&&q&&(k&&f&&d.ue.log({k:B,t:f,m:Math.abs(k-f)},r),l(),q=!1,k=0))}}function A(a){if(!a)return!1;var b="characterData"===a.type?a.target.parentElement:a.target;if(!b||!b.hasAttributes||!b.attributes)return!1;var c={"class":"gw-clock gw-clock-aria s-item-container-height-auto feed-carousel using-mouse kfs-inner-container".split(" "),id:["dealClock",
"deal_expiry_timer","timer"],role:["timer"]},d=!1;Object.keys(c).forEach(function(a){var e=b.attributes[a]?b.attributes[a].value:"";(c[a]||"").forEach(function(a){-1!==e.indexOf(a)&&(d=!0)})});return d}function x(a){if(!a)return!1;var b=(e.extractStringValue(a.nodeName)||"").toLowerCase(),c=(e.extractStringValue(a.type)||"").toLowerCase(),d=(e.extractStringValue(a.href)||"").toLowerCase();a=(e.extractStringValue(a.id)||"").toLowerCase();var f="checkbox color date datetime-local email file month number password radio range reset search tel text time url week".split(" ");
if(-1!==["select","textarea","html"].indexOf(b)||"input"===b&&-1!==f.indexOf(c)||"a"===b&&-1!==d.indexOf("http")||-1!==["sitbreaderrightpageturner","sitbreaderleftpageturner","sitbreaderpagecontainer"].indexOf(a))return!0}function l(){n=!1;f=0;b.clearTimeout(s)}function C(){b.ue.onunload(function(){ue.count("armored-cxguardrails.unresponsive-clicks.violations",h);ue.count("armored-cxguardrails.unresponsive-clicks.violationRate",h/m*100||0)})}if(b.MutationObserver&&b.addEventListener&&Object.keys&&
d&&d.ue&&d.ue.log&&d.ue_unrt&&d.ue_utils){var y=d.ue_unrt,r="cel",v="unr_mcm",B="res_mcm",p=b.performance,e=d.ue_utils,n=!1,f=0,s=0,q=!1,k=0,h=0,m=0;b.addEventListener&&(b.addEventListener("mousedown",w,!0),b.addEventListener("beforeunload",l,!0),b.addEventListener("visibilitychange",l,!0),b.addEventListener("pagehide",l,!0));b.ue&&b.ue.event&&b.ue.onSushiUnload&&b.ue.onunload&&C();(new MutationObserver(z)).observe(t,{childList:!0,attributes:!0,characterData:!0,subtree:!0})}})(ue_csm,window,document);


ue_csm.ue.exec(function(g,e){if(e.ue_err){var f="";e.ue_err.errorHandlers||(e.ue_err.errorHandlers=[]);e.ue_err.errorHandlers.push({name:"fctx",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel)if(f=g.getElementsByTagName("html")[0].innerHTML){var b=f.indexOf("var ue_t0=ue_t0||+new Date();");if(-1!==b){var b=f.substr(0,b).split(String.fromCharCode(10)),d=Math.max(b.length-10-1,0),b=b.slice(d,b.length-1);a.fcsmln=d+b.length+1;a.cinfo=a.cinfo||{};for(var c=0;c<b.length;c++)a.cinfo[d+c+1+""]=
b[c]}b=f.split(String.fromCharCode(10));a.cinfo=a.cinfo||{};if(!(a.f||void 0===a.l||a.l in a.cinfo))for(c=+a.l-1,d=Math.max(c-5,0),c=Math.min(c+5,b.length-1);d<=c;d++)a.cinfo[d+1+""]=b[d]}}})}},"fatals-context")(document,window);


(function(m,a){function c(k){function f(b){b&&"string"===typeof b&&(b=(b=b.match(/^(?:https?:)?\/\/(.*?)(\/|$)/i))&&1<b.length?b[1]:null,b&&b&&("number"===typeof e[b]?e[b]++:e[b]=1))}function d(b){var e=10,d=+new Date;b&&b.timeRemaining?e=b.timeRemaining():b={timeRemaining:function(){return Math.max(0,e-(+new Date-d))}};for(var c=a.performance.getEntries(),k=e;g<c.length&&k>n;)c[g].name&&f(c[g].name),g++,k=b.timeRemaining();g>=c.length?h(!0):l()}function h(b){if(!b){b=m.scripts;var c;if(b)for(var d=
0;d<b.length;d++)(c=b[d].getAttribute("src"))&&"undefined"!==c&&f(c)}0<Object.keys(e).length&&(p&&ue_csm.ue&&ue_csm.ue.event&&ue_csm.ue.event({domains:e,pageType:a.ue_pty||null,subPageType:a.ue_spty||null,pageTypeId:a.ue_pti||null},"csm","csm.CrossOriginDomains.2"),a.ue_ext=e)}function l(){!0===k?d():a.requestIdleCallback?a.requestIdleCallback(d):a.requestAnimationFrame?a.requestAnimationFrame(d):a.setTimeout(d,100)}function c(){if(a.performance&&a.performance.getEntries){var b=a.performance.getEntries();
!b||0>=b.length?h(!1):l()}else h(!1)}var e=a.ue_ext||{};a.ue_ext||c();return e}function q(){setTimeout(c,r)}var s=a.ue_dserr||!1,p=!0,n=1,r=2E3,g=0;a.ue_err&&s&&(a.ue_err.errorHandlers||(a.ue_err.errorHandlers=[]),a.ue_err.errorHandlers.push({name:"ext",handler:function(a){if(!a.logLevel||"FATAL"===a.logLevel){var f=c(!0),d=[],h;for(h in f){var f=h,g=f.match(/amazon(\.com?)?\.\w{2,3}$/i);g&&1<g.length||-1!==f.indexOf("amazon-adsystem.com")||-1!==f.indexOf("amazonpay.com")||-1!==f.indexOf("cloudfront-labs.amazonaws.com")||
d.push(h)}a.ext=d}}}));a.ue&&a.ue.isl?c():a.ue&&ue.attach&&ue.attach("load",q)})(document,window);





var ue_wtc_c = 3;
ue_csm.ue.exec(function(b,e){function l(){for(var a=0;a<f.length;a++)a:for(var d=s.replace(A,f[a])+g[f[a]]+t,c=arguments,b=0;b<c.length;b++)try{c[b].send(d);break a}catch(e){}g={};f=[];n=0;k=p}function u(){B?l(q):l(C,q)}function v(a,m,c){r++;if(r>w)d.count&&1==r-w&&(d.count("WeblabTriggerThresholdReached",1),b.ue_int&&console.error("Number of max call reached. Data will no longer be send"));else{var h=c||{};h&&-1<h.constructor.toString().indexOf(D)&&a&&-1<a.constructor.toString().indexOf(x)&&m&&-1<
m.constructor.toString().indexOf(x)?(h=b.ue_id,c&&c.rid&&(h=c.rid),c=h,a=encodeURIComponent(",wl="+a+"/"+m),2E3>a.length+p?(2E3<k+a.length&&u(),void 0===g[c]&&(g[c]="",f.push(c)),g[c]+=a,k+=a.length,n||(n=e.setTimeout(u,E))):b.ue_int&&console.error("Invalid API call. The input provided is over 2000 chars.")):d.count&&(d.count("WeblabTriggerImproperAPICall",1),b.ue_int&&console.error("Invalid API call. The input provided does not match the API protocol i.e ue.trigger(String, String, Object)."))}}function F(){d.trigger&&
d.trigger.isStub&&d.trigger.replay(function(a){v.apply(this,a)})}function y(){z||(f.length&&l(q),z=!0)}var t=":1234",s="//"+b.ue_furl+"/1/remote-weblab-triggers/1/OE/"+b.ue_mid+":"+b.ue_sid+":PLCHLDR_RID$s:wl-client-id%3DCSMTriger",A="PLCHLDR_RID",E=b.wtt||1E4,p=s.length+t.length,w=b.mwtc||2E3,G=1===e.ue_wtc_c,B=3===e.ue_wtc_c,H=e.XMLHttpRequest&&"withCredentials"in new e.XMLHttpRequest,x="String",D="Object",d=b.ue,g={},f=[],k=p,n,z=!1,r=0,C=function(){return{send:function(a){if(H){var b=new e.XMLHttpRequest;
b.open("GET",a,!0);G&&(b.withCredentials=!0);b.send()}else throw"";}}}(),q=function(){return{send:function(a){(new Image).src=a}}}();e.encodeURIComponent&&(d.attach&&(d.attach("beforeunload",y),d.attach("pagehide",y)),F(),d.trigger=v)},"client-wbl-trg")(ue_csm,window);


(function(k,d,h){function f(a,c,b){a&&a.indexOf&&0===a.indexOf("http")&&0!==a.indexOf("https")&&l(s,c,a,b)}function g(a,c,b){a&&a.indexOf&&(location.href.split("#")[0]!=a&&null!==a&&"undefined"!==typeof a||l(t,c,a,b))}function l(a,c,b,e){m[b]||(e=u&&e?n(e):"N/A",d.ueLogError&&d.ueLogError({message:a+c+" : "+b,logLevel:v,stack:"N/A"},{attribution:e}),m[b]=1,p++)}function e(a,c){if(a&&c)for(var b=0;b<a.length;b++)try{c(a[b])}catch(d){}}function q(){return d.performance&&d.performance.getEntriesByType?
d.performance.getEntriesByType("resource"):[]}function n(a){if(a.id)return"//*[@id='"+a.id+"']";var c;c=1;var b;for(b=a.previousSibling;b;b=b.previousSibling)b.nodeName==a.nodeName&&(c+=1);b=a.nodeName;1!=c&&(b+="["+c+"]");a.parentNode&&(b=n(a.parentNode)+"/"+b);return b}function w(){var a=h.images;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"img",a);g(b,"img",a)})}function x(){var a=h.scripts;a&&a.length&&e(a,function(a){var b=a.getAttribute("src");f(b,"script",a);g(b,"script",a)})}
function y(){var a=h.styleSheets;a&&a.length&&e(a,function(a){if(a=a.ownerNode){var b=a.getAttribute("href");f(b,"style",a);g(b,"style",a)}})}function z(){if(A){var a=q();e(a,function(a){f(a.name,a.initiatorType)})}}function B(){e(q(),function(a){g(a.name,a.initiatorType)})}function r(){var a;a=d.location&&d.location.protocol?d.location.protocol:void 0;"https:"==a&&(z(),w(),x(),y(),B(),p<C&&setTimeout(r,D))}var s="[CSM] Insecure content detected ",t="[CSM] Ajax request to same page detected ",v="WARN",
m={},p=0,D=k.ue_nsip||1E3,C=5,A=1==k.ue_urt,u=!0;ue_csm.ue_disableNonSecure||(d.performance&&d.performance.setResourceTimingBufferSize&&d.performance.setResourceTimingBufferSize(300),r())})(ue_csm,window,document);


var ue_aa_a = "C";
if (ue.trigger && (ue_aa_a === "C" || ue_aa_a === "T1")) {
    ue.trigger("UEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249", ue_aa_a);
}
(function(b,a){function n(){try{a.PerformanceObserver&&"function"===typeof a.PerformanceObserver&&(c=new a.PerformanceObserver(function(a){e(a.getEntries())}),c.observe(k))}catch(d){l()}}function p(){for(var d=k.entryTypes,b=0;b<d.length;b++)e(a.performance.getEntriesByType(d[b]))}function e(d){if(d&&Array.isArray(d)){for(var c=0,f=0;f<d.length;f++){var g=m.indexOf(d[f].name);if(-1!==g){var e=Math.round(a.performance.timing.navigationStart+d[f].startTime);b.ue.isl&&b.ue_f_paint?b.uex(h[g],"csm:"+
h[g],void 0,e):b.uet(h[g],void 0,void 0,e);c++}}m.length===c&&l()}}function l(){c&&c.disconnect&&"function"===typeof c.disconnect&&c.disconnect()}if("function"===typeof b.uet&&a.performance&&"object"===typeof a.performance&&a.performance.getEntriesByType&&"function"===typeof a.performance.getEntriesByType&&a.performance.timing&&"object"===typeof a.performance.timing&&"number"===typeof a.performance.timing.navigationStart){var k={entryTypes:["paint"]},m=["first-paint","first-contentful-paint"],h=["fp",
"fcp"],c;try{p(),n()}catch(q){b.ueLogError(q,{logLevel:"ERROR",attribution:"performanceMetrics"})}}})(ue_csm,window);


if (window.csa) {
    csa("Events")("setEntity", {
        page:{pageType: "Landing", subPageType: "BrowsePage", pageTypeId: "283155"}
    });
}
csa.plugin(function(c){var m="transitionStart",n="pageVisible",e="PageTiming",t="visibilitychange",s="$latency.visible",i=c.global,r=(i.performance||{}).timing,a=["navigationStart","unloadEventStart","unloadEventEnd","redirectStart","redirectEnd","fetchStart","domainLookupStart","domainLookupEnd","connectStart","connectEnd","secureConnectionStart","requestStart","responseStart","responseEnd","domLoading","domInteractive","domContentLoadedEventStart","domContentLoadedEventEnd","domComplete","loadEventStart","loadEventEnd"],o=i.Math,u=o.max,l=o.floor,d=i.document||{},g=(r||{}).navigationStart,f=g,v=0,p=null;if(i.Object.keys&&[].forEach&&!c.config["KillSwitch."+e]){if(!r||null===g||g<=0||void 0===g)return c.error("Invalid navigation timing data: "+g);p=new S({schemaId:"<ns>.PageLatency.5",producerId:"csa"}),"boolean"!=typeof d.hidden&&"string"!=typeof d.visibilityState||!d.removeEventListener?c.emit(s):h()?(c.emit(s),E(n,g)):c.on(d,t,function e(){h()&&(f=c.time(),d.removeEventListener(t,e),E(m,f),E(n,f),c.emit(s))}),c.once("$unload",I),c.once("$load",I),c.on("$pageTransition",function(){f=c.time()}),c.register(e,{mark:E,instance:function(e){return new S(e)}})}function S(e){var i,r=null,a=e.ent||{page:["pageType","subPageType","requestId"]},o=e.logger||c("Events",{producerId:e.producerId});if(!e||!e.producerId||!e.schemaId)return c.error("The producer id and schema Id must be defined for PageLatencyInstance.");function d(){return i||f}function n(){r=c.UUID()}this.mark=function(n,t){if(null!=n)return t=t||c.time(),n===m&&(i=t),c.once(s,function(){o("log",{messageId:r,__merge:function(e){e.markers[n]=function(e,n){return u(0,n-(e||f))}(d(),t),e.markerTimestamps[n]=l(t)},markers:{},markerTimestamps:{},navigationStartTimestamp:d()?new Date(d()).toISOString():null,schemaId:e.schemaId},{ent:a})}),t},n(),c.on("$beforePageTransition",n)}function E(e,n){e===m&&(f=n);var t=p.mark(e,n);c.emit("$timing:"+e,t)}function I(){if(!v){for(var e=0;e<a.length;e++)r[a[e]]&&E(a[e],r[a[e]]);v=1}}function h(){return!d.hidden||"visible"===d.visibilityState}});csa.plugin(function(t){var a,f="length",u="parentElement",i="target",r="getEntriesByName",e="perf",n=null,o="_osrc",c="_elt",s="_eid",l=10,d=5,g=10,h=100,m=t.global,p="SpeedIndex",v=t.config[p+".DeduplicateCarousel"],y=t.config[p+".UseTimeout"],E=t.timeout,S=m.Math,b=S.max,x=S.floor,O=S.ceil,w=m.document,T=m.performance||{},L=(T.timing||{}).navigationStart,N=Date.now,I=Object.values||(t.types||{}).ovl,_=t("PageTiming"),B=t("SpeedIndexBuffers"),Y=[],k=[],C=[],H=[],V=[],W=.1,$=.1,D=0,F=0,M=!0,P=0,R=0,X=0,J=0,U=1,j=0,q={},Q=[],z=0,A={buffered:1};function G(e){t.global.ue_csa_ss_tag||t.emit("$csmTag:"+e,0,A)}function K(){for(var e=N(),n=0;a;){if(0!==a[f]){if(!1!==a.h(a[0])&&a.shift(),n++,!X&&n%l==0&&N()-e>d)break}else a=a.n}D=0,a&&0<a[f]&&(D||(y?!0===w.hidden?(X=1,K()):t.timeout(K,0):D=t.raf(K)))}function Z(e,n,t,i){j=x(e),Y=n,k=t,V=i;var r=w.createTreeWalker(w.body,NodeFilter.SHOW_TEXT,null,null),o={w:m.innerWidth,h:m.innerHeight,x:m.pageXOffset,y:m.pageYOffset};w.body[c]=e,C.push({w:r,vp:o}),H.push({img:w.images,iter:0}),Y.h=ee,(Y.n=k).h=ne,(k.n=C).h=te,(C.n=H).h=ie,(H.n=V).h=re,a=Y,K()}function ee(e){e.m.forEach(function(e){var n=e[i];o in n||(n[o]=e.oldValue)})}function ne(n){n.m.forEach(function(e){e[i][c]=n.t-L})}function te(e){for(var n,t=e.vp,i=e.w,r=l;(n=i.nextNode())&&0<r;){r-=1;var o=(n[u]||{}).nodeName;"SCRIPT"!==o&&"STYLE"!==o&&"NOSCRIPT"!==o&&"BODY"!==o&&0!==(n.nodeValue||"").trim()[f]&&ce(n[u],oe(n),t)}return!n}function ie(e){for(var n={w:m.innerWidth,h:m.innerHeight,x:m.pageXOffset,y:m.pageYOffset},t=l;e.iter<e.img[f]&&0<t;){var i,r=e.img[e.iter];if(v){var o=ue(r);i=fe(o&&(r=o).querySelector('[aria-posinset="1"] img')||r)}else i=fe(r);ce(r,i,n),e.iter+=1,t-=1}return e.img[f]<=e.iter}function re(e){var n=[],i=0,r=0,o=F,t=x(e.y/h),a=O((e.y+m.innerHeight)/h);Q.slice(t,a).forEach(function(e){(e.elems||[]).forEach(function(e){e.lt in n||(n[e.lt]={}),e.id in n[e.lt]||(i+=(n[e.lt][e.id]=e).a)})}),G("startVL"),I(n).forEach(function(e){I(e).forEach(function(e){var n=1-r/i,t=b(e.lt,o);z+=n*(t-o),o=t,function(e,n){for(;W<=1&&W-.01<=e;)le("visuallyLoaded"+(100*W).toFixed(0),n),W+=$}((r+=e.a)/i,e.lt)})}),G("endVL"),F=e.t-L,V[f]<=1&&(le("speedIndex",z),le("visuallyLoaded0",j)),M&&(M=!1,le("atfSpeedIndex",z))}function oe(e){for(var n=e[u],t=g;n&&0<t;){if(n[c]||0===n[c])return b(n[c],j);n=n.parentElement,t-=1}}function ae(e,n){if(e){if(!e.indexOf("data:"))return oe(n);var t=T[r](e)||[];if(0<t[f])return b(O(t[0].responseEnd||0),j)}}function fe(e){return ae(e[o],e)||ae(e.currentSrc,e)||ae(e.src,e)}function ue(e){for(var n=10,t=e.parentElement;t&&0<n;){if(t.classList&&t.classList.contains("a-carousel-viewport"))return t;t=t.parentElement,n-=1}return null}function ce(e,n,t){if((n||0===n)&&!e[s]){var i=e.getBoundingClientRect(),r=i.width*i.height,o=i.width/2,a=U++;if(0!=r&&!(o<i.right-t.w||i.right<o)){for(var f={e:e,lt:n,a:r,id:a},u=x((i.top+t.y)/h),c=O((i.top+t.y+i.height)/h),l=u;l<=c;l++)l in Q||(Q[l]={elems:[],lt:0}),Q[l].elems.push(f);e[s]=a}}}function le(e,n){_("mark",e,L+O((q[e]=n)||0))}function se(e){J||(G("browserQuite"+e),B("getBuffers",Z),J=1)}L&&I&&T[r]?(G(e+"Yes"),B("registerListener",function(e){R&&(clearTimeout(P),P=E(se.bind(n,"Mut"),2500))}),t.once("$unload",function(){X=1,se("Ud")}),t.once("$load",function(){R=1,P=E(se.bind(n,"Ld"),2500)}),t.once("$timing:functional",se.bind(n,"Fn")),t.register("SpeedIndex",{getMarkers:function(e){e&&e(JSON.parse(JSON.stringify(q)))}})):G(e+"No")});csa.plugin(function(e){var m=!!e.config["LCP.elementDedup"],t=!1,n=e("PageTiming"),r=e.global.PerformanceObserver,a=e.global.performance;function i(){return a.timing.navigationStart}function o(){t||function(o){var l=new r(function(e){var t=e.getEntries();if(0!==t.length){var n=t[t.length-1];if(m&&""!==n.id&&n.element&&"IMG"===n.element.tagName){for(var r={},a=t[0],i=0;i<t.length;i++)t[i].id in r||(""!==t[i].id&&(r[t[i].id]=!0),a.startTime<t[i].startTime&&(a=t[i]));n=a}l.disconnect(),o({startTime:n.startTime,renderTime:n.renderTime,loadTime:n.loadTime})}});try{l.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}}(function(e){e&&(t=!0,n("mark","largestContentfulPaint",Math.floor(e.startTime+i())),e.renderTime&&n("mark","largestContentfulPaint.render",Math.floor(e.renderTime+i())),e.loadTime&&n("mark","largestContentfulPaint.load",Math.floor(e.loadTime+i())))})}r&&a&&a.timing&&(e.once("$unload",o),e.once("$load",o),e.register("LargestContentfulPaint",{}))});csa.plugin(function(r){var e=r("Metrics",{producerId:"csa"}),n=r.global.PerformanceObserver;n&&(n=new n(function(r){var t=r.getEntries();if(0===t.length||!t[0].processingStart||!t[0].startTime)return;!function(r){r=r||0,n.disconnect(),0<=r?e("recordMetric","firstInputDelay",r):e("recordMetric","firstInputDelay.invalid",1)}(t[0].processingStart-t[0].startTime)}),function(){try{n.observe({type:"first-input",buffered:!0})}catch(r){}}())});csa.plugin(function(d){var e="Metrics",u=0;function r(i){var t,e=i.producerId,r=i.logger,c=r||d("Events",{producerId:e}),o=(i||{}).dimensions||{},n=-1;if(!e&&!r)return d.error("Either a producer id or custom logger must be defined");function s(){n!==u&&(t=d.UUID(),n=u)}this.recordMetric=function(r,n){var e=i.logOptions||{ent:{page:["pageType","subPageType","requestId"]}};e.debugMetric=i.debugMetric,s(),c("log",{messageId:t,schemaId:i.schemaId||"<ns>.Metric.3",metrics:{},dimensions:o,__merge:function(e){e.metrics[r]=n}},e)}}d.config["KillSwitch."+e]||(new r({producerId:"csa"}).recordMetric("baselineMetricEvent",1),d.on("$beforePageTransition",function(){u++}),d.register(e,{instance:function(e){return new r(e||{})}}))});csa.plugin(function(t){var a,r=(t.global.performance||{}).timing,s=(r||{}).navigationStart||t.time();function e(){a=t.UUID()}function n(i){var r=(i=i||{}).producerId,e=i.logger,o=e||t("Events",{producerId:r});if(!r&&!e)return t.error("Either a producer id or custom logger must be defined");this.mark=function(e,r){var n=(void 0===r?t.time():r)-s;o("log",{messageId:a,schemaId:i.schemaId||"<ns>.Timer.1",markers:{},__merge:function(r){r.markers[e]=n}},i.logOptions)}}r&&(e(),t.on("$beforePageTransition",e),t.register("Timers",{instance:function(r){return new n(r||{})}}))});csa.plugin(function(t){var e="takeRecords",i="disconnect",n="function",o=t("Metrics",{producerId:"csa"}),c=t("PageTiming"),a=t.global,u=t.timeout,r=t.on,f=a.PerformanceObserver,m=0,l=!1,s=0,d=a.performance,h=a.document,v=null,y=!1,g=t.blank;function p(){l||(l=!0,clearTimeout(v),typeof f[e]===n&&f[e](),typeof f[i]===n&&f[i](),o("recordMetric","documentCumulativeLayoutShift",m),c("mark","cumulativeLayoutShiftLastTimestamp",Math.floor(s+d.timing.navigationStart)))}f&&d&&d.timing&&h&&(f=new f(function(t){v&&clearTimeout(v);t.getEntries().forEach(function(t){t.hadRecentInput||(m+=t.value,s<t.startTime&&(s=t.startTime))}),v=u(p,5e3)}),function(){try{f.observe({type:"layout-shift",buffered:!0}),v=u(p,5e3)}catch(t){}}(),g=r(h,"click",function(t){y||(y=!0,o("recordMetric","documentCumulativeLayoutShiftToFirstInput",m),g())}),r(h,"visibilitychange",function(){"hidden"===h.visibilityState&&p()}),t.once("$unload",p))});csa.plugin(function(e){var t,n=e.global,r=n.PerformanceObserver,c=e("Metrics",{producerId:"csa"}),o=0,i=0,a=-1,l=n.Math,f=l.max,u=l.ceil;if(r){t=new r(function(e){e.getEntries().forEach(function(e){var t=e.duration;o+=t,i+=t,a=f(t,a)})});try{t.observe({type:"longtask",buffered:!0})}catch(e){}t=new r(function(e){0<e.getEntries().length&&(i=0,a=-1)});try{t.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}e.on("$unload",g),e.on("$beforePageTransition",g)}function g(){c("recordMetric","totalBlockingTime",u(i||0)),c("recordMetric","totalBlockingTimeInclLCP",u(o||0)),c("recordMetric","maxBlockingTime",u(a||0)),i=o=0,a=-1}});csa.plugin(function(r){var e="CacheDetection",o="csa-ctoken-",n=r.store,t=r.deleteStored,c=r.config,a=c[e+".RequestID"],i=c[e+".Callback"],s=r.global,u=s.document||{},d=s.Date,f=r("Events"),l=r("Events",{producerId:"csa"});function p(e){try{var n=u.cookie.match(RegExp("(^| )"+e+"=([^;]+)"));return n&&n[2].trim()}catch(e){}}!function(){var e=function(){var e=p("cdn-rid");if(e)return{r:e,s:"cdn"}}()||function(){if(r.store(o+a))return{r:r.UUID().toUpperCase().replace(/-/g,"").slice(0,20),s:"device"}}()||{},n=e.r,c=e.s;if(!!n){var t=p("session-id");!function(e,n,c,t){f("setEntity",{page:{pageSource:"cache",requestId:e,cacheRequestId:a,cacheSource:t},session:{id:c}})}(n,0,t,c),"device"===c&&l("log",{schemaId:"<ns>.CacheImpression.1"},{ent:"all"}),i&&i(n,t,c)}}(),n(o+a,d.now()+36e5),r.once("$load",function(){var c=d.now();t(function(e,n){return 0==e.indexOf(o)&&parseInt(n)<c})})});csa.plugin(function(u){var i,t="Content",e="MutationObserver",n="addedNodes",a="querySelectorAll",s="matches",o="getAttributeNames",r="getAttribute",f="dataset",c="widget",l="producerId",d={ent:{element:1,page:["pageType","subPageType","requestId"]}},h=5,p=u.config[t+".BubbleUp.SearchDepth"]||20,g="csaC",m=g+"Id",y="logRender",v={},b=u.config,E=b[t+".Selectors"]||[],I=b[t+".WhitelistedAttributes"]||{href:1,class:1},w=b[t+".EnableContentEntities"],C=b[t+".EnableContentRenders"],O=b["KillSwitch.ContentRendered"],k=u.global,A=k.document||{},U=A.documentElement,L=k.HTMLElement,N={},R=[],S=function(t,e,n,i){var r=this,o=u("Events",{producerId:t||"csa"});e.type=e.type||c,r.id=e.id,r.l=o,r.e=e,r.el=n,r.rt=i,r.dlo=d,r.op=K(n,"csaOp"),r.log=function(t,e){o("log",t,e||d)},e.id&&o("setEntity",{element:e})},_=S.prototype;function j(t){var e=(t=t||{}).element,n=t.target;return e?function(t,e){var n;n=t instanceof L?H(t)||$(e[l],t,W,u.time()):N[t.id]||B(e[l],0,t,u.time());return n}(e,t):n?D(n):u.error("No element or target argument provided.")}function D(t){var e=function(t){var e=null,n=0;for(;t&&n<p;){if(n++,T(t,m)){e=t;break}t=t.parentElement}return e}(t);return e?H(e):new S("csa",{id:null},null,u.time())}function T(t,e){if(t&&t.dataset)return t.dataset[e]}function q(t,e,n){R.push({n:n,e:t,t:e}),M()}function x(){for(var t=u.time(),e=0;0<R.length;){var n=R.shift();if(v[n.n](n.e,n.t),++e%10==0&&u.time()-t>h)break}i=0,R.length&&M()}function M(){i=i||u.raf(x)}function P(t,e,n){return{n:t,e:e,t:n}}function $(t,e,n,i){var r=u.UUID(),o={id:r},c=D(e);return e[f][m]=r,n(o,e),c&&c.id&&(o.parentId=c.id),B(t,e,o,i)}function B(t,e,n,i){w&&(n.schemaId="<ns>.ContentEntity.2"),n.id=n.id||u.UUID();var r=new S(t,n,e,i);return function(t){return C&&!O&&(t.op||{}).hasOwnProperty(y)}(r)&&r.log({schemaId:"<ns>.ContentRender.1",timestamp:i}),u.emit("$content.register",r),N[n.id]=r}function H(t){return N[(t[f]||{})[m]]}function K(n,i){var r={};return o in(n=n||{})&&Object.keys(n[f]).forEach(function(t){if(!t.indexOf(i)&&i.length<t.length){var e=function(t){return(t[0]||"").toLowerCase()+t.slice(1)}(t.slice(i.length));r[e]=n[f][t]}}),r}function W(t,e){o in e&&(function(t,e){var n=K(t,g);Object.keys(n).forEach(function(t){e[t]=n[t]})}(e,t),function(e,n){(e[o]()||[]).forEach(function(t){t in I&&(n[t]=e[r](t))})}(e,t))}U&&A[a]&&k[e]&&(E.push({selector:"*[data-csa-c-type]",entity:W}),E.push({selector:".celwidget",entity:function(t,e){W(t,e),t.slotId=t.slotId||e[r]("cel_widget_id")||e.id,t.legacyId=e[r]("cel_widget_id")||e.id,t.type=t.type||c}}),v[1]=function(t,e){t.forEach(function(t){t[n]&&t[n].constructor&&"NodeList"===t[n].constructor.name&&Array.prototype.forEach.call(t[n],function(t){R.unshift(P(2,t,e))})})},v[2]=function(o,c){a in o&&s in o&&E.forEach(function(t){for(var e=t.selector,n=o[s](e),i=o[a](e),r=i.length-1;0<=r;r--)R.unshift(P(3,{e:i[r],s:t},c));n&&R.unshift(P(3,{e:o,s:t},c))})},v[3]=function(t,e){var n=t.e;H(n)||$("csa",n,t.s.entity,e)},v[4]=function(){u.register(t,{instance:j})},new k[e](function(t){q(t,u.time(),1)}).observe(U,{childList:!0,subtree:!0}),q(U,u.time(),2),q(null,u.time(),4),u.on("$content.export",function(e){Object.keys(e).forEach(function(t){_[t]=e[t]})}))});csa.plugin(function(n){var i,t="ContentImpressions",e="KillSwitch.",o="IntersectionObserver",r="getAttribute",s="dataset",c="intersectionRatio",a="csaCId",m=1e3,l=n.global,f=n.config,u=f[e+t],g=f[e+t+".ContentViews"],v=((l.performance||{}).timing||{}).navigationStart||n.time(),d={};function h(t){t&&(t.v=1,function(t){t.vt=n.time(),t.el.log({schemaId:"<ns>.ContentView.3",timeToViewed:t.vt-t.el.rt,pageFirstPaintToElementViewed:t.vt-v})}(t))}function I(t){t&&!t.it&&(t.i=n.time()-t.is>m,function(t){t.it=n.time(),t.el.log({schemaId:"<ns>.ContentImpressed.2",timeToImpressed:t.it-t.el.rt,pageFirstPaintToElementImpressed:t.it-v})}(t))}!u&&l[o]&&(i=new l[o](function(t){t.forEach(function(t){var e=function(t){if(t&&t[r])return d[t[s][a]]}(t.target);if(e){var i=t.intersectionRect;t.isIntersecting&&0<i.width&&0<i.height&&(g||e.v||h(e),.5<=t[c]&&!e.is&&(e.is=n.time(),e.timer=n.timeout(function(){I(e)},m))),t[c]<.5&&!e.it&&e.timer&&(l.clearTimeout(e.timer),e.is=0,e.timer=0)}})},{threshold:[0,.5]}),n.on("$content.register",function(t){var e=t.el;e&&(d[t.id]={el:t,v:0,i:0,is:0,vt:0,it:0},i.observe(e))}))});csa.plugin(function(e){e.config["KillSwitch.ContentLatency"]||e.emit("$content.export",{mark:function(t,n){var o=this;o.t||(o.t=e("Timers",{logger:o.l,schemaId:"<ns>.ContentLatency.1",logOptions:o.dlo})),o.t("mark",t,n)}})});csa.plugin(function(o){var t,n,i="normal",s="reload",e="history",d="new-tab",a="ajax",r=1,c=2,u="lastActive",l="lastInteraction",f="used",p="csa-tabbed-browsing",g="visibilityState",v={"back-memory-cache":1,"tab-switch":1,"history-navigation-page-cache":1},b="<ns>.TabbedBrowsing.2",m="visible",y=o.global,I=o("Events",{producerId:"csa"}),h=y.location||{},T=y.document,w=y.JSON,z=((y.performance||{}).navigation||{}).type,P=o.store,S=o.on,k=o.storageSupport(),x=!1,A={},C={},O={},$={},j=!1,q=!1,B=!1;function E(i){try{return w.parse(P(p,void 0,{session:i})||"{}")||{}}catch(i){o.error('Could not parse storage value for key "'+p+'": '+i)}return{}}function J(i,t){P(p,w.stringify(t||{}),{session:i})}function N(i){var t=C.tid||i.id,n=A[u]||{};n.tid===t&&(n.pid=i.id),$={pid:i.id,tid:t,lastInteraction:C[l]||{},initialized:!0},O={lastActive:n,lastInteraction:A[l]||{},time:o.time()}}function D(i){var t=i===d,n=T.referrer,e=!(n&&n.length)||!~n.indexOf(h.origin||""),a=t&&e,r={type:i,toTabId:$.tid,toPageId:$.pid,transitTime:o.time()-A.time||null};a||function(i,t,n){var e=i===s,a=t?A[u]||{}:C,r=A[l]||{},o=C[l]||{},d=t?r:o;n.fromTabId=a.tid,n.fromPageId=a.pid,e||!d.id||d[f]||(n.interactionId=d.id||null,r.id===d.id&&(r[f]=!0),o.id===d.id&&(o[f]=!0))}(i,t,r),I("log",{navigation:r,schemaId:b},{ent:{page:["pageType","subPageType","requestId"]}})}function F(i){B=function(i){return i&&i in v}(i.transitionType),function(){A=E(!1),C=E(!0);var i=A[l],t=C[l],n=!1,e=!1;i&&t&&i.id===t.id&&i[f]!==t[f]&&(n=!i[f],e=!t[f],t[f]=i[f]=!0,n&&J(!1,A),e&&J(!0,C))}(),N(i),j=!0,function(i){var t,n;t=H(),n=K(),(t||n)&&N(i)}(i)}function G(){x&&!B?D(a):(x=!0,D(z===c||B?e:z===r?C.initialized?s:d:C.initialized?i:d))}function H(){return!(!j||!t)&&(C[l]={id:t.messageId,used:!(A[l]={id:t.messageId,used:!1})},!(t=null))}function K(){var i=!1;if(q=T[g]===m,j){var t=A[u]||{};i=function(i,t,n){var e=!1,a=i[u];return q?a&&a.tid===$.tid&&a[m]&&a.pid===n||(i[u]={visible:!0,pid:n,tid:t},e=!0):a&&a.tid===$.tid&&a[m]&&(e=!(a[m]=!1)),e}(A,C.tid||t.tid||$.tid,C.pid||t.pid||$.pid)}return i}k.local&&k.session&&w&&T&&g in T&&(n=function(){try{return y.self!==y.top}catch(i){return!0}}(),S("$pageChange",function(i){n||(F(i),G(),J(!1,O),J(!0,$),C=$,A=O)},{buffered:1}),S("$content.interaction",function(i){t=i,H()&&(J(!1,A),J(!0,C))}),S(T,"visibilitychange",function(){!n&&K()&&J(!1,A)},{capture:!1,passive:!0}))});csa.plugin(function(c){var e=c("Metrics",{producerId:"csa"});c.on(c.global,"pageshow",function(c){c&&c.persisted&&e("recordMetric","bfCache",1)})});csa.plugin(function(e){var n,a,c,u,r,t,s,f,l,p,i,o="hasFocus",m="avail",d="client",g="document",h="inner",v="offset",b="screen",T="scroll",w="Width",y="Height",P=m+w,S=m+y,I=d+w,$=d+y,x=h+w,D=h+y,E=v+w,F=v+y,O=T+w,q=T+y,z=e("Events",{producerId:"csa"}),C=1,H=e.global||{},M=e.time,R=e.on,W=H[g]||{},X=H[b]||{},Y=H.Math||{},j=Y.abs,k=Y.max,A=Y.ceil,B=((H.performance||{}).timing||{}).responseStart,G=H.P||{},J=100;function K(){f=a=r=t=n,c=u=0,s=l=p=i=0}function L(){var e=M(),n=j(H.pageXOffset||0),t=j(H.pageYOffset||0),i=H[x]||0,o=H[D]||0;!function(e){B&&!r&&(f=A((r=e)-B))}(e),function(e,n,t){var i=n-c,o=t-u;a&&!(a&&a<=e)||((i||o)&&++s,c=n,u=t,i,o),a=e+J}(e,n,t),function(e,n,t,i,o){l=A(k(l,t+o)),n&&(p=A(k(p,n+i)))}(0,n,t,i,o)}function N(){t&&(i+=A(M()-t),t=n)}function Q(){t=t||M()}function U(e,n,t,i){n[e+w]=A(t||0),n[e+y]=A(i||0)}function V(){if(C){C=0;var e,n=function(){var e={},n=W.documentElement||{},t=W.body||{};return U("availableScreen",e,X[P],X[S]),U(g,e,k(t[O]||0,t[E]||0,n[I]||0,n[O]||0,n[E]||0),k(t[q]||0,t[F]||0,n[$]||0,n[q]||0,n[F]||0)),U(b,e,X.width,X.height),U("viewport",e,H[x],H[D]),e}();W[o]()&&N(),e={scrollCounts:s,reachedDepth:l,horizontalScrollDistance:p,dwellTime:i},"number"==typeof f&&(e.clientTimeToFirstScroll=f),K(),B=M(),W[o]()&&(t=B),z("log",{activity:e,dimensions:n,schemaId:"<ns>.PageInteractionsSummary.1"},{ent:{page:["pageType","subPageType","requestId"]}}),H.ue&&H.ue.count&&H.ue.count("csa.dwellTime",e.dwellTime)}}"function"==typeof W[o]&&(K(),R(H,T,L,{passive:!0}),R(H,"blur",N),R(H,"focus",Q),G.when&&G.when("mash").execute(function(e){e&&(R(e,"appPause",N),R(e,"appResume",Q))}),W[o]()&&(t=B||M()),R("$beforeunload",V),R("$beforePageTransition",V),R("$afterPageTransition",function(){C=1}))});csa.plugin(function(e){var o,n,r="<ns>.Navigator.4",a=e.global,i=a.navigator||{},d=i.connection||{},c=a.Math.round,t=e("Events",{producerId:"csa"});function l(){o={network:{downlink:void 0,downlinkMax:void 0,rtt:void 0,type:void 0,effectiveType:void 0,saveData:void 0},language:void 0,doNotTrack:void 0,hardwareConcurrency:void 0,deviceMemory:void 0,cookieEnabled:void 0,webdriver:void 0},v(),o.language=i.language||null,o.doNotTrack=function(){switch(i.doNotTrack){case"1":return"enabled";case"0":return"disabled";case"unspecified":return i.doNotTrack;default:return null}}(),o.hardwareConcurrency="hardwareConcurrency"in i?c(i.hardwareConcurrency||0):null,o.deviceMemory="deviceMemory"in i?c(i.deviceMemory||0):null,o.cookieEnabled="cookieEnabled"in i?i.cookieEnabled:null,o.webdriver="webdriver"in i?i.webdriver:null}function u(){t("log",{network:(n={},Object.keys(o.network).forEach(function(e){n[e]=o.network[e]+""}),n),language:o.language,doNotTrack:o.doNotTrack,hardwareConcurrency:o.hardwareConcurrency,deviceMemory:o.deviceMemory,cookieEnabled:o.cookieEnabled,webdriver:o.webdriver,schemaId:r},{ent:{page:["pageType","subPageType","requestId"]}})}function v(){!function(n){Object.keys(o.network).forEach(function(e){o.network[e]=n[e]})}({downlink:"downlink"in d?c(d.downlink||0):null,downlinkMax:"downlinkMax"in d?c(d.downlinkMax||0):null,rtt:"rtt"in d?(d.rtt||0).toFixed():null,type:d.type||null,effectiveType:d.effectiveType||null,saveData:"saveData"in d?d.saveData:null})}function k(){v(),u()}function w(){l(),u()}l(),u(),e.on("$afterPageTransition",w),e.on(d,"change",k)});
(function(t,z,C){var u=function(){var a,c=function(){return null!=a?a:a=function(){var a=[],c="unknown",b={trident:0,gecko:0,presto:0,webkit:0,unknown:-1},d,e={},c=document.createElement("nadu");for(d in c.style)if(c=(/^([A-Za-z][a-z]*)[A-Z]/.exec(d)||[])[1])c=c.toLowerCase(),c in e?e[c]++:e[c]=1;for(var n in e)a.push([n,e[n]]);a=a.sort(function(a,c){return c[1]-a[1]}).slice(0,10);for(d=0;d<a.length;d++)switch(a[d][0]){case "moz":b.gecko+=5;break;case "ms":b.trident+=5;break;case "get":b.webkit++;
break;case "webkit":b.webkit+=5;break;case "o":b.presto+=2;break;case "xv":b.presto+=2}"onhelp"in window&&b.trident++;"maxConnectionsPerServer"in window&&b.trident++;try{void 0!==window.ActiveXObject.toString&&(b.trident+=5)}catch(r){}void 0!==function(){}.toSource&&(b.gecko+=5);var a="unknown",q;for(q in b)b[q]>b[a]&&(a=q);return a}()},b=function(){return!!window.opera||!!window.opr&&!!window.opr.addons},d=function(){return!!document.documentMode},e=function(){return!d()&&"undefined"!==typeof CSS&&
CSS.supports("(-ms-ime-align:auto)")},n=function(){return"webkit"==c()},r=function(){return void 0!==z.chrome&&"Opera Software ASA"!=navigator.vendor&&void 0===navigator.msLaunchUri&&n()};return{isOpera:b,isIE:d,isEdge:e,isFirefox:function(){return"undefined"!==typeof InstallTrigger},isWebkit:n,isChrome:r,isSafari:function(){return!r()&&!e()&&!b()&&"WebkitAppearance"in document.documentElement.style}}}(),q=function(a,c,b,d){a.addEventListener?a.addEventListener(c,b,d):a.attachEvent&&a.attachEvent("on"+
c,b)},r=function(a,c,b,d){document.removeEventListener?a.removeEventListener(c,b,d||!1):document.detachEvent&&a.detachEvent("on"+c,b)},H=function(a){var c;a=a.document;"undefined"!==typeof a.hidden?c="visibilitychange":"undefined"!==typeof a.mozHidden?c="mozvisibilitychange":"undefined"!==typeof a.msHidden?c="msvisibilitychange":"undefined"!==typeof a.webkitHidden&&(c="webkitvisibilitychange");return c},T=function(a,c){var b=H(a),d=a.document;b&&q(d,b,c,!1)},U=function(a){var c=window.addEventListener?
"addEventListener":"attachEvent";(0,window[c])("attachEvent"==c?"onmessage":"message",function(c){a(c[c.message?"message":"data"])},!1)},V=function(a,c){"function"===typeof a&&Math.random()<c/100&&a.call(this)},v=function(a){try{for(var c=Array.prototype.slice.call(arguments,1),b=0;b<c.length;b++){if(!a)return!0;var d=a[c[b]];if(null===d||void 0===d)return!0;a=d}return!1}catch(e){return!0}},A=function(a){try{if(!a)return a;for(var c=Array.prototype.slice.call(arguments,1),b,d=0;d<c.length;d++){b=
a[c[d]];if(!b)break;a=b}return b}catch(e){return null}},W=function(a,c){try{if(!a)return!1;for(var b=Array.prototype.slice.call(arguments,2),d=0;d<b.length;d++){var e=a[b[d]];if(null===e||void 0===e)return d===b.length-1?typeof e===c:!1;a=e}return typeof e===c}catch(n){return!1}},I=function(a){a&&document.body&&a.parentNode===document.body&&document.body.removeChild(a)},J=function(a,c,b){var d=window.document.createElement("IFRAME");d.id=c;d.height="5px";d.width="5px";d.src=b?b:"javascript:'1'";d.style.position=
"absolute";d.style.top="-10000px";d.style.left="-10000px";d.style.visibility="hidden";d.style.opacity=0;window.document.body.appendChild(d);try{var e=d.contentDocument;if(e&&(e.open(),e.writeln("<!DOCTYPE html><html><head><title></title></head><body></body></html>"),e.close(),a)){var r=e.createElement("script");r&&(r.type="text/javascript",r.text=a,e.body.appendChild(r))}}catch(q){n(q,"JS exception while injecting iframe")}return d},n=function(a,c){t.ueLogError(a,{logLevel:"ERROR",attribution:"A9TQForensics",
message:c})},X=function(a,c,b){a={vfrd:1===c?"8":"4",dbg:a};"object"===typeof b?a.info=JSON.stringify(b):"string"===typeof b&&(a.info=b);return{server:window.location.hostname,fmp:a}};(function(a){function c(a,c,b){var d="chrm msie ffox sfri opra phnt slnm othr extr xpcm invs poev njs cjs rhn clik1 rfs uam clik stln mua nfo hlpx clkh mmh chrm1 chrm2 wgl srvr zdim nomime chrm3 otch ivm.tst ivm.clk mmh2 clkh2 achf nopl spfp4 uam1 lsph nmim1 slnm2 crtt spfp misp spfp1 spfp2 clik2 clik3 spfp3 estr".split(" ");
F=a<d.length?d[a]:"othr";t.ue&&t.ue.event&&t.ue.event(X(F,c,b),"a9_tq","a9_tq.FraudMetrics.3")}function b(){var c=!1,m="",b=6,d=function(a,c){var f,m,b=!1;for(f in a)b=b||-1<c.indexOf(f);if("function"===typeof Object.getOwnPropertyNames)for(f=Object.getOwnPropertyNames(a),m=0;m<f.length;m++)b=b||-1<c.indexOf(f[m]);if("function"===typeof Object.keys)for(f=Object.keys(a),m=0;m<f.length;m++)b=b||-1<c.indexOf(f[m]);return b},k=function(a){try{return!!a.toString().match(/\{\s*\[native code\]\s*\}$/m)}catch(c){return!1}},
l=0;"undefined"!==typeof _evaluate&&-1<_evaluate.toString().indexOf("browser.runScript")&&l++;"undefined"!==typeof ArrayBuffer&&"undefined"!==typeof print&&k(ArrayBuffer)&&!k(print)&&l++;"undefined"!==typeof ABORT_ERR&&l++;try{"undefined"!==typeof browser&&"undefined"!==typeof browser._windowInScope&&"undefined"!==typeof browser._windowInScope._response&&l++}catch(Z){}3<=l&&(c=!0);k=[function(){if(!0===d(C,"__webdriver_evaluate __selenium_evaluate __fxdriver_evaluate __driver_evaluate __webdriver_unwrapped __selenium_unwrapped __fxdriver_unwrapped __driver_unwrapped __webdriver_script_function __webdriver_script_func __webdriver_script_fn webdriver _Selenium_IDE_Recorder _selenium calledSelenium $cdc_asdjflasutopfhvcZLmcfl_ $chrome_asyncScriptInfo __$webdriverAsyncExecutor".split(" ")))return!0;
var c=function(c){return c.match(/\$[a-z]dc_/)&&a.document[c]&&a.document[c].cache_},f;for(f in C)if(c(f))return m=f,!0;if("function"===typeof Object.getOwnPropertyNames)for(var b=Object.getOwnPropertyNames(C),l=0;l<b.length;l++)if(c(b[l]))return m=f,!0;return!1},function(){return d(a,"_phantom __nightmare _selenium callPhantom callSelenium _Selenium_IDE_Recorder webdriver __webdriverFunc domAutomation domAutomationController __lastWatirAlert __lastWatirConfirm __lastWatirPrompt _WEBDRIVER_ELEM_CACHE".split(" "))||
"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Promise||"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Array||"function"===typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Symbol?!0:!1},function(){return a.webdriver||a.document.webdriver||a.document.documentElement.hasAttribute("webdriver")||a.document.documentElement.hasAttribute("selenium")||a.document.documentElement.hasAttribute("driver")||navigator.webdriver||A(p,"navigator","webdriver")||"object"===typeof a.$cdc_asdjflasutopfhvcZLmcfl_||"object"===typeof a.document.$cdc_asdjflasutopfhvcZLmcfl_||
null!=a.name&&-1<a.name.indexOf("driver")?(m=null!=a.name?a.name:"",!0):!1},function(){return a.external&&"function"===typeof a.external.toString&&a.external.toString()&&-1!=a.external.toString().indexOf("Sequentum")?(m=a.external.toString(),!0):!1},function(){for(var c in a){var f;a:{if((f=c)&&33<=f.length&&"function"===typeof a[f]){var b=a[f];if(/\.*_Array$/.test(f)||/\.*_Promise$/.test(f)||/\.*_Symbol$/.test(f)||34===f.length&&"resolve"in b&&"reject"in b&&"prototype"in b||33===f.length&&"isConcatSpreadable"in
b&&"unscopables"in b&&"toStringTag"in b&&"match"in b){f=!0;break a}}f=!1}if(f)return m=c,!0}return!1},function(){var a=!1;if(!u.isFirefox())return!1;var c;c=navigator.userAgent.match(/(firefox(?=\/))\/?\s*(\d+)/i)||[];c=3<=c.length?c[2]:null;if(!c)return!1;60<=c&&void 0===navigator.webdriver?a=!0:60>c&&"webdriver"in navigator&&(a=!0);return a?(b=43,m=c.toString(),!0):!1}];for(l=0;l<k.length;l++)if(k[l].call()){c=!0;break}return{isSel:c,isTest:!1,info:m,headlessCode:b}}function d(a){var b=new Date;
!v(a,"Function","prototype","toString")&&W(b,"function","toLocaleString")&&(a=a.Function.prototype.toString.call(b.toLocaleString))&&100<a.length&&0<=a.indexOf("this.getTime")&&c(41)}function e(){var a="AddChannel AddDesktopComponent AddFavorite AddSearchProvider AddService AddToFavoritesBar AutoCompleteSaveForm AutoScan bubbleEvent ContentDiscoveryReset ImportExportFavorites InPrivateFilteringEnabled IsSearchProviderInstalled IsServiceInstalled IsSubscribed msActiveXFilteringEnabled msAddSiteMode msAddTrackingProtectionList msClearTile msEnableTileNotificationQueue msEnableTileNotificationQueueForSquare150x150 msEnableTileNotificationQueueForSquare310x310 msEnableTileNotificationQueueForWide310x150 msIsSiteMode msIsSiteModeFirstRun msPinnedSiteState msProvisionNetworks msRemoveScheduledTileNotification msReportSafeUrl msScheduledTileNotification msSiteModeActivate msSiteModeAddButtonStyle msSiteModeAddJumpListItem msSiteModeAddThumbBarButton msSiteModeClearBadge msSiteModeClearIconOverlay msSiteModeClearJumpList msSiteModeCreateJumpList msSiteModeRefreshBadge msSiteModeSetIconOverlay msSiteModeShowButtonStyle msSiteModeShowJumpList msSiteModeShowThumbBar msSiteModeUpdateThumbBarButton msStartPeriodicBadgeUpdate msStartPeriodicTileUpdate msStartPeriodicTileUpdateBatch msStopPeriodicBadgeUpdate msStopPeriodicTileUpdate msTrackingProtectionEnabled NavigateAndFind raiseEvent setContextMenu ShowBrowserUI menuArguments onvisibilitychange scrollbar selectableContent version visibility mssitepinned AddUrlAuthentication CloseRegPopup FeatureEnabled GetJsonWebData GetRegValue Log LogShellErrorsOnly OpenPopup ReadFile RunGutsScript SaveRegInfo SetAppMaximizeTimeToRestart SetAppMinimizeTimeToRestart SetAutoStart SetAutoStartMinimized SetMaxMemory ShareEventFromBrowser ShowPopup ShowRadar WriteFile WriteRegValue summonWalrus".split(" "),
b=-1,d,h;"Microsoft Internet Explorer"===navigator.appName?(d=navigator.userAgent,h=/MSIE ([0-9]{1,}[\.0-9]{0,})/,null!==h.exec(d)&&(b=parseFloat(RegExp.$1))):"Netscape"===navigator.appName&&(d=navigator.userAgent,h=/Trident\/.*rv:([0-9]{1,}[\.0-9]{0,})/,null!==h.exec(d)&&(b=parseFloat(RegExp.$1)));if(-1===b&&null===navigator.userAgent.match(/Windows Phone/)&&window.external){for(d=b=0;d<a.length;d++)if("unknown"===typeof window.external[a[d]]){b++;break}0<b&&c(17)}}function z(){var f=a.navigator.userAgent;
if(f&&!/8.0 Safari|iPhone|iPad/.test(f)){var b={clearInterval:42,clearTimeout:41,eval:33,alert:34,prompt:35,scroll:35},d={clearInterval:46,clearTimeout:45,eval:37,alert:38,prompt:39,scroll:39},h=0;if(/Chrome/.test(f))d=b;else if(b=/Firefox/.test(f),f=/Safari/.test(f),!b&&!f)return;if(Function.prototype&&Function.prototype.toString)for(var k in d)"function"===typeof window[k]&&(f=Function.prototype.toString.call(window[k]))&&f.length!==d[k]&&(h+=1);3<=h&&(6<=h?c(40,0,h.toString()):c(40,1,h.toString()))}}
function S(){var a=Math.random().toString(36).substr(2),b=null;U(function(d){try{var h=d.split(" ");if(null!==b&&h[0]===a&&0<h[1].length){var k=JSON.parse(h[1]);for(d=0;d<k.length;d++)1==d&&"R29vZ2xlIFN3aWZ0U2hhZGVy"==k[d]&&c(27)}}catch(l){}});b=J('(function fg45s() {                     var payload = [];                     var canvas = document.createElement("canvas");                     var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl") || canvas.getContext("moz-webgl");                     if (gl != null) {                         var debugInfo = gl.getExtension("WEBGL_debug_renderer_info");                         if (debugInfo != null) {                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL)));                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL)));                             parent.postMessage(window.frameElement.id + " " + JSON.stringify(payload), parent.location.origin);                         }                     }                 }             )();',
a);window.setTimeout(function(){try{b&&document.body&&b.parentNode===document.body&&document.body.removeChild(b),b=null}catch(a){n(a,"JS exception while removing iframe")}},5E3)}function L(){function b(){r(a,"mousemove",e);r(a,"click",d)}function d(){try{c(23),b(),r(a.document,l,h)}catch(m){n(m,"JS exception - detectClickDuringTabInactive")}}function e(){try{k||(k=!0,c(24),b(),r(a.document,l,h))}catch(d){n(d,"JS exception - detectMouseMovementsDuringTabInactive")}}function h(){try{var c;"undefined"!==
typeof document.hidden?c="hidden":"undefined"!==typeof document.mozHidden?c="mozHidden":"undefined"!==typeof document.msHidden?c="msHidden":"undefined"!==typeof document.webkitHidden&&(c="webkitHidden");!0!==document[c]===!1?(q(a,"mousemove",e,!1),q(a,"click",d,!1)):b()}catch(l){n(l,"JS exception - handleVisibilityChangeDuringTabInactive")}}var k=!1,l=H(a);T(a,h)}var M=function(){var a=window.navigator,c=a.vendor,b="undefined"!==typeof window.opr,d=-1<a.userAgent.indexOf("Edg"),a=/Chrome/.test(a.userAgent);
return/Google Inc\./.test(c)&&a&&!b&&!d},F=null,N=function(a){var b=[],d=(new Date).getTime(),h=!1,k=!1,l,e,D=function(){r(a,"mousemove",s);r(a,"click",g)},s=function(a){try{var f=(new Date).getTime();if(!(100>f-d)){b.push({x:a.clientX,y:a.clientY});if(50<b.length&&(b.shift(),!(50>b.length))){var l=b[0].x,g=b[49].x,k=b[0].y,h=b[49].y;a=h-k;for(var e=l-g,l=k*g-l*h,g=a/e*-1,s=b[49].ts-b[0].ts,k=!0,h=0;h<b.length;h++)if(0!=a*b[h].x+e*b[h].y+l){k=!1;break}!0==k&&(s={grdt:g,tmsp:s},D(),c(19,0,s))}d=f}}catch(B){n(B,
"JS exception - recordHoverPosition")}},g=function(a){try{var d=a.clientX,f=a.clientY,l={hcc:b.length,cx:d,cy:f};if(0===b.length)D(),c(18,0,l);else if(null!=d&&null!=f){var g;l.hpos=b;var k=b[b.length-1];g=Math.sqrt(Math.pow(d-k.x,2)+Math.pow(f-k.y,2));100<g&&(l.hcc=b.length,l.cx=d,l.cy=f,l.dhp=g,D(),c(15,0,l))}}catch(h){n(h,"JS exception - checkClick")}},B=function(c){try{l=c.clientX,e=c.clientY,h=!0,r(a,"mouseup",B)}catch(b){n(b,"JS exception - checkMouseUp")}},p=function(){try{k=!0,r(a,"mousedown",
p)}catch(c){n(c,"JS exception - checkMouseDown")}},t=function(b){try{h||k||c(49);var d=b.clientX-l,g=b.clientY-e;0<d&&1>d&&0<g&&1>g&&c(50,0,{xDiff:d,yDiff:g});r(a,"click",t)}catch(m){n(m,"JS exception - checkFirstClick")}};q(a,"mousemove",s,!1);q(a,"mouseup",B,!1);q(a,"mousedown",p,!1);q(a,"click",t,!1);q(a,"click",g,!1)},O=function(){if(u.isFirefox()){var a=0;void 0!==window.onstorage&&a++;var b=document.createElement("div");b.style.wordSpacing="22%";"22%"===b.style.wordSpacing&&a++;"function"===
typeof b.getAttributeNames&&a++;2<a&&(void 0===window.onabsolutedeviceorientation||void 0===navigator.permissions)&&c(37,0,a)}},w=function(){return null===navigator.userAgent.match(/(iPad|iPhone|iPod|android|webOS)/i)},G=function(a,b){var d=a&&a.navigator;!d||!w()||d.mimeTypes&&0!=d.mimeTypes.length||(x?c(b,0,"chrm"):u.isFirefox()&&c(b,0,"ff"))},R=function(){var a=function(a,c){for(var b,d="",f={},e={},s=0,g=0;g<c.length;g++)e[c[g]]=String.fromCharCode(126-g);var s=0,m;for(m in a)-1<c.indexOf(m)&&
(f[m]=1,s++);d=d+s+"!";if("function"===typeof Object.getOwnPropertyNames){b=Object.getOwnPropertyNames(a);for(g=s=0;g<b.length;g++)-1<c.indexOf(b[g])&&(f[b[g]]=1,s++);d=d+s+"!"}if("function"===typeof Object.keys){b=Object.keys(a);for(g=s=0;g<b.length;g++)-1<c.indexOf(b[g])&&(f[b[g]]=1,s++);d=d+s+"!"}if("prototype"in Object&&"hasOwnProperty"in Object.prototype)for(m in f)Object.prototype.hasOwnProperty.call(f,m)&&(d+=e[m]);else for(m in f)d+=e[m];return encodeURIComponent(d)},c=document.createElement("nadu"),
a={w:a(window,"SVGFESpotLightElement XMLHttpRequestEventTarget onratechange StereoPannerNode dolphinInfo VTTCue globalStorage WebKitCSSRegionRule MozSmsFilter MediaController mozInnerScreenX onwebkitwillrevealleft DOMMatrix GeckoActiveXObject MediaQueryListEvent PhoneNumberService ServiceWorkerContainer yandex vc2hxtaq9c NavigatorDeviceStorage HTMLHtmlElement ScreenOrientation MSGesture mozCancelRequestAnimationFrame GetSVGDocument MediaSource webkitMediaStream DeviceMotionEvent webkitPostMessage doNotTrack WebKitMediaKeyError HTMLCollection InstallTrigger StorageObsolete CustomEvent orientation XMLHttpRequest Worker showModelessDialog EventSource onmouseleave SVGAnimatedPathData TouchList TextTrackCue onanimationend HTMLBodyElement fluid MSFrameUITab Generator SecurityPolicyViolationEvent ClientRectList SmartCardEvent CSSSupportsRule mmbrowser".split(" ")),
c:a(c.style,"XvPhonemes MozTextAlignLast webkitFilter MozPerspective msTextSizeAdjust OAnimationFillMode borderImageSource MozOSXFontSmoothing border-inline-start-color MozOsxFontSmoothing columns touchAction scroll-snap-coordinate webkitAnimationFillMode webkitLineSnap webkitGridAutoColumns animationDuration isolation overflowWrap offsetRotation webkitShapeOutside MozOpacity position justifySelf borderRight webkitMatchNearestMailBlockquoteColor msImeAlign parentRule MozColumnFill cssText borderRightStyle textOverflow webkitGridRow webkitBackgroundComposite length -moz-column-fill enableBackground flex-basis".split(" "))};
t.ue&&t.ue.event&&(a={vfrd:"0",info:JSON.stringify(a)},t.ue.event({server:window.location.hostname,fmp:a},"a9_tq","a9_tq.FraudMetrics.3"))},P=function(){var b=function(a){try{return"function"!==typeof a||v(p,"Function","prototype","toString")?null:p.Function.prototype.toString.call(a)}catch(b){return null}},d=function(a,c){try{if("function"!==typeof Object.getOwnPropertyDescriptor)return null;var d=Object.getPrototypeOf(a);if(!d)return null;var e=Object.getOwnPropertyDescriptor(d,c);return e?b(e.get):
null}catch(g){return null}},e=function(a){var b=[28,161,141];!v(a,"getDetails","a")&&"s"===a.getDetails.a&&0<=b.indexOf(a.getDetails.l)&&c(45,0,k)},h=function(){(function(){if("function"===typeof Object.getOwnPropertyNames&&w()){var a=Object.getOwnPropertyNames(navigator);a&&1<a.length&&c(47,0,a.length.toString())}})();0<navigator.hardwareConcurrency&&!v(p,"navigator","hardwareConcurrency")&&p.navigator.hardwareConcurrency!==navigator.hardwareConcurrency&&c(48,0,p.navigator.hardwareConcurrency.toString());
(function(){var b=[];if(!v(p,"navigator")){p===a&&(b.push("iwin"),c(51,0,b));for(var d="platform vendor maxTouchPoints userAgent deviceMemory webdriver hardwareConcurrency appVersion mimeTypes plugins languages".split(" "),f=0;f<d.length;f++){var e=d[f],g;if("object"===typeof navigator[e]){g=navigator[e];var h=p.navigator[e],k=!1;g||h?(g&&h?g.length!==h.length?k=!0:0<g.length&&0<h.length&&"string"===typeof g[0]&&g[0]!==h[0]&&(k=!0):k=!0,g=k):g=!1}else g=navigator[e],h=p.navigator[e],g=g||h?g!==h?
!0:!1:!1;g&&b.push(e)}0<b.length&&(0<=b.indexOf("webdriver")?c(51,0,b):c(39,1,b))}})()},k=function(a){if(!a)return null;for(var c={},e=0,h=0,g=0;g<a.length;g++)for(var k=a[g].obj,n=a[g].props,r=0;r<n.length;r++){var p=n[r];c[p]={};var q=A(k,n[r]);if(null===q||void 0===q)h+=1,c[p].a="m",c[p].l=0;else if(q="function"===typeof q?b(q):d(k,p))q&&!/\[native code\]/.test(q)?(c[p].a="s",e+=1):c[p].a="p",c[p].l=q.length}return{sig:c,sCount:e,mCount:h}}([{obj:A(a,"chrome","app"),props:["getDetails","getIsInstalled",
"runningState"]},{obj:a.chrome,props:["csi","loadTimes","runtime"]},{obj:navigator,props:"platform vendor userAgent mimeTypes plugins webdriver languages".split(" ")}]);k&&(e(k.sig),x&&w()&&3<=k.mCount&&(6<=k.mCount?c(46,0,k):c(46,1,k)),h())},Q=function(){var b=a.Document&&a.Document.prototype.evaluate;b&&(a.Document.prototype.evaluate=function(){try{var d=Error("test error"),e=d.stack&&d.stack.toString();e&&e.match(/(puppeteer|phantomjs|apply.xpath)/)&&c(52,0,e);a.Document.prototype.evaluate=b;return b.apply(this,
arguments)}catch(h){return n(h,"JS exception while overidding evaluate"),a.Document.prototype.evaluate=b,b.apply(this,arguments)}})};try{v(navigator,"userAgent")&&c(20);var x=M(),y,p;(a.callPhantom||a._phantom||a.PhantomEmitter||a.__phantomas||/PhantomJS/.test(navigator.userAgent))&&c(5);a.Buffer&&c(12);a.emit&&c(13);a.spawn&&c(14);(null!=a.domAutomation||null!=a.domAutomationController||null!=a._WEBDRIVER_ELEM_CACHE||/HeadlessChrome/.test(navigator.userAgent)||""===navigator.languages)&&c(0);if(u.isChrome()&&
a.webkitRequestFileSystem)a.webkitRequestFileSystem(a.TEMPORARY,1,function(){},function(){c(0)});else if(u.isSafari()&&a.localStorage){try{a.localStorage.setItem("__nadu","")}catch($){c(3)}a.localStorage.removeItem("__nadu")}G(a,30);u.isWebkit()&&x&&w()&&(void 0===a.chrome&&c(0),a.chrome&&a.chrome.app&&!1!==a.chrome.app.isInstalled&&void 0!==navigator.languages&&c(31));a.external&&"function"===typeof a.external.toString&&a.external.toString()&&-1<a.external.toString().indexOf("RuntimeObject")&&c(8);
a.FirefoxInterfaces&&"function"===typeof a.FirefoxInterfaces&&a.FirefoxInterfaces("wdICoordinate","wdIMouse","wdIStatus")&&c(2);a.XPCOMUtils&&c(9);(a.Components&&(a.Components.interfaces&&a.Components.interfaces.nsICommandProcessor||a.Components.wdICoordinate||a.Components.wdIMouse||a.Components.wdIStatus||a.Components.classes)||a.netscape&&a.netscape.security&&a.netscape.security.privilegemanager)&&c(8);a.isExternalUrlSafeForNavigation&&c(1);!a.opera||null===a.opera._browserjsran||0!==a.opera._browserjsran&&
!1!==a.opera._browserjsran||c(4);a.screen&&(1>=a.screen.availHeight||1>=a.screen.availWidth||1>=a.screen.height||1>=a.screen.width||0>=a.screen.devicePixelRatio)&&c(10);var E=window.setInterval(function(){try{var a=b();a.isSel&&(c(a.headlessCode,!0===a.isTest?1:0,a.info),window.clearInterval(E),I(y))}catch(d){window.clearInterval(E),n(d,"JS exception - detectSelenium")}},1E3);window.setTimeout(function(){try{window.clearInterval(E),I(y)}catch(a){n(a,"JS exception - clearInterval for detectSelenium")}},
1E4);var K=a.PointerEvent;a.PointerEvent=function(){c(11);if(void 0!==K){var a=Array.prototype.slice.call(arguments);return new K(a)}return null};e();N(a);L();S();0!==a.outerHeight&&0!==a.outerWidth||c(29);O();!w()||navigator.plugins&&0!=navigator.plugins.length||(x?c(38,0,"chrm"):u.isFirefox()&&c(38,0,"ff"));V(R,10);x&&w()&&a.chrome&&!a.chrome.csi&&!a.chrome.loadTimes&&c(25);z();y=J(null,Math.random().toString(36).substr(2));p=v(y,"contentWindow")?a:y.contentWindow;d(p);G(p,42);0===A(navigator,"connection",
"rtt")&&c(44);P();Q()}catch(Y){n(Y,"JS exception - ")}})(z)})(ue_csm,window,document);



ue.exec(function(d,c){function g(e,c){e&&ue.tag(e+c);return!!e}function n(){for(var e=RegExp("^https://(.*\.(images|ssl-images|media)-amazon\.com|"+c.location.hostname+")/images/","i"),d={},h=0,k=c.performance.getEntriesByType("resource"),l=!1,b,a,m,f=0;f<k.length;f++)if(a=k[f],0<a.transferSize&&a.transferSize>=a.encodedBodySize&&(b=e.exec(String(a.name)))&&3===b.length){a:{b=a.serverTiming||[];for(a=0;a<b.length;a++)if("provider"===b[a].name){b=b[a].description;break a}b=void 0}b&&(l||(l=g(b,"_cdn_fr")),
a=d[b]=(d[b]||0)+1,a>h&&(m=b,h=a))}g(m,"_cdn_mp")}d.ue&&"function"===typeof d.ue.tag&&c.performance&&c.location&&n()},"cdnTagging")(ue_csm,window);


}
/* ◬ */
</script>

</div>

<noscript>
    <img height="1" width="1" style='display:none;visibility:hidden;' src='//fls-na.amazon.com/1/batch/1/OP/ATVPDKIKX0DER:130-0450696-1458362:Z0KMT1JTKBYN6W6QW6GJ$uedata=s:%2Frd%2Fuedata%3Fnoscript%26id%3DZ0KMT1JTKBYN6W6QW6GJ:0' alt=""/>
</noscript>

<script>window.ue && ue.count && ue.count('CSMLibrarySize', 81686)</script>
</div><div id="a-popover-root" style="z-index:-1;position:absolute;"></div>
<!--       _
       .__(.)< (MEOW)
        \___)   
 ~~~~~~~~~~~~~~~~~~-->
<!-- sp:eh:3LfAzZ8CHs6wL8V/uy7AguBi0v1zE4MQ8gij++jFDN65J1TEOkEnlQM8IgugX5IJzb9lDiPbdtyrYR3OOSK3F97XVBIF6wypnXN0WSJ+9ep+ZtjL4OaiADQXMqQ= -->
</body></html>"""