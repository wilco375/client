import Vue from 'vue';
import VScrollLock from 'v-scroll-lock';
import smoothscroll from 'smoothscroll-polyfill';
import VueTippy, { TippyComponent } from 'vue-tippy';
import { localize } from 'vee-validate';
import veeValidateAr from 'vee-validate/dist/locale/ar.json';
import veeValidateDe from 'vee-validate/dist/locale/de.json';
import veeValidateEn from 'vee-validate/dist/locale/en.json';
import veeValidateEs from 'vee-validate/dist/locale/es.json';
import veeValidateId from 'vee-validate/dist/locale/id.json';
import veeValidateIt from 'vee-validate/dist/locale/it.json';
import '@open-election-compass/ui/dist/open-election-compass-ui.css';
import {
  BaseButton,
  FieldInput,
  FieldSelect,
  FieldSwitch,
  Icon,
  Modal,
} from '@open-election-compass/ui';
import OpenElectionCompass from './OpenElectionCompass.vue';
import storeModuleAlgorithm from './store/modules/algorithm/algorithm';
import storeModuleAnalysis from './store/modules/analysis/analysis';
import storeModuleFooterLinks from './store/modules/footerLinks/footerLinks';
import storeModuleLanguages from './store/modules/languages/languages';
import storeModuleOptions from './store/modules/options/options';
import storeModuleParties from './store/modules/parties/parties';
import storeModuleSections from './store/modules/sections/sections';
import storeModuleTheses from './store/modules/theses/theses';
import ar from './locales/ar.yaml';
import de from './locales/de.yaml';
import en from './locales/en.yaml';
import es from './locales/es.yaml';
import id from './locales/id.yaml';
import it from './locales/it.yaml';

export default function installOpenElectionCompassNuxtPlugin({ app, store }) {
  // Install locales
  app.i18n.mergeLocaleMessage('ar', ar);
  app.i18n.mergeLocaleMessage('de', de);
  app.i18n.mergeLocaleMessage('en', en);
  app.i18n.mergeLocaleMessage('es', es);
  app.i18n.mergeLocaleMessage('id', id);
  app.i18n.mergeLocaleMessage('it', it);

  // Install store modules
  store.registerModule('algorithm', storeModuleAlgorithm);
  store.registerModule('analysis', storeModuleAnalysis);
  store.registerModule('footerLinks', storeModuleFooterLinks);
  store.registerModule('languages', storeModuleLanguages);
  store.registerModule('options', storeModuleOptions);
  store.registerModule('parties', storeModuleParties);
  store.registerModule('sections', storeModuleSections);
  store.registerModule('theses', storeModuleTheses);

  // Install OpenElectionCompass UI
  Vue.component('BaseButton', BaseButton);
  Vue.component('FieldInput', FieldInput);
  Vue.component('FieldSelect', FieldSelect);
  Vue.component('FieldSwitch', FieldSwitch);
  Vue.component('Icon', Icon);
  Vue.component('Modal', Modal);

  // Install dependencies
  if (typeof document !== 'undefined' && typeof window !== 'undefined') {
    Vue.use(VScrollLock);
    smoothscroll.polyfill();
  }
  Vue.use(VueTippy, {
    directive: 'tooltip',
    arrow: true,
    arrowType: 'round',
    distance: 25,
  });
  Vue.component('tooltip', TippyComponent);

  localize({
    veeValidateAr,
    veeValidateDe,
    veeValidateEn,
    veeValidateEs,
    veeValidateId,
    veeValidateIt,
  });

  // Install component
  Vue.component('OpenElectionCompass', OpenElectionCompass);
}
