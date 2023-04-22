import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import Backend from "i18next-http-backend";
// import LanguageDetector from "i18next-browser-languagedetector";

i18n
  .use(Backend)
  //   .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    backend: { loadPath: "/assets/locales/{{lng}}/{{ns}}.json" },
    lng: "en",
    fallbackLng: "en",
    debug: true,
    defaultNS: ["common"],
    interpolation: { escapeValue: false },
  });

export default i18n;
