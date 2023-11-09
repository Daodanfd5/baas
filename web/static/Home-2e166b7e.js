import{c as O,u as z,L as we,p as Pe,N as Ne,h as ke,o as At,q as He,r as Rt,O as Ue,P as $t,Q as Bt,s as We,R as Tt,d as ge,t as Lt,S as Mt,w as Ft,T as Nt,x as Ge,y as qe,z as Et,U as Ye,W as Ot,X as Dt,A as Je,Y as zt,Z as jt,_ as Ke,$ as Ht,a0 as Xe,l as Ut,H as fe,G as L,a1 as Qe,a2 as Ze,M as et,a3 as Wt,v as Gt,j as tt,a4 as qt,a5 as Yt,a6 as Jt,a7 as at,a as Kt,a8 as Xt,a9 as Qt}from"./VListItem-57b736b8.js";import{g as N,n as Zt,c as i,p as M,I as G,i as Ae,j as nt,f as c,h as ne,U as lt,z as j,J as Q,m as ae,s as le,r as U,V as Re,E as ea,W as ta,X as pe,B as aa,t as st,G as Ie,k as X,y as me,Y as na,d as ye,o as Y,a as J,w as A,O as ve,D as $e,Z as he,_ as Be,$ as it,v as rt,a0 as la,a1 as ut,F as Te,a2 as Z,a3 as Le,a4 as sa,x as ia,a5 as ce,a6 as ra,N as ee,H as ua,A as ot,K as de,a7 as oa,a8 as ca,a9 as da,Q as fa,L as va,R as ga}from"./index-41454736.js";class _e{constructor(s){let{x:l,y:t,width:n,height:a}=s;this.x=l,this.y=t,this.width=n,this.height=a}get top(){return this.y}get bottom(){return this.y+this.height}get left(){return this.x}get right(){return this.x+this.width}}function ma(e){const s=e.getBoundingClientRect(),l=getComputedStyle(e),t=l.transform;if(t){let n,a,r,u,o;if(t.startsWith("matrix3d("))n=t.slice(9,-1).split(/, /),a=+n[0],r=+n[5],u=+n[12],o=+n[13];else if(t.startsWith("matrix("))n=t.slice(7,-1).split(/, /),a=+n[0],r=+n[3],u=+n[4],o=+n[5];else return new _e(s);const v=l.transformOrigin,m=s.x-u-(1-a)*parseFloat(v),V=s.y-o-(1-r)*parseFloat(v.slice(v.indexOf(" ")+1)),g=a?s.width/a:e.offsetWidth+1,_=r?s.height/r:e.offsetHeight+1;return new _e({x:m,y:V,width:g,height:_})}else return new _e(s)}function ya(e,s,l){if(typeof e.animate>"u")return{finished:Promise.resolve()};let t;try{t=e.animate(s,l)}catch{return{finished:Promise.resolve()}}return typeof t.finished>"u"&&(t.finished=new Promise(n=>{t.onfinish=()=>{n(t)}})),t}const ha="cubic-bezier(0.4, 0, 0.2, 1)";function ba(e){let s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:!1;for(;e;){if(s?_a(e):Va(e))return e;e=e.parentElement}return document.scrollingElement}function Va(e){if(!e||e.nodeType!==Node.ELEMENT_NODE)return!1;const s=window.getComputedStyle(e);return s.overflowY==="scroll"||s.overflowY==="auto"&&e.scrollHeight>e.clientHeight}function _a(e){if(!e||e.nodeType!==Node.ELEMENT_NODE)return!1;const s=window.getComputedStyle(e);return["scroll","auto"].includes(s.overflowY)}const Ca=N()({name:"VCardActions",props:O(),setup(e,s){let{slots:l}=s;return Zt({VBtn:{variant:"text"}}),z(()=>{var t;return i("div",{class:["v-card-actions",e.class],style:e.style},[(t=l.default)==null?void 0:t.call(l)])}),{}}}),xa=we("v-card-subtitle"),Sa=we("v-card-title"),ka=M({appendAvatar:String,appendIcon:G,prependAvatar:String,prependIcon:G,subtitle:String,title:String,...O(),...Pe()},"VCardItem"),pa=N()({name:"VCardItem",props:ka(),setup(e,s){let{slots:l}=s;return z(()=>{var v;const t=!!(e.prependAvatar||e.prependIcon),n=!!(t||l.prepend),a=!!(e.appendAvatar||e.appendIcon),r=!!(a||l.append),u=!!(e.title||l.title),o=!!(e.subtitle||l.subtitle);return i("div",{class:["v-card-item",e.class],style:e.style},[n&&i("div",{key:"prepend",class:"v-card-item__prepend"},[l.prepend?i(ke,{key:"prepend-defaults",disabled:!t,defaults:{VAvatar:{density:e.density,icon:e.prependIcon,image:e.prependAvatar}}},l.prepend):t&&i(Ne,{key:"prepend-avatar",density:e.density,icon:e.prependIcon,image:e.prependAvatar},null)]),i("div",{class:"v-card-item__content"},[u&&i(Sa,{key:"title"},{default:()=>{var m;return[((m=l.title)==null?void 0:m.call(l))??e.title]}}),o&&i(xa,{key:"subtitle"},{default:()=>{var m;return[((m=l.subtitle)==null?void 0:m.call(l))??e.subtitle]}}),(v=l.default)==null?void 0:v.call(l)]),r&&i("div",{key:"append",class:"v-card-item__append"},[l.append?i(ke,{key:"append-defaults",disabled:!a,defaults:{VAvatar:{density:e.density,icon:e.appendIcon,image:e.appendAvatar}}},l.append):a&&i(Ne,{key:"append-avatar",density:e.density,icon:e.appendIcon,image:e.appendAvatar},null)])])}),{}}}),Ia=we("v-card-text"),wa=M({appendAvatar:String,appendIcon:G,disabled:Boolean,flat:Boolean,hover:Boolean,image:String,link:{type:Boolean,default:void 0},prependAvatar:String,prependIcon:G,ripple:{type:[Boolean,Object],default:!0},subtitle:String,text:String,title:String,...At(),...O(),...Pe(),...He(),...Rt(),...Ue(),...$t(),...Bt(),...We(),...Tt(),...ge(),...Ae(),...Lt({variant:"elevated"})},"VCard"),ct=N()({name:"VCard",directives:{Ripple:Mt},props:wa(),setup(e,s){let{attrs:l,slots:t}=s;const{themeClasses:n}=nt(e),{borderClasses:a}=Ft(e),{colorClasses:r,colorStyles:u,variantClasses:o}=Nt(e),{densityClasses:v}=Ge(e),{dimensionStyles:m}=qe(e),{elevationClasses:V}=Et(e),{loaderClasses:g}=Ye(e),{locationStyles:_}=Ot(e),{positionClasses:x}=Dt(e),{roundedClasses:w}=Je(e),B=zt(e,l),R=c(()=>e.link!==!1&&B.isLink.value),T=c(()=>!e.disabled&&e.link!==!1&&(e.link||B.isClickable.value));return z(()=>{const $=R.value?"a":e.tag,y=!!(t.title||e.title),k=!!(t.subtitle||e.subtitle),p=y||k,h=!!(t.append||e.appendAvatar||e.appendIcon),d=!!(t.prepend||e.prependAvatar||e.prependIcon),C=!!(t.image||e.image),S=p||d||h,f=!!(t.text||e.text);return ne(i($,{class:["v-card",{"v-card--disabled":e.disabled,"v-card--flat":e.flat,"v-card--hover":e.hover&&!(e.disabled||e.flat),"v-card--link":T.value},n.value,a.value,r.value,v.value,V.value,g.value,x.value,w.value,o.value,e.class],style:[u.value,m.value,_.value,e.style],href:B.href.value,onClick:T.value&&B.navigate,tabindex:e.disabled?-1:void 0},{default:()=>{var I;return[C&&i("div",{key:"image",class:"v-card__image"},[t.image?i(ke,{key:"image-defaults",disabled:!e.image,defaults:{VImg:{cover:!0,src:e.image}}},t.image):i(jt,{key:"image-img",cover:!0,src:e.image},null)]),i(Ke,{name:"v-card",active:!!e.loading,color:typeof e.loading=="boolean"?void 0:e.loading},{default:t.loader}),S&&i(pa,{key:"item",prependAvatar:e.prependAvatar,prependIcon:e.prependIcon,title:e.title,subtitle:e.subtitle,appendAvatar:e.appendAvatar,appendIcon:e.appendIcon},{default:t.item,prepend:t.prepend,title:t.title,subtitle:t.subtitle,append:t.append}),f&&i(Ia,{key:"text"},{default:()=>{var b;return[((b=t.text)==null?void 0:b.call(t))??e.text]}}),(I=t.default)==null?void 0:I.call(t),t.actions&&i(Ca,null,{default:t.actions}),Ht(T.value,"v-card")]}}),[[lt("ripple"),T.value&&e.ripple]])}),{}}});const Pa=M({renderless:Boolean,...O()},"VVirtualScrollItem"),Aa=N()({name:"VVirtualScrollItem",inheritAttrs:!1,props:Pa(),emits:{"update:height":e=>!0},setup(e,s){let{attrs:l,emit:t,slots:n}=s;const{resizeRef:a,contentRect:r}=Xe(void 0,"border");j(()=>{var u;return(u=r.value)==null?void 0:u.height},u=>{u!=null&&t("update:height",u)}),z(()=>{var u,o;return e.renderless?i(Q,null,[(u=n.default)==null?void 0:u.call(n,{itemRef:a})]):i("div",ae({ref:a,class:["v-virtual-scroll__item",e.class],style:e.style},l),[(o=n.default)==null?void 0:o.call(n)])})}}),Ee=-1,Oe=1,Ra=M({itemHeight:{type:[Number,String],default:48}},"virtual");function $a(e,s,l){const t=le(0),n=le(e.itemHeight),a=c({get:()=>parseInt(n.value??0,10),set(h){n.value=h}}),r=U(),{resizeRef:u,contentRect:o}=Xe();Re(()=>{u.value=r.value});const v=ea(),m=new Map;let V=Array.from({length:s.value.length});const g=c(()=>{const h=(!o.value||r.value===document.documentElement?v.height.value:o.value.height)-((l==null?void 0:l.value)??0);return Math.ceil(h/a.value*1.7+1)});function _(h,d){a.value=Math.max(a.value,d),V[h]=d,m.set(s.value[h],d)}function x(h){return V.slice(0,h).reduce((d,C)=>d+(C||a.value),0)}function w(h){const d=s.value.length;let C=0,S=0;for(;S<h&&C<d;)S+=V[C++]||a.value;return C-1}let B=0;function R(){if(!r.value||!o.value)return;const h=o.value.height-56,d=r.value.scrollTop,C=d<B?Ee:Oe,S=w(d+h/2),f=Math.round(g.value/3),I=S-f,b=t.value+f*2-1;C===Ee&&S<=b?t.value=pe(I,0,s.value.length):C===Oe&&S>=b&&(t.value=pe(I,0,s.value.length-g.value)),B=d}function T(h){if(!r.value)return;const d=x(h);r.value.scrollTop=d}const $=c(()=>Math.min(s.value.length,t.value+g.value)),y=c(()=>s.value.slice(t.value,$.value).map((h,d)=>({raw:h,index:d+t.value}))),k=c(()=>x(t.value)),p=c(()=>x(s.value.length)-x($.value));return j(()=>s.value.length,()=>{V=ta(s.value.length).map(()=>a.value),m.forEach((h,d)=>{const C=s.value.indexOf(d);C===-1?m.delete(d):V[C]=h})}),{containerRef:r,computedItems:y,itemHeight:a,paddingTop:k,paddingBottom:p,scrollToIndex:T,handleScroll:R,handleItemResize:_}}const Ba=M({items:{type:Array,default:()=>[]},renderless:Boolean,...Ra(),...O(),...He()},"VVirtualScroll"),Ta=N()({name:"VVirtualScroll",props:Ba(),setup(e,s){let{slots:l}=s;const t=aa("VVirtualScroll"),{dimensionStyles:n}=qe(e),{containerRef:a,handleScroll:r,handleItemResize:u,scrollToIndex:o,paddingTop:v,paddingBottom:m,computedItems:V}=$a(e,st(e,"items"));return Ie(()=>e.renderless,()=>{me(()=>{var g;a.value=ba(t.vnode.el,!0),(g=a.value)==null||g.addEventListener("scroll",r)}),na(()=>{var g;(g=a.value)==null||g.removeEventListener("scroll",r)})}),z(()=>{const g=V.value.map(_=>i(Aa,{key:_.index,renderless:e.renderless,"onUpdate:height":x=>u(_.index,x)},{default:x=>{var w;return(w=l.default)==null?void 0:w.call(l,{item:_.raw,index:_.index,...x})}}));return e.renderless?i(Q,null,[i("div",{class:"v-virtual-scroll__spacer",style:{paddingTop:X(v.value)}},null),g,i("div",{class:"v-virtual-scroll__spacer",style:{paddingBottom:X(m.value)}},null)]):i("div",{ref:a,class:["v-virtual-scroll",e.class],onScroll:r,style:[n.value,e.style]},[i("div",{class:"v-virtual-scroll__container",style:{paddingTop:X(v.value),paddingBottom:X(m.value)}},[g])])}),{scrollToIndex:o}}}),ue=ye({__name:"TaskCard",props:{title:{},tasks:{}},setup(e){const s=e,l=async t=>{await L.selectConfig(t)};return(t,n)=>(Y(),J(ct,{title:s.title},{default:A(()=>[i(Ta,{items:s.tasks,height:"300"},{default:A(({item:a})=>[i(Ut,{title:a.text,subtitle:a.next},{append:A(()=>[i(fe,{class:"ml-auto",onClick:r=>l(a.task)},{default:A(()=>[ve("设置")]),_:2},1032,["onClick"])]),_:2},1032,["title","subtitle"])]),_:1},8,["items"])]),_:1},8,["title"]))}});const La=M({fluid:{type:Boolean,default:!1},...O(),...ge()},"VContainer"),dt=N()({name:"VContainer",props:La(),setup(e,s){let{slots:l}=s;const{rtlClasses:t}=$e();return z(()=>i(e.tag,{class:["v-container",{"v-container--fluid":e.fluid},t.value,e.class],style:e.style},l)),{}}}),ft=(()=>he.reduce((e,s)=>(e[s]={type:[Boolean,String,Number],default:!1},e),{}))(),vt=(()=>he.reduce((e,s)=>{const l="offset"+Be(s);return e[l]={type:[String,Number],default:null},e},{}))(),gt=(()=>he.reduce((e,s)=>{const l="order"+Be(s);return e[l]={type:[String,Number],default:null},e},{}))(),De={col:Object.keys(ft),offset:Object.keys(vt),order:Object.keys(gt)};function Ma(e,s,l){let t=e;if(!(l==null||l===!1)){if(s){const n=s.replace(e,"");t+=`-${n}`}return e==="col"&&(t="v-"+t),e==="col"&&(l===""||l===!0)||(t+=`-${l}`),t.toLowerCase()}}const Fa=["auto","start","end","center","baseline","stretch"],Na=M({cols:{type:[Boolean,String,Number],default:!1},...ft,offset:{type:[String,Number],default:null},...vt,order:{type:[String,Number],default:null},...gt,alignSelf:{type:String,default:null,validator:e=>Fa.includes(e)},...O(),...ge()},"VCol"),te=N()({name:"VCol",props:Na(),setup(e,s){let{slots:l}=s;const t=c(()=>{const n=[];let a;for(a in De)De[a].forEach(u=>{const o=e[u],v=Ma(a,u,o);v&&n.push(v)});const r=n.some(u=>u.startsWith("v-col-"));return n.push({"v-col":!r||!e.cols,[`v-col-${e.cols}`]:e.cols,[`offset-${e.offset}`]:e.offset,[`order-${e.order}`]:e.order,[`align-self-${e.alignSelf}`]:e.alignSelf}),n});return()=>{var n;return it(e.tag,{class:[t.value,e.class],style:e.style},(n=l.default)==null?void 0:n.call(l))}}}),Me=["start","end","center"],mt=["space-between","space-around","space-evenly"];function Fe(e,s){return he.reduce((l,t)=>{const n=e+Be(t);return l[n]=s(),l},{})}const Ea=[...Me,"baseline","stretch"],yt=e=>Ea.includes(e),ht=Fe("align",()=>({type:String,default:null,validator:yt})),Oa=[...Me,...mt],bt=e=>Oa.includes(e),Vt=Fe("justify",()=>({type:String,default:null,validator:bt})),Da=[...Me,...mt,"stretch"],_t=e=>Da.includes(e),Ct=Fe("alignContent",()=>({type:String,default:null,validator:_t})),ze={align:Object.keys(ht),justify:Object.keys(Vt),alignContent:Object.keys(Ct)},za={align:"align",justify:"justify",alignContent:"align-content"};function ja(e,s,l){let t=za[e];if(l!=null){if(s){const n=s.replace(e,"");t+=`-${n}`}return t+=`-${l}`,t.toLowerCase()}}const Ha=M({dense:Boolean,noGutters:Boolean,align:{type:String,default:null,validator:yt},...ht,justify:{type:String,default:null,validator:bt},...Vt,alignContent:{type:String,default:null,validator:_t},...Ct,...O(),...ge()},"VRow"),Ce=N()({name:"VRow",props:Ha(),setup(e,s){let{slots:l}=s;const t=c(()=>{const n=[];let a;for(a in ze)ze[a].forEach(r=>{const u=e[r],o=ja(a,r,u);o&&n.push(o)});return n.push({"v-row--no-gutters":e.noGutters,"v-row--dense":e.dense,[`align-${e.align}`]:e.align,[`justify-${e.justify}`]:e.justify,[`align-content-${e.alignContent}`]:e.alignContent}),n});return()=>{var n;return it(e.tag,{class:["v-row",t.value,e.class],style:e.style},(n=l.default)==null?void 0:n.call(l))}}});const Ua=M({active:Boolean,max:[Number,String],value:{type:[Number,String],default:0},...O(),...Qe({transition:{component:Ze}})},"VCounter"),Wa=N()({name:"VCounter",functional:!0,props:Ua(),setup(e,s){let{slots:l}=s;const t=c(()=>e.max?`${e.value} / ${e.max}`:String(e.value));return z(()=>i(et,{transition:e.transition},{default:()=>[ne(i("div",{class:["v-counter",e.class],style:e.style},[l.default?l.default({counter:t.value,max:e.max,value:e.value}):t.value]),[[rt,e.active]])]})),{}}});const Ga=M({text:String,clickable:Boolean,...O(),...Ae()},"VLabel"),qa=N()({name:"VLabel",props:Ga(),setup(e,s){let{slots:l}=s;return z(()=>{var t;return i("label",{class:["v-label",{"v-label--clickable":e.clickable},e.class],style:e.style},[e.text,(t=l.default)==null?void 0:t.call(l)])}),{}}}),Ya=M({floating:Boolean,...O()},"VFieldLabel"),oe=N()({name:"VFieldLabel",props:Ya(),setup(e,s){let{slots:l}=s;return z(()=>i(qa,{class:["v-field-label",{"v-field-label--floating":e.floating},e.class],style:e.style,"aria-hidden":e.floating||void 0},l)),{}}});function xt(e){const{t:s}=la();function l(t){let{name:n}=t;const a={prepend:"prependAction",prependInner:"prependAction",append:"appendAction",appendInner:"appendAction",clear:"clear"}[n],r=e[`onClick:${n}`],u=r&&a?s(`$vuetify.input.${a}`,e.label??""):void 0;return i(Wt,{icon:e[`${n}Icon`],"aria-label":u,onClick:r},null)}return{InputIcon:l}}const St=M({focused:Boolean,"onUpdate:focused":Z()},"focus");function kt(e){let s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:ut();const l=Te(e,"focused"),t=c(()=>({[`${s}--focused`]:l.value}));function n(){l.value=!0}function a(){l.value=!1}return{focusClasses:t,isFocused:l,focus:n,blur:a}}const Ja=["underlined","outlined","filled","solo","solo-inverted","solo-filled","plain"],pt=M({appendInnerIcon:G,bgColor:String,clearable:Boolean,clearIcon:{type:G,default:"$clear"},active:Boolean,centerAffix:{type:Boolean,default:void 0},color:String,baseColor:String,dirty:Boolean,disabled:{type:Boolean,default:null},error:Boolean,flat:Boolean,label:String,persistentClear:Boolean,prependInnerIcon:G,reverse:Boolean,singleLine:Boolean,variant:{type:String,default:"filled",validator:e=>Ja.includes(e)},"onClick:clear":Z(),"onClick:appendInner":Z(),"onClick:prependInner":Z(),...O(),...Ue(),...We(),...Ae()},"VField"),It=N()({name:"VField",inheritAttrs:!1,props:{id:String,...St(),...pt()},emits:{"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,s){let{attrs:l,emit:t,slots:n}=s;const{themeClasses:a}=nt(e),{loaderClasses:r}=Ye(e),{focusClasses:u,isFocused:o,focus:v,blur:m}=kt(e),{InputIcon:V}=xt(e),{roundedClasses:g}=Je(e),{rtlClasses:_}=$e(),x=c(()=>e.dirty||e.active),w=c(()=>!e.singleLine&&!!(e.label||n.label)),B=Le(),R=c(()=>e.id||`input-${B}`),T=c(()=>`${R.value}-messages`),$=U(),y=U(),k=U(),p=c(()=>["plain","underlined"].includes(e.variant)),{backgroundColorClasses:h,backgroundColorStyles:d}=Gt(st(e,"bgColor")),{textColorClasses:C,textColorStyles:S}=tt(c(()=>e.error||e.disabled?void 0:x.value&&o.value?e.color:e.baseColor));j(x,b=>{if(w.value){const P=$.value.$el,F=y.value.$el;requestAnimationFrame(()=>{const H=ma(P),E=F.getBoundingClientRect(),D=E.x-H.x,W=E.y-H.y-(H.height/2-E.height/2),q=E.width/.75,K=Math.abs(q-H.width)>1?{maxWidth:X(q)}:void 0,be=getComputedStyle(P),se=getComputedStyle(F),ie=parseFloat(be.transitionDuration)*1e3||150,re=parseFloat(se.getPropertyValue("--v-field-label-scale")),Ve=se.getPropertyValue("color");P.style.visibility="visible",F.style.visibility="hidden",ya(P,{transform:`translate(${D}px, ${W}px) scale(${re})`,color:Ve,...K},{duration:ie,easing:ha,direction:b?"normal":"reverse"}).finished.then(()=>{P.style.removeProperty("visibility"),F.style.removeProperty("visibility")})})}},{flush:"post"});const f=c(()=>({isActive:x,isFocused:o,controlRef:k,blur:m,focus:v}));function I(b){b.target!==document.activeElement&&b.preventDefault()}return z(()=>{var D,W,q;const b=e.variant==="outlined",P=n["prepend-inner"]||e.prependInnerIcon,F=!!(e.clearable||n.clear),H=!!(n["append-inner"]||e.appendInnerIcon||F),E=n.label?n.label({...f.value,label:e.label,props:{for:R.value}}):e.label;return i("div",ae({class:["v-field",{"v-field--active":x.value,"v-field--appended":H,"v-field--center-affix":e.centerAffix??!p.value,"v-field--disabled":e.disabled,"v-field--dirty":e.dirty,"v-field--error":e.error,"v-field--flat":e.flat,"v-field--has-background":!!e.bgColor,"v-field--persistent-clear":e.persistentClear,"v-field--prepended":P,"v-field--reverse":e.reverse,"v-field--single-line":e.singleLine,"v-field--no-label":!E,[`v-field--variant-${e.variant}`]:!0},a.value,h.value,u.value,r.value,g.value,_.value,e.class],style:[d.value,e.style],onClick:I},l),[i("div",{class:"v-field__overlay"},null),i(Ke,{name:"v-field",active:!!e.loading,color:e.error?"error":typeof e.loading=="string"?e.loading:e.color},{default:n.loader}),P&&i("div",{key:"prepend",class:"v-field__prepend-inner"},[e.prependInnerIcon&&i(V,{key:"prepend-icon",name:"prependInner"},null),(D=n["prepend-inner"])==null?void 0:D.call(n,f.value)]),i("div",{class:"v-field__field","data-no-activator":""},[["filled","solo","solo-inverted","solo-filled"].includes(e.variant)&&w.value&&i(oe,{key:"floating-label",ref:y,class:[C.value],floating:!0,for:R.value,style:S.value},{default:()=>[E]}),i(oe,{ref:$,for:R.value},{default:()=>[E]}),(W=n.default)==null?void 0:W.call(n,{...f.value,props:{id:R.value,class:"v-field__input","aria-describedby":T.value},focus:v,blur:m})]),F&&i(qt,{key:"clear"},{default:()=>[ne(i("div",{class:"v-field__clearable",onMousedown:K=>{K.preventDefault(),K.stopPropagation()}},[n.clear?n.clear():i(V,{name:"clear"},null)]),[[rt,e.dirty]])]}),H&&i("div",{key:"append",class:"v-field__append-inner"},[(q=n["append-inner"])==null?void 0:q.call(n,f.value),e.appendInnerIcon&&i(V,{key:"append-icon",name:"appendInner"},null)]),i("div",{class:["v-field__outline",C.value],style:S.value},[b&&i(Q,null,[i("div",{class:"v-field__outline__start"},null),w.value&&i("div",{class:"v-field__outline__notch"},[i(oe,{ref:y,floating:!0,for:R.value},{default:()=>[E]})]),i("div",{class:"v-field__outline__end"},null)]),p.value&&w.value&&i(oe,{ref:y,floating:!0,for:R.value},{default:()=>[E]})])])}),{controlRef:k}}});function Ka(e){const s=Object.keys(It.props).filter(l=>!sa(l)&&l!=="class"&&l!=="style");return ia(e,s)}const Xa=M({active:Boolean,color:String,messages:{type:[Array,String],default:()=>[]},...O(),...Qe({transition:{component:Ze,leaveAbsolute:!0,group:!0}})},"VMessages"),Qa=N()({name:"VMessages",props:Xa(),setup(e,s){let{slots:l}=s;const t=c(()=>ce(e.messages)),{textColorClasses:n,textColorStyles:a}=tt(c(()=>e.color));return z(()=>i(et,{transition:e.transition,tag:"div",class:["v-messages",n.value,e.class],style:[a.value,e.style],role:"alert","aria-live":"polite"},{default:()=>[e.active&&t.value.map((r,u)=>i("div",{class:"v-messages__message",key:`${u}-${t.value}`},[l.message?l.message({message:r}):r]))]})),{}}}),Za=Symbol.for("vuetify:form");function en(){return ra(Za,null)}const tn=M({disabled:{type:Boolean,default:null},error:Boolean,errorMessages:{type:[Array,String],default:()=>[]},maxErrors:{type:[Number,String],default:1},name:String,label:String,readonly:{type:Boolean,default:null},rules:{type:Array,default:()=>[]},modelValue:null,validateOn:String,validationValue:null,...St()},"validation");function an(e){let s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:ut(),l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:Le();const t=Te(e,"modelValue"),n=c(()=>e.validationValue===void 0?t.value:e.validationValue),a=en(),r=U([]),u=le(!0),o=c(()=>!!(ce(t.value===""?null:t.value).length||ce(n.value===""?null:n.value).length)),v=c(()=>!!(e.disabled??(a==null?void 0:a.isDisabled.value))),m=c(()=>!!(e.readonly??(a==null?void 0:a.isReadonly.value))),V=c(()=>{var y;return(y=e.errorMessages)!=null&&y.length?ce(e.errorMessages).slice(0,Math.max(0,+e.maxErrors)):r.value}),g=c(()=>{let y=(e.validateOn??(a==null?void 0:a.validateOn.value))||"input";y==="lazy"&&(y="input lazy");const k=new Set((y==null?void 0:y.split(" "))??[]);return{blur:k.has("blur")||k.has("input"),input:k.has("input"),submit:k.has("submit"),lazy:k.has("lazy")}}),_=c(()=>{var y;return e.error||(y=e.errorMessages)!=null&&y.length?!1:e.rules.length?u.value?r.value.length||g.value.lazy?null:!0:!r.value.length:!0}),x=le(!1),w=c(()=>({[`${s}--error`]:_.value===!1,[`${s}--dirty`]:o.value,[`${s}--disabled`]:v.value,[`${s}--readonly`]:m.value})),B=c(()=>e.name??ee(l));ua(()=>{a==null||a.register({id:B.value,validate:$,reset:R,resetValidation:T})}),ot(()=>{a==null||a.unregister(B.value)}),me(async()=>{g.value.lazy||await $(!0),a==null||a.update(B.value,_.value,V.value)}),Ie(()=>g.value.input,()=>{j(n,()=>{if(n.value!=null)$();else if(e.focused){const y=j(()=>e.focused,k=>{k||$(),y()})}})}),Ie(()=>g.value.blur,()=>{j(()=>e.focused,y=>{y||$()})}),j(_,()=>{a==null||a.update(B.value,_.value,V.value)});function R(){t.value=null,de(T)}function T(){u.value=!0,g.value.lazy?r.value=[]:$(!0)}async function $(){let y=arguments.length>0&&arguments[0]!==void 0?arguments[0]:!1;const k=[];x.value=!0;for(const p of e.rules){if(k.length>=+(e.maxErrors??1))break;const d=await(typeof p=="function"?p:()=>p)(n.value);if(d!==!0){if(d!==!1&&typeof d!="string"){console.warn(`${d} is not a valid value. Rule functions must return boolean true or a string.`);continue}k.push(d||"")}}return r.value=k,x.value=!1,u.value=y,r.value}return{errorMessages:V,isDirty:o,isDisabled:v,isReadonly:m,isPristine:u,isValid:_,isValidating:x,reset:R,resetValidation:T,validate:$,validationClasses:w}}const wt=M({id:String,appendIcon:G,centerAffix:{type:Boolean,default:!0},prependIcon:G,hideDetails:[Boolean,String],hint:String,persistentHint:Boolean,messages:{type:[Array,String],default:()=>[]},direction:{type:String,default:"horizontal",validator:e=>["horizontal","vertical"].includes(e)},"onClick:prepend":Z(),"onClick:append":Z(),...O(),...Pe(),...tn()},"VInput"),je=N()({name:"VInput",props:{...wt()},emits:{"update:modelValue":e=>!0},setup(e,s){let{attrs:l,slots:t,emit:n}=s;const{densityClasses:a}=Ge(e),{rtlClasses:r}=$e(),{InputIcon:u}=xt(e),o=Le(),v=c(()=>e.id||`input-${o}`),m=c(()=>`${v.value}-messages`),{errorMessages:V,isDirty:g,isDisabled:_,isReadonly:x,isPristine:w,isValid:B,isValidating:R,reset:T,resetValidation:$,validate:y,validationClasses:k}=an(e,"v-input",v),p=c(()=>({id:v,messagesId:m,isDirty:g,isDisabled:_,isReadonly:x,isPristine:w,isValid:B,isValidating:R,reset:T,resetValidation:$,validate:y})),h=c(()=>{var d;return(d=e.errorMessages)!=null&&d.length||!w.value&&V.value.length?V.value:e.hint&&(e.persistentHint||e.focused)?e.hint:e.messages});return z(()=>{var I,b,P,F;const d=!!(t.prepend||e.prependIcon),C=!!(t.append||e.appendIcon),S=h.value.length>0,f=!e.hideDetails||e.hideDetails==="auto"&&(S||!!t.details);return i("div",{class:["v-input",`v-input--${e.direction}`,{"v-input--center-affix":e.centerAffix},a.value,r.value,k.value,e.class],style:e.style},[d&&i("div",{key:"prepend",class:"v-input__prepend"},[(I=t.prepend)==null?void 0:I.call(t,p.value),e.prependIcon&&i(u,{key:"prepend-icon",name:"prepend"},null)]),t.default&&i("div",{class:"v-input__control"},[(b=t.default)==null?void 0:b.call(t,p.value)]),C&&i("div",{key:"append",class:"v-input__append"},[e.appendIcon&&i(u,{key:"append-icon",name:"append"},null),(P=t.append)==null?void 0:P.call(t,p.value)]),f&&i("div",{class:"v-input__details"},[i(Qa,{id:m.value,active:S,messages:h.value},{message:t.message}),(F=t.details)==null?void 0:F.call(t,p.value)])])}),{reset:T,resetValidation:$,validate:y}}}),xe=Symbol("Forwarded refs");function Se(e,s){let l=e;for(;l;){const t=Reflect.getOwnPropertyDescriptor(l,s);if(t)return t;l=Object.getPrototypeOf(l)}}function nn(e){for(var s=arguments.length,l=new Array(s>1?s-1:0),t=1;t<s;t++)l[t-1]=arguments[t];return e[xe]=l,new Proxy(e,{get(n,a){if(Reflect.has(n,a))return Reflect.get(n,a);if(!(typeof a=="symbol"||a.startsWith("$")||a.startsWith("__"))){for(const r of l)if(r.value&&Reflect.has(r.value,a)){const u=Reflect.get(r.value,a);return typeof u=="function"?u.bind(r.value):u}}},has(n,a){if(Reflect.has(n,a))return!0;if(typeof a=="symbol"||a.startsWith("$")||a.startsWith("__"))return!1;for(const r of l)if(r.value&&Reflect.has(r.value,a))return!0;return!1},set(n,a,r){if(Reflect.has(n,a))return Reflect.set(n,a,r);if(typeof a=="symbol"||a.startsWith("$")||a.startsWith("__"))return!1;for(const u of l)if(u.value&&Reflect.has(u.value,a))return Reflect.set(u.value,a,r);return!1},getOwnPropertyDescriptor(n,a){var u;const r=Reflect.getOwnPropertyDescriptor(n,a);if(r)return r;if(!(typeof a=="symbol"||a.startsWith("$")||a.startsWith("__"))){for(const o of l){if(!o.value)continue;const v=Se(o.value,a)??("_"in o.value?Se((u=o.value._)==null?void 0:u.setupState,a):void 0);if(v)return v}for(const o of l){const v=o.value&&o.value[xe];if(!v)continue;const m=v.slice();for(;m.length;){const V=m.shift(),g=Se(V.value,a);if(g)return g;const _=V.value&&V.value[xe];_&&m.push(..._)}}}}})}const ln=M({autoGrow:Boolean,autofocus:Boolean,counter:[Boolean,Number,String],counterValue:Function,prefix:String,placeholder:String,persistentPlaceholder:Boolean,persistentCounter:Boolean,noResize:Boolean,rows:{type:[Number,String],default:5,validator:e=>!isNaN(parseFloat(e))},maxRows:{type:[Number,String],validator:e=>!isNaN(parseFloat(e))},suffix:String,modelModifiers:Object,...wt(),...pt()},"VTextarea"),Pt=N()({name:"VTextarea",directives:{Intersect:Yt},inheritAttrs:!1,props:ln(),emits:{"click:control":e=>!0,"mousedown:control":e=>!0,"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,s){let{attrs:l,emit:t,slots:n}=s;const a=Te(e,"modelValue"),{isFocused:r,focus:u,blur:o}=kt(e),v=c(()=>typeof e.counterValue=="function"?e.counterValue(a.value):(a.value||"").toString().length),m=c(()=>{if(l.maxlength)return l.maxlength;if(!(!e.counter||typeof e.counter!="number"&&typeof e.counter!="string"))return e.counter});function V(f,I){var b,P;!e.autofocus||!f||(P=(b=I[0].target)==null?void 0:b.focus)==null||P.call(b)}const g=U(),_=U(),x=le(""),w=U(),B=c(()=>e.persistentPlaceholder||r.value||e.active);function R(){var f;w.value!==document.activeElement&&((f=w.value)==null||f.focus()),r.value||u()}function T(f){R(),t("click:control",f)}function $(f){t("mousedown:control",f)}function y(f){f.stopPropagation(),R(),de(()=>{a.value="",da(e["onClick:clear"],f)})}function k(f){var b;const I=f.target;if(a.value=I.value,(b=e.modelModifiers)!=null&&b.trim){const P=[I.selectionStart,I.selectionEnd];de(()=>{I.selectionStart=P[0],I.selectionEnd=P[1]})}}const p=U(),h=U(+e.rows),d=c(()=>["plain","underlined"].includes(e.variant));Re(()=>{e.autoGrow||(h.value=+e.rows)});function C(){e.autoGrow&&de(()=>{if(!p.value||!_.value)return;const f=getComputedStyle(p.value),I=getComputedStyle(_.value.$el),b=parseFloat(f.getPropertyValue("--v-field-padding-top"))+parseFloat(f.getPropertyValue("--v-input-padding-top"))+parseFloat(f.getPropertyValue("--v-field-padding-bottom")),P=p.value.scrollHeight,F=parseFloat(f.lineHeight),H=Math.max(parseFloat(e.rows)*F+b,parseFloat(I.getPropertyValue("--v-input-control-height"))),E=parseFloat(e.maxRows)*F+b||1/0,D=pe(P??0,H,E);h.value=Math.floor((D-b)/F),x.value=X(D)})}me(C),j(a,C),j(()=>e.rows,C),j(()=>e.maxRows,C),j(()=>e.density,C);let S;return j(p,f=>{f?(S=new ResizeObserver(C),S.observe(p.value)):S==null||S.disconnect()}),ot(()=>{S==null||S.disconnect()}),z(()=>{const f=!!(n.counter||e.counter||e.counterValue),I=!!(f||n.details),[b,P]=oa(l),[{modelValue:F,...H}]=je.filterProps(e),[E]=Ka(e);return i(je,ae({ref:g,modelValue:a.value,"onUpdate:modelValue":D=>a.value=D,class:["v-textarea v-text-field",{"v-textarea--prefixed":e.prefix,"v-textarea--suffixed":e.suffix,"v-text-field--prefixed":e.prefix,"v-text-field--suffixed":e.suffix,"v-textarea--auto-grow":e.autoGrow,"v-textarea--no-resize":e.noResize||e.autoGrow,"v-text-field--plain-underlined":d.value},e.class],style:e.style},b,H,{centerAffix:h.value===1&&!d.value,focused:r.value}),{...n,default:D=>{let{isDisabled:W,isDirty:q,isReadonly:K,isValid:be}=D;return i(It,ae({ref:_,style:{"--v-textarea-control-height":x.value},onClick:T,onMousedown:$,"onClick:clear":y,"onClick:prependInner":e["onClick:prependInner"],"onClick:appendInner":e["onClick:appendInner"]},E,{active:B.value||q.value,centerAffix:h.value===1&&!d.value,dirty:q.value||e.dirty,disabled:W.value,focused:r.value,error:be.value===!1}),{...n,default:se=>{let{props:{class:ie,...re}}=se;return i(Q,null,[e.prefix&&i("span",{class:"v-text-field__prefix"},[e.prefix]),ne(i("textarea",ae({ref:w,class:ie,value:a.value,onInput:k,autofocus:e.autofocus,readonly:K.value,disabled:W.value,placeholder:e.placeholder,rows:e.rows,name:e.name,onFocus:R,onBlur:o},re,P),null),[[lt("intersect"),{handler:V},null,{once:!0}]]),e.autoGrow&&ne(i("textarea",{class:[ie,"v-textarea__sizer"],id:`${re.id}-sizer`,"onUpdate:modelValue":Ve=>a.value=Ve,ref:p,readonly:!0,"aria-hidden":"true"},null),[[ca,a.value]]),e.suffix&&i("span",{class:"v-text-field__suffix"},[e.suffix])])}})},details:I?D=>{var W;return i(Q,null,[(W=n.details)==null?void 0:W.call(n,D),f&&i(Q,null,[i("span",null,null),i(Wa,{active:e.persistentCounter||r.value,value:v.value,max:m.value},n.counter)])])}:void 0})}),nn({},g,_,w)}}),sn=ye({__name:"Summary",setup(e){const s=fa({queue:[],closed:[],running:[],waiting:[]});me(async()=>{const n=await Jt(L.cur_serv.serv_name);s.queue=n.queue,s.closed=n.closed,s.running=n.running,s.waiting=n.waiting});const l=async()=>{await L.callServStart()},t=async()=>{await L.callServStop()};return(n,a)=>(Y(),J(dt,{class:"fill-height"},{default:A(()=>[i(at,{class:"align-center text-left fill-height"},{default:A(()=>[i(Ce,null,{default:A(()=>[i(Kt,{flat:"",color:ee(L).is_running?"green":"grey"},{default:A(()=>[ee(L).is_running?(Y(),J(fe,{key:0,variant:"outlined",onClick:a[0]||(a[0]=r=>t())},{default:A(()=>[ve(" 停止 ")]),_:1})):(Y(),J(fe,{key:1,variant:"outlined",onClick:a[1]||(a[1]=r=>l())},{default:A(()=>[ve(" 启动 ")]),_:1}))]),_:1},8,["color"])]),_:1}),i(Ce,null,{default:A(()=>[i(te,null,{default:A(()=>[i(ue,{title:"queue",tasks:s.queue},null,8,["tasks"])]),_:1}),i(te,null,{default:A(()=>[i(ue,{title:"closed",tasks:s.closed},null,8,["tasks"])]),_:1}),i(te,null,{default:A(()=>[i(ue,{title:"running",tasks:s.running},null,8,["tasks"])]),_:1}),i(te,null,{default:A(()=>[i(ue,{title:"waiting",tasks:s.waiting},null,8,["tasks"])]),_:1})]),_:1}),i(Ce,null,{default:A(()=>[i(te,null,{default:A(()=>[i(ct,{title:"Log"},{default:A(()=>[i(Pt,{readonly:""})]),_:1})]),_:1})]),_:1})]),_:1})]),_:1}))}}),rn=ye({__name:"RawJson",setup(e){const s=U("");Re(async()=>{if(L.cur_conf&&L.cur_serv){const n=await Xt(L.cur_conf.name,L.cur_serv.serv_name);s.value=JSON.stringify(n,null,2)}});const l=async()=>{if(L.cur_conf&&L.cur_serv){const n=t(s.value);if(!n)return console.error("Wrong json format");await Qt(n,L.cur_conf.name,L.cur_serv.serv_name)}};function t(n){try{return JSON.parse(n)}catch{}}return(n,a)=>(Y(),J(dt,{class:"fill-height"},{default:A(()=>[i(at,{class:"align-center text-center fill-height"},{default:A(()=>[i(Pt,{modelValue:s.value,"onUpdate:modelValue":a[0]||(a[0]=r=>s.value=r),"auto-grow":""},null,8,["modelValue"]),i(fe,{onClick:l},{default:A(()=>[ve(" 保存 ")]),_:1})]),_:1})]),_:1}))}}),un={key:0},dn=ye({__name:"Home",setup(e){return(s,l)=>ee(L).cur_conf?ee(L).cur_conf.name==="summary"?(Y(),J(sn,{key:1})):ee(L).cur_conf.name!==""?(Y(),J(rn,{key:2})):ga("",!0):(Y(),va("div",un))}});export{dn as default};
