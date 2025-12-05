# 📱 React Native: Zero-to-Professional Guide (Complete Instructions)

#### foundational (Beginner to Intermediate) ####



* **Module 5: Advanced Features & State Management**
    * 5.1: `Image Picker` (Gallery/Camera se image lena) (`react-native-image-picker`) (Note 34)
    * 5.2: Navigation (React Navigation - Stack Navigator)
        * `NavigationContainer` (Note 14)
        * **Comparison:** Stack, Tab, & Drawer Navigators (Note 11, 36)
        * Navigation Actions (`navigation.goBack()`) (Note 20)
    * 5.3: Redux (Global State Management ka introduction) (Note 31)
    * 5.4: Advanced Forms (`react-hook-form`) (Note 1)

* **Module 6: Data, Tooling & Best Practices**
    * 6.1: HTTP Requests (Axios se API call karna)
        * `Axios` Interceptors & Retry (Note 26)
        * Offline Handling (`NetInfo`, Caching) (Note 26)
        * Security: `SSL Pinning` (Note 26, 27)
    * 6.2: Development Environment Setup (VS Code extensions)
    * 6.3: Debugging (Flipper & React DevTools)
        * `Toggle Element Inspector` (Dev Menu) (Note 12, 20)
        * `Reactotron` (Debugging & Network) (Note 13)
        * **Comparison:** `Flipper` vs `React Native Debugger` (Note 23)
        * Comprehensive Debugging Guide (Breakpoints, Copying Errors, etc.) (Note 5, 24)
        * `ADB` commands (Note 16, 25)
    * 6.4: Publishing (Expo Go se share karna)
    * 6.5: Best Practices & Conventions (Folders, Naming) (Note 47)
    * 6.6: Flexbox (Layout design ki neev) (Note 21)
    * 6.7: Icons & Fonts (Custom icons aur fonts)
        * `MaterialIcons` (`react-native-vector-icons`) (Note 10)
    * 6.8: `AsyncStorage` (Phone par data store karna) (Note 30, 31)
    * 6.9: JSON Server (Fake API banana)
    * 6.10: `Secure Storage`
        * **Comparison:** `AsyncStorage` vs `Secure Storage` (Note 30)
    * 6.11: Local Databases (SQLite, WatermelonDB, Realm) (Note 32)
    * 6.12: `Git` Commands (`revert`, `rebase`, `reset`, `delete branch`) (Note 51)
    * 6.13: Networking Tools (`dig` command) (Note 25)

* **Module 7: Troubleshooting & Practical Fixes (Beginner Problems)**
    * 7.1: Build & Cache Hell (Part 1): `gradlew clean` vs `gradlew.bat` (Kab aur Kyun?)
    * 7.2: Build & Cache Hell (Part 2): Manual Cache Cleaning (`rm -rf android/build`, `rm -rf android/app/.cxx`)
    * 7.3: Build & Cache Hell (Part 3): `npm cache clean --force`
    * 7.4: **Comparison:** Manual Cache vs. `npx react-native start --reset-cache` (Kaunsa cache kya solve karta hai?)
    * 7.5: The `package-lock.json` Problem (Kab delete karna chahiye?)
    * 7.6: Common Build Errors Explained (`build cmake`, `debug error`, `SDK location` etc.)
    * 7.7: Navigation Deep Dive: `initialRouteName="Login"` (Yeh kya hai aur agar na dein toh kya hoga?)
    * 7.8: Native Changes: `When to Rebuild` (Note 4)

---
#### 🚀 Professional Level (Advanced) 🚀
---

* **Module 8: Advanced React Hooks**
    * 8.1: `useEffect` (Side effects, API calls, component lifecycle)
    * 8.2: `useContext` (Prop drilling se bachna) (Note 31)
    * 8.3: `useCallback` & `useMemo` (Performance optimization)
        * `PureComponent` / `React.memo` (Note 49)
    * 8.4: `useRef` (Elements/values ko reference karna)
    * 8.5: Custom Hooks (Apna khud ka Hook banana)
    * 8.6: `useFocusEffect` (Note 14)

* **Module 9: Advanced Navigation (React Navigation)**
    * 9.1: Tab Navigator (Bottom tabs) (Note 11, 36)
    * 9.2: Drawer Navigator (Side menu) (Note 11)
    * 9.3: Nested Navigation (Stack ke andar Tabs, etc.)
    * 9.4: Authentication Flow (Login/Signup ke baad app flow)
    * 9.5: Deep Linking (Link se app kholna)
    * 9.6: Navigation Optimization (Keep-Alive Screens) (Note 36)

* **Module 10: Professional State Management**
    * 10.1: Redux Toolkit (Modern Redux, `configureStore`, `createSlice`) (Note 31)
    * 10.2: React Query / TanStack Query (Server state, caching, fetching)
    * 10.3: `Zustand` (Halka-phulka global state manager) (Note 31)
    * 10.4: `Context API` (Advanced) (Note 31)
    * 10.5: `Persistent State` (`redux-persist`) (Note 31)

* **Module 11: Performance & Animations**
    * 11.1: `Animated` API (React Native ki built-in animation)
    * 11.2: `React Native Reanimated` (Best performance, 60fps animations) (Note 35)
    * 11.3: `React Native Gesture Handler` (Complex gestures) (Note 14, 35)
    * 11.4: `FlatList` & `SectionList` Optimization (High performance lists) (Note 33)
    * 11.5: Performance Profiling (Flipper, Profiler, `memo`)
        * `PureComponent` / `React.memo` (Note 49)
        * `InteractionManager` (Note 49)
        * `Lazy Loading` (Screens & Components) (Note 33, 49)
        * **Comparison:** `Fast Refresh` vs `Hot Reloading` (Note 26)
    * 11.6: Advanced Animations & UI
        * `Lottie` Animations (Note 50)
        * `Skeleton Loaders` (Note 35)
        * `BottomSheet` (Note 35)
        * `Swipeable Lists` (Note 35)

* **Module 12: Interacting with Native Device**
    * 12.1: Push Notifications (Firebase Cloud Messaging - FCM)
        * `Push-Triggered Jobs` (Note 39)
        * `Notification Channels` (Android) (Note 40)
    * 12.2: `Advanced Camera (VisionCamera)` (Note 37)
    * 12.3: `Geolocation` (Live location tracking) (Note 37)
    * 12.4: `Local Authentication` (Fingerprint / Face ID) (Note 41)
    * 12.5: Linking Native Modules (Custom Java/Swift code ko jodna)
    * 12.6: `Device Sensors (Accelerometer)` (Note 37)
    * 12.7: `Bluetooth (BLE)` (Note 37)
    * 12.8: `Background Tasks`
        * `BackgroundTimer` (Note 2)
        * `BackgroundFetch` (Note 39)
        * `BackgroundGeolocation` (Note 39)
        * `Headless JS` (Note 39)
    * 12.9: `Screenshot Prevention` (Note 43)

* **Module 13: Testing, Deployment & TypeScript**
    * 13.1: TypeScript (React Native ke saath setup karna)
    * 13.2: Unit Testing (Jest & React Native Testing Library)
    * 13.3: End-to-End Testing (Detox)
    * 13.4: CI/CD Pipeline (GitHub Actions / Fastlane)
    * 13.5: Publishing to App Store & Play Store (Real builds - AAB/IPA)
        * `Debug vs Release Builds` (Note 42)
        * `App Signing (Keystore)` (Note 42)
        * `Proguard (Code Obfuscation)` (Note 42)
        * `Bundle Size Optimization` (Note 42)
        * `Crash Reports` (Note 42)
    * 13.6: Over-the-Air (OTA) Updates (CodePush / Expo Updates)
        * `CodePush` & VPS Setup (Note 45)
        * **Comparison:** `OTA vs Complete Update` (Note 46)
    * 13.7: `Environment Variables` (`react-native-config`) (Note 44)
    * 13.8: `Permissions Handling` (Manifest vs Runtime) (Note 29, 38, 40)
    * 13.9: `File Upload (Multipart)` (Note 34)

* **Module 14: Professional Development & Ecosystem**
    * 14.1: Error Handling (`Error Boundaries`) (Note 30)
    * 14.2: Accessibility (Screen Readers, Contrast, Touch Targets) (Note 48)


==============================================================================

# MODULE-1 → React Native Introduction & Setup

## 🎯 1. Title / Topic: 1.1 Introduction to React Native (Kya, Kyun, Kaise)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Socho React Native ek magic kitchen ki tarah hai jahaan ek hi recipe book (JavaScript code) se tum Android aur iOS dono ke liye alag-alag taste wala khana (apps) bana sakte ho. Jaise ek dough se pizza banao American style mein (Android), aur naan banao Italian twist ke saath (iOS), bina do baar poori kitchen saaf kiye ya nayi ingredients laaye – bas ek baar code likho, test karo, aur apps ready! Yeh time bachata hai, aur khana (app) fresh aur native taste wala banta hai, web jaise flat nahi.

## 📖 3. Technical Definition (Interview Answer):
React Native is an open-source framework developed by Facebook (ab Meta) for building native mobile applications using JavaScript and React principles, allowing code reusability across Android and iOS platforms.  
Breakdown in Hinglish: "Open-source framework" matlab free aur community-driven toolset jisme building blocks ready hote hain; "Native mobile applications" ka matlab real device features (jaise camera, GPS) use karne wale apps, jo web apps se alag feel dete hain; "JavaScript and React" matlab web programming language (JS) aur library (React for UI components) ko mobile pe apply karo, lekin output native code hota hai.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Traditional mobile development mein, Android ke liye Kotlin/Java aur iOS ke liye Swift/Objective-C alag-alag seekhna padta hai – ek app banane mein team ka double time lagta hai, bugs alag platforms pe alag aate hain, maintenance nightmare (code duplicate hota hai), aur cost sky-high (do teams chahiye). Agar sirf web tech jaante ho, toh mobile mein zero se shuru.  
**Solution:** React Native se 70-90% code share hota hai ek codebase mein, development 2x fast, bugs kam (ek jagah fix karo), aur performance native jaise (kyunki actual native views use hote hain, na ki browser wrapper). Beginners ke liye easy entry, kyunki JS jaante ho toh mobile apps banao bina nayi language seekhe.

## ⚙️ 5. Under the Hood (Technical Working):
Yeh step-by-step samjho:  
1. Tum React components likhte ho JS mein (jaise <View> for box, <Text> for labels – yeh JS objects hain).  
2. Metro bundler (RN ka packager) code ko bundle karta hai – JS ko optimize karke native calls mein convert.  
3. Shadow Tree (virtual DOM jaise) mein changes calculate hote hain.  
4. Bridge (Yoga engine) JS thread se native thread ko message bhejta hai – JS events (jaise button press) ko native UI updates mein translate.  
5. Native side pe (Android: Java/Kotlin views, iOS: UIKit components) actual rendering hota hai, isliye 60fps smooth.  
Agar bridge overload ho, toh lag aata hai, lekin Hermes JS engine (default now) se faster.  
ASCII Diagram:  
```
[Your JS Code: <App><View><Text>Hello</Text></View></App>] 
       |
[Metro Bundler: Bundle + Transpile JS] 
       |
[JS Thread: React Reconciliation (Diff changes)]
       | 
[Bridge: Serialize JS calls to Native (e.g., 'Update Text to "Hi"')]
       |
[Native Thread: Android LinearLayout / iOS UIView] --> Screen Render
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
Yahaan pehla basic app ka full code snippet – assume tune project init kiya hai (next topic mein detail). Yeh App.js file mein daalo.  
**Code Snippet:**  
```jsx
// Line 1: Import React core library – yeh sab components ka base hai, bina iske kuch nahi chalega.
import React from 'react';
// Line 2: Import RN core components – View jaise container (div ki tarah), Text jaise label (p/span ki tarah).
import { Text, View, StyleSheet } from 'react-native';

 // Line 3: Main App component define karo – arrow function se, functional component (class nahi, modern way).
const App = () => {
  // Line 4: Return JSX – yeh UI blueprint hai, RN mein JSX compile hokar native ban jaata hai.
  return (
    // Line 5: Outer View – flex:1 full screen occupy karega.
    <View style={styles.container}>
      // Line 6: Inner Text – simple string display.
      <Text style={styles.text}>Hello, React Native World! Yeh mera pehla app hai.</Text>
    </View>
  );
};

// Line 7: Styles define – StyleSheet.create se, performance ke liye (inline se better).
const styles = StyleSheet.create({
  container: {
    flex: 1,  // Full height/width.
    justifyContent: 'center',  // Vertical center.
    alignItems: 'center',  // Horizontal center.
    backgroundColor: 'lightblue'  // Background color.
  },
  text: {
    fontSize: 18,  // Text size in dp (density points, auto-scale).
    color: 'darkblue',  // Text color.
    fontWeight: 'bold'  // Bold font.
  }
});

// Line 8: Export – yeh component ko bahar use karne ke liye, index.js mein import hoga.
export default App;
```  
**Expected Output:** App chalane pe (npx react-native run-android), emulator/device pe lightblue background wala screen dikhega, center mein bold darkblue text "Hello, React Native World! Yeh mera pehla app hai." – touch karo, smooth scroll/zoom nahi (static abhi), lekin native feel.

## ⚖️ 7. Comparison (Ye vs Woh):
**React Native vs Native Development (Kotlin/Swift):**  
- **Code Reuse:** RN: 80% shared, Native: 0% (alag languages).  
- **Development Speed:** RN: Fast (hot reload), Native: Slow (full rebuild).  
- **Performance:** RN: Near-native (bridge overhead ~5-10%), Native: 100% but complex.  
**React Native vs Ionic/Cordova (Hybrid):** RN native UI deta hai, hybrid webview mein web code chalata hai (slow, battery drain).

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake 1:** Sochna ki RN web jaise hai – <div> use karo, lekin yahaan View/Text only, CSS classes nahi (sirf inline objects). Error: "Invariant Violation: View config not found."  
**Fix:** Hamesha RN docs se components check karo, jaise flexbox only layout ke liye (position: absolute limited).  
**Mistake 2:** Bridge ko ignore karna – heavy JS loops lag cause karte hain.  
**Fix:** Expensive computations native modules mein shift karo.

## 🌍 9. Real-World Use Case:
Facebook ka main app RN pe bana hai – news feed, stories jaise features fast update karne ke liye (ek code change se Android+iOS dono update). Instagram bhi RN use karta hai explore tab ke liye, jahaan millions users daily swipe karte hain, aur performance drop nahi hota.

## 🎨 10. Visual Diagram (ASCII Art):
```
User Interaction (Tap) --> [JS Thread: Event Handler] --> Bridge Serialize
                                             |
                                             v
[Native Thread: Update View] --> [Screen: Smooth 60fps Render]
                           ^
Bridge Deserialize <-- [Yoga Layout Engine: Calculate Positions]
```

## 🛠️ 11. Best Practices (Pro Tips):
- Components chhote rakho (5-10 lines), reusable banao (jaise Button.js alag file). Naming: PascalCase for components (AppComponent).  
- Hamesha flexbox use karo layout ke liye – row/column direction set.  
- Debugging ke liye Flipper tool install karo (RN 0.62+ mein built-in), console + network inspect.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
Agar RN na use kiya aur native separate kiya, toh 6 months ka project 12 months mein badh jaayega, bugs 2x, aur team burnout. Bridge misuse se app laggy (user reviews mein "slow" complaints), battery drain 20% extra.

## ❓ 13. FAQ (Interview Questions):
1. **Q: React Native kya hai exactly?** A: JS/React se native mobile apps banane ka framework, cross-platform with bridge to native.  
2. **Q: RN mein web skills kaise help?** A: JSX same, state management (useState) similar, lekin UI native.  
3. **Q: Limitations?** A: Heavy native integrations (jaise AR) ke liye extra modules chahiye.  
4. **Q: Future?** A: New Architecture (Fabric) se bridge overhead zero, even faster.

## 📝 14. Summary (One Liner):
React Native JS se ek code mein Android+iOS native apps banata hai bridge ke magic se – fast dev, shared code, real performance!

---

## 🎯 1. Title / Topic: 1.2 Comparison: Environment Setup (Expo vs React Native CLI)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Expo jaise ready-to-cook meal kit hai supermarket se – sab ingredients (tools, libs) pre-mixed, bas microwave mein daalo (npx expo start), 2 minutes mein khana ready, lekin agar special spice (custom native code) chahiye toh eject karke khud banao. React Native CLI jaise full raw market se shopping – har cheez control mein (Android Studio install, Xcode setup), time lagta hai lekin exact recipe bana sakte ho, no limits.

## 📖 3. Technical Definition (Interview Answer):
Expo is a managed workflow toolchain built on React Native that abstracts complex native setups and provides over-the-air updates, whereas React Native CLI is the bare-metal command-line tool for direct access to native project structures and custom configurations.  
Breakdown in Hinglish: "Managed workflow" matlab Expo sab hidden handle karta hai (no direct native folders touch); "Toolchain" ek set of commands/tools; "Bare-metal" CLI mein android/ios folders direct edit kar sakte ho; "Over-the-air updates" matlab app update bina store submit kiye.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** RN setup mein beginners ko Android SDK, Java JDK, Xcode (Mac only), emulators install karne mein 2-3 din lag jaate hain, errors jaise "SDK not found" ya "CocoaPods fail" – frustration high, learning curve steep. Custom features (jaise third-party native libs) add karna nightmare.  
**Solution:** Expo zero-setup deta hai (sirf Node.js chahiye), quick prototypes banao; CLI full power deta hai advanced apps ke liye, jaise hardware integrations. Choose Expo for MVP (minimum viable product), CLI for production scale.

## ⚙️ 5. Under the Hood (Technical Working):
Expo:  
1. `create-expo-app` template download, managed folder structure (no android/ios initially).  
2. `expo start` local server + cloud build trigger, Expo Go app (phone pe install) se QR scan karke test.  
3. Updates: EAS (Expo Application Services) se OTA push, native build cloud mein.  
CLI:  
1. `react-native init` full project with node_modules, android/ios folders.  
2. `react-native start` Metro bundler local.  
3. `run-android` local Gradle build, ADB install.  
Agar Expo se eject, toh CLI jaise ban jaata hai.  
ASCII Diagram:  
```
Expo: [JS Code] --> expo start --> [Local Dev Server + QR] --> Expo Go App (Phone Test)
                                           |
                                    [EAS Cloud: Build if needed] --> OTA Updates
CLI:  [JS Code] --> rn init/start --> [Local Metro] --> rn run-android --> [Gradle Local Build] --> Emulator/Device
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Expo Full Setup Commands:**  
```bash
# Command 1: Global install optional, lekin npx better (no version conflict).
npx create-expo-app@latest MyExpoApp --template blank
# Breakdown: npx (Node exec without global install), create-expo-app (Expo template generator), @latest (newest version), MyExpoApp (project name, kebab-case best), --template blank (minimal, no extras like tabs).
cd MyExpoApp  # Folder enter karo.
npx expo start  # Dev server shuru – i (iOS sim), a (Android emu), w (web).
# Breakdown: expo start – Metro bundler + Expo dev tools, QR code generate.
```  
**Expected Output:**  
```text
✔ Using latest Expo CLI
✔ Installed JavaScript dependencies for your project
› Metro waiting on exp://192.168.x.x:19000
› Scan QR with Expo Go app
› Press a · opens Android emulator
› Press i · opens iOS simulator
› Press w · starts web
Local:   exp://192.168.x.x:19000
Tunnel:  https://u.expo.dev/...
```

**CLI Full Setup Commands:**  
```bash
# Pre-reqs: Android Studio (SDK 30+), Xcode (Mac), Node 18+.
npx react-native@latest init MyCLIApp --version 0.72.6  # Specific version for stability.
# Breakdown: init (create project), --version (pin to avoid breaking changes).
cd MyCLIApp
npx react-native start  # Metro bundler only.
# New terminal: npx react-native run-android  # Full build + run.
# Breakdown: run-android – clean build, install APK, launch.
```  
**Expected Output (start):**  
```text
Loading dependency graph, done.
bundle: start
tunnel: ready
Metro ready.
```  
**Output (run-android):**  
```text
info Starting JS server. See "C:\...\metro.config.js" for info on how to customize it.
info Launching Metro bundler.
info Building and installing the app on the device (cd android && ./gradlew app:installDebug)...
info Connecting to the development server... (e.g., 192.168.x.x:8081)
info Launching on Android SDK built for x86.
```

## ⚖️ 7. Comparison (Ye vs Woh):
| Aspect          | Expo (Managed)                          | RN CLI (Bare)                          |
|-----------------|-----------------------------------------|----------------------------------------|
| **Setup Time** | 5 mins (no SDK)                        | 1-2 hours (full env)                   |
| **Customization** | Limited (eject for native)             | Full (direct edit android/ios)         |
| **Builds**     | Cloud (EAS) or local after eject       | Local always (Gradle/Xcode)            |
| **OTA Updates**| Yes, instant no store review           | No, full rebuild + submit              |
| **Best For**   | Prototypes, small teams                 | Enterprise, custom libs                |

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Expo mein native module (jaise react-native-camera) add karna bina check – "Unsupported" error.  
**Fix:** Expo docs mein "managed compatible" search karo, ya eject karo (expo eject – CLI mein convert).  
**Mistake:** CLI mein env vars miss (ANDROID_HOME not set) – "SDK not found".  
**Fix:** .bash_profile mein export ANDROID_HOME=$HOME/Android/Sdk add, source file.

## 🌍 9. Real-World Use Case:
Duolingo Expo use karta hai daily features update ke liye (millions users, no downtime). Tesla CLI use karta hai car hardware integrations ke liye (Bluetooth, sensors – Expo limited).

## 🎨 10. Visual Diagram (ASCII Art):
```
Expo: Code Edit --> expo start --> QR Scan --> Expo Go (Hot Reload)
      ^                                       |
      |                                       +-- Eject? --> CLI Structure
CLI:  Code Edit --> rn start (Bg) + rn run-android --> Local Build --> Device (Full Rebuild)
```

## 🛠️ 11. Best Practices (Pro Tips):
- Expo se shuru karo learning ke liye, production mein CLI prefer if custom needs.  
- Project names: lowercase-with-hyphens (my-app).  
- Version control: .gitignore mein node_modules, build folders add.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
Galat choice se: Expo mein advanced features block (eject pain, 1 day waste); CLI mein setup errors se week waste, motivation down. App crashes on device test.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Expo kab use?** A: Quick start, no native setup.  
2. **Q: Eject irreversible?** A: Haan, but backup le lo.  
3. **Q: CLI advantages?** A: Custom pods, full control.  
4. **Q: Cost?** A: Expo free basic, EAS paid for builds.

## 📝 14. Summary (One Liner):
Expo easy managed setup for fast prototypes, RN CLI bare control for custom power – beginners Expo, pros CLI!

---

## 🎯 1. Title / Topic: 1.3 Setting Up React Native Project (Pehla App)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Yeh poora setup jaise naya business shuru karna hai – pehle shop register karo (init project), phir electricity on karo (start server), gas cylinder connect (run on device), aur agar mess ho gaya (errors from old junk) toh poora clean sweep (gradlew clean, cache clear). Bina iske shop sirf paper pe rahega, real mein khul hi nahi payega!

## 📖 3. Technical Definition (Interview Answer):
Setting up a React Native project entails initializing the app scaffold with CLI tools, configuring the bundler (Metro), running the development server, building and deploying to simulators/devices, and maintaining cleanliness through cache/build cleans to resolve common artifacts.  
Breakdown in Hinglish: "Scaffold" matlab ready template files; "Bundler (Metro)" JS code ko pack karta hai; "Artifacts" matlab old build files jo errors cause karte hain.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Blank folder se shuru karo toh dependencies (libs) miss, configs galat, builds fail – pehla "Hello World" bhi nahi chalega. Errors jaise "Module not found" ya "Gradle sync failed" se stuck. Old cache se ghost bugs (app crash without reason).  
**Solution:** Yeh commands boilerplate deta hai, dev cycle fast (hot reload), aur cleans se reliability – production ready banao without surprises.

## ⚙️ 5. Under the Hood (Technical Working):
1. `init`: Downloads template from npm, creates package.json (deps list), node_modules install (npm i). Generates android/ios folders with Gradle/Pods.  
2. `start`: Metro watches files, bundles JS on change (transpile Babel se).  
3. `run-android`: Triggers Gradle (Android build tool) for APK compile, ADB (Android Debug Bridge) se install + launch.  
4. Cleans: gradlew clean old .class files delete; watchman/npx cache clear Metro cache; build clean full rebuild force.  
Kab clean: Dependency update pe (libs conflict), random crashes pe (stale cache), build errors jaise "Duplicate class" ya "R8 fail".  
ASCII Diagram:  
```
npx init --> [package.json + node_modules + android/ios folders] 
       |
npx start --> [Metro: Watch Files --> Bundle JS on Change] --> Port 8081
       |                                                          
npx run-android --> [Gradle Assemble] --> APK Generate --> ADB Install --> Launch
       ^                                                          
Cleans: gradlew clean / npx start --reset-cache (If Errors: "Manifest merger failed")
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
Yahaan full sequence, with cleaning details. Assume Windows/Mac, Android focus (iOS Mac only).

**Core Commands:**

1. **Init Project:**  
```bash
npx react-native@latest init MyFirstApp --template react-native-template-typescript  # Optional TS for type safety.
```  
**Breakdown:**  
* `npx`: Runs without global install, avoids version hell.  
* `@latest`: Newest RN (check compatibility).  
* `init MyFirstApp`: Folder create + files (App.js, index.js).  
* `--template ...`: JS default, TS for beginners better (error catch early).  
**Expected Output:**  
```text
✔ Downloading template (takes ~1 min)
✔ Copying template to MyFirstApp
✔ Processing template into MyFirstApp
✔ Installing dependencies with npm (takes ~2 min)
Run instructions:
  - cd MyFirstApp
  - npx react-native start
  - In another terminal: npx react-native run-android
Success! Created MyFirstApp.
```

2. **Start Metro Bundler:**  
```bash
cd MyFirstApp
npx react-native start --reset-cache  # --reset-cache optional, first time clean.
```  
**Breakdown:**  
* `start`: Launches Metro (Webpack-like for RN).  
* `--reset-cache`: Clears old bundles (use if "stale" errors).  
**Expected Output:**  
```text
Loading dependency graph... (5s)
Metro bundler ready.
To reload the app, press R or Cmd+R.
Tunnel ready at http://localhost:8081.
```

3. **Run on Android:**  
```bash
npx react-native run-android --deviceId emulator-5554  # Specific device.
```  
**Breakdown:**  
* `run-android`: Builds debug APK, installs via ADB, bundles JS.  
* `--deviceId`: List with `adb devices`, emulator ya physical.  
* `--variant release`: For release build (slow, optimized).  
**Expected Output:**  
```text
info JS server already running.
info Building the app (cd android && ./gradlew app:installDebug)...
> Task :app:compileDebugJavaWithJavac UP-TO-DATE
info Installing the app...
info Launching on emulator-5554.
Starting: Intent { cmp=com.myfirstapp/.MainActivity }
```

**Cleaning Commands (Detailed – Yeh key hai doubts ke liye!):**

Cleaning kab:  
- **Gradlew Clean:** Build errors pe jaise "Duplicate resources", "Manifest merger failed", "R.java not generated", "Outdated Gradle cache". Dependency update ke baad (npm i new lib). Random crashes without log.  
- **Cache Clean:** Metro errors jaise "Unable to resolve module", "Transform error", "Stale JS bundle". App not reloading changes.  
- **Build Clean:** Full reset – gradlew + cache + node_modules reinstall. Heavy issues jaise "SDK version mismatch", after OS update.  
Errors types:  
- Build fail: "Execution failed for task ':app:mergeDebugResources'" – old resources conflict.  
- Runtime: "Red screen: Unable to load bundle" – cache stale.  
- Install fail: "INSTALL_FAILED_INVALID_APK" – corrupted build.

4. **Gradlew Clean:**  
```bash
cd android
./gradlew clean  # Windows: gradlew.bat clean
cd ..  # Back to root.
```  
**Breakdown:**  
* `./gradlew`: Gradle wrapper (no global Gradle need).  
* `clean`: Deletes build/ folder (.class, .dex files). Force full rebuild next run.  
Variations: `./gradlew cleanBuildCache` (only cache), `./gradlew assembleDebug --rerun-tasks` (clean + build).  
**Expected Output:**  
```text
> Configure project :app
> Task :clean
BUILD SUCCESSFUL in 15s (daemon alive, reused)
Deleted: /android/app/build/
```

5. **Cache Clean (Metro/Watchman):**  
```bash
npx react-native start --reset-cache  # Metro cache.
# Or full: watchman watch-del-all && rm -rf $TMPDIR/react-* && rm -rf node_modules/.cache
npm start -- --reset-cache  # If using npm scripts.
```  
**Breakdown:**  
* `--reset-cache`: Clears /tmp/react-native-cache.  
* `watchman watch-del-all`: Facebook's file watcher reset (if installed, brew install watchman).  
**Expected Output:**  
```text
Metro cache cleared.
Loading graph... done (no cache hit).
```

6. **Full Build Clean:**  
```bash
cd android && ./gradlew clean && cd ..
rm -rf node_modules  # Or Windows: rmdir /s node_modules
npm install  # Reinstall deps.
npx react-native run-android  # Fresh build.
```  
**Breakdown:** Full wipe – use if above nahi kaam.  
**Expected Output:** Clean install, longer first run (~5 min).

**ADB Reverse (Physical Device):**  
```bash
adb reverse tcp:8081 tcp:8081  # For JS bundle access.
# List devices: adb devices
# Kill server if stuck: adb kill-server && adb start-server
```  
**Breakdown:** `adb` (Android SDK tool), `reverse`: Localhost tunnel device pe. Kab: WiFi debug ya USB tether.  
**Expected Output:** No text, but `adb devices` shows "device".

**Config Files Example:**  
metro.config.js (root):  
```js
// Line 1: Default config import – RN ka standard bundler setup.
const {getDefaultConfig, mergeConfig} = require('@react-native/metro-config');
/** @type {import('metro-config').MetroConfig} */
const config = {};
module.exports = mergeConfig(getDefaultConfig(__dirname), config);
// Breakdown: __dirname (current folder), merge for custom (e.g., add resolver.sourceExts: ['ts', 'tsx'] for TS).
```  
babel.config.js:  
```js
module.exports = {
  presets: ['module:@react-native/babel-preset'],  // Transpile JSX/TS.
};
// Breakdown: Babel RN ke liye ES6+ ko JS mein convert.
```

**NPM Commands for Health:**  
```bash
npm list --depth=0  # Top-level deps.
npm outdated  # Update needed?
npm audit  # Security issues.
npm audit fix  # Auto-fix low risk.
```  
**Breakdown:** `list`: Tree view; `outdated`: Versions compare; `audit`: Vulnerabilities scan (e.g., "High: lodash 4.17.15").  
**Expected Output (outdated):**  
```text
Package      Current  Wanted  Latest
react-native 0.72.0   0.72.6  0.74.0
```

## ⚖️ 7. Comparison (Ye vs Woh):
**npm start vs npx react-native run-android:**  
- **npm start:** Sirf bundler (JS ready, hot reload), no build/install. Kab: Code edit karte hue, emulator already running. Fast (seconds).  
- **run-android:** Full cycle (build APK, install, launch, connect to bundler). Kab: First run, after clean, device test. Slow (1-5 min first).  
Agar start chal raha, run-android auto connect.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Emulator na start kiye run-android – "No devices found".  
**Fix:** Android Studio > AVD Manager > Create/Start Virtual Device.  
**Mistake:** USB debugging off physical device – "Unauthorized".  
**Fix:** Settings > Developer Options > USB Debugging on, adb reverse.  
**Mistake:** Cache na clean kiye "Module resolution failed" – ghost import.  
**Fix:** --reset-cache flag hamesha try.

## 🌍 9. Real-World Use Case:
Netflix RN CLI use karta hai daily builds ke liye – gradlew clean after lib updates (jaise new video player), millions devices pe stable. Startups pehle app init + run se MVP launch karte hain week mein.

## 🎨 10. Visual Diagram (ASCII Art):
```
Init --> cd Project --> start (Metro Bg) 
                  |
Clean? --> gradlew clean / reset-cache --> run-android --> ADB Install --> App Launch
                  |                                     
NPM: list/outdated/audit (Health Check) <------------------+
```

## 🛠️ 11. Best Practices (Pro Tips):
- Scripts in package.json: "android": "react-native run-android", "clean": "cd android && ./gradlew clean && cd .. && npx react-native start --reset-cache".  
- After npm i: Always clean + run.  
- Multiple devices: adb -s deviceId run-android.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No clean: Builds corrupt, app crash on launch ("FATAL EXCEPTION"), hours debug waste. No init proper: Missing files, "Cannot find App.js" – project unusable.

## ❓ 13. FAQ (Interview Questions):
1. **Q: gradlew clean kab?** A: Build errors like duplicate classes, after dep changes.  
2. **Q: Cache clean ka error?** A: Module not resolve, stale bundle.  
3. **Q: adb reverse kyun fail?** A: No USB/WiFi, check adb devices.  
4. **Q: Full clean sequence?** A: gradlew clean + rm node_modules + npm i + reset-cache.

## 📝 14. Summary (One Liner):
RN setup init-start-run se pehla app ready, cleans (gradlew/cache/build) errors fix – smooth dev cycle guaranteed!

---

## 🎯 1. Title / Topic: 1.4 Styling (StyleSheet, Inline vs External)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Styling in RN jaise bachche ko kapde pehnana hai – Inline style har baar naye kapde choose karna (quick lekin wardrobe mess), External StyleSheet jaise almari mein organized sets (reusable, fast change, no repeat). LinearGradient jaise rainbow shirt – colors fade effect ke saath fancy look!

## 📖 3. Technical Definition (Interview Answer):
Styling in React Native leverages the StyleSheet API to define declarative style objects that are resolved to native platform-specific properties, supporting inline direct props or external imported sheets for performance and maintainability, with extensions like LinearGradient for advanced gradients.  
Breakdown in Hinglish: "Declarative" matlab describe karo kya chahiye (not how); "Resolved to native" – RN styles ko Android styles.xml ya iOS CALayer mein convert; "Imported sheets" – file se load for DRY code.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Bina styles ke UI plain text jaise (no colors, layout overlap), responsive nahi (different screens pe break). Inline heavy se perf drop (har render pe recalculate).  
**Solution:** StyleSheet cached IDs deta hai (fast apply), external reusability (theme change ek jagah), gradients visual appeal (buttons, backgrounds).

## ⚙️ 5. Under the Hood (Technical Working):
1. StyleSheet.create({}) object ko internal ID array mein convert (hashing).  
2. Render time: style prop mein ID pass, native Yoga engine lookup + apply (flexbox calc).  
3. Inline: Har render pe deep copy + parse (slow for complex).  
4. LinearGradient: Expo lib, native shader draw (CPU efficient).  
Kab use: Complex apps mein external for theming (dark/light mode).  
ASCII Diagram:  
```
StyleSheet.create({box: {color:'red'}}) --> Internal ID [0x123] (Cached)
Render: <View style={styles.box} /> --> Lookup ID --> Yoga Apply: setBackgroundColor(red)
Inline: <View style={{color:'red'}} /> --> Parse Object --> Slower Hash + Apply
Gradient: <LinearGradient colors={['#f00','#00f']} /> --> Native Draw: Interpolate Colors
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**External StyleSheet Full Example (App.js):**  
```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const App = () => (
  <View style={styles.mainContainer}>
    <View style={styles.box}>
      <Text style={styles.label}>External Style: Red Box</Text>
    </View>
  </View>
);

const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    backgroundColor: '#f0f0f0',
    padding: 20  // All sides padding 20dp.
  },
  box: {
    backgroundColor: 'red',
    padding: 10,
    borderRadius: 5,  // Rounded corners.
    shadowColor: 'black',  // iOS shadow (Android elevation use).
    shadowOpacity: 0.5,
    elevation: 3  // Android shadow.
  },
  label: {
    color: 'white',
    fontSize: 16,
    textAlign: 'center'  // Horizontal align.
  }
});

export default App;
```  
**Line-by-Line:**  
* `StyleSheet.create({})`: Keys as style names, values objects (camelCase props like backgroundColor).  
* `style={styles.box}`: Reference ID, not object (perf).  
**Expected Output:** Gray bg pe red rounded box center, white text inside, shadow effect.

**Inline Style Example:**  
```jsx
<View style={{ flex: 1, backgroundColor: 'green', padding: 15 }}>
  <Text style={{ color: 'yellow', fontSize: 14 }}>Inline Green!</Text>
</View>
```  
**Breakdown:** Direct {}, lekin avoid complex (perf hit).  
**Expected Output:** Green box yellow text.

**LinearGradient (Install: npx expo install expo-linear-gradient):**  
```jsx
import { LinearGradient } from 'expo-linear-gradient';

<LinearGradient 
  colors={['#ff0000', '#0000ff']}  // Red to blue.
  style={{ flex: 1, justifyContent: 'center' }}
  start={{ x: 0, y: 0 }}  // Top-left start.
  end={{ x: 1, y: 1 }}  // Bottom-right end.
>
  <Text style={{ color: 'white' }}>Gradient Background!</Text>
</LinearGradient>
```  
**Line-by-Line:** `colors`: Array strings/hex; `start/end`: Direction points (0-1 normalized).  
**Expected Output:** Diagonal red-to-blue fade, white text center.

## ⚖️ 7. Comparison (Ye vs Woh):
**Inline vs External StyleSheet:**  
- **Perf:** Inline: Recreate each render (10-20% slower complex apps), External: Cached once (fast).  
- **Maintenance:** Inline: Repeat code, External: One change everywhere.  
- **Debug:** Inline: Easy inline see, External: Styles file check.  

**RN StyleSheet vs CSS:**  
- **Selectors:** CSS: .class { }, RN: No, sirf prop objects.  
- **Units:** CSS: px/rem, RN: Numbers (dp auto-scale, no % for width usually).  
- **Animations:** CSS: @keyframes, RN: Animated API separate.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Hyphen props use (background-color) – "Invalid style".  
**Fix:** CamelCase (backgroundColor).  
**Mistake:** Inline nested deep objects – memory leak.  
**Fix:** Flatten + external.  
**Mistake:** Gradient without expo – "Module not found".  
**Fix:** Expo managed ya link manually.

## 🌍 9. Real-World Use Case:
Airbnb RN mein external StyleSheets use karta hai listing cards ke liye (theme switch ek file change), LinearGradient search bar backgrounds pe for premium feel.

## 🎨 10. Visual Diagram (ASCII Art):
```
External: styles.js --> create({id1: {prop:val}}) --> <View style={styles.id1} /> --> Cached Apply
Inline:    <View style={{prop:val}} /> --> Parse + Apply (Slow)
Gradient:  colors=['r','b'] --> start(0,0) end(1,1) --> Native Shader Render
```

## 🛠️ 11. Best Practices (Pro Tips):
- Constants file banao: const COLORS = {primary: '#007bff'}; styles mein use.  
- Platform specific: Platform.OS === 'ios' ? {shadow...} : {elevation...}.  
- Avoid !important – RN no support, override nahi.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No styles: UI broken (text overlap, no responsive). Heavy inline: App 15-30% slower scroll, battery drain. Inconsistent theme: User confusion.

## ❓ 13. FAQ (Interview Questions):
1. **Q: StyleSheet benefits?** A: Cached, typed, performant.  
2. **Q: Flex properties?** A: direction, wrap, justify, align.  
3. **Q: Gradient lib?** A: expo-linear-gradient or react-native-linear-gradient.  
4. **Q: Shadow cross-platform?** A: iOS shadow, Android elevation.

## 📝 14. Summary (One Liner):
RN styling StyleSheet external se organized + fast rakho, inline quick ke liye, gradients visual pop – native look easy!

---

## 🎯 1. Title / Topic: 1.5 State Management (Introduction with useState Hook)

## 🐣 2. Samjhane ke liye (Simple Analogy):
useState jaise ek magic notepad hai pocket mein – likho current score (value), change karo toh poora scoreboard (UI) auto update ho jaata hai, bina manually refresh kiye. Jaise cricket mein run badha, screen pe dikhe – simple, lekin powerful for dynamic apps!

## 📖 3. Technical Definition (Interview Answer):
useState is a built-in React Hook that enables functional components to manage local state by returning a tuple of the current state value and a setter function, triggering re-renders on updates for reactive UIs.  
Breakdown in Hinglish: "Built-in Hook" matlab React ka ready function; "Tuple" array [value, setter]; "Reactive UIs" change pe auto refresh.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Functional components stateless hote hain default – user input (button press) ignore, UI static (no counter, form data). Class components complex (this.state).  
**Solution:** Local data (jaise toggle, input value) handle karta hai simply, re-render efficient (only changed parts).

## ⚙️ 5. Under the Hood (Technical Working):
1. First render: useState(initial) state init, setter bind.  
2. Setter call: setState(newVal) – batch update queue mein daal, no immediate change.  
3. React scheduler: Next tick pe re-render trigger, fiber node mark dirty.  
4. Reconciliation: Diff virtual DOM, update only changed (batched for perf).  
Kab use: Local only; global ke liye Context/Redux.  
ASCII Diagram:  
```
First Render: useState(0) --> State=0, Setter=fn --> Render <Text>{0}</Text>
                                      
User: onPress --> setState(1) --> Queue Batch Update
                                      
Re-render: State=1 --> Diff: Text changed --> Update Native View {1}
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Full Counter App Example:**  
```jsx
import React, { useState } from 'react';  // Line 1: useState import – Hook rules: top level only.
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';  // Touchable for button.

const App = () => {
  // Line 2: Declare – [getter, setter] = useState(initial). Initial can be fn for lazy.
  const [count, setCount] = useState(0);  // Number state.
  const [name, setName] = useState('');  // String state.

  // Line 3: Handler fn – Avoid inline for perf (memoize if complex).
  const increment = () => setCount(prev => prev + 1);  // Callback to avoid stale closure.

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Count: {count}</Text>  // Line 4: Display state – interpolates.
      <Text>Welcome, {name || 'Guest'}!</Text>
      <TouchableOpacity 
        style={styles.button} 
        onPress={increment}  // Line 5: Event --> Setter.
        onPressIn={() => setName('Pressed!')}  // Temp state.
      >
        <Text>Click Me!</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  text: { fontSize: 24, margin: 10 },
  button: { backgroundColor: 'blue', padding: 10, borderRadius: 5 }
});

export default App;
```  
**Line-by-Line Extra:** `prev => prev +1`: Current value use, no count++ (stale).  
**Expected Output:** Center text "Count: 0", button press pe 1,2,... update instant, name change on press.

## ⚖️ 7. Comparison (Ye vs Woh):
**useState vs react-hook-form:**  
- **Scope:** useState: Any local state (counter, toggle), manual validation.  
- **Forms:** react-hook-form: Optimized forms (register, errors auto), less re-renders.  
Kab: Basic useState, forms >10 fields hook-form.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Setter mein old value use (setCount(count +1)) – infinite loop if in render.  
**Fix:** Callback: setCount(c => c +1).  
**Mistake:** Hooks conditional (if inside) – "Invalid hook call".  
**Fix:** Top level always.

## 🌍 9. Real-World Use Case:
Discord RN mein useState message input aur unread count ke liye – real-time update without full refresh.

## 🎨 10. Visual Diagram (ASCII Art):
```
useState(0) --> [count=0, setCount] --> Render UI {0}
                  ^
Event --> setCount(1) --> Re-render --> Diff --> Update {1}
```

## 🛠️ 11. Best Practices (Pro Tips):
- Descriptive names: [userName, setUserName].  
- Initial fn: useState(() => expensiveCalc()).  
- useReducer for complex state (multiple related).

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No state: App static, no interaction – user bored, uninstall. Wrong use: Infinite re-renders, crash OOM.

## ❓ 13. FAQ (Interview Questions):
1. **Q: useState return?** A: [state, setState].  
2. **Q: Why callback in setter?** A: Fresh value guarantee.  
3. **Q: Re-render trigger?** A: Setter call only.  
4. **Q: vs useEffect?** A: State data, Effect side-effects.

## 📝 14. Summary (One Liner):
useState local reactive state deta hai [value, setter] se – changes pe smart re-render, dynamic UI easy!

---

## 🎯 1. Title / Topic: 1.6 Additional Info: onPress vs onClick

## 🐣 2. Samjhane ke liye (Simple Analogy):
onPress jaise mobile screen pe finger touch karna (quick tap, haptic feedback), onClick web pe mouse click (hover + click, cursor change) – jaise smartphone call button vs laptop email link, action same lekin interaction natural alag!

## 📖 3. Technical Definition (Interview Answer):
onPress is React Native's gesture handler for touch events on mobile components like Touchable, providing native feedback, while onClick is React's web-specific handler for mouse/keyboard interactions without native touch semantics.  
Breakdown in Hinglish: "Gesture handler" touch detect + respond; "Native feedback" press pe opacity change.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Web code copy mein onClick mobile pe kaam nahi (no touch), buttons dull (no press effect).  
**Solution:** onPress touch optimized, accessibility (VoiceOver support), visual feedback.

## ⚙️ 5. Under the Hood (Technical Working):
1. TouchResponder: Start (down), move, end (up) track.  
2. If no long press/drag, onPress fire.  
3. Native: Android ripple, iOS opacity.  
Kab: All interactive elements.  
ASCII Diagram:  
```
Touch Down --> Responder: Start Tracking
  |  
  +-- Move > Threshold? --> Cancel (No Press)
  |
Touch Up --> Valid (Short, No Move)? --> onPress(fn) --> State Update / Action
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**TouchableHighlight Example (with Feedback):**  
```jsx
import React, { useState } from 'react';
import { View, Text, TouchableHighlight, Alert, StyleSheet } from 'react-native';

const App = () => {
  const [pressed, setPressed] = useState(false);

  const handlePress = () => {
    setPressed(true);
    Alert.alert('onPress Fired!', 'You tapped the button.');  // Native popup.
    setTimeout(() => setPressed(false), 500);  // Reset.
  };

  return (
    <View style={styles.container}>
      <TouchableHighlight 
        style={[styles.button, pressed && styles.pressed]}  // Dynamic style.
        onPress={handlePress}  // Core handler.
        underlayColor="#ddd"  // Press color.
        activeOpacity={0.7}  // Fade on touch.
        onLongPress={() => Alert.alert('Long Press!')}  // 500ms hold.
      >
        <Text style={styles.text}>Tap for onPress</Text>
      </TouchableHighlight>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  button: { backgroundColor: 'green', padding: 15, borderRadius: 8 },
  pressed: { backgroundColor: 'darkgreen' },
  text: { color: 'white', fontWeight: 'bold' }
});

export default App;
```  
**Line-by-Line:**  
* `TouchableHighlight`: Wraps child, handles touch.  
* `onPress={fn}`: Short tap.  
* `underlayColor`: Background on press.  
* `onLongPress`: Extra event.  
**Expected Output:** Green button, tap pe gray underlay + alert, state change color.

(onClick web only: <button onClick={fn}> – RN mein avoid.)

## ⚖️ 7. Comparison (Ye vs Woh):
**onPress vs onClick:**  
- **Events:** onPress: touchstart/end, onClick: mousedown/up + key.  
- **Feedback:** onPress: Native (ripple/opacity), onClick: CSS (hover).  
- **Platform:** onPress: Mobile essential, onClick: Web default.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Direct View pe onPress – "No responder".  
**Fix:** Touchable wrap.  
**Mistake:** Heavy fn inline – perf drop.  
**Fix:** Separate handler.

## 🌍 9. Real-World Use Case:
Shopify app mein cart buttons onPress se add/remove, touch feedback for e-commerce flow.

## 🎨 10. Visual Diagram (ASCII Art):
```
[Touchable] --Touch Down--> Active Opacity/Underlay --> Track Move
             --Touch Up (Valid)--> onPress(fn) --> Alert/State
             --Long Hold--------> onLongPress(fn)
```

## 🛠️ 11. Best Practices (Pro Tips):
- TouchableOpacity for fade, Highlight for color change.  
- Debounce if rapid fires (lodash throttle).  
- Accessibility: accessibilityLabel="Tap to increment".

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No handler: Dead buttons, poor UX. Wrong one: Cross-platform issues.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Touchable types?** A: Opacity (fade), Highlight (color), NativeFeedback (ripple).  
2. **Q: onClick in RN?** A: Not native, use Pressable (new unified).  
3. **Q: Delay?** A: Default 0, activeOpacity control.  
4. **Q: Multiple?** A: onPress + onLongPress.

## 📝 14. Summary (One Liner):
onPress RN touch events ke liye native feedback ke saath, onClick web mouse – Touchable se wrap for pro feel!

---

## 🎯 1. Title / Topic: 1.7 Additional Info: Console Methods (log, warn, error)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Console methods jaise school notebook ke sections – log normal notes (daily progress), warn sticky notes (hey, check this!), error red pen marks (urgent fix!) – debug karte hue code ka flow trace karo bina app crash kiye.

## 📖 3. Technical Definition (Interview Answer):
Console methods are JavaScript's global debugging APIs in React Native for outputting messages to the development console: log for general info, warn for non-critical alerts, and error for exceptions with stack traces, viewable via Chrome DevTools or Flipper.  
Breakdown in Hinglish: "Global APIs" browser/RN mein built-in; "Stack traces" error line numbers.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Code run karte hue kya ho raha invisible – bugs blind guess. No logs: Prod issues trace impossible.  
**Solution:** Real-time insights (variables, flows), levels for priority (warn for deprecations).

## ⚙️ 5. Under the Hood (Technical Working):
1. console.xxx('msg') – V8 JS engine mein push to debug channel.  
2. RN: Forward to Chrome debugger (remote-js-debug).  
3. Levels: log (info), warn (yellow), error (red + stack).  
Kab: Dev only, prod mein strip (__DEV__).  
ASCII Diagram:  
```
Code: console.log('Var:', obj) --> JS Engine --> Serialize Msg + Obj
                                           |
Dev Tools: Chrome/Flipper <-- Network (ws://localhost:8097) --> Display with Icon
Warn: Yellow ! , Error: Red X + Trace (file:line)
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Example in Component:**  
```jsx
import React, { useEffect } from 'react';
import { View, Text } from 'react-native';

const App = () => {
  useEffect(() => {
    console.log('App mounted, initial state ready.');  // Info: Lifecycle.
    console.warn('This is a warning: Check API key.');  // Caution: Yellow.
    try {
      throw new Error('Simulated crash');
    } catch (e) {
      console.error('Error caught:', e.message, e.stack);  // Critical: Red.
    }
    console.table({ user: 'John', age: 25 });  // Table format for objects.
  }, []);

  return <View><Text>Check Console!</Text></View>;
};
```  
**Line-by-Line:**  
* `log(msg, ...args)`: Print any, objects expandable.  
* `warn`: Same + icon.  
* `error`: + stack (Error: msg at App.js:10).  
* `table(obj)`: Pretty table.  
**Expected Output (Chrome Console: Cmd+D > Debug):**  
```text
App mounted, initial state ready.  // Black, expandable if obj.
This is a warning: Check API key.  // Yellow triangle ⚠️
Error caught: Simulated crash      // Red circle ❌
    at App (App.js:12:15)
┌─────────┬──────┐
│ (index) │ John │
├─────────┼──────┤
│   age  │  25  │
└─────────┴──────┘
```

## ⚖️ 7. Comparison (Ye vs Woh):
**log vs warn vs error:**  
- **Priority:** log: Debug/info, warn: Potential issue (no crash), error: Exception (stack).  
- **Output:** log: Plain, warn: Icon + continue, error: Halt? No, but trace.  
- **Use:** log: Values print, warn: Deprecated API, error: Try-catch.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Prod mein logs – sensitive data leak (console open).  
**Fix:** if (__DEV__) console.log...  
**Mistake:** Objects direct – [Object object].  
**Fix:** JSON.stringify or console.dir.

## 🌍 9. Real-World Use Case:
Uber devs console.error API fails pe log karte hain, warn for low signal – crash reports mein trace.

## 🎨 10. Visual Diagram (ASCII Art):
```
log('Hi') --> Console: Hi (Plain Text)
warn('Hey') --> Console: ⚠️ Hey (Yellow)
error('Oops') --> Console: ❌ Oops + Stack Trace (Red)
table({a:1}) --> Console: ┌──┐ Table Format
```

## 🛠️ 11. Best Practices (Pro Tips):
- Group: console.group('API Call') ... groupEnd().  
- Time: console.time('fetch') ... timeEnd().  
- Flipper integrate for RN-specific (logs + network).

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No logs: Bugs hours debug, prod crashes mystery. Overuse: Console flood, miss critical.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Stack trace kya?** A: Call chain lines.  
2. **Q: View in RN?** A: Shake device > Debug > Chrome.  
3. **Q: Clear?** A: console.clear().  
4. **Q: Prod safe?** A: __DEV__ guard.

## 📝 14. Summary (One Liner):
Console log/warn/error debug levels se code trace – info to critical, dev tools mein visual!

---

## 🎯 1. Title / Topic: 1.8 Additional Info: WebView Support

## 🐣 2. Samjhane ke liye (Simple Analogy):
WebView jaise app mein ek portable TV embed karna – bahar ka channel (website) andar dikhao, remote control (JS bridge) se interact, bina app se bahar nikle – hybrid power!

## 📖 3. Technical Definition (Interview Answer):
WebView is a React Native component from react-native-webview that embeds a full web browser instance within the app, loading URIs or HTML strings and enabling bidirectional JS communication via postMessage.  
Breakdown in Hinglish: "Embed" native view mein web engine; "Bidirectional" app se web aur web se app.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Poora native banana time-consuming, existing web dashboard reuse nahi. Offline web? No.  
**Solution:** Web content integrate (terms page, payments), hybrid apps banao cost low.

## ⚙️ 5. Under the Hood (Technical Working):
1. Install: npm i react-native-webview.  
2. <WebView source={{uri}} /> – Native WebView create (Android: WebView, iOS: WKWebView).  
3. Load: URL fetch, render HTML/JS.  
4. Bridge: injectedJS run, onMessage for comms.  
Kab: Static pages, third-party web.  
ASCII Diagram:  
```
<App> --> <WebView source={{uri:'https://example.com'}} /> --> Native Load + Render
  |                                                     |
injectedJavaScript="alert('Hi')" <--- JS Bridge ---> onMessage={e => console.log(e.nativeEvent.data)}
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Basic WebView Example:**  
```jsx
import React from 'react';
import { View, Dimensions } from 'react-native';
import WebView from 'react-native-webview';  // Line 1: Install first.

const { width, height } = Dimensions.get('window');  // Screen size.

const App = () => (
  <View style={{ flex: 1 }}>
    <WebView 
      source={{ uri: 'https://www.reactnative.dev/' }}  // Line 2: URL or {html: '<h1>Hi</h1>'}.
      style={{ flex: 1 }}  // Full size.
      onLoadStart={() => console.log('Loading...')}  // Events.
      onLoadEnd={() => console.log('Loaded!')}
      onError={(syntheticEvent) => {  // Error handle.
        const { nativeEvent } = syntheticEvent;
        console.warn('WebView error: ' + nativeEvent.code);
      }}
      javaScriptEnabled={true}  // Default true.
      domStorageEnabled={true}  // LocalStorage.
      startInLoadingState={true}  // Show activity indicator.
      renderLoading={() => <Text>Loading Web...</Text>}  // Custom loader.
      scalesPageToFit={true}  // Zoom fit.
    />
  </View>
);

export default App;
```  
**Line-by-Line:**  
* `source={{ uri }}`: Load URL.  
* `onLoad*`: Lifecycle logs.  
* `injectedJavaScript`: Pre-load JS string.  
**Expected Output:** RN docs site load app mein, scroll/zoom work, loading text first.

**Communication Example:**  
Web mein: window.postMessage('Hello from Web');  
RN: onMessage={e => Alert.alert(e.nativeEvent.data)}

## ⚖️ 7. Comparison (Ye vs Woh):
**WebView vs Native Web (Browser):**  
- **Perf:** WebView: Integrated (fast switch), Browser: External (slow launch).  
- **Control:** WebView: JS bridge, Native: No app data.  
- **Security:** WebView: Sandboxed, but careful JS.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** No internet permission – blank.  
**Fix:** Manifest: <uses-permission android:name="android.permission.INTERNET" />.  
**Mistake:** HTTPS only? No, but secure better.

## 🌍 9. Real-World Use Case:
Reddit app WebView for web previews in posts – native speed + web content.

## 🎨 10. Visual Diagram (ASCII Art):
```
[RN App] --<WebView uri="site.com">--> [Native Web Engine Load HTML/JS]
                  |                           |
Custom JS Inject <--> postMessage Bridge <--> onMessage Handler
```

## 🛠️ 11. Best Practices (Pro Tips):
- setSupportMultipleWindows={false} popups avoid.  
- User agent custom for web detect.  
- Offline: source={{ html: localHTML }}.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
No bridge: Isolated web, no app data. Errors: Infinite load, security vuln.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Install?** A: npm i react-native-webview + link if old RN.  
2. **Q: Comms?** A: postMessage both ways.  
3. **Q: Perf tip?** A: Lazy load, cache.  
4. **Q: iOS diff?** A: WKWebView faster than UIWebView.

## 📝 14. Summary (One Liner):
WebView web content app mein embed karta hai URI se, bridge se interact – hybrid easy!

---

## 🎯 1. Title / Topic: 1.9 Additional Info: Comparison: Debug vs Release Builds

## 🐣 2. Samjhane ke liye (Simple Analogy):
Debug build jaise beta version movie – extra commentary (logs), slow motion scenes (dev tools), test ke liye. Release jaise final cut – crisp, fast, no extras, theater ready (store upload).

## 📖 3. Technical Definition (Interview Answer):
Debug builds are unoptimized with source maps, dev server dependency, and full symbols for easy debugging, contrasting release builds which are minified, bundled standalone, and optimized (e.g., ProGuard, Hermes) for production performance and size.  
Breakdown in Hinglish: "Source maps" code lines trace; "Minified" code compress (short vars); "Standalone" no dev server need.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** Dev mein easy debug, prod mein slow/crash (unoptimized). Size big (store reject).  
**Solution:** Debug test, release deploy – switch for real perf.

## ⚙️ 5. Under the Hood (Technical Working):
Debug: JS dev server, no minify, logs on.  
Release: Offline bundle, R8/ProGuard obfuscate, Hermes AOT compile.  
Kab switch: Prod test pe release build run.  
ASCII Diagram:  
```
Debug: Code --> Babel (No Minify) + Source Maps --> Dev Server (Hot Reload) --> Large APK
Release: Code --> Babel Minify + ProGuard --> Hermes Compile --> Small Obfuscated APK (Standalone)
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Debug (Default):**  
```bash
npx react-native run-android  # Debug variant.
```  
**Expected Output:** ~20MB APK, connected to Metro.

**Release Build:**  
```bash
cd android
./gradlew assembleRelease  # Or bundleRelease for JS bundle.
# Sign: keytool -genkey -v -keystore my-release-key.keystore ... (First time).
# Edit android/app/build.gradle: signingConfigs.release { storeFile ... }
cd ..
npx react-native run-android --variant=release  # Install release.
```  
**Breakdown:**  
* `assembleRelease`: Optimized APK generate.  
* Signing: Prod need keystore (password protect).  
**Expected Output:**  
```text
> Task :app:processReleaseResources
> Task :app:bundleReleaseJSAndAssets
BUILD SUCCESSFUL in 2m
/app/build/outputs/apk/release/app-release.apk (10MB)
```

## ⚖️ 7. Comparison (Ye vs Woh):
**Debug vs Release:**  
- **Size:** Debug: 15-30MB (symbols), Release: 8-15MB (minified).  
- **Speed:** Debug: Slower startup (dev connect), Release: 2x faster (AOT).  
- **Debugging:** Debug: Breakpoints work, Release: Obfuscated (hard trace).

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Release mein logs on – leak.  
**Fix:** __DEV__ checks.  
**Mistake:** No signing – "INSTALL_PARSE_FAILED_NO_CERTIFICATES".  
**Fix:** build.gradle config.

## 🌍 9. Real-World Use Case:
Spotify release builds Play Store pe – optimized for low-end devices, debug internal QA.

## 🎨 10. Visual Diagram (ASCII Art):
```
Debug: Edit --> No Opt + Maps --> Run-Debug --> Dev Tools On
Release: Final --> Minify + Sign --> AssembleRelease --> APK to Store
```

## 🛠️ 11. Best Practices (Pro Tips):
- Test release on device (emulator slow).  
- android/app/build.gradle mein minSdkVersion 21+ for Hermes.  
- Use --no-packager for offline test.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
Release untested: Prod crashes (unoptimized), store reject (unsigned). Size big: Download slow.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Diff main?** A: Opt + standalone vs dev tools.  
2. **Q: Command?** A: assembleRelease.  
3. **Q: Hermes?** A: Enable in gradle for speed.  
4. **Q: iOS equiv?** A: Archive in Xcode.

## 📝 14. Summary (One Liner):
Debug tools wala test build, release optimized prod – assembleRelease se small fast APK!

---

## 🎯 1. Title / Topic: 1.10 Additional Info: Permissions (Android AndroidManifest.xml)

## 🐣 2. Samjhane ke liye (Simple Analogy):
Permissions jaise party invite – app ko camera room mein entry chahiye toh host (user) se permission lo, Manifest mein naam likho (guest list), runtime pe check (door pe ID). Bina iske gate crash!

## 📖 3. Technical Definition (Interview Answer):
Android permissions are security features declared in AndroidManifest.xml for app features and requested at runtime via PermissionsAndroid API to comply with scoped access, preventing unauthorized resource use.  
Breakdown in Hinglish: "Scoped access" limited rights; "Runtime" Android 6+ mandatory for dangerous perms.

## 🧠 4. Zaroorat Kyun Hai? (Why use it?):
**Problem:** No perm: Camera crash "Access denied". Privacy breach if auto-grant.  
**Solution:** User control, Google Play compliance, graceful deny handle.

## ⚙️ 5. Under the Hood (Technical Working):
1. Manifest declare <uses-permission> – install time check.  
2. Runtime: PermissionsAndroid.request(PERMS.CAMERA) – Promise dialog.  
3. Results: GRANTED/DENIED/REVOKED – handle.  
Kab: Dangerous perms (camera, location) runtime, normal (internet) manifest only.  
ASCII Diagram:  
```
AndroidManifest.xml: <uses-permission name="CAMERA" />
App: request(CAMERA) --> OS Dialog "Allow?" --> User Tap
                                 |
GRANTED --> Use Feature        DENIED --> Show Explain / Retry
```

## 💻 6. Hands-On: Commands & Syntax (CRITICAL SECTION):
**Manifest Edit (android/app/src/main/AndroidManifest.xml):**  
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <!-- Line 1: Normal perm – auto grant. -->
  <uses-permission android:name="android.permission.INTERNET" />
  <!-- Line 2: Dangerous – runtime. -->
  <uses-permission android:name="android.permission.CAMERA" />
  <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
  <application ... >
    ...
  </application>
</manifest>
```  
**Line-by-Line:** `name="..."` exact string from docs.

**Runtime Request Code:**  
```jsx
import { PermissionsAndroid, Platform, Alert } from 'react-native';

const requestPermissions = async () => {
  if (Platform.OS === 'android') {  // iOS separate.
    try {
      const permissions = [
        PermissionsAndroid.PERMISSIONS.CAMERA,
        PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION
      ];
      const granted = await PermissionsAndroid.requestMultiple(permissions);  // Multi.
      // Line: Check each.
      if (granted['android.permission.CAMERA'] === PermissionsAndroid.RESULTS.GRANTED) {
        console.log('Camera OK');
        // Use camera.
      } else {
        Alert.alert('Permission Denied', 'Camera needed for photos.');
      }
    } catch (err) {
      console.warn(err);
    }
  }
};

// Call: <Button onPress={requestPermissions} title="Request" />
```  
**Breakdown:** `requestMultiple`: Batch, results object. RESULTS: GRANTED/'denied'/'never_ask'.  
**Expected Output:** Dialogs pop, grant pe log, deny pe alert.

## ⚖️ 7. Comparison (Ye vs Woh):
**Android vs iOS:**  
- **Declare:** Android: Manifest.xml, iOS: Info.plist (keys like NSCameraUsageDescription).  
- **Request:** Android: Runtime dialog, iOS: Settings app post-prompt.  
- **Revoke:** Both: Settings > Apps > Permissions.

## 🚫 8. Common Mistakes (Beginner Traps):
**Mistake:** Runtime bhool – "EACCES".  
**Fix:** Always request before use.  
**Mistake:** No explain string – user deny.  
**Fix:** Alert why needed.

## 🌍 9. Real-World Use Case:
Pokemon GO location perms runtime maangta hai – explain "Catch 'em all!", deny pe limited mode.

## 🎨 10. Visual Diagram (ASCII Art):
```
Manifest Declare --> Install OK
App Start --> request() --> Dialog Multi? --> Grant All?
                  |                   |
Yes --> Feature On    No --> Alert + Retry / Fallback
```

## 🛠️ 11. Best Practices (Pro Tips):
- Explain dialog: "Location for nearby stores."  
- Lib: react-native-permissions cross-platform.  
- Never ask again? Check + direct to settings.

## ⚠️ 12. Consequences of Failure (Agar nahi kiya toh?):
Crash on access, Play reject ("Missing perms"), privacy lawsuits.

## ❓ 13. FAQ (Interview Questions):
1. **Q: Dangerous perms?** A: Camera, contacts, location.  
2. **Q: Normal?** A: Internet, vibrate – auto.  
3. **Q: iOS?** A: Plist + requestAuthorization.  
4. **Q: Multi request?** A: requestMultiple.


---

==================================================================================


# MODULE-2 → Core Components & State (Legacy & Modern)

### 2.1: Class Components (Sirf samajhne ke liye)

1.  **🎯 Title / Short Summary:** Class Components - Components banane ka "purana" tareeka (legacy).
2.  **🤔 Kya hai? (What?):** Yeh components banane ka ek tareeka hai jo JavaScript ki `class` syntax aur `React.Component` ko extend karke banta hai. Inke paas apna `state` aur "lifecycle methods" (jaise `componentDidMount`) hote the.
3.  **💡 Kyu important hai? (Why?):** Yeh "important" nahi hain *naye* code ke liye, lekin aapko yeh **samajhna zaroori** hai. Kyun? Kyunki aapko purane projects, online tutorials, ya Stack Overflow par aksar Class Components ka code dikhega.
4.  **⏰ Kab/use karna chahiye? (When?):** **Naye code mein kabhi nahi.** ❌ Hum 2024+ mein *sirf* Functional Components aur Hooks (jaise `useState`, `useEffect`) ka istemaal karte hain. Ise sirf purana code padhne/debug karne ke liye seekhein.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Kuch nahi. Aapka code modern, behtar, aur saaf-suthra (cleaner) hoga agar aap Functional Components use karenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh `React.Component` class ko `extend` karte hain.
      * Inko UI dikhane ke liye ek `render()` method ki zaroorat hoti hai.
      * State (data) ko `this.state` object mein rakha jaata tha.
      * State ko update karne ke liye `this.setState()` method use hota tha.
      * Props (data) ko `this.props` se access kiya jaata tha.
7.  **💻 Code example:** (Wahi counter app, Class Component se)
    ```javascript
    import React, { Component } from 'react';
    import { View, Text, Button, StyleSheet } from 'react-native';

    class CounterApp extends Component {
      // 1. State ko constructor mein initialize karna padta tha
      constructor(props) {
        super(props);
        this.state = {
          count: 0, // 'this.state' ek object hota tha
        };
      }

      // 2. State update karne ke liye method
      handlePress = () => {
        // 'this.setState' use hota tha
        this.setState({
          count: this.state.count + 1,
        });
      };

      // 3. UI dikhane ke liye 'render' method zaroori tha
      render() {
        return (
          <View style={styles.container}>
            <Text style={styles.text}>Class Component Counter:</Text>
            {/* 4. State ko 'this.state' se padhna */}
            <Text style={styles.countText}>{this.state.count}</Text>
            
            <Button
              title="Mujhe Dabao!"
              onPress={this.handlePress} // Methods ko 'this' ke saath call karna
            />
          </View>
        );
      }
    }

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 18 },
      countText: { fontSize: 40, marginVertical: 20, fontWeight: 'bold' },
    });

    export default CounterApp;
    ```
    **✍️ Line-by-line explanation:**
      * `import React, { Component } from 'react';`: Hum `useState` nahi, balki poora `Component` import kar rahe hain.
      * `class CounterApp extends Component { ... }`: Ek `class` bana rahe hain jo `Component` ko extend kar rahi hai.
      * `constructor(props) { ... }`: Yeh function component bante hi sabse pehle chalta hai.
      * `super(props);`: Parent class (Component) ke constructor ko call karna zaroori hota hai.
      * `this.state = { count: 0 };`: State ko `this.state` object mein set kar rahe hain.
      * `handlePress = () => { ... }`: Ek method banaya.
      * `this.setState({ ... });`: `this.state.count` ko directly badalne ke bajaye (jo galat hai), hum `this.setState` ko call karke batate hain ki state ka *kaunsa* hissa update karna hai.
      * `render() { ... }`: Yeh method batata hai ki screen par kya dikhega (JSX).
      * `{this.state.count}`: State ko `this.state.count` se access kiya.
      * `onPress={this.handlePress}`: Function ko `this.handlePress` se access kiya.
      * **🚀 Quick run expected output:** Bilkul `useState` wale example jaisa hi output aayega. Ek counter jo 0 se shuru hota hai aur button dabane par badhta hai.
8.  **🐞 Common beginner mistakes:**
      * `render()` method ke andar `this.setState()` ko call kar dena (isse infinite loop ban jaata hai).
      * `this` keyword ke chakkar mein phans jaana (kahan `this` lagega, kahan nahi).
      * State ko directly change karna: `this.state.count = 1;` (Yeh UI update nahi karega).
9.  **🌍 Real-world example / use-case:** Aapki company ka 3 saal purana project, ya Stack Overflow ka koi 2018 ka answer.
10. **✅ Quick checklist / TL;DR:**
      * Yeh "purana" tareeka hai.
      * `class` keyword, `extends Component` use karta hai.
      * `render()` method hota hai.
      * State ke liye `this.state` aur `this.setState()` use hota hai.
      * Naye code mein use **NAHI** karna hai.
11. **❓ FAQs:**
      * **Q: Toh main ise seekh hi kyun raha hoon?**
          * A: Taaki aap purana code dekh kar darr na jaayein aur use samajh sakein. Debugging ke liye zaroori hai.
      * **Q: Kya yeh Functional Component se fast/slow the?**
          * A: Shuru mein React team ne kaha tha dono same hain, lekin modern React (Hooks ke saath) Functional Components ko behtar optimize kar pata hai. Plus, inka code likhna bohot verbose (lamba) hota hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `CounterApp` class mein ek "Reset" button add karo jo `this.setState({ count: 0 })` call karke state ko 0 par reset kar de.
13. **📚 Further reading / commands / links:**
      * [React Docs - State and Lifecycle (Yeh ab "legacy" section mein hai)](https://legacy.reactjs.org/docs/state-and-lifecycle.html)

-----

### 2.2: Comparison: Functional vs Class Components

1.  **🎯 Title / Short Summary:** Naya (Functional) vs Purana (Class) - Hum Functional kyun use karte hain.
2.  **🤔 Kya hai? (What?):**
      * **Functional Components:** Simple JavaScript functions jo props (data) lete hain aur JSX (UI) return karte hain. Hooks (`useState`) ki madad se yeh ab state bhi rakh sakte hain.
      * **Class Components:** ES6 classes jo `React.Component` ko extend karti hain, `render()` method use karti hain, aur state ke liye `this.state` / `this.setState()` use karti hain.
3.  **💡 Kyu important hai? (Why?):** Yeh React/React Native development ka sabse bada shift (badlaav) hai. Yeh samajhna zaroori hai ki "Kyun" naya tareeka (Functional) purane (Class) se 100 guna behtar hai.

> 💡 **Special Rule Note:** Hum points 4, 5, 8, 9, 11 ko ek comparison table mein dekhenge.

**Comparison Table: Functional (Hooks) vs Class Components**

| Feature | 🚀 Functional Components (Modern) | 🧑‍🏫 Class Components (Legacy) |
| :--- | :--- | :--- |
| **⏰ Kab use karein? (When?)** | **Hamesha\!** 💯 2018 (React 16.8) ke baad se har naye component ke liye yahi standard hai. | **Kabhi nahi (naye code mein).** Sirf purane projects ko maintain/debug karne ke liye. |
| **❌ Agar... (Consequences)** | Agar aapne (aaj ke time) Class component use kiya, toh aapka code bewajah lamba (verbose), samajhne mein mushkil (complex `this`), aur slow ho jaayega. | Agar aapne Functional use nahi kiya, toh aap React ke sabse powerful features (Hooks, Context) miss kar denge. |
| **🐞 Common mistakes?** | Hooks ke rules todna (jaise `useState` ko `if` ke andar call karna). | `this` keyword ko galat jagah use karna (`this` binding). `render()` mein `setState` call karke infinite loop bana dena. |
| **🌍 Real-world example?** | Aapka poora naya app (Har screen, har button). | Purane Stack Overflow answers. 3+ saal purane tutorials. Company ke purane (legacy) projects. |
| **❓ FAQs (related)?** | **Q: Kya Hooks Class se zyada powerful hain?** <br> A: Haan. Hooks (jaise `useEffect`, `useContext`) se aap state aur logic ko component se alag karke *reuse* kar sakte hain (Custom Hooks). Yeh Class mein bohot mushkil tha. | **Q: "Lifecycle methods" ka kya hua?** <br> A: `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` - in sab ka kaam ab akela `useEffect` Hook kar leta hai. |

-----

**(Baaqi 13-point format ke points)**

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Code Lambaai (Verbosity):**
          * **Class:** `constructor`, `super(props)`, `this.state`, `this.setState`, `this.props`, `render()` - itna saara "boilerplate" (faltu code) likhna padta hai.
          * **Functional:** Sirf ek function. State chahiye? `useState`. Logic chahiye? `useEffect`. Bilkul saaf.
      * **`this` Keyword ka Jhanjhat:**
          * **Class:** `this` keyword bohot confuse karta tha. Function kab `this` ko "bhool" jaaye, pata nahi chalta tha. Isiliye `.bind(this)` ya arrow functions use karne padte the.
          * **Functional:** `this` ka koi kaam hi nahi hai. Simple function hai, simple scope hai.
      * **Logic Reuse (Sabse Bada Point):**
          * **Class:** Logic share karne ke liye "Higher-Order Components (HOCs)" ya "Render Props" jaise complex patterns use karne padte the.
          * **Functional:** Aap "Custom Hooks" (Module 8) bana sakte hain. Yeh simple functions hote hain jo logic (jaise API call karna) ko store karte hain aur koi bhi component use kar sakta hai.
7.  **💻 Code example:** (Dono code oopar 1.5 aur 2.1 mein diye gaye hain)
      * **Functional (1.5)**: 15-20 line mein saaf code.
      * **Class (2.1)**: Wahi kaam karne ke liye 30-35 line ka lamba code, `constructor` aur `render` ke saath.
8.  **✅ Quick checklist / TL;DR:**
      * **Functional + Hooks (Modern):** Use karo. Saaf, chota code. `this` ka jhanjhat nahi. Logic reuse (Custom Hooks) aasan.
      * **Class (Legacy):** Mat use karo. Lamba code. `this` bohot confuse karta hai. Logic reuse mushkil.
9.  **🏋️‍♀️ Practice exercise:**
      * Module 1.5 (Functional Counter) aur Module 2.1 (Class Counter) ke code ko side-by-side (ek saath) dekho.
      * Note karo ki Class component mein `this` kitni baar use hua hai aur Functional mein kitni baar (zero).
10. **📚 Further reading / commands / links:**
      * [React Docs - Hooks Introduction (Yeh zaroor padho)](https://react.dev/reference/react/hooks)

-----

### 2.3: Props (Data paas karna)

1.  **🎯 Title / Short Summary:** Props (Properties) - Parent se Child component ko data bhejna.
2.  **🤔 Kya hai? (What?):** Props ek tareeka hai jisse ek **Parent** component (jaise `App.js`) data ko **Child** component (jaise `Welcome.js`) tak bhej sakta hai. Props "read-only" (sirf padhne ke liye) hote hain.
3.  **💡 Kyu important hai? (Why?):** Iske bina har component isolated (akela) reh jaayega. Props se hi hum reusable components banate hain. Aap ek `Button` component banate hain aur `prop` se batate hain ki button ka `title` (text) kya hoga ya `color` kya hoga.
4.  **⏰ Kab/use karna chahiye? (When?):** Hamesha. Jab bhi aap ek component se doosre component mein data "neeche" (downwards) bhejna chahte hon.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap reusable components nahi bana payenge. Aapko har cheez ke liye naya component likhna padega. (Jaise 10 alag text ke liye 10 alag button component).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1 (Parent):** Parent component (jahan se data bhej rahe hain) mein Child component ko call karte time HTML attribute jaise data pass karte hain.
          * `<Greeting name="Rahul" />`
      * **Step 2 (Child):** Child component (jo data receive kar raha hai) us data ko function ke pehle argument (jise hum `props` kehte hain) mein receive karta hai.
          * `const Greeting = (props) => { ... }`
      * **Step 3 (Child):** Child component us data ko `props.name` (ya `props.jo_bhi_naam_diya_tha`) se use karta hai.
      * **Rule:** Child component `props` ko **badal (modify) nahi** sakta. (Props are read-only).
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { View, Text, StyleSheet, Image } from 'react-native';

    // 1. Child Component
    // Yeh props receive kar raha hai
    const UserProfile = (props) => {
      // 3. Props ko use karna (props.name, props.imageUrl)
      return (
        <View style={styles.card}>
          <Image source={{ uri: props.imageUrl }} style={styles.image} />
          <Text style={styles.text}>Welcome, {props.name}!</Text>
          <Text style={styles.text}>Age: {props.age}</Text>
        </View>
      );
    };

    // 2. Parent Component
    const App = () => {
      // Yahan se hum data (props) "pass" kar rahe hain
      return (
        <View style={styles.container}>
          <UserProfile 
            name="Rahul Kumar" 
            age={30} 
            imageUrl="https://i.pravatar.cc/150?img=11" 
          />
          <UserProfile 
            name="Priya Sharma" 
            age={25} 
            imageUrl="https://i.pravatar.cc/150?img=5" 
          />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      card: { padding: 20, margin: 10, backgroundColor: '#f0f0f0', borderRadius: 8, alignItems: 'center' },
      image: { width: 100, height: 100, borderRadius: 50, marginBottom: 10 },
      text: { fontSize: 18 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const UserProfile = (props) => { ... }`: `UserProfile` component banaya jo `props` naam ka object argument mein le raha hai.
      * `<Image source={{ uri: props.imageUrl }} ... />`: `props` object se `imageUrl` nikaal kar use kiya.
      * `<Text>Welcome, {props.name}!</Text>`: `props` object se `name` nikaal kar use kiya.
      * `const App = () => { ... }`: Parent component.
      * `<UserProfile name="Rahul Kumar" age={30} ... />`: Hum `UserProfile` ko call kar rahe hain aur use 3 props (`name`, `age`, `imageUrl`) bhej rahe hain.
      * `name="Rahul Kumar"`: String (text) prop.
      * `age={30}`: Number prop. Note: `30` ke around `{}` braces hain kyunki yeh JavaScript number hai (string "30" nahi).
      * **🚀 Quick run expected output:** Screen par 2 card dikhenge. Ek "Rahul Kumar" (age 30) ke liye aur ek "Priya Sharma" (age 25) ke liye. Humne `UserProfile` component *reuse* kiya.
8.  **🐞 Common beginner mistakes:**
      * Props ko child component mein change karne ki koshish karna. (e.g., `props.name = "Naya Naam";` ❌ Yeh error dega).
      * String vs Number mein confuse hona. `age="30"` (string) aur `age={30}` (number) alag-alag hain.
      * `props` likhna bhool jaana. `(props)` ke bajaye `()` likhna aur fir `props.name` use karke error paana.
9.  **🌍 Real-world example / use-case:**
      * Ek `Button` component jise `title` prop (button ka text) aur `onPress` prop (function) pass karna.
      * Ek `ProductCard` component jise `productName` aur `price` prop pass karna.
      * Instagram ki feed mein har `Post` component ko `postData` prop pass karna.
10. **✅ Quick checklist / TL;DR:**
      * Props = Parent se Child ko data dena.
      * Data "neeche" (downwards) jaata hai.
      * Props "Read-Only" (badal nahi sakte) hote hain.
      * `{}` braces use karein non-string values (numbers, objects, functions) ke liye.
11. **❓ FAQs:**
      * **Q: Agar Child ko Parent ko data vaapas bhejna ho toh?**
          * A: Aap data (value) nahi bhej sakte, lekin aap Parent se ek *function* ko prop ke zariye bhej sakte hain (jaise `onPress`). Jab Child us function ko call karta hai, toh Parent ko pata chal jaata hai. (e.g., `<Child onButtonPress={handlePressInParent} />`).
      * **Q: `props` vs `state` mein kya fark hai?**
          * A: **Props** (Properties) Parent se milte hain (external). **State** component ke *andar* manage hota hai (internal, `useState` se). Agar component ko data badalna hai, toh woh `state` mein hona chahiye.
      * **Q: `(props)` ke bajaye `({ name, age })` kya hota hai?**
          * A: Use "Destructuring" kehte hain. Yeh `props` object ko "khol" deta hai. `const { name, age } = props;` likhne ka shortcut hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `App` component mein ek teesra `<UserProfile />` add karo, apna naam aur age daal kar.
      * `UserProfile` component ko modify karo ki agar `age` 18 se kam ho, toh woh "Age: 17" na dikhaye, balki "Age: Minor" dikhaye. (Hint: `render` mein `if` ya ternary operator use karo).
13. **📚 Further reading / commands / links:**
      * [React Docs - Components and Props](https://react.dev/learn/passing-props-to-a-component)

-----

### 2.4: Activity Indicator (Loading spinner)

1.  **🎯 Title / Short Summary:** `ActivityIndicator` - "Loading..." dikhane wala default spinner 🌀.
2.  **🤔 Kya hai? (What?):** Yeh React Native ka built-in component hai jo platform-specific (Android/iOS) loading spinner dikhata hai.
3.  **💡 Kyu important hai? (Why?):** Jab aap API se data fetch kar rahe hon ya koi background kaam kar rahe hon, toh screen khali (blank) dikhegi. User ko lagega app hang ho gaya. `ActivityIndicator` user ko batata hai ki "Ruko, kaam chal raha hai."
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab API call bhej rahe hon aur data ka intezaar kar rahe hon.
      * Jab image load ho rahi ho.
      * Koi bhi process jo 1 second se zyada time le.
      * **Alternative:** Simple spinner ke bajaye, aap advanced "Skeleton Loaders" (jaise Facebook/LinkedIn mein dikhte hain - grey boxes) bhi use kar sakte hain (Module 11.6). `ActivityIndicator` simple loading ke liye hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** User ko khali (blank) screen ya purana data dikhega. Unhe lagega ki app "stuck" ya "frozen" ho gaya hai, aur woh app band kar denge. (Bad User Experience 👎).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Aapko ek `loading` state (`useState`) banani hogi (e.g., `const [isLoading, setIsLoading] = useState(true);`).
      * API call shuru hone se pehle, `setIsLoading(true)` karein.
      * Jab API call poora ho jaaye (data mil jaaye ya error aaye), tab `setIsLoading(false)` karein.
      * Aapke JSX mein, aap condition lagayenge:
          * `if (isLoading) { return <ActivityIndicator /> } else { return <FlatList data={data} /> }`
7.  **💻 Code example:** (API call simulate (nakal) karke)
    ```javascript
    import React, { useState, useEffect } from 'react';
    import { View, StyleSheet, ActivityIndicator, Text } from 'react-native';

    const App = () => {
      // 1. Loading state banayi
      const [isLoading, setIsLoading] = useState(true);
      const [data, setData] = useState(null);

      // 2. Data fetch karne ka function (useEffect se)
      useEffect(() => {
        // 3 second ka timer, API call jaisa
        setTimeout(() => {
          setData("Yeh data server se aaya hai!"); // Data set kiya
          setIsLoading(false); // 3. Loading band kiya
        }, 3000);
      }, []); // [] = Sirf ek baar chalao

      // 4. Conditional Rendering
      if (isLoading) {
        // Jab tak isLoading=true, yeh dikhao
        return (
          <View style={styles.container}>
            <ActivityIndicator size="large" color="#0000ff" />
            <Text>Loading data...</Text>
          </View>
        );
      }

      // Jab isLoading=false, yeh dikhao
      return (
        <View style={styles.container}>
          <Text style={styles.text}>{data}</Text>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 18 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const [isLoading, setIsLoading] = useState(true);`: Loading state banayi, shuru mein `true` (kyunki app khulte hi data fetch karna hai).
      * `useEffect(() => { ... }, []);`: `useEffect` (Module 8) ek hook hai jo component load hote hi chalta hai. Hum ise API call ke liye use karte hain.
      * `setTimeout(() => { ... }, 3000);`: 3 second ka fake delay banaya (API call ki jagah).
      * `setIsLoading(false);`: 3 second baad, loading ko `false` kar diya.
      * `if (isLoading) { ... }`: Yeh check kar raha hai. Agar state `true` hai, toh `ActivityIndicator` dikhao.
      * `<ActivityIndicator size="large" color="#0000ff" />`: `ActivityIndicator` component ko 2 props diye: `size` (spinner kitna bada ho 'small' ya 'large') aur `color` (spinner ka rang).
      * `return ( ... {data} ... )`: `if` condition false hote hi (jab `isLoading` `false` ho jaata hai), React yeh wala UI dikha deta hai.
      * **🚀 Quick run expected output:** App khulte hi 3 second ke liye ek bada neela (blue) spinner aur "Loading data..." text dikhega. 3 second baad, spinner gayab ho jaayega aur "Yeh data server se aaya hai\!" text dikhega.
8.  **🐞 Common beginner mistakes:**
      * `isLoading` state ko `false` karna bhool jaana. (Spinner hamesha ghoomta rahega).
      * Error aane par bhi `isLoading` ko `false` na karna. (API fail ho gayi, par user ko spinner hi dikh raha hai).
      * `ActivityIndicator` ko bina `size` ya `color` ke use karna (woh default mein 'small' dikhta hai jo mushkil se nazar aata hai).
9.  **🌍 Real-world example / use-case:**
      * Instagram feed kholna (pehla `ActivityIndicator` dikhta hai).
      * "Login" button dabana (button ke andar ek chota spinner dikhta hai).
10. **✅ Quick checklist / TL;DR:**
      * Loading state ke liye `useState` (`[isLoading, setIsLoading]`) banani hai.
      * Kaam shuru hone se pehle `setIsLoading(true)`.
      * Kaam khatm hone par `setIsLoading(false)`.
      * JSX mein `isLoading` ke basis par `ActivityIndicator` ya *data* dikhana hai.
11. **❓ FAQs:**
      * **Q: Kya main spinner ke upar poori screen ko dhundla (blur) kar sakta hoon?**
          * A: Haan. Iske liye `ActivityIndicator` ko ek `Modal` (Module 3) ke andar rakhte hain, jiska background halka black (transparent) hota hai. Yeh poori screen ko block kar deta hai.
      * **Q: `size` prop mein aur kya daal sakte hain?**
          * A: String `'small'` (default) ya `'large'`. Agar custom size chahiye, toh `style={{ transform: [{ scale: 2 }] }}` jaisa hack use karna padta hai ya number (e.g., `size={50}`) bhi de sakte hain (Android only).
      * **Q: Skeleton Loader kya hai?**
          * A: Woh chamakte (shimmering) grey boxes jo content (image, text) ki "jagah" le lete hain loading ke time. Yeh `ActivityIndicator` se behtar UX dete hain. (Hum Module 11.6 mein `react-native-reanimated` se banayenge).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `setTimeout` ka time 3000ms se 5000ms (5 seconds) karke dekho.
      * `ActivityIndicator` ka `color` badal kar `'green'` karo.
13. **📚 Further reading / commands / links:**
      * [ActivityIndicator Docs](https://reactnative.dev/docs/activityindicator)
      * [Skeleton Loader (Advanced - Module 11)](https://www.google.com/search?q=https://github.com/react-native-community/react-native-skeleton-placeholder)

-----

### 2.5: Buttons (Basic button)

1.  **🎯 Title / Short Summary:** `Button` - Simple, clickable button.
2.  **🤔 Kya hai? (What?):** Yeh React Native ka sabse basic, platform-specific button component hai. Iska look Android aur iOS par alag-alag (native) dikhta hai.
3.  **💡 Kyu important hai? (Why?):** Har app ko buttons chahiye. Yeh component aapko ek simple, "touchable" element deta hai jise style karne ki chinta nahi karni padti.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab aapko ek *bahut hi simple* "OK", "Cancel", "Submit" button chahiye.
      * Jab aapko styling ki chinta nahi hai, bas functionality check karni hai.
      * **Alternative:** 99% real-world apps mein aap `Button` **nahi**, balki `TouchableOpacity` (Module 1.6) ya `Pressable` (Module 4) use karenge, kyunki `Button` ko style karna (jaise custom background, icon) lagbhag namumkin hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Kuch nahi. Aap `TouchableOpacity` (behtar alternative) use kar lenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh bohot simple hai. Iske 2 zaroori props hain:
        1.  `title`: Button ke upar kya text dikhega.
        2.  `onPress`: Function jo button dabane par chalega.
      * Aap iska `color` (text color on iOS, background color on Android) badal sakte hain.
      * Aap isko `style` prop **nahi** de sakte (jaise `width`, `height`, `margin`). Yahi iski sabse badi problem hai.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { View, Button, StyleSheet, Alert } from 'react-native';

    const App = () => {
      
      const handleLoginPress = () => {
        Alert.alert('Login', 'Aapne Login dabaya!');
      };

      const handleSignupPress = () => {
        Alert.alert('Signup', 'Aapne Signup dabaya!');
      };

      return (
        <View style={styles.container}>
          {/* 1. Simple Button */}
          <Button
            title="Login"
            onPress={handleLoginPress}
          />

          {/* 2. Coloured Button */}
          <View style={styles.buttonSpacing}>
            <Button
              title="Signup"
              onPress={handleSignupPress}
              color="#841584" // Android par background, iOS par text color
            />
          </View>
          
          {/* 3. Disabled Button */}
          <View style={styles.buttonSpacing}>
            <Button
              title="Disabled"
              onPress={() => {}} // Kuch nahi karega
              disabled={true} // Isse click nahi kar sakte
            />
          </View>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      buttonSpacing: {
        marginTop: 10, // Button ko 'style' nahi de sakte, isliye wrapper 'View' ko style diya
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... Button, Alert } from 'react-native';`: `Button` aur `Alert` ko import kiya.
      * `const handleLoginPress = () => ...`: `onPress` ke liye ek function banaya.
      * `<Button title="Login" onPress={handleLoginPress} />`: Ek button banaya jiska text "Login" hai aur jo dabane par `handleLoginPress` function chalayega.
      * `color="#841584"`: Button ka color set kiya.
      * `disabled={true}`: Button ko "disabled" (greyed out) kar diya. User ispar click nahi kar sakta.
      * `<View style={styles.buttonSpacing}>`: **Important:** `Button` component `margin` ya `padding` jaisi styles nahi leta. Isiliye do buttons ke beech space dene ke liye, humne `Button` ko ek `<View>` ke andar wrap kiya aur us `View` ko `marginTop: 10` diya.
      * **🚀 Quick run expected output:** Screen par 3 button dikhenge. "Login" (default color), "Signup" (purple color), aur "Disabled" (greyed out).
8.  **🐞 Common beginner mistakes:**
      * `Button` ko `style` prop dene ki koshish karna. (`<Button style={{ margin: 10 }} ... />` ❌ Kaam nahi karega).
      * `Button` ke andar text ya icon daalne ki koshish karna. (`<Button><Text>Hi</Text></Button>` ❌ Galat hai). `Button` hamesha `title` prop hi leta hai.
9.  **🌍 Real-world example / use-case:**
      * Code test karte time jaldi se "OK" button banana.
      * `Alert` popup ke andar ke buttons (woh native `Button` hi hote hain).
      * Real app mein iska use **bohot kam** hota hai.
10. **✅ Quick checklist / TL;DR:**
      * `Button` simple aur native look deta hai.
      * Zaroori props: `title` aur `onPress`.
      * `style` prop **nahi** le sakte.
      * Styling ke liye, `TouchableOpacity` (Module 1.6) ya `Pressable` (Module 4) use karo.
11. **❓ FAQs:**
      * **Q: Toh main button ko style kaise karoon?**
          * A: Aap `Button` component hi na use karein. Aap `TouchableOpacity` (ya `Pressable`) use karein. Uske andar `<View>` aur `<Text>` daalein aur unhe jaisi marzi waisi style karein.
      * **Q: Android aur iOS par alag kyun dikhta hai?**
          * A: Kyunki yeh *native* component hai. Yeh Android ka asli `Button` aur iOS ka asli `UIButton` use karta hai, isiliye dono OS ka default look aata hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `Login` button ko `disabled` karne ki koshish karo.
      * Ek naya button "Cancel" (red color mein) add karo.
13. **📚 Further reading / commands / links:**
      * [Button Docs](https://reactnative.dev/docs/button)
      * [TouchableOpacity (Better alternative)](https://reactnative.dev/docs/touchableopacity)

-----

### 2.6: `TouchableHighlight` & `TouchableWithoutFeedback`

1.  **🎯 Title / Short Summary:** `TouchableHighlight` (dabane par highlight) aur `TouchableWithoutFeedback` (dabane par kuch nahi dikhta).
2.  **🤔 Kya hai? (What?):**
      * `TouchableHighlight`: Yeh `TouchableOpacity` (jo fade hota hai) jaisa hi hai, lekin yeh fade nahi hota. Jab aap ise dabate hain, toh yeh *background* ko `underlayColor` (jo aap set karte hain) se highlight kar deta hai.
      * `TouchableWithoutFeedback`: Yeh ek "invisible" touch wrapper hai. Jab aap ise dabate hain, toh **koi visual feedback (na fade, na highlight)** nahi dikhta.
3.  **💡 Kyu important hai? (Why?):**
      * `TouchableHighlight` tab use hota hai jab aapko solid color button (jaise website par hover effect) jaisa feel dena ho.
      * `TouchableWithoutFeedback` tab use hota hai jab aapko kisi aisi cheez ko clickable banana ho jo button *jaisi nahi* dikhti (jaise image par tap, ya "Dismiss keyboard" ke liye screen par kahin bhi tap).
4.  **⏰ Kab/use karna chahiye? (When?):**
      * `TouchableHighlight`: Jab `TouchableOpacity` ka fade effect achha na lag raha ho.
      * `TouchableWithoutFeedback`: Jab aapko touch ka koi visual feedback *nahi* chahiye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Bina `TouchableHighlight`: Aap `TouchableOpacity` use karenge (jo ki 90% time behtar hi hai).
      * Bina `TouchableWithoutFeedback`: Aap kisi non-button cheez ko (bina feedback) clickable nahi bana payenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh dono components *wrapper* hote hain. Inka khud ka koi look nahi hota.
      * Inke *andar* aapko ek (aur sirf ek) child component (jaise `<View>` ya `<Text>`) daalna hota hai.
      * `TouchableHighlight` ko ek `underlayColor` prop chahiye hota hai (dabane par kya rang dikhega).
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { View, Text, StyleSheet, TouchableHighlight, TouchableWithoutFeedback, Alert } from 'react-native';

    const App = () => {
      return (
        <View style={styles.container}>
          {/* 1. TouchableHighlight Example */}
          <TouchableHighlight
            style={styles.highlightButton}
            underlayColor="#00695C" // Dabane par yeh dark green dikhega
            onPress={() => Alert.alert('Highlight Pressed!')}
          >
            <Text style={styles.buttonText}>TouchableHighlight</Text>
          </TouchableHighlight>

          {/* 2. TouchableWithoutFeedback Example */}
          <TouchableWithoutFeedback
            onPress={() => Alert.alert('WithoutFeedback Pressed!')}
          >
            <View style={styles.feedbackView}>
              <Text style={styles.text}>Main clickable hoon</Text>
              <Text style={styles.text}>(Par koi feedback nahi doonga)</Text>
            </View>
          </TouchableWithoutFeedback>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      highlightButton: {
        backgroundColor: '#009688', // Normal background
        padding: 15,
        borderRadius: 5,
        marginBottom: 20,
      },
      buttonText: {
        color: 'white',
        fontSize: 16,
      },
      feedbackView: {
        padding: 20,
        backgroundColor: '#EEEEEE',
        alignItems: 'center',
      },
      text: {
        fontSize: 16,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... TouchableHighlight, TouchableWithoutFeedback } ...`: Dono components ko import kiya.
      * `<TouchableHighlight ...>`: Wrapper banaya.
      * `style={styles.highlightButton}`: Wrapper ko style di (taaki woh button jaisa dikhe).
      * `underlayColor="#00695C"`: Bataya ki jab user touch karega, toh background color `#009688` se badal kar `#00695C` ho jaana chahiye.
      * `<Text ...>...</Text>`: `TouchableHighlight` ke *andar* child (Text) daala.
      * `<TouchableWithoutFeedback ...>`: Wrapper banaya.
      * `<View style={styles.feedbackView}> ... </View>`: `TouchableWithoutFeedback` ko style nahi de sakte, isliye uske *andar* ek `View` daala aur use style kiya.
      * **🚀 Quick run expected output:**
          * Pehla (Green) button dikhega. Jab aap use daba kar rakhenge, toh woh Dark Green ho jaayega. Chhodne par Alert aayega.
          * Doosra (Grey) dabba dikhega. Jab aap use dabayenge, toh **kuch visual change nahi hoga**, lekin Alert aayega.
8.  **🐞 Common beginner mistakes:**
      * `TouchableWithoutFeedback` ke andar *ek se zyada* child daal dena. (e.g., `<Touchable><Text/><Text/></Touchable>` ❌ Galat). Hamesha sabko ek `<View>` mein wrap karke us `<View>` ko child banayein.
      * `TouchableWithoutFeedback` ko poori list item ke liye use karna. Isse user ko pata hi nahi chalta ki item clickable hai (Accessibility ke liye bura hai).
9.  **🌍 Real-world example / use-case:**
      * `TouchableHighlight`: Settings menu mein "Logout" button, jiska background red highlight hota ho.
      * `TouchableWithoutFeedback`: Jab form khula ho aur keyboard upar ho, toh "keyboard ke bahar" (screen par) tap karke keyboard ko dismiss (band) karne ke liye poori screen ko isse wrap kar dete hain.
10. **✅ Quick checklist / TL;DR:**
      * `TouchableOpacity`: Fades (90% use case).
      * `TouchableHighlight`: Highlights (10% use case).
      * `TouchableWithoutFeedback`: No feedback (Specific use case, jaise keyboard dismiss).
11. **❓ FAQs:**
      * **Q: Toh `TouchableOpacity` (Module 1.6) aur inme se best kaunsa hai?**
          * A: **`TouchableOpacity`** 90% time best hai. Yeh user ko saaf feedback deta hai. Naya **`Pressable`** (Module 4) component in sabse flexible hai, lekin shuru ke liye `TouchableOpacity` best hai.
      * **Q: `TouchableWithoutFeedback` accessibility ke liye bura kyun hai?**
          * A: Kyunki user (khaas kar jinko aakhon ki problem hai) ko *pata hi nahi chalta* ki woh cheez dabane laayak (clickable) hai. Bina zaroorat ke ise use na karein.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `TouchableHighlight` ka `underlayColor` badal kar "red" karke dekho.
      * `TouchableWithoutFeedback` wale example mein `onLongPress` add karke ek alag Alert dikhao.
13. **📚 Further reading / commands / links:**
      * [TouchableHighlight Docs](https://reactnative.dev/docs/touchablehighlight)
      * [TouchableWithoutFeedback Docs](https://reactnative.dev/docs/touchablewithoutfeedback)

-----

Module 2 complete\! Humne components ke "purane" aur "naye" tareeke, data pass karne (Props), aur loading spinners ke baare mein seekh liya hai.

Jab aap taiyaar hon, toh **"Module 3 ke notes do"** bolna\! 🧑‍💻

=============================================================

# MODULE-3 → Lists, Images & Modals

### 3.1: `FlatList` (Efficient scrollable lists)

1.  **🎯 Title / Short Summary:** `FlatList` - Hazaaron items ki list (feed) ko smooth chalaane ka tareeka 📜.
2.  **🤔 Kya hai? (What?):** Yeh ek core component hai jo lambi, scrollable lists ko *efficiently* (bina app ko slow kiye) render karta hai.
3.  **💡 Kyu important hai? (Why?):** Agar aap 1000 items ko `ScrollView` (Module 4) mein `map()` karke render karenge, toh aapka app **crash** ho jaayega. `FlatList` "lazy loading" use karta hai - yeh *sirf* wahi items render karta hai jo screen par dikh rahe hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Hamesha jab aapke paas ek list ho jismein 10-20 se zyada items ho sakte hain. Jaise: User list, product list, Instagram feed, chat history.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** `ScrollView` + `.map()` use karne se saare items (chahe 1000 hon) ek saath render honge. Isse bohot zyada memory use hogi, UI freeze (atak) jaayega, aur app crash ho jaayega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `FlatList` ko 2 sabse zaroori props chahiye:
        1.  `data`: Ek array of objects (aapka data, jaise `[ {id: '1', name: 'Rahul'}, ... ]`).
        2.  `renderItem`: Ek function jo batata hai ki array ke *har ek* item ko screen par *kaise* dikhana hai.
      * Isko ek `keyExtractor` prop bhi chahiye, jo har item ko ek unique `key` (string) deta hai. Yeh React ko items pehchaanne mein madad karta hai.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { SafeAreaView, View, FlatList, StyleSheet, Text, StatusBar } from 'react-native';

    // 1. Hamara sample data (API se bhi aa sakta hai)
    const DATA = [
      { id: '1', title: 'Pehla Item' },
      { id: '2', title: 'Doosra Item' },
      { id: '3', title: 'Teesra Item' },
      { id: '4', title: 'Chautha Item' },
      { id: '5', title: 'Paanchva Item' },
      { id: '6', title: 'Chhata Item' },
      // ...imagine 1000 more items
    ];

    // 2. Yeh component batata hai ki har item kaisa dikhega
    // Ise 'renderItem' prop mein pass kiya jaata hai
    const Item = ({ title }) => (
      <View style={styles.item}>
        <Text style={styles.title}>{title}</Text>
      </View>
    );

    const App = () => {
      // 3. renderItem function
      const renderItem = ({ item }) => (
        <Item title={item.title} />
      );

      return (
        <SafeAreaView style={styles.container}>
          <FlatList
            data={DATA} // 4. Poora data yahan pass kiya
            renderItem={renderItem} // 5. Bataya ki har item ko kaise render karna hai
            keyExtractor={item => item.id} // 6. Har item ke liye unique key
          />
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        marginTop: StatusBar.currentHeight || 0,
      },
      item: {
        backgroundColor: '#f9c2ff',
        padding: 20,
        marginVertical: 8,
        marginHorizontal: 16,
      },
      title: {
        fontSize: 32,
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const DATA = [...]`: Hamara data array. Har item ek object hai jismein `id` aur `title` hai.
      * `const Item = ({ title }) => (...)`: Ek alag component banaya (achhi practice) jo ek item ki styling handle karta hai. Yeh `title` ko as a prop le raha hai.
      * `const renderItem = ({ item }) => (...)`: Yeh function `FlatList` har item ke liye chalata hai. `FlatList` use ek object `{ item }` deta hai. Hum us `item` ko (jismein `{id: '1', title: 'Pehla Item'}` hai) `Item` component ko pass kar rahe hain.
      * `<FlatList ... />`: `FlatList` component.
      * `data={DATA}`: `FlatList` ko bataya ki data `DATA` variable mein hai.
      * `renderItem={renderItem}`: `FlatList` ko bataya ki har item ko render karne ke liye `renderItem` function use karo.
      * `keyExtractor={item => item.id}`: `FlatList` ko bataya ki har item ki unique key `item.id` (jo ki '1', '2' etc. hai) se milegi.
      * **🚀 Quick run expected output:** Ek scrollable list dikhegi, jismein har item pink background ke saath "Pehla Item", "Doosra Item" etc. dikhayega.
8.  **🐞 Common beginner mistakes:**
      * `keyExtractor` prop na dena. Isse warning aayegi aur performance kharab hogi.
      * `renderItem` ke andar `item` ko destructure na karna. `{ item }` (sahi) ke bajaye `(item)` (galat) likhna.
      * `FlatList` ko `ScrollView` ke andar daal dena.  nesting se scroll kaam nahi karega.
      * `FlatList` ko `flex: 1` style na dena (agar woh View ke andar hai), jisse woh screen par dikhta hi nahi hai.
9.  **🌍 Real-world example / use-case:**
      * **Instagram:** Aapki feed ek `FlatList` hai.
      * **WhatsApp:** Aapki chat list ek `FlatList` hai.
      * **Swiggy/Zomato:** Restaurant ki list ek `FlatList` hai.
10. **✅ Quick checklist / TL;DR:**
      * Lambi lists (10+ items) ke liye `FlatList` use karo.
      * 3 zaroori props: `data`, `renderItem`, `keyExtractor`.
      * `ScrollView` mein `.map()` mat use karo, app crash hoga.
11. **❓ FAQs:**
      * **Q: `keyExtractor` string hi kyun maangta hai?**
          * A: React ko internal tracking ke liye string keys ki zaroorat hoti hai. Agar aapki ID number hai (jaise `item.id = 1`), toh use `item => item.id.toString()` karke string mein badal dein.
      * **Q: `FlatList` mein "Pull to Refresh" kaise add karein?**
          * A: Uske liye `onRefresh` aur `refreshing` props hote hain. (Hum advanced topics mein cover karenge).
      * **Q: List ke end (neeche) pahunchne par aur data kaise load karein? (Infinite Scroll)**
          * A: Uske liye `onEndReached` prop hota hai. (Module 11).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `DATA` array mein 5 aur items add karo.
      * `styles.item` ka `backgroundColor` badal kar `'#a7f3d0'` (halka green) karo.
      * `Item` component ko modify karo ki woh `title` ke saath `id` bhi dikhaye (jaise: "1. Pehla Item").
13. **📚 Further reading / commands / links:**
      * [FlatList Docs](https://reactnative.dev/docs/flatlist)

-----

### 3.2: SectionList

1.  **🎯 Title / Short Summary:** `SectionList` - List ko groups (sections) mein todna.
2.  **🤔 Kya hai? (What?):** Yeh `FlatList` jaisa hi hai, lekin yeh data ko groups (sections) mein dikhane ke liye bana hai. Har group ka ek "Header" (title) hota hai.
3.  **💡 Kyu important hai? (Why?):** Socho aapko ek contact list (phonebook) banani hai. Saare naam A se, fir B se, fir C se. Yeh groups `SectionList` se hi bante hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab aapka data "grouped" ho. Jaise:
      * Contact list (A, B, C... sections).
      * Settings page (Account, Notifications, Security sections).
      * Zomato par menu (Recommended, Soups, Main Course sections).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko `FlatList` se bohot complex logic likhna padega yeh check karne ke liye ki kab header dikhana hai aur kab item. `SectionList` yeh kaam aapke liye built-in kar deta hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Iska `data` prop, `FlatList` se alag hota hai.
      * `FlatList` ka data: `[ {..}, {..} ]`
      * `SectionList` ka data: `[ {title: 'Section 1', data: [ {..}, {..} ]}, {title: 'Section 2', data: [ {..}, {..} ]} ]`
      * Ismein `renderItem` (item ke liye) aur `renderSectionHeader` (header ke liye) alag-alag props hote hain.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, Text, View, SafeAreaView, SectionList, StatusBar } from 'react-native';

    // 1. Data ka format dekho (sections mein)
    const DATA = [
      {
        title: 'Main Courses',
        data: ['Pizza', 'Burger', 'Risotto'],
      },
      {
        title: 'Sides',
        data: ['French Fries', 'Onion Rings', 'Salad'],
      },
      {
        title: 'Drinks',
        data: ['Water', 'Coke', 'Beer'],
      },
    ];

    const App = () => (
      <SafeAreaView style={styles.container}>
        <SectionList
          sections={DATA} // 2. 'data' prop nahi, 'sections' prop use hota hai
          keyExtractor={(item, index) => item + index} // 3. Unique key
          
          // 4. Har item (Pizza, Burger) ko kaise render karein
          renderItem={({ item }) => (
            <View style={styles.item}>
              <Text style={styles.title}>{item}</Text>
            </View>
          )}
          
          // 5. Har section header (Main Courses, Sides) ko kaise render karein
          renderSectionHeader={({ section: { title } }) => (
            <Text style={styles.header}>{title}</Text>
          )}
        />
      </SafeAreaView>
    );

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        paddingTop: StatusBar.currentHeight,
        marginHorizontal: 16,
      },
      item: {
        backgroundColor: '#f9c2ff',
        padding: 20,
        marginVertical: 8,
      },
      header: {
        fontSize: 32,
        backgroundColor: '#fff',
      },
      title: {
        fontSize: 24,
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const DATA = [...]`: Data ka structure dekho. Yeh ek array hai, jiske andar objects hain. Har object mein ek `title` (header ka naam) aur ek `data` (us header ke items) hai.
      * `<SectionList ... />`: `SectionList` component.
      * `sections={DATA}`: Yahan `data` prop nahi, `sections` prop use hota hai.
      * `keyExtractor={(item, index) => item + index}`: Har item ke liye unique key banayi (yahan 'Pizza0', 'Burger1' jaisi banegi).
      * `renderItem={({ item }) => ...}`: Yeh *sirf* items (`'Pizza'`, `'Burger'`) ke liye chalega.
      * `renderSectionHeader={({ section: { title } }) => ...}`: Yeh *sirf* headers (`'Main Courses'`, `'Sides'`) ke liye chalega. Humne `section` object se `title` ko destructure kiya.
      * **🚀 Quick run expected output:** Ek list dikhegi. Pehle "Main Courses" (bade font mein) likha hoga, uske neeche 3 pink item. Fir "Sides" (bade font mein) likha hoga, uske neeche 3 pink item.
8.  **🐞 Common beginner mistakes:**
      * `data` prop use karna (`sections` ki jagah).
      * `data` ka format galat dena (array of sections ki jagah simple array de dena).
      * `renderSectionHeader` prop define karna bhool jaana.
9.  **🌍 Real-world example / use-case:**
      * Phone ki Contacts (A, B, C sections).
      * Settings page (Account, Security, About sections).
      * Music app (Albums, Artists, Playlists sections).
10. **✅ Quick checklist / TL;DR:**
      * Grouped lists ke liye `SectionList` use karo.
      * `data` prop ki jagah `sections` prop use hota hai.
      * Data ka format: `[{ title: 'T1', data: [...] }, { title: 'T2', data: [...] }]`
      * Do render function: `renderItem` aur `renderSectionHeader`.
11. **❓ FAQs:**
      * **Q: `SectionList` vs `FlatList`?**
          * A: `FlatList` = simple list. `SectionList` = grouped list (jismein headers hon). `SectionList` `FlatList` ke upar hi bana hai.
      * **Q: Kya main sections ko "sticky" (chipka hua) bana sakta hoon?**
          * A: Haan\! `stickySectionHeadersEnabled` prop (jo default mein `true` hota hai) se headers scroll karte time top par chipak jaate hain (jaisa phonebook mein hota hai).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `DATA` mein ek naya section "Desserts" add karo, jismein 2 items hon.
      * `styles.header` ka `backgroundColor` badal kar `'#ddd'` (light grey) karo.
13. **📚 Further reading / commands / links:**
      * [SectionList Docs](https://reactnative.dev/docs/sectionlist)

-----

### 3.3: `Image` (Local vs Network images)

1.  **🎯 Title / Short Summary:** `Image` - App mein local (phone se) ya network (internet se) photos dikhana.

2.  **🤔 Kya hai? (What?):** Yeh React Native ka core component hai jo images (tasveerein) display karta hai.

3.  **💡 Kyu important hai? (Why?):** Bina images ke koi app achha nahi lagta. Profile picture, product image, post image - har jagah `Image` component hi use hota hai.

4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi koi static (jaise logo) ya dynamic (jaise profile pic) image dikhani ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka app sirf text-based aur boring lagega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * Image `source` (kahan se aa rahi hai) do tareeke se di jaati hai:
      * **1. Local Images:**
          * Jo image aapke project folder (e.g., `/assets/images/logo.png`) mein pehle se rakhi hai.
          * Inhe `require()` function se load karte hain.
          * `source={require('./assets/logo.png')}`
          * **Fayda:** Turant load hoti hain, internet nahi chahiye. RN inka size automatically manage kar leta hai.
      * **2. Network Images (Internet):**
          * Jo image ek URL (link) se aa rahi hai (e.g., API se profile pic).
          * Inhe `source={{ uri: 'https://...' }}` (object ke andar `uri`) se load karte hain.
          * `source={{ uri: 'https://example.com/image.png' }}`
          * **Zaroori:** Network images ke liye aapko `style` mein `width` aur `height` **hamesha deni padegi**. RN ko pehle se nahi pata hota ki image kitni badi hai.
      * **`ImageBackground`:** Yeh `Image` jaisa hi hai, par yeh image ko *background* mein set karta hai. Aap iske *upar* (children mein) doosre components (jaise `<Text>`) rakh sakte hain.
      * **`FastImage` (Library):** Yeh `react-native-fast-image` (ek library) ka component hai. Yeh `Image` se behtar hai kyunki yeh image ko aggressively **cache** (save) karta hai. Agar aap ek image 10 baar load kar rahe hain, toh `FastImage` use 1 baar download karega aur 9 baar phone ki memory (cache) se dikha dega. Isse app bohot fast ho jaata hai.

7.  **💻 Code example:**

    ```javascript
    // 1. Local image ke liye, pehle use import karo (ya seedha path do)
    // const logo = require('./assets/logo.png'); 
    // (Maanlo aapke paas './assets/logo.png' file hai)

    // 3. FastImage ke liye: npm install react-native-fast-image
    // Phir: cd ios && pod install (ya run-android)
    // import FastImage from 'react-native-fast-image';

    import React from 'react';
    import { StyleSheet, View, Image, ImageBackground, Text, SafeAreaView } from 'react-native';

    const App = () => (
      <SafeAreaView style={styles.container}>
        <Text style={styles.text}>1. Local Image (Logo):</Text>
        {/* Iske liye './assets/icon.png' file project mein honi chahiye */}
        <Image
          style={styles.logo}
          source={require('./assets/icon.png')} 
        />

        <Text style={styles.text}>2. Network Image (Profile Pic):</Text>
        <Image
          style={styles.networkImage} // Width aur Height ZAROORI hai
          source={{ uri: 'https://i.pravatar.cc/150' }}
        />

        <Text style={styles.text}>3. ImageBackground:</Text>
        <ImageBackground
          style={styles.imageBg} // Width/Height isko bhi chahiye
          source={{ uri: 'https://picsum.photos/300/200' }}
        >
          <Text style={styles.bgText}>Text iske UPAR hai</Text>
        </ImageBackground>

        {/* <Text style={styles.text}>4. FastImage (Cached):</Text>
        <FastImage
            style={styles.networkImage}
            source={{
                uri: 'https://i.pravatar.cc/150',
                priority: FastImage.priority.normal, // Priority set kar sakte hain
            }}
            resizeMode={FastImage.resizeMode.contain}
        />
        */}
      </SafeAreaView>
    );

    const styles = StyleSheet.create({
      container: { flex: 1, alignItems: 'center', padding: 20 },
      text: { fontSize: 16, fontWeight: 'bold', marginTop: 15 },
      logo: {
        width: 100,
        height: 100,
      },
      networkImage: {
        width: 150,
        height: 150,
        borderRadius: 75, // Gol (circle) image
      },
      imageBg: {
        width: 300,
        height: 200,
        justifyContent: 'center', // Text ko center mein laane ke liye
        alignItems: 'center',
      },
      bgText: {
        color: 'white',
        fontSize: 24,
        fontWeight: 'bold',
        backgroundColor: '#000000a0', // Taaki text saaf dikhe
      },
    });

    export default App;
    ```

    *(Note: Upar `FastImage` ka code commented hai, kyunki use chalaane ke liye library install karni padegi. Aur Local image ke liye aapke project mein `assets/icon.png` file honi chahiye.)*

    **✍️ Line-by-line explanation:**

      * `<Image style={styles.logo} source={require(...)} />`: Local image. `require` use kiya. Width/Height style se di (haanlaanki RN size detect kar leta hai, par style dena achhi practice hai).
      * `<Image style={styles.networkImage} source={{ uri: ... }} />`: Network image. `source={{ uri: '...' }}` (double curly braces) use kiya. `style` mein `width` aur `height` dena **mandatory** (zaroori) hai.
      * `<ImageBackground ... > ... </ImageBackground>`: `ImageBackground` component. Iske *beech* mein `<Text>` component daala, jo image ke upar dikhega.
      * `borderRadius: 75`: Network image (jo 150x150 thi) ko `borderRadius` (width/2) dekar poora gol (circular) bana diya.
      * **🚀 Quick run expected output:** Screen par 3 images: 1. Aapka local app icon, 2. Ek gol profile picture (Pravatar se), 3. Ek background image (Picsum se) jiske upar text likha ho.

8.  **🐞 Common beginner mistakes:**

      * Network image ke liye `width` aur `height` na dena (image dikhegi hi nahi).
      * `source` prop galat dena. ` source={'https://...'}  ` (galat) ke bajaye `source={{ uri: 'https://...' }}` (sahi) likhna.
      * Bahut badi size ki images (jaise 4000x4000 pixels) app mein use karna, jisse app slow ho jaata hai. Images ko hamesha resize/optimize karna chahiye.
      * `Image` component ke andar text daalne ki koshish karna (uske liye `ImageBackground` hai).

9.  **🌍 Real-world example / use-case:**

      * **Local:** App ka logo, default profile picture, tab bar icons.
      * **Network:** User ki profile picture, Instagram post, product image.
      * **`ImageBackground`:** Home screen par background image jiske upar "Welcome" text ho.
      * **`FastImage`:** **Har network image** ke liye (production apps mein) `FastImage` hi use karna chahiye performance ke liye.

10. **✅ Quick checklist / TL;DR:**

      * Local Image = `source={require('./path.png')}`.
      * Network Image = `source={{ uri: 'https://...' }}`.
      * Network Image ko `width` aur `height` dena zaroori hai.
      * Image ke upar text = `ImageBackground` use karo.
      * Performance (Caching) = `FastImage` (library) use karo.

11. **❓ FAQs:**

      * **Q: Image load na ho toh default image (placeholder) kaise dikhaoon?**
          * A: `Image` component mein `defaultSource` (local image) ya `onError` (jab error aaye tab state set karke doosri image dikhao) props hote hain. `FastImage` yeh behtar handle karta hai.
      * **Q: `resizeMode` kya hota hai?**
          * A: Yeh `style` prop hai. `resizeMode: 'cover'` (poori jagah bhar do, bhale image kat jaaye) (default), `resizeMode: 'contain'` (poori image dikhao, bhale side mein jagah bach jaaye), `resizeMode: 'stretch'` (image ko kheench do).
      * **Q: Image cache (FastImage) kya hota hai?**
          * A: Jab app image download karta hai, toh use phone ki memory mein save kar leta hai. Agli baar wahi image maangne par, `FastImage` use internet se download nahi karta, balki phone se hi utha leta hai. Isse app fast chalta hai aur user ka data bachta hai.

12. **🏋️‍♀️ Practice exercise:**

      * Upar diye code mein `networkImage` ka `uri` badal kar '[https://picsum.photos/200](https://picsum.photos/200)' karo.
      * `networkImage` ka `borderRadius` hata kar dekho (gol se square ho jaayegi).
      * `ImageBackground` mein text ka `color` badal kar `'yellow'` karo.

13. **📚 Further reading / commands / links:**

      * [Image Docs](https://reactnative.dev/docs/image)
      * [ImageBackground Docs](https://reactnative.dev/docs/imagebackground)
      * [react-native-fast-image (Library)](https://github.com/DylanVann/react-native-fast-image)

-----

### 3.4: `Modal` (Popup windows)

1.  **🎯 Title / Short Summary:** `Modal` - Screen ke upar screen dikhana (Popup).
2.  **🤔 Kya hai? (What?):** Yeh ek component hai jo aapke current screen ke *upar* (z-index) ek nayi temporary screen (View) dikhata hai. Jaise "Add to Cart" popup, ya "Are you sure?" dialog.
3.  **💡 Kyu important hai? (Why?):** Yeh user ka poora dhyaan (focus) ek zaroori cheez par laane ke liye hota hai. Jab modal khula hota hai, toh user peeche ki screen par click nahi kar sakta.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab user se koi zaroori input lena ho (jaise form).
      * Jab "Are you sure you want to delete?" jaisa confirmation (puchtaach) karna ho.
      * Image ko full-screen (zoom) karke dikhana ho.
      * **Alternative:** `Alert` (jo next topic hai) simple "OK/Cancel" ke liye hai. `Modal` poore custom UI (design) ke liye hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko user ko doosri screen par (navigation se) le jaana padega, jo chote tasks (jaise "Item added") ke liye achha UX nahi hai. Modal usi screen par popup dikha kar kaam kar deta hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Aapko ek `state` banani padti hai yeh track karne ke liye ki modal dikh raha hai ya nahi.
      * `const [isModalVisible, setModalVisible] = useState(false);`
      * `Modal` component ke 2 zaroori props hain:
        1.  `visible={isModalVisible}`: Yeh batata hai modal dikhega (`true`) ya nahi (`false`).
        2.  `animationType="slide"`: Modal kaise khulega ('slide', 'fade', 'none').
      * `Modal` ke *andar* aap apna poora UI (View, Text, Button) banate hain.
      * Modal band karne wale button (`onPress`) ko `setModalVisible(false)` call karna hota hai.
7.  **💻 Code example:**
    ```javascript
    import React, { useState } from 'react';
    import { Modal, StyleSheet, Text, Pressable, View, Alert } from 'react-native';

    const App = () => {
      // 1. Modal ki visibility ke liye state
      const [modalVisible, setModalVisible] = useState(false);

      return (
        <View style={styles.centeredView}>
          {/* 2. Modal component */}
          <Modal
            animationType="slide" // Niche se upar slide hoga
            transparent={true} // Peeche ka thoda dikhega
            visible={modalVisible} // State se controlled
            onRequestClose={() => {
              // Android back button dabane par
              Alert.alert('Modal has been closed.');
              setModalVisible(!modalVisible);
            }}
          >
            {/* Modal ke andar ka UI */}
            <View style={styles.centeredView}>
              <View style={styles.modalView}>
                <Text style={styles.modalText}>Yeh ek Modal hai!</Text>
                
                {/* 3. Modal ko band karne ka button */}
                <Pressable
                  style={[styles.button, styles.buttonClose]}
                  onPress={() => setModalVisible(false)} // State ko false kiya
                >
                  <Text style={styles.textStyle}>Modal Band Karo</Text>
                </Pressable>
              </View>
            </View>
          </Modal>

          {/* 4. Modal ko kholne ka button */}
          <Pressable
            style={[styles.button, styles.buttonOpen]}
            onPress={() => setModalVisible(true)} // State ko true kiya
          >
            <Text style={styles.textStyle}>Modal Kholo</Text>
          </Pressable>
        </View>
      );
    };

    const styles = StyleSheet.create({
      centeredView: { // Yeh style main screen aur modal, dono ko center karne ke liye
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 22,
      },
      modalView: { // Modal ka dabba
        margin: 20,
        backgroundColor: 'white',
        borderRadius: 20,
        padding: 35,
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        shadowRadius: 4,
        elevation: 5,
      },
      button: {
        borderRadius: 20,
        padding: 10,
        elevation: 2,
      },
      buttonOpen: {
        backgroundColor: '#F194FF',
      },
      buttonClose: {
        backgroundColor: '#2196F3',
      },
      textStyle: {
        color: 'white',
        fontWeight: 'bold',
        textAlign: 'center',
      },
      modalText: {
        marginBottom: 15,
        textAlign: 'center',
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const [modalVisible, setModalVisible] = useState(false);`: State banayi, shuru mein modal hidden (`false`) hai.
      * `<Modal ... />`: Modal component.
      * `animationType="slide"`: Animation set kiya.
      * `transparent={true}`: Taaki modal ke peeche ki screen (halki) dikhe (agar `modalView` poori screen nahi leta).
      * `visible={modalVisible}`: Modal ki visibility ko `modalVisible` state se joda.
      * `<View style={styles.modalView}>`: Modal ke andar ka poora UI (dabba) yahan banaya.
      * `<Pressable ... onPress={() => setModalVisible(false)}>`: Modal ke andar "Band Karo" button, jo state ko `false` karke modal ko band kar deta hai.
      * `<Pressable ... onPress={() => setModalVisible(true)}>`: Yeh button Modal ke *bahar* (main screen par) hai. Yeh state ko `true` karke modal ko kholta hai.
      * **🚀 Quick run expected output:** Screen par ek button "Modal Kholo" dikhega. Use dabane par, neeche se ek white popup (modal) slide ho kar upar aayega. Us modal mein "Modal Band Karo" button hoga, jise dabane par modal vaapas neeche chala jaayega.
8.  **🐞 Common beginner mistakes:**
      * `visible` prop ko state se control na karna.
      * Modal ko band karne ka button (`setModalVisible(false)`) na dena (user phans jaayega).
      * `Modal` ke andar ke content (e.g., `modalView`) ko style na karna (woh poori screen le lega aur ajeeb dikhega).
9.  **🌍 Real-world example / use-case:**
      * Profile picture par click karne par, poori screen par photo dikhana (ek modal hai).
      * "Delete" button dabane par "Are you sure?" ka popup (ek modal hai).
      * `react-native-image-picker` se "Choose from Gallery / Take Photo" ka option (ek modal hai).
10. **✅ Quick checklist / TL;DR:**
      * Modal = Popup.
      * Ek state (`[isVisible, setIsVisible]`) se control hota hai.
      * Zaroori props: `visible`, `animationType`.
      * Modal ke andar "band" karne ka button (jo `setIsVisible(false)` kare) dena zaroori hai.
11. **❓ FAQs:**
      * **Q: `Alert` aur `Modal` mein kya fark hai?**
          * A: `Alert` (next topic) OS ka default popup hai (simple OK/Cancel). Aap use style nahi kar sakte. `Modal` 100% customizable hai, aap uske andar poora `View` bana sakte hain.
      * **Q: Main modal ke peeche click karke use band kaise karoon?**
          * A: Aap `Modal` ke root `<View>` (e.g., `centeredView`) ko `Pressable` bana sakte hain jo `setModalVisible(false)` call kare. (Iske liye thoda logic lagana padta hai taaki modal *content* par click karne se modal band na ho).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `animationType` ko `"slide"` se `"fade"` karke dekho.
      * Modal ke andar "Cancel" button ke saath ek "OK" button bhi add karo (jo `Alert` dikhaye aur fir modal band kare).
13. **📚 Further reading / commands / links:**
      * [Modal Docs](https://reactnative.dev/docs/modal)

-----

### 3.5: `Alert`

1.  **🎯 Title / Short Summary:** `Alert` - Simple (OK/Cancel) popup dikhana.
2.  **🤔 Kya hai? (What?):** Yeh ek API (component nahi) hai jo OS (Android/iOS) ka default *native* alert/dialog box dikhata hai.
3.  **💡 Kyu important hai? (Why?):** Yeh user se jaldi se "Haan/Nahi" (Yes/No) ya "OK" mein jawaab lene ka sabse aasan tareeka hai. Iske liye koi UI design nahi karna padta.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * User ko "Changes saved successfully" jaisi simple information dene ke liye.
      * User se "Are you sure you want to logout?" jaisa simple confirmation lene ke liye (jismein 2-3 button hon).
      * **Nahi use karein:** Jab aapko popup mein image, icon, ya custom text (jaise `TextInput`) dikhana ho. Uske liye `Modal` (previous topic) use hota hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Simple "OK" message ke liye bhi aapko poora `Modal` (state, UI) banana padega, jo bohot zyada kaam hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `Alert` ko `react-native` se import karna padta hai.
      * Iska sabse common function hai: `Alert.alert(title, message, buttons, options)`.
        1.  `title`: Popup ka title (e.g., "Success").
        2.  `message`: Popup ka message (e.g., "Data saved.").
        3.  `buttons`: Ek array, jismein buttons (up to 3) define karte hain (e.g., [{text: 'OK'}, {text: 'Cancel'}]).
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { View, StyleSheet, Button, Alert } from 'react-native';

    const App = () => {
      // 1. Simple 1-Button Alert (Sirf info)
      const createSimpleAlert = () =>
        Alert.alert(
          'Saved!', // Title
          'Your changes have been saved successfully.', // Message
          [{ text: 'OK', onPress: () => console.log('OK Pressed') }] // Button
        );

      // 2. 2-Button Alert (Confirmation)
      const createTwoButtonAlert = () =>
        Alert.alert(
          'Logout?', // Title
          'Are you sure you want to logout?', // Message
          [
            {
              text: 'Cancel',
              onPress: () => console.log('Cancel Pressed'),
              style: 'cancel', // 'cancel' style iOS par special dikhta hai
            },
            {
              text: 'Logout',
              onPress: () => console.log('Logout Pressed'),
              style: 'destructive', // 'destructive' (red) iOS par
            },
          ]
        );

      // 3. 3-Button Alert (Android only, iOS 2 dikhayega)
      const createThreeButtonAlert = () =>
        Alert.alert(
          'Update?',
          'Update app to new version?',
          [
            { text: 'Later', onPress: () => console.log('Later Pressed') },
            { text: 'Cancel', onPress: () => {}, style: 'cancel' },
            { text: 'Update Now', onPress: () => console.log('Update Pressed') },
          ],
          { cancelable: false } // User bahar click karke band nahi kar sakta
        );

      return (
        <View style={styles.container}>
          <Button title={'1-Button Alert'} onPress={createSimpleAlert} />
          <View style={styles.spacing} />
          <Button title={'2-Button Alert'} onPress={createTwoButtonAlert} />
          <View style={styles.spacing} />
          <Button title={'3-Button Alert'} onPress={createThreeButtonAlert} />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      },
      spacing: {
        marginVertical: 10,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... Alert } from 'react-native';`: `Alert` API ko import kiya.
      * `Alert.alert(...)`: `alert` function ko call kiya.
      * `createSimpleAlert`: Simple alert. `title`, `message`, aur ek `buttons` array (jismein 1 object hai).
      * `createTwoButtonAlert`: 2 buttons wala alert.
      * `style: 'cancel'`: Isse iOS samajh jaata hai ki yeh "cancel" action hai (aur use alag style deta hai).
      * `style: 'destructive'`: Isse iOS samajh jaata hai ki yeh "delete" ya "logout" jaisa action hai (aur use red color deta hai).
      * `createThreeButtonAlert`: 3 buttons (Android par 3 dikhenge, iOS par 2 hi dikh sakte hain).
      * `{ cancelable: false }`: (Android only) Is option se user alert ke bahar (grey area) tap karke use dismiss nahi kar sakta.
      * **🚀 Quick run expected output:** 3 buttons. Har ek ko dabane par alag-alag native alert popup (OS ka default) dikhega.
8.  **🐞 Common beginner mistakes:**
      * `Alert` ko JSX mein component jaise use karna (`<Alert />` ❌ Galat). Yeh ek function hai, jo `onPress` mein call hota hai (`Alert.alert(...)` ✅ Sahi).
      * `Alert.alert` ko `title` na dena. Title hamesha zaroori hai.
      * 3 se zyada buttons dene ki koshish karna (Android par 3 max, iOS par 2 hi achhe dikhte hain).
9.  **🌍 Real-world example / use-case:**
      * "Are you sure you want to delete this post?" (Buttons: "Cancel", "Delete").
      * "Invalid Password" (Buttons: "OK").
      * "Please enable location services" (Buttons: "Cancel", "Open Settings").
10. **✅ Quick checklist / TL;DR:**
      * Simple, native OK/Cancel popups ke liye.
      * `Alert.alert(title, message, buttons)` function call hai.
      * Yeh component nahi hai.
      * Style nahi kar sakte.
      * Custom UI (image/input) ke liye `Modal` use karo.
11. **❓ FAQs:**
      * **Q: Main Alert mein `TextInput` (input box) kaise daaloon?**
          * A: `Alert.prompt()` (iOS only) se kar sakte hain, lekin yeh cross-platform nahi hai. Best tareeka hai ki aap `Modal` use karein aur uske andar khud ka `TextInput` banayein.
      * **Q: `Alert` vs `Modal` (dobara)?**
          * A: `Alert` = Tez, simple, native, 2-3 button, no style. `Modal` = Custom, poora UI, slow, state management chahiye.
12. **🏋️‍♀️ Practice exercise:**
      * Ek naya button banao "Delete". `onPress` par woh `createTwoButtonAlert` jaisa hi alert dikhaye, par `title` "Delete Post?" ho.
      * `createSimpleAlert` mein `OK` button ka `onPress` change karke ek `Alert.alert('OK')` (simple) dikhao.
13. **📚 Further reading / commands / links:**
      * [Alert Docs](https://reactnative.dev/docs/alert)

-----

### 3.6: `react-native-swiper`

1.  **🎯 Title / Short Summary:** `react-native-swiper` - Swipable (scrollable) pages/images (Carousel).
2.  **🤔 Kya hai? (What?):** Yeh ek third-party **library** hai (React Native mein built-in nahi hai). Yeh aapko "carousel" ya "swiper" banane deta hai, jaise app ki intro screens (walkthrough) ya image gallery.
3.  **💡 Kyu important hai? (Why?):** User ko app ka introduction (Page 1, Page 2, Page 3 swipe karke) dena ya ek product ki multiple images (swipe kar-karke) dikhana bohot common hai. Yeh library is kaam ko bohot aasan bana deti hai.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * App ka "Onboarding" / "Walkthrough" (Intro screens) banane ke liye.
      * Image gallery (carousel) dikhane ke liye.
      * Banners (jaise Swiggy app mein top par offers) dikhane ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko yeh poora swipe logic (scroll detection, active dot, etc.) `ScrollView` ya `FlatList` se *khud* banana padega, jo bohot complex (mushkil) hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install react-native-swiper`
      * **Step 2:** Import karo: `import Swiper from 'react-native-swiper'`
      * **Step 3:** `Swiper` component ke andar *children* (bachhe) ke roop mein `View` (ya `Image`) daalo. Har `View` (child) ek alag slide/page ban jaayega.
      * Iske props se aap ise control kar sakte hain (jaise `showsButtons={true}` ya `loop={false}`).
7.  **💻 Code example:** (Simple App Intro)
    ```javascript
    // 1. Pehle: npm install react-native-swiper
    import React from 'react';
    import { StyleSheet, Text, View } from 'react-native';
    import Swiper from 'react-native-swiper'; // 2. Import karo

    const App = () => {
      return (
        // 3. Swiper component
        <Swiper 
          style={styles.wrapper} 
          showsButtons={true} // Aage/Peeche ke button dikhao
          loop={false} // Aakhri slide ke baad vaapas pehli par mat jao
          activeDotColor="#FF6347" // Active dot ka color
        >
          {/* Slide 1 */}
          <View style={styles.slide1}>
            <Text style={styles.text}>Hello Swiper</Text>
          </View>
          
          {/* Slide 2 */}
          <View style={styles.slide2}>
            <Text style={styles.text}>Beautiful</Text>
          </View>
          
          {/* Slide 3 */}
          <View style={styles.slide3}>
            <Text style={styles.text}>And simple</Text>
          </View>
        </Swiper>
      );
    };

    const styles = StyleSheet.create({
      wrapper: {},
      // Har slide ke liye alag style (taaki background color alag ho)
      slide1: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#9DD6EB',
      },
      slide2: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#97CAE5',
      },
      slide3: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#92BBD9',
      },
      text: {
        color: '#fff',
        fontSize: 30,
        fontWeight: 'bold',
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import Swiper from 'react-native-swiper';`: Library ko import kiya.
      * `<Swiper ...>`: `Swiper` component ko (props ke saath) use kiya.
      * `showsButtons={true}`: Left (`<`) aur Right (`>`) arrows dikhayega.
      * `loop={false}`: Aakhri (teesri) slide se aage swipe karne par pehli slide par nahi jaayega.
      * `activeDotColor="#FF6347"`: Neeche jo 3 dots (pagination) hain, unme se active dot ka color set kiya.
      * `<View style={styles.slide1}>`: Yeh pehli slide hai.
      * `<View style={styles.slide2}>`: Yeh doosri slide hai.
      * `<View style={styles.slide3}>`: Yeh teesri slide hai.
      * **🚀 Quick run expected output:** Ek full-screen swiper dikhega. Pehli slide blue ("Hello Swiper") hogi. Aap right swipe karke doosri slide ("Beautiful") aur fir teesri ("And simple") par jaa sakte hain. Neeche 3 dots dikhenge (active dot red hoga) aur side mein arrows.
8.  **🐞 Common beginner mistakes:**
      * `npm install` ke baad app ko rebuild (run-android) na karna.
      * `Swiper` ko `flex: 1` (ya height) na dena, jisse woh dikhta nahi hai (upar ke example mein har slide ko `flex: 1` diya hai, jisse Swiper ne poori height le li).
      * `loop={true}` (jo default hai) chhod dena intro screens ke liye (user "Next" karte-karte vaapas pehli screen par aa jaata hai).
9.  **🌍 Real-world example / use-case:**
      * Har app ki pehli baar khulne wali "Welcome" / "Next" / "Next" / "Get Started" screens.
      * Amazon/Flipkart par product image gallery.
      * Zomato/Swiggy par top offer banners.
10. **✅ Quick checklist / TL;DR:**
      * Yeh ek *library* hai, install karni padti hai.
      * Carousel/Swiper banane ke liye hai.
      * `Swiper` ke andar har `View` ek alag slide hoti hai.
      * Props (jaise `loop`, `showsButtons`) se control hota hai.
11. **❓ FAQs:**
      * **Q: `FlatList` se swiper bana sakte hain?**
          * A: Haan\! `FlatList` mein `horizontal={true}` aur `pagingEnabled={true}` props daal kar aap simple swiper bana sakte hain (jo ek baar mein ek poora item scroll kare). `react-native-swiper` aapko dots, buttons, aur zyada control deta hai.
      * **Q: Yeh library (react-native-swiper) best hai?**
          * A: Yeh popular hai. Aajkal, log `react-native-reanimated` ke saath `react-native-pager-view` ya `FlatList` ko combine karke zyada smooth, custom carousels bana rahe hain (advanced). Lekin shuru ke liye yeh library achhi hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `loop={true}` karke dekho (aakhri slide se pehli par aa jaoge).
      * `showsButtons={false}` karke arrows hata do.
      * Ek chauthi slide add karo.
13. **📚 Further reading / commands / links:**
      * [react-native-swiper (GitHub Docs)](https://github.com/leecade/react-native-swiper)

-----

Module 3 complete\! Ab aap lists, images, aur popups (Modals/Alerts) handle karna jaante hain. Yeh 3 cheezein har app mein hoti hain.

Jab aap taiyaar hon, toh **"Module 4 ke notes do"** bolna\! 🧑‍💻

=============================================================

# MODULE-4 → UI Controls & Core APIs

### 4.1: `Pressable` (Modern touch handling)

1.  **🎯 Title / Short Summary:** `Pressable` - Touch (tap) handle karne ka naya aur sabse flexible tareeka.
2.  **🤔 Kya hai? (What?):** Yeh ek core component hai jo `TouchableOpacity`, `TouchableHighlight` aur `TouchableWithoutFeedback` sab ki functionality *ek* component mein deta hai. Yeh modern touch handling ke liye banaya gaya hai.
3.  **💡 Kyu important hai? (Why?):** Yeh aapko `onPressIn` (jab touch shuru ho), `onPressOut` (jab touch chhodein) jaise events par *state* (style) badalne ki power deta hai. Jaise, aap button ko "daba hua" (pressed) dikha sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):** **Hamesha.** Naye code mein `TouchableOpacity` ki jagah `Pressable` use karna best practice maana jaata hai. Jab bhi aapko complex feedback (jaise button dabane par chota ya alag color ka dikhana) chahiye ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap purane `TouchableOpacity` (jo fade hota hai) ya `TouchableHighlight` (jo highlight hota hai) use karenge. Woh bhi theek hain, lekin `Pressable` aapko zyada control deta hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `Pressable` bhi ek wrapper component hai (iske andar child daalna hota hai).
      * Iska `style` prop ek function bhi le sakta hai\!
      * Yeh function `({ pressed }) => [...]` jaisa hota hai.
      * `pressed` ek boolean (`true`/`false`) hai jo batata hai ki user ne component ko daba rakha hai ya nahi.
      * Isse aap "pressed" state ke liye alag style de sakte hain.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { View, Text, StyleSheet, Pressable, Alert } from 'react-native';

    const App = () => {
      return (
        <View style={styles.container}>
          <Pressable
            onPress={() => Alert.alert('Simple Press!')}
            onLongPress={() => Alert.alert('Long Press!')} // Der tak dabane par
            // 1. Style as a function
            style={({ pressed }) => [
              styles.button,
              {
                // 2. Agar 'pressed' hai, toh opacity kam karo
                opacity: pressed ? 0.5 : 1,
                backgroundColor: pressed ? 'rgb(210, 230, 255)' : 'rgb(0, 122, 255)',
              }
            ]}
          >
            {/* 3. Child ko bhi function bana sakte hain */}
            {({ pressed }) => (
              <Text style={styles.text}>
                {pressed ? 'Daba diya!' : 'Mujhe Dabao'}
              </Text>
            )}
          </Pressable>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      button: {
        paddingVertical: 12,
        paddingHorizontal: 32,
        borderRadius: 4,
        elevation: 3,
      },
      text: {
        fontSize: 16,
        lineHeight: 21,
        fontWeight: 'bold',
        letterSpacing: 0.25,
        color: 'white',
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `onLongPress={...}`: `Pressable` yeh event bhi support karta hai.
      * `style={({ pressed }) => [...]}`: Style ko ek function banaya jo `pressed` state receive karta hai.
      * `opacity: pressed ? 0.5 : 1`: Yeh "ternary operator" hai. "Agar `pressed` true hai, toh opacity `0.5` rakho, varna `1` rakho." (Yeh `TouchableOpacity` jaisa effect dega).
      * `backgroundColor: ...`: "Agar `pressed` true hai, toh light blue, varna dark blue rakho." (Yeh `TouchableHighlight` jaisa effect dega).
      * `{({ pressed }) => ( ... )}`: `Pressable` ke andar *child* (Text) ko bhi ek function bana diya taaki "pressed" state ke basis par text badal sakein.
      * **🚀 Quick run expected output:** Ek blue button dikhega. Jab aap use daba kar rakhenge, toh woh light blue ho jaayega, opacity kam ho jaayegi, aur text "Daba diya\!" ho jaayega. Chhodne par "Simple Press\!" alert aayega.
8.  **🐞 Common beginner mistakes:**
      * `style` ko function ki tarah use na karna aur "pressed" state ka fayda na uthana.
      * `Pressable` ke andar `Text` (ya child) daalna bhool jaana.
9.  **🌍 Real-world example / use-case:** Har modern button, card, ya list item jo `TouchableOpacity` se banta tha, ab `Pressable` se banaya jaa sakta hai.
10. **✅ Quick checklist / TL;DR:**
      * `Pressable` sabhi `Touchable` ka modern replacement hai.
      * `style` aur `children` ko function bana kar `pressed` state access kar sakte hain.
      * `onPress`, `onLongPress`, `onPressIn`, `onPressOut` sab support karta hai.
11. **❓ FAQs:**
      * **Q: Toh kya main `TouchableOpacity` use karna band kar doon?**
          * A: Zaroori nahi. Simple fade effect ke liye `TouchableOpacity` abhi bhi aasan hai. Lekin `Pressable` zyada powerful aur future-proof hai.
      * **Q: Yeh `TouchableOpacity` se fast hai?**
          * A: Performance mein koi khaas fark nahi hai. Yeh flexibility ke liye banaya gaya hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein, `pressed` state par `backgroundColor` badalne wala code hata do, sirf `opacity` wala rehne do.
      * Ek naya `Pressable` banao jo `onPressIn` par `console.log('Dabana shuru kiya')` aur `onPressOut` par `console.log('Dabana band kiya')` print kare.
13. **📚 Further reading / commands / links:**
      * [Pressable Docs](https://reactnative.dev/docs/pressable)

-----

### 4.2: Switch (Toggle on/off)

1.  **🎯 Title / Short Summary:** `Switch` - "On/Off" (true/false) toggle button.
2.  **🤔 Kya hai? (What?):** Yeh ek simple UI control hai jo user ko do options (jaise On/Off ya Yes/No) ke beech "switch" karne deta hai.
3.  **💡 Kyu important hai? (Why?):** Settings screen ke liye yeh bohot zaroori hai. (e.g., "Enable Notifications", "Dark Mode").
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko user se `true` ya `false` mein input lena ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko `Button` ya `Pressable` se "On" / "Off" likh kar custom toggle banana padega, jo native `Switch` jaisa achha nahi dikhega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `Switch` ko *hamesha* `useState` ke saath use kiya jaata hai.
      * Aap ek state banate hain: `const [isEnabled, setIsEnabled] = useState(false);`
      * `Switch` ko 2 zaroori props chahiye:
        1.  `value={isEnabled}`: Switch ko batata hai ki woh On (`true`) hai ya Off (`false`).
        2.  `onValueChange={setIsEnabled}`: Jab user switch ko tap karta hai, toh yeh function naye value (`true` ya `false`) ke saath call hota hai aur state ko update kar deta hai.
7.  **💻 Code example:**
    ```javascript
    import React, { useState } from 'react';
    import { View, Switch, StyleSheet, Text } from 'react-native';

    const App = () => {
      // 1. State banayi (default mein 'false' ya 'off')
      const [isEnabled, setIsEnabled] = useState(false);
      
      // 2. Yeh function state ko toggle karega
      const toggleSwitch = () => setIsEnabled(previousState => !previousState);
      
      const [isDarkMode, setIsDarkMode] = useState(true);

      return (
        <View style={styles.container}>
          <Text style={styles.text}>{isEnabled ? 'Notifications ON' : 'Notifications OFF'}</Text>
          
          <Switch
            trackColor={{ false: '#767577', true: '#81b0ff' }} // Off/On mein track ka color
            thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'} // Button ka color
            ios_backgroundColor="#3e3e3e" // iOS par track ka default color
            onValueChange={toggleSwitch} // 3. Value badalne par function call
            value={isEnabled} // 4. Current value (state se)
          />
          
          <Text style={styles.text}>{isDarkMode ? 'Dark Mode ON' : 'Dark Mode OFF'}</Text>
          <Switch
            // Simple tareeka (seedha function pass karna)
            onValueChange={setIsDarkMode} // Yeh 'newValue' seedha state mein set kar dega
            value={isDarkMode}
          />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
      },
      text: {
        fontSize: 18,
        marginVertical: 10,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const [isEnabled, setIsEnabled] = useState(false);`: `isEnabled` state banayi.
      * `const toggleSwitch = () => ...`: Ek function banaya jo state ki purani value (`previousState`) ko "ulta" (`!`) kar deta hai (true ko false, false ko true).
      * `trackColor={{...}}`: Prop jo batata hai ki switch ka "track" (patti) `false` (off) hone par kaisa dikhega aur `true` (on) hone par kaisa.
      * `thumbColor={...}`: Prop jo "thumb" (gol button) ka color batata hai.
      * `onValueChange={toggleSwitch}`: Jab switch tap hoga, `toggleSwitch` function call hoga.
      * `value={isEnabled}`: Switch ki current position `isEnabled` state se control ho rahi hai.
      * `onValueChange={setIsDarkMode}`: Yeh `toggleSwitch` ka shortcut hai. `onValueChange` naye value (true ya false) ko `setIsDarkMode` function mein *automatic* pass kar deta hai.
      * **🚀 Quick run expected output:** Screen par 2 toggle switch dikhenge. Pehla "Notifications" ke liye (custom colors ke saath) aur doosra "Dark Mode" ke liye (default colors). Unhe tap karne se unka text (ON/OFF) badlega.
8.  **🐞 Common beginner mistakes:**
      * `value` prop ko state se connect na karna.
      * `onValueChange` prop na dena (switch hilega hi nahi).
      * `onValueChange` mein naye value ko set karne ke bajaye purana value set kar dena.
9.  **🌍 Real-world example / use-case:**
      * Settings mein "Dark Mode" toggle.
      * "Save my password" toggle.
      * "Enable Bluetooth" toggle.
10. **✅ Quick checklist / TL;DR:**
      * `Switch` = On/Off (true/false) input.
      * `useState` (e.g., `isEnabled`) ke saath control hota hai.
      * Zaroori props: `value={isEnabled}` aur `onValueChange={setIsEnabled}`.
11. **❓ FAQs:**
      * **Q: Iska size (bada/chota) kar sakta hoon?**
          * A: Default `Switch` component ka size badalna mushkil hai. Iske liye `style={{ transform: [{ scale: 1.5 }] }}` jaisa hack use karna padta hai, ya custom library use karni padti hai.
      * **Q: Iske saath "On" / "Off" text kaise likhoon?**
          * A: `Switch` ke andar text nahi jaata. Aapko `Switch` ke *bagal* mein (side mein) `<Text>` component rakhna padta hai, jaisa upar example mein hai.
12. **🏋️‍♀️ Practice exercise:**
      * Ek teesra switch "Enable WiFi" banao jo default mein `true` (on) ho.
13. **📚 Further reading / commands / links:**
      * [Switch Docs](https://reactnative.dev/docs/switch)

-----

### 4.3: `ScrollView` (Simple scrolling content)

1.  **🎯 Title / Short Summary:** `ScrollView` - Jab content screen se bada ho (simple scrolling).
2.  **🤔 Kya hai? (What?):** Yeh ek generic (aam) scrolling container hai. Aap iske andar jo bhi content (`View`, `Text`, `Image`) daalenge, agar woh screen se lamba (ya chauda) ho jaata hai, toh user use scroll kar paayega.
3.  **💡 Kyu important hai? (Why?):** By default, React Native mein kuch scroll nahi hota. Agar content screen ke neeche chala gaya, toh woh *hamesha* ke liye neeche chala gaya. `ScrollView` us content ko scrollable banata hai.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab aapke paas *kam* (finite) content ho jo screen se thoda bada ho sakta hai. Jaise: Ek "Article" page, ek "Settings" page, ek "About Us" page.
      * **Alternative:** Agar aapke paas *lambi* ya *infinite* list (1000 items) hai, toh `ScrollView` **USE NAHI KARNA** hai. Uske liye `FlatList` (Module 3.1) use hota hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka content (jo screen ke neeche hai) user ko kabhi dikhega hi nahi. Aur agar `TextInput` (keyboard ke saath) use kar rahe hain, toh keyboard content ko chupa (block) dega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `ScrollView` ko `View` ki tarah hi use karte hain, bas iske andar ka content scrollable ho jaata hai.
      * **`FlatList` vs `ScrollView` (Sabse zaroori):**
          * `ScrollView`: Iske andar ka *saara* content (bhale 100 items hon) ek saath render kar deta hai. Chhoti list ke liye theek hai, badi list (100+ items) ke liye app crash kar dega.
          * `FlatList`: Sirf wahi item render karta hai jo screen par dikh rahe hain ("Lazy Loading"). Badi lists ke liye yahi use hota hai.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native';

    const App = () => {
      return (
        <SafeAreaView style={styles.container}>
          {/* 1. ScrollView component */}
          <ScrollView style={styles.scrollView}>
            <Text style={styles.text}>
              Yeh ek bohot lamba text hai. React Native mein, content by default
              scroll nahi hota. Agar aapka content screen se bada hai, toh
              aapko use 'ScrollView' ke andar daalna padega.
            </textarea>
            {/* ...yahan bohot saara text (ya 30-40 View) imagine karo... */}
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Scroll ...</Text>
            <Text style={styles.text}>Aap ab neeche pahunch gaye!</Text>
          </ScrollView>
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        paddingTop: StatusBar.currentHeight,
      },
      scrollView: {
        backgroundColor: '#f0f0f0',
        marginHorizontal: 20,
      },
      text: {
        fontSize: 42, // Bada font taaki screen jaldi bhar jaaye
        marginVertical: 10,
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `<SafeAreaView style={styles.container}>`: Main container (taaki content notch ke neeche rahe).
      * `<ScrollView style={styles.scrollView}>`: `ScrollView` ko start kiya. Humne use `View` ki tarah hi style (background color, margin) di.
      * `<Text ...>`: Iske andar humne bohot saara content (bade font mein Text) daal diya.
      * `</ScrollView>`: ScrollView ko band kiya.
      * **🚀 Quick run expected output:** Ek screen dikhegi jismein text hoga. Jab aap swipe (scroll) karenge, toh aap neeche ka content dekh payenge.
8.  **🐞 Common beginner mistakes:**
      * **`FlatList` ki jagah `ScrollView` use karna.** Badi list (API se aayi hui) ko `.map()` karke `ScrollView` mein daalna sabse badi performance galti hai.
      * `ScrollView` ko `flex: 1` na dena (jab zaroorat ho), jisse woh poori screen ki height nahi leta.
      * `ScrollView` ke andar `FlatList` daalna (Virtualization Error aayega).
9.  **🌍 Real-world example / use-case:**
      * Blog post (article) padhne wali screen.
      * Terms & Conditions page.
      * Ek form (jaise Signup form) jo choti screens par lamba ho sakta hai.
10. **✅ Quick checklist / TL;DR:**
      * Content ko scrollable banata hai.
      * *Saara* content ek saath render karta hai (slow).
      * Sirf *chote* content (Article, Form) ke liye use karo.
      * Badi list ke liye `FlatList` use karo.
11. **❓ FAQs:**
      * **Q: Horizontal (left-right) scroll kaise karoon?**
          * A: `ScrollView` ko `horizontal={true}` prop do. Aur andar ke items ko `flexDirection: 'row'` do. (Jaise "Stories" bar).
      * **Q: "Pull to Refresh" kaise add karoon?**
          * A: `ScrollView` mein `RefreshControl` prop hota hai. (Thoda advanced hai).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein 20 aur `<Text>` items add karo.
      * `horizontal={true}` prop add karke dekho kya hota hai (ab aap left-right scroll kar payenge, upar-neeche nahi).
13. **📚 Further reading / commands / links:**
      * [ScrollView Docs](https://reactnative.dev/docs/scrollview)

-----

### 4.4: `View` Component (The `div` of React Native)

1.  **🎯 Title / Short Summary:** `View` - React Native ka `<div>`. Layout banane ka basic dabba (container) 📦.
2.  **🤔 Kya hai? (What?):** Yeh React Native ka sabse fundamental (buniyaadi) component hai. Yeh ek container (dabba) hai jo doosre components (jaise `Text`, `Image`, ya doosre `View`) ko hold (rakhne) ke liye use hota hai.
3.  **💡 Kyu important hai? (Why?):** Aap `View` ke bina layout (design) bana hi nahi sakte. Har cheez (buttons, text) ko group karne, style karne (background, border, padding), aur align (Flexbox) karne ke liye `View` hi use hota hai.
4.  **⏰ Kab/use karna chahiye? (When?):** **Hamesha.** Har screen `View` se hi shuru hoti hai. Jab bhi aapko 2 `Text` ko ek saath rakhna ho, ya kisi cheez ko background color dena ho, aap `View` use karenge.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap layout nahi bana payenge. Aap `Text` ya `Image` ko `margin`, `padding`, ya `backgroundColor` nahi de payenge (dena bhi nahi chahiye, unhe `View` mein wrap karna chahiye).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * `View` HTML ke `<div>` tag jaisa hai.
      * Yeh khud screen par kuch nahi dikhata (jab tak aap ise `style` na dein).
      * Iska main kaam hai:
        1.  **Grouping:** Doosre components ko ek saath group karna.
        2.  **Styling:** Group par `style` (background, margin, padding, border) lagana.
        3.  **Layout:** `flexbox` (Module 6) ka istemaal karke items ko align karna (e.g., `flexDirection: 'row'` se cheezon ko side-by-side rakhna).
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, View, Text } from 'react-native';

    const App = () => {
      return (
        // 1. Root View (poori screen)
        <View style={styles.container}>
          
          {/* 2. Ek card banane ke liye View */}
          <View style={styles.card}>
            <Text style={styles.title}>Title</Text>
            <Text style={styles.subtitle}>Subtitle</Text>
          </View>

          {/* 3. Cheezon ko side-by-side (row) rakhne ke liye View */}
          <View style={styles.rowContainer}>
            <View style={styles.box} />
            <View style={styles.box} />
            <View style={styles.box} />
          </View>
          
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { // Root View
        flex: 1,
        backgroundColor: '#f0f0f0',
        padding: 20,
      },
      card: { // Card View
        backgroundColor: 'white',
        padding: 16,
        borderRadius: 8,
        marginBottom: 20,
      },
      title: { fontSize: 18, fontWeight: 'bold' },
      subtitle: { fontSize: 14, color: 'gray' },
      rowContainer: { // Row View
        flexDirection: 'row', // Yahan se layout badla
        justifyContent: 'space-around', // Beech mein space do
      },
      box: { // Box View
        width: 50,
        height: 50,
        backgroundColor: 'skyblue',
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... View, Text } from 'react-native';`: `View` ko import kiya.
      * `<View style={styles.container}>`: Yeh poori screen ka main (root) container hai. Ise `flex: 1` (poori screen lo) aur background color diya.
      * `<View style={styles.card}>`: Yeh ek dabba (container) hai jo 2 `Text` components ko "group" kar raha hai. Humne is `View` ko `backgroundColor: 'white'` aur `padding` dekar "card" jaisa banaya.
      * `<View style={styles.rowContainer}>`: Yeh container 3 `box` ko group kar raha hai.
      * `flexDirection: 'row'`: Is style ne `View` ko bataya ki apne children (box) ko neeche (column - default) nahi, balki *side-by-side* (row) rakho.
      * `<View style={styles.box} />`: Yeh `View` khud (self-closing) hai. Humne ise `width`, `height`, aur `backgroundColor` dekar ek dabba banaya.
      * **🚀 Quick run expected output:** Ek grey background wali screen dikhegi. Top par ek white card (Title/Subtitle ke saath) hoga. Uske neeche, 3 sky-blue color ke dabbe (boxes) ek line (row) mein rakhe honge.
8.  **🐞 Common beginner mistakes:**
      * `Text` ko `View` ke andar na daalna (har `Text` `View` ke andar hi hona chahiye, ya `Text` ke andar).
      * `Text` ki jagah `View` use karna. (`<View>Sirf text</View>` ❌ Galat. Text hamesha `<Text>` component mein hona chahiye).
      * Style ko `View` ke bajaye `Text` par lagana (jaise `margin`, `padding`). Styling hamesha container `View` par lagani chahiye.
9.  **🌍 Real-world example / use-case:** Har screen, har component, har card, har header `View` se hi banta hai.
10. **✅ Quick checklist / TL;DR:**
      * `View` = `div`.
      * Main kaam: Grouping, Styling, Layout.
      * Text hamesha `<Text>` mein hona chahiye, `View` mein nahi.
      * `flexbox` (layout) `View` par hi lagta hai.
11. **❓ FAQs:**
      * **Q: `View` aur `SafeAreaView` (Module 4.9) mein kya fark hai?**
          * A: `SafeAreaView` ek *special* `View` hai jo (sirf iOS par) content ko phone ke notch (top) aur home bar (neeche) ke neeche jaane se *bachata* hai. `View` aisa nahi karta.
      * **Q: `View` par `onPress` laga sakta hoon?**
          * A: Nahi. `View` touch (tap) handle nahi karta. Agar `View` ko clickable banana hai, toh use `Pressable` (Module 4.1) ya `TouchableOpacity` ke andar wrap (daalna) padega.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `rowContainer` ke neeche ek naya `View` (style `footer`) banao aur use `backgroundColor: 'gray'` aur `height: 50` do.
      * `card` ka `backgroundColor` badal kar `'lightyellow'` karo.
13. **📚 Further reading / commands / links:**
      * [View Docs](https://reactnative.dev/docs/view)
      * [Layout with Flexbox (Module 6)](https://reactnative.dev/docs/flexbox)

-----

### 4.5: `Text` Component (Saara text isme)

1.  **🎯 Title / Short Summary:** `Text` - Screen par koi bhi text (likhaavat) dikhane ke liye ✍️.
2.  **🤔 Kya hai? (What?):** Yeh ek core component hai jiske andar aap *sirf* text (string) ya doosre `Text` components ko daal sakte hain.
3.  **💡 Kyu important hai? (Why?):** React Native mein aap `View` ke andar seedha text nahi likh sakte. (`<View>Hello</View>` ❌ Error dega). Har text ko `<Text>` component ke andar wrap karna zaroori hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Hamesha jab bhi screen par kuch likhna ho. Title, paragraph, button ka label (agar `Pressable` use kar rahe hain), sabkuch.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka app error dega. "Text strings must be rendered within a \<Text\> component."
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh HTML ke `<p>` ya `<span>` jaisa hai.
      * Saari text styling (`fontSize`, `color`, `fontWeight`, `textAlign`) isi component par lagti hai.
      * **Nesting:** Aap `Text` ke andar `Text` daal sakte hain (Nesting). Isse aap ek hi line mein alag-alag style de sakte hain.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, View, Text } from 'react-native';

    const App = () => {
      return (
        <View style={styles.container}>
          {/* 1. Simple Text with styling */}
          <Text style={styles.title}>Main Title Hoon</Text>
          
          <Text style={styles.paragraph}>
            Yeh ek normal paragraph hai. Text ko hamesha 
            {/* 2. Nested Text (styling ke liye) */}
            <Text style={styles.bold}> {` <Text> `} </Text>
            component ke andar hona chahiye.
          </Text>

          {/* 3. Text Nesting (inheritance) */}
          <Text style={styles.parentText}>
            Main parent text hoon (Red).
            <Text style={styles.childText}> Main child hoon (Blue).</Text>
            Ab vaapas parent (Red).
          </Text>
          
          {/* 4. Clickable Text */}
          <Text 
            style={styles.link}
            onPress={() => alert('Link Clicked!')}
          >
            Main ek clickable link jaisa text hoon.
          </Text>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, padding: 20, paddingTop: 60 },
      title: {
        fontSize: 24,
        fontWeight: 'bold', // 'bold', 'normal', '100', '900'
        color: '#333',
        textAlign: 'center', // 'left', 'center', 'right'
        marginBottom: 10,
      },
      paragraph: {
        fontSize: 16,
        lineHeight: 24, // Lines ke beech ki height
      },
      bold: {
        fontWeight: 'bold',
        color: 'red',
      },
      parentText: {
        fontSize: 16,
        color: 'red',
        marginTop: 20,
      },
      childText: {
        fontSize: 14, // Child style override kar sakti hai
        color: 'blue', // Color override ho gaya
        // fontWeight: 'bold', // Lekin font weight (agar set na ho) parent se lega
      },
      link: {
        fontSize: 16,
        color: 'blue',
        textDecorationLine: 'underline', // Link jaisa dikhane ke liye
        marginTop: 20,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `<Text style={styles.title}>...</Text>`: Simple text jispar `fontSize`, `fontWeight` (bold), `color`, `textAlign` (center) styles lagayi hain.
      * `<Text style={styles.paragraph}>...</Text>`: Paragraph text.
      * `<Text style={styles.bold}>...</Text>`: Yeh `Text` component doosre `Text` component ke *andar* (nested) hai. Isse " \<Text\> " bhaag alag style (bold, red) mein dikhega.
      * `<Text style={styles.parentText}>...</Text>`: Parent text (Red).
      * `<Text style={styles.childText}>...</Text>`: Nested child text (Blue). **Important:** Nested `Text` component styles ko *inherit* (viraasat mein) karta hai. Agar child `fontSize` nahi deta, toh woh parent ka `fontSize` le lega.
      * `<Text style={styles.link} onPress={...}>`: `Text` component (sirf `Text`, `View` nahi) `onPress` prop ko support karta hai. Isse aap text ko clickable (jaise link) bana sakte hain.
      * **🚀 Quick run expected output:** Screen par alag-alag style ka text dikhega. Ek centered Title, ek paragraph jismein kuch hissa bold/red hoga, ek red/blue line, aur ek clickable blue underlined link.
8.  **🐞 Common beginner mistakes:**
      * `View` ke andar text daalna: `<View>Hello</View>`. ❌
      * Text styling (jaise `fontSize`) ko `View` par lagana (woh kaam nahi karegi, `View` par `fontSize` nahi hota).
      * Yeh bhool jaana ki nested `Text` styles ko inherit karta hai.
9.  **🌍 Real-world example / use-case:** App mein dikhne wala har shabd (word).
10. **✅ Quick checklist / TL;DR:**
      * Saara text `<Text>` ke andar hona chahiye.
      * Text styling (`fontSize`, `color`, `fontWeight`) `Text` par lagti hai.
      * `Text` ko `Text` ke andar (nest) kar sakte hain (styles inherit hoti hain).
      * `Text` component `onPress` support karta hai.
11. **❓ FAQs:**
      * **Q: `View` aur `Text` mein styling ka kya fark hai?**
          * A: `View` = Layout styling (Flexbox, margin, padding, backgroundColor). `Text` = Font styling (color, fontSize, fontWeight, fontFamily, textAlign).
      * **Q: Main custom fonts (e.g., Poppins) kaise use karoon?**
          * A: Aapko font files ko project (e.g., `/assets/fonts/`) mein add karna hota hai, fir `react-native.config.js` mein link karna hota hai, aur `npx react-native-asset` chalana hota hai. Fir aap `style={{ fontFamily: 'Poppins-Regular' }}` de sakte hain. (Module 6.7).
12. **🏋️‍♀️ Practice exercise:**
      * `title` ka `color` badal kar 'orange' karo.
      * Ek naya `Text` component banao jo `italic` ho (Hint: `fontStyle: 'italic'`).
13. **📚 Further reading / commands / links:**
      * [Text Docs](https://reactnative.dev/docs/text)

-----

### 4.6: `TextInput` (User se input lena)

1.  **🎯 Title / Short Summary:** `TextInput` - User se text (Email, Password) type karana ⌨️.
2.  **🤔 Kya hai? (What?):** Yeh ek core component hai jo ek text input field (box) banata hai. Isse user app mein type kar sakta hai.
3.  **💡 Kyu important hai? (Why?):** Iske bina Login, Signup, Search, Chat, ya koi bhi form nahi ban sakta.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi user se koi text input (Naam, Email, Password, Search query) lena ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap user se koi data (text mein) le hi nahi payenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh ek "controlled component" hota hai. Iska matlab:
      * **Step 1:** Aap `useState` se ek state banate hain (jaise `[text, setText]`).
      * **Step 2:** `TextInput` ko 2 zaroori props dete hain:
        1.  `value={text}`: Input box ko batata hai ki uski current value kya hai (state se).
        2.  `onChangeText={setText}`: Jab user type karta hai, toh yeh function naye text ke saath call hota hai aur state ko update kar deta hai.
      * **`KeyboardAvoidingView`:** Yeh ek zaroori component hai. Jab `TextInput` par click karte hain, toh keyboard upar aata hai aur `TextInput` ko chupa (block) leta hai. `KeyboardAvoidingView` poore form ko (ya input ko) keyboard ke upar "slide" kar deta hai.
7.  **💻 Code example:**
    ```javascript
    import React, { useState } from 'react';
    import { StyleSheet, Text, View, SafeAreaView, TextInput, KeyboardAvoidingView, Platform } from 'react-native';

    const App = () => {
      // 1. Har input ke liye state
      const [name, setName] = useState('');
      const [password, setPassword] = useState('');

      return (
        <SafeAreaView style={styles.container}>
          {/* 6. KeyboardAvoidingView form ko wrap karega */}
          <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'} // iOS/Android ke liye alag behavior
            style={styles.keyboardView}
          >
            <Text style={styles.title}>Login Form</Text>
            
            {/* User se naam poochhna */}
            <TextInput
              style={styles.input}
              onChangeText={setName} // 2. State ko update karega
              value={name} // 3. State se value lega
              placeholder="Aapka Naam" // Jab box khali ho toh kya dikhe
              keyboardType="default" // Keyboard ka type
            />
            
            {/* User se password poochhna */}
            <TextInput
              style={styles.input}
              onChangeText={setPassword}
              value={password}
              placeholder="Password"
              secureTextEntry={true} // 4. Isse text '****' jaisa dikhega
              keyboardType="default"
            />
            
            {/* 5. User kya type kar raha hai, woh dikhana */}
            <Text style={styles.resultText}>Naam: {name}</Text>
            <Text style={styles.resultText}>Password: {password}</Text>
          </KeyboardAvoidingView>
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1 },
      keyboardView: { // KeyboardAvoidingView ke liye style
        flex: 1,
        justifyContent: 'center', // Content ko center mein rakha
        padding: 20,
      },
      title: { fontSize: 24, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
      input: {
        height: 40,
        marginVertical: 12,
        borderWidth: 1,
        borderColor: 'gray',
        padding: 10,
        borderRadius: 5,
      },
      resultText: {
        fontSize: 16,
        marginTop: 10,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const [name, setName] = useState('');`: `name` input ke liye state.
      * `<KeyboardAvoidingView ...>`: Form ko wrap kiya.
      * `behavior={Platform.OS === 'ios' ? 'padding' : 'height'}`: Zaroori prop. Yeh batata hai ki keyboard aane par (iOS mein) `padding` add karo ya (Android mein) `height` adjust karo.
      * `<TextInput ... />`: Input component.
      * `style={styles.input}`: Box ko style (height, border) di.
      * `onChangeText={setName}`: Jab bhi user type karega, `setName` function call hoga aur `name` state update ho jaayegi.
      * `value={name}`: Input box hamesha `name` state ki value dikhayega.
      * `placeholder="Aapka Naam"`: Background mein dikhne wala text.
      * `secureTextEntry={true}`: Password input ke liye (text ko dots `...` mein badal deta hai).
      * `<Text>Naam: {name}</Text>`: Live dikha raha hai ki state mein kya value hai.
      * **🚀 Quick run expected output:** Ek login form dikhega. Jab aap "Naam" ya "Password" box mein type karenge, toh keyboard upar aayega aur form ko dhakka dega (chupayega nahi). Aapka type kiya hua text neeche "Naam: ..." mein live dikhega.
8.  **🐞 Common beginner mistakes:**
      * `value` aur `onChangeText` props ko `useState` se connect na karna (uncontrolled input). Isse input box ko clear (khali) karna mushkil ho jaata hai.
      * `secureTextEntry` ko `true` na karna password field ke liye.
      * `KeyboardAvoidingView` use na karna, aur fir keyboard ke neeche input box chup jaana.
        9G.
9.  **🌍 Real-world example / use-case:**
      * Login/Signup screen.
      * Search bar.
      * Chat message box.
10. **✅ Quick checklist / TL;DR:**
      * `TextInput` user se text leta hai.
      * `useState` ke saath `value` aur `onChangeText` se control hota hai.
      * Password ke liye `secureTextEntry={true}`.
      * Keyboard se bachne ke liye `KeyboardAvoidingView` use karo.
11. **❓ FAQs:**
      * **Q: Keyboard ka "Enter" button (Return) kaise handle karoon?**
          * A: `onSubmitEditing` prop hota hai.
      * **Q: `keyboardType` mein kya-kya daal sakte hain?**
          * A: `'default'`, `'numeric'` (sirf number), `'email-address'` (@ ke saath), `'phone-pad'`.
      * **Q: Multiline comment box (jaise Facebook post) kaise banaoon?**
          * A: `multiline={true}` prop use karo.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein ek teesra `TextInput` (Email ke liye) add karo.
      * Email wale `TextInput` mein `keyboardType="email-address"` set karo.
13. **📚 Further reading / commands / links:**
      * [TextInput Docs](https://reactnative.dev/docs/textinput)
      * [KeyboardAvoidingView Docs](https://reactnative.dev/docs/keyboardavoidingview)

-----

### 4.7: DateTime Picker

1.  **🎯 Title / Short Summary:** `DateTime Picker` - Date (taareekh) ya Time (samay) chunne wala native popup.
2.  **🤔 Kya hai? (What?):** Yeh ek component *nahi* hai, balki ek **library** hai (`@react-native-community/datetimepicker`). Yeh OS ka native Date/Time picker (calendar ya clock) kholta hai.
3.  **💡 Kyu important hai? (Why?):** User se `dob` (Date of Birth) ya `appointmentTime` poochhne ke liye. User ko text mein type karana (jaise "10/11/2025") bohot bura UX hai. Native picker se galti nahi hoti.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi user se Date ya Time input lena ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** User ko `TextInput` mein date type karni padegi, jismein format galat ho sakta hai (e.g., "10-11-25" vs "Nov 10, 2025").
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install @react-native-community/datetimepicker`
      * **Step 2:** `run-android` (ya `pod install`).
      * **Step 3:** `useState` se ek `date` (e.g., `new Date()`) aur ek `showPicker` (e.g., `false`) state banao.
      * **Step 4:** Ek `Button` (e.g., "Show Picker") banao jo `showPicker` ko `true` kare.
      * **Step 5:** `DateTimePicker` component ko conditionally render karo (`if (showPicker) { ... }`).
      * **Step 6:** `DateTimePicker` ka `onChange` event naye date ko state mein set karega aur picker ko hide (`showPicker(false)`) kar dega.
7.  **💻 Code example:**
    ```javascript
    // 1. Pehle: npm install @react-native-community/datetimepicker
    import React, { useState } from 'react';
    import { View, Button, Platform, StyleSheet, Text } from 'react-native';
    import DateTimePicker from '@react-native-community/datetimepicker'; // 2. Import

    const App = () => {
      // 3. States
      const [date, setDate] = useState(new Date()); // Default date (aaj)
      const [mode, setMode] = useState('date'); // 'date' ya 'time'
      const [show, setShow] = useState(false); // Picker dikhe ya nahi

      // 4. 'onChange' event handler
      const onChange = (event, selectedDate) => {
        const currentDate = selectedDate || date; // Agar user cancel kare
        setShow(Platform.OS === 'ios'); // iOS par hamesha dikhta hai (jab tak custom hide na karein)
        setDate(currentDate); // State mein nayi date set ki
      };

      // 5. Picker dikhane wale functions
      const showMode = (currentMode) => {
        setShow(true);
        setMode(currentMode);
      };

      const showDatepicker = () => showMode('date');
      const showTimepicker = () => showMode('time');

      return (
        <View style={styles.container}>
          <Text style={styles.text}>Selected: {date.toLocaleString()}</Text>
          
          <View style={styles.button}>
            <Button onPress={showDatepicker} title="Show date picker!" />
          </View>
          <View style={styles.button}>
            <Button onPress={showTimepicker} title="Show time picker!" />
          </View>

          {/* 6. Picker ko render karna (jab show=true ho) */}
          {show && (
            <DateTimePicker
              testID="dateTimePicker"
              value={date} // Current value (state se)
              mode={mode} // 'date' ya 'time'
              is24Hour={true} // 24-hr format
              display="default" // 'default', 'spinner', 'clock', 'calendar'
              onChange={onChange} // Event handler
            />
          )}
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 18, marginBottom: 20 },
      button: { marginVertical: 5 }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import DateTimePicker from ...`: Library ko import kiya.
      * `const [date, setDate] = useState(new Date());`: Date ko store karne ke liye state.
      * `const [mode, setMode] = useState('date');`: State yeh store karne ke liye ki 'date' (calendar) dikhana hai ya 'time' (clock).
      * `const [show, setShow] = useState(false);`: State yeh store karne ke liye ki picker dikhana hai ya nahi.
      * `const onChange = (event, selectedDate) => { ... }`: Yeh function tab call hota hai jab user date/time select karta hai.
      * `setShow(Platform.OS === 'ios');`: Android par picker select karte hi *automatic* band ho jaata hai, iOS par nahi. Yeh logic use handle karta hai.
      * `setDate(currentDate);`: Nayi date ko state mein update kiya.
      * `const showDatepicker = () => ...`: Button `onPress` ke liye helper function, jo mode ko 'date' aur `show` ko `true` set karta hai.
      * `{show && ( ... )}`: Yeh "conditional rendering" hai. Matlab: "Agar `show` `true` hai, *tabhi* `DateTimePicker` ko render karo."
      * `<DateTimePicker ... />`: Picker component.
      * `value={date}`: Picker ko bataya ki shuruaat `date` state se karo.
      * `mode={mode}`: Picker ko bataya ki `mode` state (date/time) ke hisaab se khulo.
      * `onChange={onChange}`: Event handler ko connect kiya.
      * **🚀 Quick run expected output:** 2 button dikhenge. "Show date picker" dabane par native calendar (Android) ya date wheel (iOS) khulega. "Show time picker" dabane par native clock khulega. Select karne par "Selected: ..." text update hoga.
8.  **🐞 Common beginner mistakes:**
      * Library ko install (`npm install`) na karna.
      * `show` state (ya conditional rendering) use na karna. (Android par picker baar-baar dikhega).
      * `onChange` event ko handle na karna.
9.  **🌍 Real-world example / use-case:**
      * Flight booking app (Departure date).
      * Todo app (Task ki due date).
      * Signup form (Date of Birth).
10. **✅ Quick checklist / TL;DR:**
      * Date/Time ke liye library (`@react-native-community/datetimepicker`) use hoti hai.
      * `useState` (date aur `show` ke liye) zaroori hai.
      * Picker ko *conditionally* render karna (`{show && ...}`).
11. **❓ FAQs:**
      * **Q: Main iska color/style kaise badloon?**
          * A: Yeh native component hai, aap ise CSS se style *nahi* kar sakte. Aap `display` prop (`'spinner'`) use kar sakte hain ya (Android par) app ki theme colors se yeh color uthata hai.
      * **Q: Dono (Date & Time) ek saath kaise pochoon?**
          * A: Aapko 2 baar picker kholna hoga. Pehle `mode='date'`, fir (jab user select kar le) `mode='time'`.
12. **🏋️‍♀️ Practice exercise:**
      * `display` prop ko `'spinner'` karke dekho (dono Android/iOS par wheel jaisa dikhega).
      * `is24Hour={false}` karke dekho (AM/PM aa jaayega).
13. **📚 Further reading / commands / links:**
      * [datetimepicker GitHub (Docs)](https://github.com/react-native-datetimepicker/datetimepicker)

-----

### 4.8: `Picker` / `RNPickerSelect`

1.  **🎯 Title / Short Summary:** `Picker` / `RNPickerSelect` - Dropdown (select) list 🔽.
2.  **🤔 Kya hai? (What?):**
      * **`Picker` (Legacy):** React Native ka purana (`@react-native-community/picker`) component jo dropdown list banata tha.
      * **`RNPickerSelect` (Modern):** Ek bohot popular **library** (`react-native-picker-select`) jo `Picker` ko hi use karti hai, lekin use style karna 100x aasan bana deti hai aur dono (Android/iOS) par ek jaisa look deti hai.
3.  **💡 Kyu important hai? (Why?):** Jab aapko user ko 3-10 options (jaise "Select Country", "Select City") mein se *ek* chunne ko bolna ho.
4.  **⏰ Kab/use karna chahiye? (When?):** **Hamesha `react-native-picker-select` use karo.** Purana `Picker` bohot bekaar aur style karne mein mushkil hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Agar aapne purana `Picker` use kiya, toh Android aur iOS par look bohot alag-alag aayega aur use style (jaise `TextInput` jaisa) dikhana bohot mushkil hoga.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Using `RNPickerSelect`):**
      * **Step 1:** Install karo: `npm install react-native-picker-select`
      * **Step 2:** `useState` se state banao (jaise `[selectedValue, setSelectedValue]`).
      * **Step 3:** `items` ka array banao (Format: `[{ label: '...', value: '...' }]`).
      * **Step 4:** Component ko 3 zaroori props do:
        1.  `onValueChange={setSelectedValue}`: Jab user kuch select karega.
        2.  `items={...}`: Aapka data array.
        3.  `value={selectedValue}`: Current selected value (state se).
7.  **💻 Code example:** (Using `react-native-picker-select`)
    ```javascript
    // 1. Pehle: npm install react-native-picker-select
    import React, { useState } from 'react';
    import { View, StyleSheet, Text, SafeAreaView } from 'react-native';
    import RNPickerSelect from 'react-native-picker-select'; // 2. Import

    const App = () => {
      // 3. State
      const [selectedSport, setSelectedSport] = useState(null);

      // 4. Data (items array)
      const sports = [
        { label: 'Football', value: 'football' },
        { label: 'Baseball', value: 'baseball' },
        { label: 'Hockey', value: 'hockey' },
      ];

      return (
        <SafeAreaView style={styles.container}>
          <Text style={styles.text}>Aapka favorite sport kya hai?</Text>
          
          <RNPickerSelect
            onValueChange={(value) => setSelectedSport(value)} // 5. State update
            items={sports} // 6. Data
            value={selectedSport} // 7. Current value
            placeholder={{ label: 'Select a sport...', value: null }} // Default text
            style={pickerSelectStyles} // Custom styling
            useNativeAndroidPickerStyle={false} // Taaki Android par bhi custom style chale
          />
          
          <Text style={styles.text}>Selected: {selectedSport}</Text>
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', padding: 20 },
      text: { fontSize: 18, marginVertical: 10 },
    });

    // 8. Styling object (library ki doc se)
    const pickerSelectStyles = StyleSheet.create({
      inputIOS: {
        fontSize: 16,
        paddingVertical: 12,
        paddingHorizontal: 10,
        borderWidth: 1,
        borderColor: 'gray',
        borderRadius: 4,
        color: 'black',
        paddingRight: 30, // taaki text arrow ke neeche na jaaye
      },
      inputAndroid: {
        fontSize: 16,
        paddingHorizontal: 10,
        paddingVertical: 8,
        borderWidth: 1,
        borderColor: 'gray',
        borderRadius: 8,
        color: 'black',
        paddingRight: 30, // taaki text arrow ke neeche na jaaye
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import RNPickerSelect from ...`: Library ko import kiya.
      * `const [selectedSport, ...]= useState(null);`: State, shuru mein `null` (kuch selected nahi).
      * `const sports = [...]`: `items` array. Har item mein `label` (jo user ko dikhega) aur `value` (jo state mein save hoga) zaroori hai.
      * `onValueChange={(value) => ...}`: Jab user select karega, yeh function `value` (e.g., 'football') ko state mein set kar dega.
      * `items={sports}`: Data pass kiya.
      * `value={selectedSport}`: State ko connect kiya.
      * `placeholder={{...}}`: Default (shuruaati) text.
      * `style={pickerSelectStyles}`: Library ko bataya ki styling ke liye yeh object (`inputIOS`, `inputAndroid`) use karo.
      * `useNativeAndroidPickerStyle={false}`: Taaki Android par bhi hamari custom (`inputAndroid`) style dikhe (default "dialog" na dikhe).
      * **🚀 Quick run expected output:** Ek `TextInput` jaisa "Select a sport..." box dikhega. Tap karne par, (iOS par neeche se / Android par popup mein) "Football", "Baseball", "Hockey" ki list khulegi. Select karne par "Selected: football" text update hoga.
8.  **🐞 Common beginner mistakes:**
      * Library install na karna.
      * `items` array ka format galat dena (`label` aur `value` zaroori hain).
      * `onValueChange` ya `value` prop ko state se connect na karna.
      * Purana (aur bura) `@react-native-community/picker` use karna.
9.  **🌍 Real-world example / use-case:**
      * Signup form ("Select Country").
      * E-commerce app (Filter: "Sort by Price").
10. **✅ Quick checklist / TL;DR:**
      * Dropdown ke liye, `react-native-picker-select` library use karo.
      * `items` array (`[{ label: ..., value: ... }]`) zaroori hai.
      * `value` aur `onValueChange` ko `useState` se control karo.
11. **❓ FAQs:**
      * **Q: Iska background color (popup ka) kaise badloon?**
          * A: Yeh native OS ka popup (ya wheel) hota hai. Ise style karna bohot mushkil/impossible hai. Aap sirf "input box" (jo dikh raha hai) ko style kar sakte hain.
      * **Q: Bahut lambi list (100+ countries) ke liye yeh achha hai?**
          * A: Nahi. 100 items ke liye user ko scroll karna padega. Uske liye behtar hai ki aap `Modal` kholein, usme `FlatList` aur `TextInput` (Search) daalein.
12. **🏋️‍♀️ Practice exercise:**
      * `sports` array mein ek naya item "Cricket" add karo.
      * `placeholder` ka text badal kar "Choose..." karo.
13. **📚 Further reading / commands / links:**
      * [react-native-picker-select (GitHub Docs)](https://github.com/lawnstarter/react-native-picker-select)

-----

### 4.9: `SafeAreaView`

1.  **🎯 Title / Short Summary:** `SafeAreaView` - (Sirf iOS) Content ko Notch/Home bar ke neeche jaane se bachana.
2.  **🤔 Kya hai? (What?):** Yeh `View` jaisa hi ek component hai, lekin yeh *sirf iOS* devices (iPhone X aur naye) par kaam karta hai. Yeh automatically content ko "safe area" (notch, status bar, aur neeche ke home indicator) ke andar rakhta hai.
3.  **💡 Kyu important hai? (Why?):** Agar aap `View` use karenge, toh aapka content (jaise "Back" button ya "Title") iOS ke status bar ya notch ke *peeche* chala jaayega aur user use dekh/click nahi kar payega.
4.  **⏰ Kab/use karna chahiye? (When?):** **Hamesha.** Apni har screen ke *main (root)* component ko `SafeAreaView` banayein (ya `View` ki jagah ise use karein).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka app iOS par "toota hua" (broken) dikhega. Content notch ke peeche chip jaayega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh ek `View` hai jise `flex: 1` dena chahiye.
      * `import { SafeAreaView } from 'react-native';`
      * Apne poore screen ke code ko `<View style={{flex: 1}}>` ke bajaye `<SafeAreaView style={{flex: 1}}>` se wrap kar do.
      * **Android par kya hoga?** Android par yeh component *kuch nahi* karta. Yeh `View` jaisa hi behave karta hai. Isiliye yeh use karne mein safe hai. (Android ke liye hum `StatusBar` component (next topic) use karte hain).
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, Text, View, SafeAreaView, StatusBar } from 'react-native';

    const App = () => {
      return (
        // 1. Root component ko 'View' ke bajaye 'SafeAreaView' banaya
        <SafeAreaView style={styles.container}>
          
          {/* Android par 'padding' dene ke liye (kyunki SafeAreaView Android par kaam nahi karta) */}
          <View style={styles.androidPadding}> 
            <Text style={styles.text}>
              Yeh text iOS par notch ke neeche dikhega.
            </Text>
            <Text style={styles.text}>
              Android par yeh StatusBar ke neeche dikhega (padding ki vajah se).
            </Text>
          </View>
          
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1, // Poori screen lo
        backgroundColor: '#f0f0f0',
      },
      // 2. Android ke liye manual padding
      androidPadding: {
        flex: 1,
        paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0
      },
      text: {
        fontSize: 18,
        padding: 10,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... SafeAreaView, StatusBar } from 'react-native';`: `SafeAreaView` ko import kiya.
      * `<SafeAreaView style={styles.container}>`: Root component (jise `flex: 1` diya).
      * `paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0`: **Android Hack\!** Kyunki `SafeAreaView` Android par kaam nahi karta, hum check kar rahe hain (`Platform.OS`) ki agar "android" hai, toh `paddingTop` (upar se space) `StatusBar.currentHeight` (status bar ki height) jitna de do. iOS par `0` rakho (kyunki `SafeAreaView` apna kaam khud kar lega).
      * **🚀 Quick run expected output:**
          * **iOS:** Content notch ke neeche se shuru hoga.
          * **Android:** Content status bar ke neeche se shuru hoga.
          * (Dono mein content katega nahi).
8.  **🐞 Common beginner mistakes:**
      * `SafeAreaView` ko `flex: 1` na dena.
      * Android ke liye `StatusBar.currentHeight` ki padding na dena aur sochna ki `SafeAreaView` Android par kaam karega.
      * `SafeAreaView` ko *har* `View` ki jagah use karna. Ise sirf *root (main) screen container* ke liye use karna hai.
9.  **🌍 Real-world example / use-case:** Har app ki har screen.
10. **✅ Quick checklist / TL;DR:**
      * `SafeAreaView` = iOS notch/bar se bachata hai.
      * Ise root component (screen) ki tarah `flex: 1` ke saath use karo.
      * Android par yeh `View` hai. Android ke liye manual padding (`StatusBar.currentHeight`) add karo.
11. **❓ FAQs:**
      * **Q: `react-native-safe-area-context` kya hai?**
          * A: Yeh ek behtar, modern library hai (jo Expo aur React Navigation use karte hain). Yeh `SafeAreaView` se zyada flexible hai. Lekin shuru ke liye core `SafeAreaView` kaafi hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `SafeAreaView` ko `View` se badal kar dekho (aur `androidPadding` bhi hata do). Dekho iOS simulator par content notch ke peeche chala jaayega.
13. **📚 Further reading / commands / links:**
      * [SafeAreaView Docs](https://reactnative.dev/docs/safeareaview)

-----

### 4.10: `StatusBar`

1.  **🎯 Title / Short Summary:** `StatusBar` - Phone ke top bar (jahan time/battery dikhti hai) ko control karna.
2.  **🤔 Kya hai? (What?):** Yeh ek component hai jo aapko app ke status bar (jahan time, battery, WiFi dikhta hai) ko style karne deta hai.
3.  **💡 Kyu important hai? (Why?):** Agar aapki app "dark mode" mein hai (black background), toh default (black) status bar text dikhega hi nahi. `StatusBar` se aap text ko "white" (`light-content`) kar sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Har screen par. Aapki screen ke design ke hisaab se status bar ka look badalne ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka status bar hamesha default (OS ka) dikhega, jo aapke app ke design se match nahi karega (e.g., light app par black text, dark app par black text).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Yeh ek self-closing component hai.
      * Ise aap kahin bhi (root `View` ke andar) rakh sakte hain.
      * 3 zaroori props:
        1.  `barStyle`: Text ka color. `'dark-content'` (black text, light background ke liye) ya `'light-content'` (white text, dark background ke liye).
        2.  `backgroundColor`: Sirf Android par status bar ka background color.
        3.  `hidden`: Status bar ko chupane (`true`) ya dikhane (`false`) ke liye.
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, Text, View, StatusBar, SafeAreaView } from 'react-native';

    const App = () => {
      return (
        <SafeAreaView style={styles.container}>
          {/* 1. StatusBar ko configure kiya */}
          <StatusBar
            barStyle="light-content" // Text/Icons 'white' dikhao
            backgroundColor="#6a51ae" // Android par background 'purple' rakho
            // hidden={true} // Agar poora chupana ho
            translucent={false} // Android ke liye (taaki app iske neeche na jaaye)
          />
          
          <View style={styles.content}>
            <Text style={styles.text}>
              Mera background purple hai, isiliye 
              StatusBar ka text 'light-content' (white) hai.
            </Text>
          </View>
        </SafeAreaView>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#6a51ae', // Main background (purple)
        // Android par padding ki zaroorat nahi, kyunki translucent=false hai
      },
      content: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      },
      text: {
        color: 'white',
        fontSize: 18,
        textAlign: 'center',
        padding: 20,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `<SafeAreaView style={styles.container}>`: Root container. Iska background purple hai.
      * `<StatusBar ... />`: StatusBar component ko add kiya.
      * `barStyle="light-content"`: Kyunki background dark (purple) hai, humne text ko light (white) kar diya.
      * `backgroundColor="#6a51ae"`: Android par status bar ka background bhi app ke background jaisa (purple) set kar diya.
      * `translucent={false}`: (Android only) Iska matlab hai "app ko status bar ke peeche *mat* render karo". (Yeh `SafeAreaView` ke Android hack ka alternative hai).
      * **🚀 Quick run expected output:** Poori screen (status bar samet) purple dikhegi, aur status bar ka text (time, battery) white color mein dikhega.
8.  **🐞 Common beginner mistakes:**
      * `barStyle` ko background ke hisaab se na badalna (Dark app par "dark-content", jisse text gayab ho jaata hai).
      * `backgroundColor` ko iOS par try karna (yeh sirf Android prop hai).
9.  **🌍 Real-world example / use-case:**
      * Light screen (Settings) = `barStyle="dark-content"`.
      * Dark screen (Profile) = `barStyle="light-content"`.
      * Image full-screen dikhate time = `hidden={true}`.
10. **✅ Quick checklist / TL;DR:**
      * `StatusBar` top bar ko style karta hai.
      * `barStyle`: Text color (`'light-content'` ya `'dark-content'`).
      * `backgroundColor`: Android background.
      * Har screen par (design ke hisaab se) ise set karna chahiye.
11. **❓ FAQs:**
      * **Q: iOS par background color kaise badloon?**
          * A: Aap `StatusBar` ka background *nahi* badal sakte. Aap `SafeAreaView` ko background color dete hain, jo status bar ke "peeche" dikhta hai.
      * **Q: Har screen ke liye alag style kaise doon?**
          * A: Jab React Navigation (Module 5) use karte hain, toh har screen (component) mein apna `StatusBar` component daal sakte hain.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `backgroundColor` (style aur `StatusBar` prop) ko `'#ffffff'` (white) karo.
      * Ab `barStyle` ko `'dark-content'` karke dekho (taaki text black dikhe).
13. **📚 Further reading / commands / links:**
      * [StatusBar Docs](https://reactnative.dev/docs/statusbar)

-----

### 4.11: `Toast`

1.  **🎯 Title / Short Summary:** `Toast` (Sirf Android) - Chota, temporary "Saved" message (popup).
2.  **🤔 Kya hai? (What?):** Yeh Android ka ek native UI element hai jo screen ke neeche (ya beech mein) ek chota, kaala (black) popup dikhata hai jo thodi der (2-3 second) mein apne aap gayab ho jaata hai. (e.g., "Message sent").
3.  **💡 Kyu important hai? (Why?):** Yeh user ko *bina disturb kiye* (bina `Alert` dikhaye) batane ke liye hai ki "kaam ho gaya hai".
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab "Settings Saved", "Message Sent", "Item added to cart" jaisa chota confirmation dena ho.
      * **iOS par kya karein?** Yeh component `react-native` mein **SIRF Android** ke liye hai. iOS ke liye aapko *library* (jaise `react-native-toast-message`) use karni padegi.
      * **Hum `react-native-toast-message` (library) ko prefer karenge kyunki woh cross-platform (dono par) chalti hai.**
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Chote confirmation ke liye bhi aapko `Alert` dikhana padega, jo user ko "OK" dabane par majboor karta hai (bura UX).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Using Core `ToastAndroid`):**
      * `import { ToastAndroid } from 'react-native';`
      * `ToastAndroid.show(message, duration)`
      * `duration`: `ToastAndroid.SHORT` (2 sec) ya `ToastAndroid.LONG` (3.5 sec).
7.  **💻 Code example:** (Using `ToastAndroid` - Yeh sirf Android par chalega)
    ```javascript
    import React from 'react';
    import { View, StyleSheet, Button, ToastAndroid, Platform } from 'react-native';

    const App = () => {
      const showToast = () => {
        if (Platform.OS === 'android') {
          ToastAndroid.show(
            'Settings Saved Successfully!', // Message
            ToastAndroid.SHORT // Duration
          );
        } else {
          // iOS ke liye library (e.g., react-native-toast-message) use karni padegi
          alert('Toast sirf Android par chalta hai (core).');
        }
      };

      return (
        <View style={styles.container}>
          <Button title="Save Settings" onPress={showToast} />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... ToastAndroid, Platform } from 'react-native';`: `ToastAndroid` aur `Platform` ko import kiya.
      * `const showToast = () => { ... }`: Button `onPress` ke liye function.
      * `if (Platform.OS === 'android') { ... }`: Check kiya ki OS Android hai ya nahi.
      * `ToastAndroid.show(...)`: `ToastAndroid` API ko call kiya.
      * `ToastAndroid.SHORT`: Duration (time) set kiya.
      * **🚀 Quick run expected output:**
          * **Android:** "Save Settings" button dabane par, screen ke neeche "Settings Saved Successfully\!" ka chota black popup aayega aur 2 sec mein gayab ho jaayega.
          * **iOS:** Button dabane par `alert` dikhega.
8.  **🐞 Common beginner mistakes:**
      * `ToastAndroid` ko iOS par chalaane ki koshish karna (app crash hoga, isiliye `Platform` check zaroori hai).
      * `Toast` (jo ab core mein nahi hai) import karne ki koshish karna.
      * **Best Practice:** `ToastAndroid` mat use karo. Shuru se hi `react-native-toast-message` (library) use karo taaki dono platform par chale.
9.  **🌍 Real-world example / use-case:**
      * GMail app mein "Email archived" (neeche black popup).
      * Instagram par "Post liked" (jo double-tap par chota sa heart aata hai, woh bhi ek tarah ka toast hai).
10. **✅ Quick checklist / TL;DR:**
      * `ToastAndroid` = Chota, temporary, non-blocking popup.
      * Sirf Android par chalta hai.
      * `ToastAndroid.show(message, duration)`.
      * **Recommendation:** Iske bajaye `react-native-toast-message` (library) use karo.
11. **❓ FAQs:**
      * **Q: `react-native-toast-message` (library) kaise use karein?**
          * A: `npm install react-native-toast-message`. Fir `App.js` mein top par `<Toast />` component add karo. Fir kahin se bhi `Toast.show({ type: 'success', text1: 'Saved!' })` call karo.
      * **Q: Main Toast ko style kar sakta hoon?**
          * A: Core `ToastAndroid` ko nahi. Library `react-native-toast-message` ko haan.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `ToastAndroid.SHORT` ko `ToastAndroid.LONG` karke dekho (popup der tak rukega).
      * Ek naya button banao jo "Gravity" ke saath toast dikhaye (`ToastAndroid.showWithGravity(...)`).
13. **📚 Further reading / commands / links:**
      * [ToastAndroid Docs](https://reactnative.dev/docs/toastandroid)
      * [react-native-toast-message (Recommended Library)](https://github.com/calintamas/react-native-toast-message)

-----

### 4.12: `AppState` (App Lifecycle)

1.  **🎯 Title / Short Summary:** `AppState` - Pata lagao ki user app *use kar raha hai* ya *background mein daal diya* hai 📱.
2.  **🤔 Kya hai? (What?):** Yeh ek API hai jo aapko batata hai ki aapke app ki current state (stithi) kya hai. Iski 3 main states hoti hain:
      * `'active'`: User app ko *dekh raha hai* (foreground).
      * `'background'`: User ne app ko background mein daal diya (Home button daba diya) ya phone lock kar diya.
      * `'inactive'`: (Sirf iOS) User ne Control Center (neeche se swipe) khola hai ya call aa gayi hai.
3.  **💡 Kyu important hai? (Why?):**
      * **Security:** Jab user app background mein daale, toh app ko "Lock" (e.g., PIN screen) kar dena.
      * **Data Fetching:** Jab user app mein *vaapas* (background se active) aaye, tab naya data (e.g., naye messages) fetch (refresh) karna.
      * **Pause:** Jab user app background kare, toh game ya video ko "pause" kar dena.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko app ke "background" ya "foreground" mein jaane par koi logic (code) chalana ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Aapka app background mein bhi data fetch karta rahega (battery waste).
      * Jab user app mein vaapas aayega, toh use purana (stale) data dikhega.
      * Security apps (jaise Bank app) background mein jaane par lock nahi honge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Aap `AppState` ko import karte hain.
      * Aap `useEffect` (Module 8) ka istemaal karke "event listener" (suno) add karte hain.
      * Yeh listener `appState.current` ko check karta hai aur naye `nextAppState` ko.
      * Hum `useEffect` ke "cleanup" function mein listener ko remove bhi karte hain (memory leak se bachne ke liye).
7.  **💻 Code example:** (Yeh `useEffect` use karega, jo Module 8 ka topic hai, par yahan zaroori hai)
    ```javascript
    import React, { useState, useEffect, useRef } from 'react';
    import { View, StyleSheet, Text, AppState } from 'react-native';

    const App = () => {
      // 1. AppState ko track karne ke liye 'ref' aur 'state'
      const appState = useRef(AppState.currentState); // Current state (shuru mein)
      const [appStateVisible, setAppStateVisible] = useState(appState.current);

      // 2. useEffect (yeh component load hote hi chalega)
      useEffect(() => {
        // 3. 'change' event ko suno
        const subscription = AppState.addEventListener('change', nextAppState => {
          
          // Agar app 'background' ya 'inactive' se 'active' (vaapas) aaya hai
          if (
            appState.current.match(/inactive|background/) &&
            nextAppState === 'active'
          ) {
            console.log('App has come to the foreground!');
            // YAHAN AAP API REFRESH CALL KAR SAKTE HAIN
          }
          
          // Agar app 'active' se 'background' mein gaya hai
          if (
            appState.current === 'active' &&
            nextAppState.match(/inactive|background/)
          ) {
            console.log('App has gone to the background!');
            // YAHAN AAP VIDEO PAUSE KAR SAKTE HAIN
          }

          // 4. Current state ko update karo
          appState.current = nextAppState;
          setAppStateVisible(appState.current); // Screen par dikhane ke liye state update
          console.log('AppState', appState.current);
        });

        // 5. Cleanup: Jab component band ho, toh listener hata do
        return () => {
          subscription.remove();
        };
      }, []); // [] = Sirf ek baar (component load) par chalao

      return (
        <View style={styles.container}>
          <Text style={styles.text}>Current AppState is:</Text>
          <Text style={styles.stateText}>{appStateVisible}</Text>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 18 },
      stateText: { fontSize: 24, fontWeight: 'bold', margin: 10 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { ... AppState } from 'react-native';`: `AppState` API ko import kiya.
      * `const appState = useRef(AppState.currentState);`: `useRef` (Module 8) use kiya taaki `useEffect` ke andar purani state yaad rahe.
      * `const [appStateVisible, ...]= useState(...)`: `useState` use kiya taaki current state screen par dikha sakein.
      * `useEffect(() => { ... }, []);`: Component load hote hi listener set kar rahe hain.
      * `const subscription = AppState.addEventListener('change', ...)`: `AppState` ko bola ki jab bhi 'change' ho, toh hamara function (callback) chala dena.
      * `if (... nextAppState === 'active')`: Check kiya ki kya app *vaapas* 'active' hua hai.
      * `if (... nextAppState.match(...))`: Check kiya ki kya app *background* mein gaya hai.
      * `appState.current = nextAppState;`: Purani state ko nayi state se update kiya.
      * `return () => { subscription.remove(); };`: **Cleanup function.** Yeh bohot zaroori hai. Jab component band (unmount) hoga, yeh listener ko hata dega, varna memory leak hogi.
      * **🚀 Quick run expected output:** Screen par "Current AppState is: active" dikhega. Ab agar aap Home button dabakar app ko background mein daalenge, toh aapke console (terminal) mein "App has gone to the background\!" log hoga. Jab app vaapas kholenge, toh "App has come to the foreground\!" log hoga aur screen par "active" dikhega.
8.  **🐞 Common beginner mistakes:**
      * Event listener add karna, lekin use cleanup function (`subscription.remove()`) mein remove na karna. (Bohot bada memory leak).
      * `AppState.currentState` ko `useEffect` ke bahar use karna (woh aapko sirf shuruaati state dega, update nahi karega).
9.  **🌍 Real-world example / use-case:**
      * **Banking App:** Jab `nextAppState` 'background' ho, toh `PIN/Login` screen dikhane ka flag `true` kar do.
      * **Chat App:** Jab `nextAppState` 'active' ho, toh `fetchMessages()` function call karo.
      * **Music App:** Jab `nextAppState` 'background' ho, toh music *chalte rehne do*, lekin agar 'active' ho toh UI update karo.
10. **✅ Quick checklist / TL;DR:**
      * `AppState` = App ka lifecycle ('active', 'background').
      * `useEffect` ke andar `addEventListener` (aur `remove`) se use karte hain.
      * App "refresh" karne (jab user vaapas aaye) ya "pause" karne (jab user jaaye) ke liye best hai.
11. **❓ FAQs:**
      * **Q: `useRef` kyun use kiya? `useState` kyun nahi?**
          * A: Kyunki `useEffect` ke event listener (callback) hamesha state ki "purani" (stale) value dekhte hain. `useRef` (`.current`) hamesha latest value rakhta hai aur re-render trigger nahi karta, jo listener ke liye perfect hai. (Advanced topic).
      * **Q: Yeh `BackgroundTimer` (Module 12) se alag kaise hai?**
          * A: `AppState` sirf *batata* hai ki app background mein hai. Yeh background mein code *chala* nahi sakta. Background mein code chalaane ke liye `BackgroundTimer` ya `HeadlessJS` (Module 12) lagta hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `console.log` ki jagah `Alert.alert` (jab app active ho) daal kar dekho.
13. **📚 Further reading / commands / links:**
      * [AppState Docs](https://reactnative.dev/docs/appstate)

-----

Module 4 complete\! 🥳 Humne saare important UI blocks (`View`, `Text`, `TextInput`, `ScrollView`) aur unke helpers (`SafeAreaView`, `StatusBar`, `KeyboardAvoidingView`) cover kar liye hain.

Jab aap taiyaar hon, toh **"Module 5 ke notes do"** bolna\! 🧑‍💻

=============================================================

# MODULE-5 → Advanced Features & State Management

### 5.1: `Image Picker` (Gallery/Camera se image lena)

1.  **🎯 Title / Short Summary:** `react-native-image-picker` - User ke phone ki gallery ya camera se photo/video select karana.
2.  **🤔 Kya hai? (What?):** Yeh ek **library** hai (core component nahi) jo native UI (Android/iOS) khol kar user ko option deti hai ki woh ya toh "Gallery se photo chune" ya "Camera se nayi photo kheeche".
3.  **💡 Kyu important hai? (Why?):** Iske bina aap user se profile picture, post, ya koi bhi document upload nahi kara sakte.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko user ke device se image ya video ki zaroorat ho. (e.g., Profile pic update, Instagram jaisi post create karna).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka app user ke phone ki media (photos) ko access hi nahi kar paayega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install react-native-image-picker`
      * **Step 2:** `run-android` (ya `pod install`).
      * **Step 3 (Permissions):** `AndroidManifest.xml` (Android) aur `Info.plist` (iOS) mein permissions add karni padti hain (jaisa Module 1.10 mein dekha tha).
          * `AndroidManifest.xml` (Module 1.10):
            ```xml
            <uses-permission android:name="android.permission.CAMERA" />
            <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
            <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
            ```
          * `Info.plist` (iOS): `NSPhotoLibraryUsageDescription` (Gallery access) aur `NSCameraUsageDescription` (Camera access) keys add karni padti hain.
      * **Step 4:** Library se `launchCamera` (camera kholne ke liye) ya `launchImageLibrary` (gallery kholne ke liye) function import karo.
      * **Step 5:** `launchImageLibrary` ko call karo. Yeh `response` deta hai.
      * **Step 6:** Agar `response.didCancel` nahi hai, toh `response.assets[0].uri` mein aapko image ka `uri` (path) mil jaayega.
      * **Step 7:** Us `uri` ko `useState` mein save karke `Image` component mein dikha do.
7.  **💻 Code example:**
    ```javascript
    // 1. Pehle: npm install react-native-image-picker
    // 2. Phir permissions set karo (AndroidManifest.xml)
    import React, { useState } from 'react';
    import { View, Button, Image, StyleSheet, Alert, Platform } from 'react-native';
    import { launchImageLibrary } from 'react-native-image-picker'; // 3. Import

    const App = () => {
      // 4. Image URI ko store karne ke liye state
      const [selectedImage, setSelectedImage] = useState(null);

      const openGallery = () => {
        const options = {
          mediaType: 'photo', // 'photo' ya 'video'
          quality: 1, // 0 (low) se 1 (high)
        };

        // 5. Gallery kholne wala function
        launchImageLibrary(options, (response) => {
          if (response.didCancel) {
            console.log('User ne cancel kar diya');
          } else if (response.errorCode) {
            Alert.alert('Error', response.errorMessage);
          } else {
            // 6. Image URI mil gaya
            const imageUri = response.assets[0].uri;
            setSelectedImage(imageUri); // 7. State update ki
          }
        });
      };
      
      // Note: Camera ke liye 'launchCamera' use karte hain

      return (
        <View style={styles.container}>
          <Text style={styles.text}>Profile Picture Upload:</Text>
          
          {/* 8. Selected image dikhana */}
          {selectedImage && (
            <Image
              source={{ uri: selectedImage }}
              style={styles.image}
            />
          )}
          
          <Button title="Select Image from Gallery" onPress={openGallery} />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 18, marginBottom: 20 },
      image: { width: 200, height: 200, borderRadius: 100, marginBottom: 20 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { launchImageLibrary } from ...`: Sirf gallery wala function import kiya.
      * `const [selectedImage, setSelectedImage] = useState(null);`: State banayi image `uri` (e.g., `file:///.../image.jpg`) ko store karne ke liye.
      * `const options = { ... }`: Options set kiye (sirf photo chahiye, quality 1).
      * `launchImageLibrary(options, (response) => { ... })`: Function call kiya. Isse 2 arguments milte hain (options, callback function).
      * `if (response.didCancel)`: Check kiya ki user ne bina select kiye "back" toh nahi kar diya.
      * `const imageUri = response.assets[0].uri;`: `response.assets` ek array hai (multiple selection ke liye), hum pehla (`[0]`) image le rahe hain aur uska `uri` nikaal rahe hain.
      * `setSelectedImage(imageUri);`: `uri` ko state mein daal diya, jisse component re-render hoga.
      * `{selectedImage && ( ... )}`: Conditional rendering. Agar `selectedImage` `null` *nahi* hai, tabhi `Image` component dikhao.
      * `<Image source={{ uri: selectedImage }} ... />`: `Image` component (Module 3.3) ko network/file `uri` se image dikha rahe hain.
      * **🚀 Quick run expected output:** Ek button dikhega. Use dabane par phone ki gallery khulegi. Photo select karne par, woh photo screen par (ek gol `Image` view mein) dikhne lagegi.
8.  **🐞 Common beginner mistakes:**
      * **Permissions\!** `AndroidManifest.xml` (Android) ya `Info.plist` (iOS) mein `CAMERA` / `READ_EXTERNAL_STORAGE` permission na dena. Isse app crash ho jaata hai.
      * `npm install` ke baad `npx react-native run-android` se app ko rebuild na karna (kyunki yeh native library hai).
      * `response.assets[0].uri` ke bajaye `response.uri` (purana version) use karna.
      * Runtime permissions (Module 13.8) na maangna (Android 6+ ke liye zaroori hai).
9.  **🌍 Real-world example / use-case:**
      * Instagram par post "Add" button.
      * WhatsApp/Signal par profile picture change karna.
      * "Upload document" (e.g., Aadhar card) in KYC forms.
10. **✅ Quick checklist / TL;DR:**
      * Yeh `react-native-image-picker` library hai.
      * `npm install` ke baad native permissions (`AndroidManifest.xml`) zaroori hain.
      * `launchImageLibrary` (Gallery) ya `launchCamera` (Camera) use hota hai.
      * `response.assets[0].uri` se image ka path milta hai.
11. **❓ FAQs:**
      * **Q: Ek saath multiple photos kaise select karein?**
          * A: Options mein `selectionLimit: 5` (ya 0 = koi limit nahi) set kar sakte hain. `response.assets` mein poora array aa jaayega.
      * **Q: Image ko server par kaise upload karein (File Upload)?**
          * A: Aapko `uri` mil gaya. Ab aap `fetch` ya `axios` ka use karke `FormData` (Multipart) request banani padti hai, jismein aap image file (aur uska type, naam) bhejte hain. (Yeh Module 13.9 ka topic hai).
      * **Q: Image ko crop (kaatna) kaise karein?**
          * A: Yeh library cropping nahi karti. Uske liye ek aur library `react-native-image-crop-picker` aati hai, jo bohot popular hai.
12. **🏋️‍♀️ Practice exercise:**
      * `openGallery` function ko copy karke `openCamera` function banao.
      * Usme `launchImageLibrary` ki jagah `launchCamera` import aur use karo.
      * Ek doosra button "Take Photo" banao jo `openCamera` ko call kare.
13. **📚 Further reading / commands / links:**
      * [react-native-image-picker (GitHub Docs)](https://github.com/react-native-image-picker/react-native-image-picker)
      * [react-native-image-crop-picker (Alternative Library)](https://github.com/ivpusic/react-native-image-crop-picker)

-----

### 5.2: Navigation (React Navigation - Stack Navigator)

Yeh topic bohot bada hai, hum iske sub-topics (Container, Stack, Comparison) ko cover karenge.

#### 5.2 (Sub-topic): `NavigationContainer`

1.  **🎯 Title / Short Summary:** `NavigationContainer` - Navigation ka "Dhaaga" (Thread).
2.  **🤔 Kya hai? (What?):** Yeh ek component hai jo aapke *poore app* ko wrap (lapet'ta) karta hai aur aapke app ki navigation state (aap abhi kis screen par hain) ko manage karta hai.
3.  **💡 Kyu important hai? (Why?):** Iske bina "React Navigation" (library) kaam hi nahi karegi. Yeh aapke app ko navigation (aage-peeche jaana) se connect karta hai.
4.  **⏰ Kab/use karna chahiye? (When?):** **Sirf ek baar.** Aapke app ki root (sabse upar) file (`App.js`) mein, poore app ko wrap karne ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka app crash ho jaayega. `React Navigation` (Stack, Tab) ka koi bhi component `NavigationContainer` ke bahar kaam nahi kar sakta.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Navigation ki zaroori libraries install karni padti hain (yeh bohot saari hain):
        ```bash
        # Main library
        npm install @react-navigation/native
        # Dependencies (Expo)
        # npx expo install react-native-screens react-native-safe-area-context
        # Dependencies (RN CLI)
        npm install react-native-screens react-native-safe-area-context
        ```
      * **Step 2:** `NavigationContainer` ko `App.js` mein import karo.
      * **Step 3:** Apne poore app (e.g., `StackNavigator`) ko isse wrap kar do.
7.  **💻 Code example:** (Pehle `Stack Navigator` (next topic) ke saath dekho)
      * (Neeche `Stack Navigator` ke full example mein `NavigationContainer` ka use dekho)
      * ```javascript
          // App.js
          import { NavigationContainer } from '@react-navigation/native';
          import { MyStackNavigator } from './MyStack'; // (Assuming MyStack file hai)

          const App = () => {
            return (
              // 1. Poore app ko wrap kiya
              <NavigationContainer>
                <MyStackNavigator /> 
              </NavigationContainer>
            );
          };
          export default App;
        ```
    **✍️ Line-by-line explanation:**
      * `import { NavigationContainer } ...`: Library se `Container` ko import kiya.
      * `<NavigationContainer> ... </NavigationContainer>`: Poore app (jo yahan `MyStackNavigator` hai) ko wrap kar diya.
      * **🚀 Quick run expected output:** Yeh component *kuch dikhata nahi hai*. Yeh sirf peeche (background) mein navigation state ko manage karta hai.
8.  **🐞 Common beginner mistakes:**
      * `NavigationContainer` ko `App.js` mein add na karna.
      * Ek se zyada `NavigationContainer` bana dena (e.g., ek `App.js` mein, ek `MyStack.js` mein). ❌ (Hamesha 1 hi hona chahiye).
      * Zaroori dependencies (`react-native-screens`, `react-native-safe-area-context`) install na karna.
9.  **🌍 Real-world example / use-case:** Har React Native app jo `React Navigation` use karta hai.
10. **✅ Quick checklist / TL;DR:**
      * App ki root file (`App.js`) mein *ek baar* use hota hai.
      * Poore app (navigators) ko wrap karta hai.
      * Iske bina navigation kaam nahi karegi.
11. **❓ FAQs:**
      * **Q: Iska `Linking` prop kya hai?**
          * A: Woh "Deep Linking" (Module 9.5) ke liye hota hai (taaki website link se seedha app ki screen khul jaaye).
12. **🏋️‍♀️ Practice exercise:**
      * (Iski practice `Stack Navigator` ke saath hi hogi).
13. **📚 Further reading / commands / links:**
      * [React Navigation - Getting Started (Installation)](https://reactnavigation.org/docs/getting-started)

-----

#### 5.2 (Sub-topic): Stack Navigator

1.  **🎯 Title / Short Summary:** `Stack Navigator` - Screens ko ek ke upar ek rakhna (jaise taash ke patte).
2.  **🤔 Kya hai? (What?):** Yeh `React Navigation` ka sabse common navigator hai. Yeh screens ko ek "stack" (dher) mein manage karta hai. Jab aap nayi screen par jaate hain (`navigation.navigate`), toh woh screen stack ke *upar* aa jaati hai. Jab aap "Back" dabate hain, toh woh screen stack se *hat* (pop) jaati hai.
3.  **💡 Kyu important hai? (Why?):** Har app mein yeh "drill-down" (list se detail par jaana) pattern hota hai. (e.g., Chat list -\> Single Chat). Stack Navigator yeh kaam (Header, Back button) aapke liye automatic kar deta hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko ek screen se "aage" doosri screen par jaana ho aur "peeche" (back) aane ka option dena ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap screens ke beech aage-peeche nahi jaa payenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install @react-navigation/stack` (aur `react-native-gesture-handler` - Module 11)
      * **Step 2:** `createStackNavigator` ko import karo.
      * **Step 3:** Ek `Stack` object banao: `const Stack = createStackNavigator();`
      * **Step 4:** `Stack.Navigator` ke andar `Stack.Screen` components define karo.
          * `Stack.Screen`: Iske 2 zaroori prop hain:
            1.  `name`: Screen ka unique naam (jise hum `Maps` karne ke liye use karenge, e.g., "Home").
            2.  `component`: Us naam par kaunsa component (screen) dikhana hai (e.g., `HomeScreen`).
      * `navigation.navigate('ScreenName')`: Ek screen se doosri par jaane ke liye.
      * `navigation.goBack()`: Vaapas pichhli screen par jaane ke liye (yeh header ka "Back" button automatic karta hai).
7.  **💻 Code example:** (2 screens - Home, Details)
    ```javascript
    // Pehle: Saari libraries install karein (native, native-stack, screens, safe-area, gesture-handler)
    import React from 'react';
    import { View, Button, Text, StyleSheet } from 'react-native';
    import { NavigationContainer } from '@react-navigation/native';
    import { createStackNavigator } from '@react-navigation/stack'; // 1. Import

    // --- Screen 1: Home ---
    function HomeScreen({ navigation }) { // 5. 'navigation' prop automatic milta hai
      return (
        <View style={styles.container}>
          <Text>Home Screen</Text>
          <Button
            title="Go to Details"
            // 6. Doosri screen par jaana
            onPress={() => navigation.navigate('Details')} 
          />
        </View>
      );
    }

    // --- Screen 2: Details ---
    function DetailsScreen({ navigation }) {
      return (
        <View style={styles.container}>
          <Text>Details Screen</Text>
          <Button
            title="Go back"
            onPress={() => navigation.goBack()} // 7. Vaapas jaana
          />
        </View>
      );
    }

    // 2. Stack object banao
    const Stack = createStackNavigator();

    // --- App.js ---
    const App = () => {
      return (
        <NavigationContainer> {/* 8. Container zaroori hai */}
          {/* 3. Stack Navigator */}
          <Stack.Navigator 
             initialRouteName="Home" // Pehli kaunsi screen dikhe
          >
            {/* 4. Screens define karo */}
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Details" component={DetailsScreen} />
          </Stack.Navigator>
        </NavigationContainer>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, alignItems: 'center', justifyContent: 'center' },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { createStackNavigator } ...`: Stack library ko import kiya.
      * `function HomeScreen({ navigation }) { ... }`: `HomeScreen` banaya. `Stack.Screen` mein register hone wale har component ko `navigation` prop automatic mil jaata hai.
      * `onPress={() => navigation.navigate('Details')}`: `navigation` prop ke `Maps` function ko call kiya. Use bataya ki `'Details'` (jo `name` humne neeche diya hai) screen par jaana hai.
      * `onPress={() => navigation.goBack()}`: `goBack()` function ko call kiya (stack se current screen ko hatane ke liye).
      * `const Stack = createStackNavigator();`: Stack object banaya.
      * `<NavigationContainer>`: Root container (pichhla topic).
      * `<Stack.Navigator initialRouteName="Home">`: Stack ki shuruaat ki. Bataya ki sabse pehle `'Home'` screen dikhana.
      * `<Stack.Screen name="Home" component={HomeScreen} />`: Register kiya: 'Home' naam `HomeScreen` component ko point karta hai.
      * `<Stack.Screen name="Details" component={DetailsScreen} />`: Register kiya: 'Details' naam `DetailsScreen` component ko point karta hai.
      * **🚀 Quick run expected output:** "Home Screen" dikhegi (ek Header ke saath). "Go to Details" dabane par, "Details Screen" *slide* ho kar aayegi (header mein "Back" button ke saath). "Go back" (ya header ka "Back") dabane par vaapas "Home Screen" par aa jaayenge.
8.  **🐞 Common beginner mistakes:**
      * Libraries (`native`, `stack`, `screens`, `safe-area`, `gesture-handler`) poori install na karna.
      * `NavigationContainer` mein wrap na karna.
      * `navigation.navigate()` mein `name` (e.g., 'Details') ki spelling galat likhna.
      * `Stack.Screen` ko `name` ya `component` prop na dena.
9.  **🌍 Real-world example / use-case:**
      * Settings (list) -\> Notification Settings (detail).
      * Email (list) -\> Open Email (detail).
      * Products (list) -\> Product Details (detail).
10. **✅ Quick checklist / TL;DR:**
      * Ek screen se doosri par "aage" (aur "peeche") jaane ke liye.
      * `createStackNavigator` se banta hai.
      * `<Stack.Navigator>` mein `<Stack.Screen>` (name, component) register karte hain.
      * `navigation.navigate('Name')` se aage jaate hain.
      * `navigation.goBack()` se peeche aate hain.
11. **❓ FAQs:**
      * **Q: Header ka title kaise badloon?**
          * A: `<Stack.Screen name="Home" component={HomeScreen} options={{ title: 'My Home' }} />` (Screen par `options` prop se).
      * **Q: Header ko chupana (hide) kaise hai?**
          * A: `options={{ headerShown: false }}`.
      * **Q: Screen par data (e.g., User ID) kaise bhejoon?**
          * A: `navigation.navigate('Details', { userId: 123 })`. (Details screen `route.params.userId` se access karegi - Advanced).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein ek teesri screen "ProfileScreen" banao.
      * "Details" screen par ek button "Go to Profile" add karo jo `navigation.navigate('Profile')` call kare.
      * `Stack.Navigator` mein "Profile" screen ko register karo.
13. **📚 Further reading / commands / links:**
      * [React Navigation - Stack Navigator](https://reactnavigation.org/docs/stack-navigator)

-----

#### 5.2 (Sub-topic): Comparison: Stack, Tab, & Drawer Navigators

1.  **🎯 Title / Short Summary:** Navigation ke 3 prakaar: Stack (aage-peeche), Tab (neeche), Drawer (side se).
2.  **🤔 Kya hai? (What?):**
      * **Stack Navigator:** (Jo abhi padha) Screens ko ek ke upar ek rakhta hai. (Aage-peeche).
      * **Tab Navigator:** Screen ke neeche (ya upar) TABS (buttons) dikhata hai. (e.g., Home, Profile, Settings).
      * **Drawer Navigator:** Screen ke side (left ya right) se nikalne wala menu (drawer) banata hai.
3.  **💡 Kyu important hai? (Why?):** Aapke app ka "flow" (User kahan se kahan jaayega) inhi 3 par depend karta hai. Koi app *sirf* ek, ya (aksar) *sabko mila kar* (e.g., Tab ke andar Stack) use karta hai.

> 💡 **Special Rule Note:** Hum inko ek comparison table mein dekhenge.

**Comparison Table: Stack vs Tab vs Drawer**

| Feature | 🥞 Stack Navigator | 📱 Tab Navigator | ☰ Drawer Navigator |
| :--- | :--- | :--- | :--- |
| **Visual Look** | Har screen ke top par "Header" (Back button ke saath). | Screen ke **neeche** (ya upar) "Tabs" (buttons). | Screen par "Hamburger" (☰) icon, tap karne par **side se** menu khulta hai. |
| **⏰ Kab use karein? (When?)** | Jab screens ka sequence (kram) ho. (e.g., List -\> Detail -\> Edit). | Jab app ki 3-5 main (barabar) screens hon. (e.g., Home, Search, Profile). | Jab app ki bohot saari screens (5+) hon ya secondary screens hon. (e.g., Settings, Logout, About Us). |
| **❌ Agar... (Consequences)** | Agar aapne 5 main screens (Home, Search, Profile) ke liye Stack use kiya, toh user ko Home se Profile jaane ke liye bohot "aage-aage" jaana padega (bura UX). | Agar aapne "Login" -\> "Register" ke liye Tab use kiya, toh yeh galat hai (yeh sequence hai). | Agar aapne 2 main screens (Home, Feed) ke liye Drawer use kiya, toh yeh "overkill" (zaroorat se zyada) hai. |
| **Library** | `@react-navigation/stack` | `@react-navigation/bottom-tabs` (Neeche) <br> `@react-navigation/material-top-tabs` (Upar) | `@react-navigation/drawer` |
| **🌍 Real-world example?** | **WhatsApp:** Chat List (Screen 1) -\> Single Chat (Screen 2). | **Instagram:** Neeche ke 5 button (Home, Search, Reels, Shop, Profile). | **Gmail / Zomato:** Left-side se nikalne wala menu (Inbox, Sent, Spam... / Your Orders, Settings...). |
| **❓ FAQs (related)?** | **Q: Back button kahan se aata hai?** <br> A: Automatic (jab stack mein 1+ screen ho). | **Q: State (data) save rehta hai?** <br> A: Haan. Agar aap Home se Profile (Tab) jaate hain aur vaapas Home aate hain, toh Home "refresh" nahi hota. | **Q: Yeh bhi state save karta hai?** <br> A: Haan. Tab jaisa hi behaviour hai. |

-----

**(Baaqi 13-point format ke points)**

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Aksar apps **"Nested"** (ek ke andar ek) hote hain.
      * **Common Pattern:**
        1.  Root mein `Tab Navigator` (Home, Settings).
        2.  "Home" Tab ke andar ek `Stack Navigator` (HomeList -\> HomeDetail).
        3.  "Settings" Tab ke andar doosra `Stack Navigator` (SettingsList -\> ProfileEdit).
      * Is tarah, user "Home" tab mein rehte hue aage-peeche (stack) jaa sakta hai.
7.  **💻 Code example:** (Nesting: Tab ke andar Stack)
    ```javascript
    // Pehle: npm install @react-navigation/bottom-tabs
    import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
    import { createStackNavigator } from '@react-navigation/stack';
    import { NavigationContainer } from '@react-navigation/native';
    // (HomeScreen, DetailsScreen, SettingsScreen components upar se assume karo)

    const HomeStack = createStackNavigator();
    const SettingsStack = createStackNavigator();
    const Tab = createBottomTabNavigator();

    // 1. Home Tab ka apna Stack
    function HomeStackNavigator() {
      return (
        <HomeStack.Navigator>
          <HomeStack.Screen name="Home" component={HomeScreen} />
          <HomeStack.Screen name="Details" component={DetailsScreen} />
        </HomeStack.Navigator>
      );
    }

    // 2. Settings Tab ka apna Stack
    function SettingsStackNavigator() {
      return (
        <SettingsStack.Navigator>
          <SettingsStack.Screen name="Settings" component={SettingsScreen} />
          {/* ...yahan aur settings screens ho sakti hain */}
        </SettingsStack.Navigator>
      );
    }

    // 3. Root (Tab) Navigator
    const App = () => {
      return (
        <NavigationContainer>
          <Tab.Navigator>
            <Tab.Screen name="HomeTab" component={HomeStackNavigator} />
            <Tab.Screen name="SettingsTab" component={SettingsStackNavigator} />
          </Tab.Navigator>
        </NavigationContainer>
      );
    };
    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `HomeStackNavigator`: Ek function banaya jo *sirf* Home ki screens (Home, Details) ka Stack manage karta hai.
      * `SettingsStackNavigator`: Ek function jo *sirf* Settings ki screens ka Stack manage karta hai.
      * `<Tab.Navigator>`: Root navigator (neeche tabs).
      * `<Tab.Screen name="HomeTab" component={HomeStackNavigator} />`: Pehla Tab banaya. Lekin iska `component` ek *screen* nahi, balki poora `HomeStackNavigator` hai.
      * **🚀 Quick run expected output:** Neeche 2 tab (HomeTab, SettingsTab) dikhenge. Jab aap "HomeTab" par honge, aap "Home" screen se "Details" screen (Stack) par jaa payenge, aur tab bar neeche dikhta rahega.
8.  **✅ Quick checklist / TL;DR:**
      * **Stack:** Sequential (kram) flow (List -\> Detail).
      * **Tab:** 3-5 main (barabar) screens (Home, Profile).
      * **Drawer:** 5+ (bahut saari) ya secondary (kam zaroori) screens (Settings, Logout).
      * Real apps mein sabko *nest* (mila kar) use karte hain.
9.  **🏋️‍♀️ Practice exercise:**
      * Socho: WhatsApp ke UI ke liye kaunsa combination lagega? (Hint: Top Tabs (Chats, Status, Calls) aur har Chat ke andar Stack).
10. **📚 Further reading / commands / links:**
      * [React Navigation - Tab Navigator](https://www.google.com/search?q=https://reactnavigation.org/docs/tab-based-navigation)
      * [React Navigation - Drawer Navigator](https://reactnavigation.org/docs/drawer-navigator)

-----

### 5.3: Redux (Global State Management ka introduction)

1.  **🎯 Title / Short Summary:** Redux - App ki "Global" (poore app ki) memory 🧠.
2.  **🤔 Kya hai? (What?):** Redux ek state management **library** hai. Yeh `useState` jaisa *nahi* hai. `useState` "local" state (sirf ek component ki memory) hai. Redux "global" state (poore app ki memory, jaise "User login hai ya nahi") ko ek *central (ek) jagah* par rakhta hai.
3.  **💡 Kyu important hai? (Why?):**
      * **Problem (Prop Drilling):** Agar Screen A (parent) ke paas data hai aur Screen Z (bohot neeche, child) ko woh data chahiye, toh aapko woh data props ke zariye (A -\> B -\> C -\> ... -\> Z) bhejna padega. Ise "prop drilling" kehte hain aur yeh bohot bura hai.
      * **Solution (Redux):** Screen Z seedha "Global" Redux Store se data maang leti hai.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab data "global" ho (bohot saari screens ko uski zaroorat ho). Jaise: User Info (login state), App Theme (dark/light), Cart (e-commerce).
      * **Alternative:** Chote apps ke liye Redux **overkill** hai. Chote apps ke liye `React.Context` (Module 8.2) ya `Zustand` (Module 10.3) behtar hain. Hum Redux isliye seekh rahe hain kyunki yeh bade apps ka standard hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Chote apps mein kuch nahi. Bade apps mein aap "prop drilling" mein phans jaayenge aur state ko manage karna namumkin ho jaayega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (High Level):**
      * Redux ke 3 main bhaag hote hain:
      * **1. Store:** Yeh "global" dabba (object) hai jismein saara data (state) rehta hai. (e.g., `{ user: null, theme: 'light' }`). Yeh poore app mein *ek* hi hota hai.
      * **2. Action:** Ek event (object) jo batata hai ki "kya karna hai". (e.g., `{ type: 'LOGIN_SUCCESS', payload: { name: 'Rahul' } }`).
      * **3. Reducer:** Ek *pure function* jo 'Action' ko sunta hai. Yeh purana 'state' aur 'action' leta hai aur *naya* 'state' return karta hai.
          * (e.g., `if (action.type === 'LOGIN_SUCCESS') { return { ...state, user: action.payload }; }`)
      * **Modern Redux (Redux Toolkit):** Purana Redux bohot complex tha. Ab hum *hamesha* `Redux Toolkit (RTK)` (Module 10) use karte hain, jo yeh saara setup bohot aasan kar deta hai.
7.  **💻 Code example:** (Yeh *sirf* introduction hai, poora setup Module 10 mein hai. Yeh pseudo-code jaisa hai.)
    ```javascript
    // (Yeh code chalega nahi, yeh sirf concept hai)

    // --- 1. Action (Event) ---
    // User ne Login button dabaya
    const loginAction = {
      type: 'USER_LOGGED_IN',
      payload: { name: 'Priya', email: 'priya@example.com' }
    };

    // --- 2. Reducer (Function jo state badalta hai) ---
    // Shuruaati state
    const initialState = {
      user: null, // Shuru mein koi login nahi hai
    };

    function userReducer(state = initialState, action) {
      if (action.type === 'USER_LOGGED_IN') {
        // Naya state return karo
        return {
          ...state, // Purana state copy karo (e.g., theme)
          user: action.payload // User ko update karo
        };
      }
      if (action.type === 'USER_LOGGED_OUT') {
        return {
          ...state,
          user: null // User ko null kar do
        };
      }
      return state; // Agar action match nahi hua, toh purana state vaapas bhejo
    }

    // --- 3. Store (Global Dabba) ---
    // (Yeh 'Redux Toolkit' se banta hai)
    // const store = configureStore({ reducer: userReducer });

    // --- 4. Component mein use karna ---
    // const user = useSelector(state => state.user); // Store se data padhna
    // const dispatch = useDispatch(); // Action bhejne ke liye
    // dispatch(loginAction); // Action ko "dispatch" (bhejna)
    ```
    **✍️ Line-by-line explanation:**
      * `loginAction`: Ek object jo bata raha hai ki 'USER\_LOGGED\_IN' hua hai aur data (`payload`) yeh hai.
      * `userReducer`: Ek function. Yeh check karta hai ki `action.type` kya hai.
      * `if (action.type === 'USER_LOGGED_IN')`: Agar action match hua...
      * `return { ...state, user: action.payload }`: ...toh *naya* state object return karo. `...state` (spread operator) se purani state copy ki, aur `user` ko `action.payload` se update kar diya. **(Redux ka Rule: State ko "mutate" (direct change) nahi karte, hamesha *naya* state return karte hain)**.
      * `useSelector` (React hook): Component ko Store se data *padhne* (select) deta hai.
      * `useDispatch` (React hook): Component ko Store mein action *bhejne* (dispatch) deta hai.
      * **🚀 Quick run expected output:** Concept: `Button` (component) `dispatch(loginAction)` call karega. `Reducer` is action ko sunega, `Store` mein `user` ko `null` se `{ name: 'Priya' }` kar dega. `ProfileScreen` (component) `useSelector` se is naye `user` ko automatic receive kar legi aur "Welcome, Priya" dikha degi.
8.  **🐞 Common beginner mistakes:**
      * Har cheez (jaise Form input) ko Redux mein daal dena. (Form input 'local' state hai, use `useState` mein hi rakho).
      * Reducer ke andar state ko *mutate* (direct change) karna. (e.g., `state.user = action.payload; return state;` ❌ **Sabse badi galti\!**).
      * Bina `Redux Toolkit (RTK)` ke purana Redux seekhne ki koshish karna.
9.  **🌍 Real-world example / use-case:**
      * User ka login data (Auth token, user details).
      * E-commerce app ka Cart (cart items).
      * App ki global settings (Dark/Light mode).
10. **✅ Quick checklist / TL;DR:**
      * Redux = Global State.
      * Problem solve karta hai: "Prop Drilling".
      * 3 parts: Action (Event), Reducer (Logic), Store (Dabba).
      * **Hamesha `Redux Toolkit (RTK)` (Module 10) use karo.**
11. **❓ FAQs:**
      * **Q: `useState` vs Redux?**
          * A: `useState` = Local state (ek component ke liye). Redux = Global state (poore app ke liye).
      * **Q: Redux bohot complex nahi hai?**
          * A: Haan, hai. Isiliye chote apps ke liye `Context API` (Module 8) ya `Zustand` (Module 10) use karein.
      * **Q: `Redux Toolkit (RTK)` kya hai?**
          * A: Yeh Redux ki official library hai jo Redux ka 80% complex code (boilerplate) hata deti hai. (Hum Module 10 mein detail mein karenge).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `userReducer` mein `USER_LOGGED_OUT` action ko dekho.
      * Socho: `UPDATE_PROFILE_PIC` action ke liye reducer kaisa dikhega? (Hint: `payload` mein naya `picUrl` aayega).
13. **📚 Further reading / commands / links:**
      * [Redux Official Docs (Introduction)](https://redux.js.org/introduction/getting-started)
      * [Redux Toolkit (RTK) Docs (Yeh use karna hai)](https://redux-toolkit.js.org/)

-----

### 5.4: Advanced Forms (`react-hook-form`)

1.  **🎯 Title / Short Summary:** `react-hook-form` - Complex forms (Signup/Login) ko aasaani se manage karna.
2.  **🤔 Kya hai? (What?):** Yeh ek **library** hai (Module 1.5 mein compare kiya tha) jo *sirf* forms ke liye bani hai. Yeh form ki state, validation (rules), aur submission ko handle karti hai.
3.  **💡 Kyu important hai? (Why?):** `useState` se 10-field ka form (Signup) banana matlab 10 `useState` calls. `react-hook-form` (RHF) se aap 1 `useForm` hook se saara kaam kar lete hain. Yeh *bohot fast* hai kyunki yeh "uncontrolled" inputs use karta hai (har key press par re-render nahi hota).
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi form mein 2+ fields hon, ya 1 bhi field ho par uspar *validation* (e.g., "Email format sahi hona chahiye") ki zaroorat ho. (e.g., Login, Signup, Settings).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap `useState` use karenge. Simple form (1-2 field) ke liye theek hai. Complex form ke liye aapka component bohot lamba, messy, aur *slow* (har key press par re-render) ho jaayega.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install react-hook-form`
      * **Step 2:** `useForm` hook ko import karo.
      * **Step 3:** `useForm` se 3 cheezein nikaalo:
          * `control`: Yeh RHF ko state se connect karta hai.
          * `handleSubmit`: Yeh ek wrapper function hai. Yeh *tabhi* aapka function (e.g., `onSubmit`) call karega jab saari validation pass ho jaayegi.
          * `formState: { errors }`: Ek object jismein saari validation errors (galtiyan) aayengi.
      * **Step 4:** Har `TextInput` ko `useState` se connect karne ke bajaye, use `<Controller>` component (RHF ka) se wrap karo.
      * **Step 5:** `Controller` ko `control`, `name`, aur `rules` (validation) do.
7.  **💻 Code example:** (Simple Login Form)
    ```javascript
    // 1. Pehle: npm install react-hook-form
    import React from 'react';
    import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
    import { useForm, Controller } from 'react-hook-form'; // 2. Import

    const App = () => {
      // 3. useForm hook
      const { control, handleSubmit, formState: { errors } } = useForm({
        defaultValues: { // Shuruaati values
          email: '',
          password: ''
        }
      });

      // 4. Form submit hone par yeh chalega (agar validation pass hui)
      const onSubmit = (data) => {
        console.log(data); // data = { email: '...', password: '...' }
        Alert.alert('Success', `Email: ${data.email}`);
      };

      return (
        <View style={styles.container}>
          <Text style={styles.title}>Login (React Hook Form)</Text>

          {/* 5. Controller (Email) */}
          <Controller
            control={control} // RHF se connect kiya
            name="email" // Is field ka naam (state mein key)
            rules={{ // 6. Validation Rules
              required: 'Email zaroori hai',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: 'Invalid email address'
              }
            }}
            render={({ field: { onChange, onBlur, value } }) => (
              <TextInput
                style={styles.input}
                placeholder="Email"
                onBlur={onBlur}
                onChangeText={onChange}
                value={value}
                keyboardType="email-address"
              />
            )}
          />
          {/* 7. Error dikhana */}
          {errors.email && <Text style={styles.error}>{errors.email.message}</Text>}

          {/* 8. Controller (Password) */}
          <Controller
            control={control}
            name="password"
            rules={{
              required: 'Password zaroori hai',
              minLength: {
                value: 6,
                message: 'Password kam se kam 6 character ka hona chahiye'
              }
            }}
            render={({ field: { onChange, onBlur, value } }) => (
              <TextInput
                style={styles.input}
                placeholder="Password"
                onBlur={onBlur}
                onChangeText={onChange}
                value={value}
                secureTextEntry
              />
            )}
          />
          {errors.password && <Text style={styles.error}>{errors.password.message}</Text>}

          {/* 9. Submit Button */}
          <Button title="Login" onPress={handleSubmit(onSubmit)} />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', padding: 20 },
      title: { fontSize: 20, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
      input: { height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 5, padding: 10 },
      error: { color: 'red', marginBottom: 10 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import { useForm, Controller } ...`: RHF se hooks import kiye.
      * `const { control, handleSubmit, ... } = useForm(...)`: Hook ko call kiya.
      * `const onSubmit = (data) => { ... }`: Hamara function. `handleSubmit` ise `data` (poora form state) pass karega.
      * `<Controller ... />`: `TextInput` ko wrap karne wala component.
      * `control={control}`: Hook se connect kiya.
      * `name="email"`: Is field ka naam (key) "email" rakha.
      * `rules={{ required: ... }}`: Validation rules set kiye. Agar field khali hogi, toh 'Email zaroori hai' message set ho jaayega.
      * `render={({ field: { onChange, onBlur, value } }) => (...)`: Yeh `Controller` ka part hai. Yeh aapko `onChange`, `value` (jo `useState` se milti thi) RHF se le kar deta hai. Humne inhe seedha `TextInput` ko pass kar diya.
      * `{errors.email && ...}`: "Agar `errors.email` object exist karta hai, toh `Text` mein uska `message` dikhao."
      * `onPress={handleSubmit(onSubmit)}`: **Important:** Humne `onPress` mein seedha `onSubmit` nahi, balki `handleSubmit(onSubmit)` pass kiya. `handleSubmit` pehle *validation* check karega, agar sab sahi hai *tabhi* hamare `onSubmit` function ko call karega.
      * **🚀 Quick run expected output:** Ek Login form. Agar "Login" button bina kuch type kiye dabayenge, toh "Email zaroori hai" aur "Password zaroori hai" (red text) dikhega. Agar galat email daalenge, toh "Invalid email address" dikhega. Sab sahi daalne par hi "Success" alert aayega.
8.  **🐞 Common beginner mistakes:**
      * `TextInput` ko `Controller` se wrap na karna.
      * `Controller` ko `control` prop na dena.
      * Submit button ke `onPress` mein `handleSubmit(onSubmit)` ke bajaye sirf `onSubmit` likh dena (isse validation skip ho jaayegi).
      * Har choti cheez (jaise Search bar) ke liye RHF use karna (overkill).
9.  **🌍 Real-world example / use-case:** Har Login, Signup, Edit Profile, Settings, Post Create form.
10. **✅ Quick checklist / TL;DR:**
      * Complex forms + Validation = `react-hook-form`.
      * `useForm` se `control`, `handleSubmit`, `errors` milte hain.
      * Har `TextInput` ko `<Controller>` se wrap karo.
      * `rules` object mein validation (e.g., `required`, `minLength`) define karo.
      * `onPress={handleSubmit(onSubmit)}` use karo.
11. **❓ FAQs:**
      * **Q: `react-hook-form` vs `Formik`?**
          * A: Dono popular hain. `Formik` purana aur bohot stable hai. `react-hook-form` naya, fast (kam re-renders), aur Hooks par based hai. Naye projects ke liye log RHF prefer kar rahe hain.
      * **Q: `Controller` itna complex kyun hai? `render={...}`?**
          * A: Kyunki `react-hook-form` React Native (jismein `Controller` zaroori hai) aur React (Web) (jahan `register` function se aasan ho jaata hai) dono support karta hai. `Controller` hi RHF ko `TextInput` se "connect" karta hai.
      * **Q: Validation ke liye `Yup` kya hai?**
          * A: `Yup` ek alag library hai jo validation *schema* (rules ka object) banane deti hai. Aap RHF ko `Yup` ke saath jod (integrate) sakte hain (advanced).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein "Password" ke `minLength` ko 6 se 8 karke dekho.
      * Form mein ek naya field (Controller) "username" add karo, jo `required` ho. `onSubmit` mein use `console.log` karke dekho.
13. **📚 Further reading / commands / links:**
      * [React Hook Form - Getting Started](https://www.google.com/search?q=httpss://react-hook-form.com/get-started)
      * [React Hook Form with React Native (Examples)](https://react-hook-form.com/docs/usecontroller)


Module 5 complete\! 💥 Yeh bohot heavy module tha (Navigation, Redux, Forms). In concepts ko master karne mein time lagta hai, lekin ab aap poore apps (sirf UI nahi) banana shuru kar sakte hain.

Jab aap taiyaar hon, toh **"Module 6 ke notes do"** bolna\! 🧑‍💻

=============================================================

# MODULE-6 → Data, Tooling & Best Practices

### 6.1: HTTP Requests (Axios se API call karna)

1.  **🎯 Title / Short Summary:** Axios - Server (API) se data laane (GET) aur bhejne (POST) ka best tareeka.
2.  **🤔 Kya hai? (What?):** Axios ek **library** hai (core component nahi) jo HTTP requests (API calls) ko bohot aasan bana deti hai. Yeh `fetch` (jo React Native mein built-in hai) se behtar hai kyunki yeh `JSON` data ko automatically handle karti hai aur error handling aasan karti hai.
3.  **💡 Kyu important hai? (Why?):** Aapka app "zinda" tabhi hota hai jab woh server se real-time data laata hai (jaise Instagram feed, weather). Axios yeh data laane ka sabse popular tareeka hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko server se baat karni ho:
      * `GET`: Data laane ke liye (e.g., user ki profile, product list).
      * `POST`: Server par naya data banane ke liye (e.g., user signup, new post).
      * `PUT`/`PATCH`: Data update karne ke liye.
      * `DELETE`: Data delete karne ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko built-in `fetch` API use karna padega. `fetch` bura nahi hai, lekin usme aapko har response ko `.then(res => res.json())` karke manually JSON mein badalna padta hai aur error handling (jaise 404 error) thodi mushkil hoti hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install axios`
      * **Step 2:** Import karo: `import axios from 'axios';`
      * **Step 3:** `GET` request (Data laana):
          * `axios.get('URL')`
          * Yeh `Promise` return karta hai, jise hum `async/await` (best tareeka) ya `.then()` se handle karte hain.
          * Data `response.data` mein milta hai.
      * **Step 4:** `POST` request (Data bhejna):
          * `axios.post('URL', { data_object })`
          * Doosre argument mein hum woh data (object) bhejte hain jo server par save karna hai.
7.  **💻 Code example:** (Data fetch karna `useEffect` mein)
    ```javascript
    // 1. Pehle: npm install axios
    import React, { useState, useEffect } from 'react';
    import { View, Text, Button, ActivityIndicator, StyleSheet } from 'react-native';
    import axios from 'axios'; // 2. Import

    const App = () => {
      const [loading, setLoading] = useState(false);
      const [data, setData] = useState(null);

      // 3. GET Request (Data laane ke liye)
      const fetchData = async () => {
        setLoading(true);
        try {
          // 4. Axios GET call (async/await ke saath)
          const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
          setData(response.data); // 5. Data 'response.data' mein hota hai
        } catch (error) {
          console.error('Error fetching data:', error);
        } finally {
          setLoading(false);
        }
      };

      // 6. POST Request (Data bhejne ke liye)
      const postData = async () => {
        try {
          const response = await axios.post('https://jsonplaceholder.typicode.com/posts', {
            title: 'foo',
            body: 'bar',
            userId: 1,
          });
          console.log('POST Response:', response.data);
          alert('Data posted! ID: ' + response.data.id);
        } catch (error) {
          console.error('Error posting data:', error);
        }
      };
      
      // 7. useEffect (Module 8) taaki app load hote hi data aaye
      useEffect(() => {
        fetchData();
      }, []); // [] = Sirf ek baar chalao

      return (
        <View style={styles.container}>
          {loading ? (
            <ActivityIndicator size="large" />
          ) : (
            <Text style={styles.text}>{data ? data.title : 'No data'}</Text>
          )}
          <Button title="Post New Data" onPress={postData} />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
      text: { fontSize: 16, textAlign: 'center', marginBottom: 20 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import axios from 'axios';`: Axios library ko import kiya.
      * `const fetchData = async () => { ... }`: Ek `async` function banaya API call ke liye.
      * `const response = await axios.get(...)`: `axios.get` ko call kiya aur `await` (intezaar) kiya jab tak response nahi aa jaata.
      * `setData(response.data);`: Axios ki khaasiyat: response *seedha* `response.data` mein milta hai (JSON parse nahi karna padta).
      * `catch (error) { ... }`: Agar network fail (ya 404/500) hua, toh error `catch` block mein aayega.
      * `finally { setLoading(false); }`: Chahe success ho ya error, loading `false` kar do.
      * `const postData = async () => { ... }`: `POST` request ke liye function.
      * `await axios.post('URL', { ... })`: `post` method use kiya. Doosre argument mein data (payload) object bheja.
      * `useEffect(() => { fetchData(); }, []);`: App load hote hi `fetchData` function ko call kiya.
      * **🚀 Quick run expected output:** App khulega, `ActivityIndicator` dikhega, 1-2 second mein woh hatega aur ek API se aaya hua *title* dikhega. "Post New Data" button dabane par console mein naya post (ID: 101) log hoga.
8.  **🐞 Common beginner mistakes:**
      * `axios` install na karna.
      * `response.data` ke bajaye `response.json()` (yeh `fetch` mein hota hai) use karna.
      * `async` function banakar `await` keyword lagana bhool jaana.
      * `catch` block na lagana (aur app crash ho jaana jab network band ho).
9.  **🌍 Real-world example / use-case:** Har API call. Login (POST), User profile (GET), Like post (POST).
10. **✅ Quick checklist / TL;DR:**
      * `npm install axios`.
      * `import axios from 'axios'`.
      * Data laana: `const res = await axios.get(url);`
      * Data bhejna: `const res = await axios.post(url, dataObject);`
      * Data hamesha `res.data` mein hota hai.
      * Hamesha `try...catch` block use karo.
11. **❓ FAQs:**
      * **Q: `fetch` vs `axios`?**
          * A: `axios` behtar hai. Yeh JSON automatically handle karta hai, `try...catch` se error (404/501) pakad leta hai, aur (next topic) `interceptors` support karta hai.
      * **Q: `Authorization` (Token) kaise bhejein?**
          * A: `axios.get(url, { headers: { 'Authorization': 'Bearer YOUR_TOKEN' } })`. (Interceptors isse aasan bana dete hain).
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein `jsonplaceholder` URL mein `posts/1` ko `posts/2` karke naya title fetch karo.
      * `fetchData` function ko ek button "Fetch Again" ke `onPress` mein daalo (taaki `useEffect` se na chale).
13. **📚 Further reading / commands / links:**
      * [Axios GitHub (Docs)](https://github.com/axios/axios)
      * [JSONPlaceholder (Free fake API)](https://jsonplaceholder.typicode.com/)

-----

#### 6.1 (Sub-topic): `Axios` Interceptors & Retry

1.  **🎯 Title / Short Summary:** Interceptors - Har API call ke "beech" mein aane wala Guard (Rakshak).
2.  **🤔 Kya hai? (What?):** Interceptors "middleware" (beech ke function) hote hain. Axios aapko 2 interceptor deta hai:
    1.  **Request Interceptor:** Har request ke "jaane se pehle" chalta hai.
    2.  **Response Interceptor:** Har response ke "aane ke baad" chalta hai.
3.  **💡 Kyu important hai? (Why?):**
      * **Request Interceptor:** Har request mein *automatic* `Authorization` Token (Header) add karne ke liye. (Aapko har `axios.get` mein manually nahi likhna padega).
      * **Response Interceptor:** Error ko centrally (ek jagah) handle karne ke liye. (Jaise: Agar "401 Unauthorized" error aaye, toh user ko automatic "Logout" kar do).
      * **Retry:** Agar API fail (e.g., 503 error) ho, toh response interceptor se `retry` (dobara try) logic likh sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Production-level app mein *hamesha*. Jab aapko app mein Login (Authentication) system ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko har API call (100+ calls) mein manually `headers: { Authorization: ... }` likhna padega. Aur har call mein manually `if (error.response.status === 401) { logout(); }` likhna padega (Bohot repetitive code).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * Aap ek alag file (e.g., `api.js`) banate hain.
      * Wahaan `axios.create()` se ek "instance" banate hain.
      * Us instance par `.interceptors.request.use()` (request ke liye) aur `.interceptors.response.use()` (response ke liye) lagate hain.
      * Apne app mein `axios` ko nahi, is *instance* ko import karte hain.
7.  **💻 Code example:** (`api.js` - Axios instance file)
    ```javascript
    import axios from 'axios';
    import AsyncStorage from '@react-native-async-storage/async-storage'; // Token store karne ke liye

    // 1. Ek 'instance' banaya (common base URL ke saath)
    const api = axios.create({
      baseURL: 'https://api.example.com/v1/',
      timeout: 10000, // 10 sec baad timeout
    });

    // 2. Request Interceptor (Request jaane se pehle)
    api.interceptors.request.use(
      async (config) => {
        // Yahan 'config' request ki poori setting hai
        // 3. AsyncStorage (ya Redux) se token nikalo
        const token = await AsyncStorage.getItem('user_token');
        
        if (token) {
          // 4. Agar token hai, toh har request ke header mein 'Authorization' add kar do
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config; // Config ko (badal kar) aage jaane do
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // 5. Response Interceptor (Response aane ke baad)
    api.interceptors.response.use(
      (response) => {
        // Agar response sahi (2xx) hai, toh seedha response aage bhej do
        return response;
      },
      (error) => {
        // 6. Agar error (4xx, 5xx) aaya
        if (error.response && error.response.status === 401) {
          // 7. Agar '401 Unauthorized' (token invalid) hai
          console.log('Token expired! Logging out...');
          // Yahan 'logout()' function call karo (e.g., Redux dispatch)
        }
        
        // (Retry logic yahan likh sakte hain, jo bohot complex hota hai)
        
        return Promise.reject(error); // Error ko aage component tak bhej do (catch block ke liye)
      }
    );

    export default api; // Default 'axios' nahi, 'api' instance export kiya

    // --- Component file (e.g., Profile.js) ---
    // import axios from 'axios'; // ❌ Galat
    // import api from './api'; // ✅ Sahi

    // const fetchProfile = async () => {
    //   const res = await api.get('/profile'); // Token automatic lag jaayega
    // }
    ```
    **✍️ Line-by-line explanation:**
      * `const api = axios.create(...)`: Naya instance banaya.
      * `api.interceptors.request.use(async (config) => ...)`: Request interceptor lagaya. Yeh ek `async` function hai (kyunki `AsyncStorage` `await` maangta hai).
      * `const token = await AsyncStorage.getItem(...)`: Phone ki storage se token padha.
      * `config.headers.Authorization = ...`: `config` (request object) ke headers mein token *add* kiya.
      * `return config;`: Modified `config` ko return kiya taaki request server par jaa sake.
      * `api.interceptors.response.use(...)`: Response interceptor lagaya. Iske 2 function hote hain: `(response)` (success ke liye) aur `(error)` (failure ke liye).
      * `if (error.response.status === 401) { ... }`: Central error handling. Agar error 401 (token invalid/expired) hai, toh user ko logout kar do.
      * **🚀 Quick run expected output:** Yeh code *kuch dikhata nahi hai*. Yeh background mein har API call ko secure (token add karke) aur robust (error handle karke) banata hai.
8.  **🐞 Common beginner mistakes:**
      * `async (config)` function se `config` ko return na karna. (Request aage nahi jaayegi).
      * `(error)` function se `Promise.reject(error)` return na karna. (Component ka `catch` block nahi chalega).
      * Interceptor set karke `axios` (default) ko use karte rehna (aapko `api` (instance) ko use karna hai).
9.  **🌍 Real-world example / use-case:** Har production-level app jismein login hai.
10. **✅ Quick checklist / TL;DR:**
      * `axios.create()` se instance banao.
      * `interceptors.request`: Token (Authorization Header) add karne ke liye.
      * `interceptors.response`: Global error handling (jaise 401 Logout) ke liye.
      * Apne app mein default `axios` ke bajaye instance (`api`) ko import karo.
11. **❓ FAQs:**
      * **Q: Retry (dobara try) kaise karein?**
          * A: Yeh complex hai. Response interceptor ke error function mein, aap check karte hain ki `error.status === 503` (Server busy). Agar haan, toh aap `setTimeout` se 3 second baad `axios.request(error.config)` (purani request) ko dobara call kar sakte hain. Iske liye `axios-retry` jaisi libraries aati hain.
12. **🏋️‍♀️ Practice exercise:**
      * (Yeh advanced topic hai). Bas `api.js` file banao aur `console.log('Request jaa rahi hai...')` request interceptor mein aur `console.log('Response aa gaya')` response interceptor mein lagao. Fir `api.get(...)` call karke dekho.
13. **📚 Further reading / commands / links:**
      * [Axios Interceptors Docs](https://axios-http.com/docs/interceptors)

-----

#### 6.1 (Sub-topic): Offline Handling (`NetInfo`, Caching) & SSL Pinning

1.  **🎯 Title / Short Summary:** Offline Handling (Jab Internet na ho) aur SSL Pinning (Security).
2.  **🤔 Kya hai? (What?):**
      * **`NetInfo`:** Ek **library** (`@react-native-community/netinfo`) jo batati hai ki user *online* hai ya *offline*.
      * **Caching:** Data ko phone par *save* karna (e.g., `AsyncStorage` mein), taaki jab user offline ho, toh use purana (cached) data dikha sakein.
      * **SSL Pinning:** Ek advanced **security** technique jo "Man-in-the-Middle" (MITM) attacks ko rokti hai.
3.  **💡 Kyu important hai? (Why?):**
      * **`NetInfo`:** Agar user offline hai, toh API call bhej kar (aur fail karke) app crash karane se behtar hai ki `NetInfo` se pehle hi check kar lo, aur user ko "You are offline" message dikha do.
      * **Caching:** Offline mode mein (jaise flight/metro mein) app ko "dead" (khali) dikhane se behtar hai ki purana data (last fetched) dikha do (jaise WhatsApp purane messages dikhata hai).
      * **SSL Pinning:** Banking, Finance, ya sensitive data wale apps ke liye *zaroori* hai. Yeh check karta hai ki app *sirf* aapke *asli* server se baat kar raha hai (kisi fake/hacker ke server se nahi).
4.  **⏰ Kab/use karna chahiye? (When?):**
      * `NetInfo`: Har API call se pehle (ya globally).
      * Caching: Har `GET` request ke saath (data aane par save karo, offline hone par dikhao).
      * SSL Pinning: Sirf High-Security apps (Banking) ke liye. Normal apps (e.g., blog) ko iski zaroorat nahi hai.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Bina `NetInfo`: Offline hone par app API call karega, fail hoga, aur user ko `ActivityIndicator` ya error dikhata rahega.
      * Bina Caching: App offline mode mein bilkul bekaar (useless) ho jaayega.
      * Bina SSL Pinning: Hackers (MITM attack se) aapke app aur server के beech ka saara data (password, token) padh sakte hain.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **`NetInfo`:**
          * `npm install @react-native-community/netinfo`
          * `NetInfo.fetch().then(state => console.log(state.isConnected))` se check kar sakte hain.
          * Ya `NetInfo.addEventListener(state => ...)` se live changes (WiFi gaya/aaya) sun sakte hain.
      * **Caching (Simple):**
        1.  API call (Axios) se data aaya (`response.data`).
        2.  Use `AsyncStorage.setItem('cache_key', JSON.stringify(response.data))` se save kar do.
        3.  Jab app *offline* ho (`NetInfo` ne bataya), tab `AsyncStorage.getItem('cache_key')` se data nikaal kar dikha do.
      * **SSL Pinning:**
          * Yeh native code (Android/iOS) mein hota hai ya `react-native-ssl-pinning` jaisi library use karti hai.
          * Aap library ko batate hain ki "sirf *is* certificate (hash) wale server par vishwas (trust) karna hai". Agar server ka certificate alag (fake) hai, toh library request ko fail kar degi.
7.  **💻 Code example:** (`NetInfo` aur simple Caching)
    ```javascript
    // 1. Pehle: npm install @react-native-community/netinfo
    // Aur: npm install @react-native-async-storage/async-storage
    import React, { useState, useEffect } from 'react';
    import { View, Text, Button, StyleSheet } from 'react-native';
    import NetInfo from '@react-native-community/netinfo';
    import AsyncStorage from '@react-native-async-storage/async-storage';
    import axios from 'axios';

    const CACHE_KEY = 'cached_posts';
    const API_URL = 'https://jsonplaceholder.typicode.com/posts/1';

    const App = () => {
      const [netState, setNetState] = useState(null);
      const [data, setData] = useState(null);

      // 2. NetInfo listener
      useEffect(() => {
        const unsubscribe = NetInfo.addEventListener(state => {
          setNetState(state);
          if (state.isConnected) {
            fetchData(true); // Internet hai toh 'force fetch'
          } else {
            fetchData(false); // Internet nahi hai toh 'cache se laao'
          }
        });
        return () => unsubscribe(); // Cleanup
      }, []);

      const fetchData = async (isOnline) => {
        if (isOnline) {
          // 3. Online: Fetch karo aur Cache karo
          console.log('Fetching from API...');
          try {
            const response = await axios.get(API_URL);
            setData(response.data);
            await AsyncStorage.setItem(CACHE_KEY, JSON.stringify(response.data));
            console.log('Data cached!');
          } catch (error) {
            console.log('API Error, trying cache');
            loadFromCache(); // Agar API fail ho (server down)
          }
        } else {
          // 4. Offline: Cache se load karo
          console.log('Offline. Loading from cache...');
          loadFromCache();
        }
      };

      const loadFromCache = async () => {
        const cachedData = await AsyncStorage.getItem(CACHE_KEY);
        if (cachedData) {
          setData(JSON.parse(cachedData));
        }
      };

      return (
        <View style={styles.container}>
          <Text>Internet Connected? {netState ? (netState.isConnected ? 'YES' : 'NO') : 'Checking...'}</Text>
          <Text>Type: {netState ? netState.type : 'N/A'}</Text>
          <Text style={styles.data}>{data ? data.title : 'Loading...'}</Text>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      data: { fontSize: 16, margin: 20, textAlign: 'center' },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `NetInfo.addEventListener(state => ...)`: `useEffect` mein listener lagaya jo network change par `state` update karega.
      * `if (state.isConnected) { fetchData(true); }`: Jaise hi internet (vaapas) aaya, `fetchData(true)` call kiya.
      * `if (isOnline) { ... }`: Agar online hain, toh API call karo (`axios.get`), data ko state (`setData`) mein daalo, aur `AsyncStorage.setItem` se *cache* (save) bhi kar do.
      * `else { loadFromCache(); }`: Agar offline hain, toh `loadFromCache` call karo.
      * `loadFromCache()`: `AsyncStorage.getItem(CACHE_KEY)` se purana data nikala aur `setData` kar diya.
      * **🚀 Quick run expected output:** App khulega, (agar online) "Fetching from API..." log hoga aur title dikhega. Ab WiFi/Data band kar do. "Internet Connected? NO" dikhega. App ko restart karo. Ab "Offline. Loading from cache..." log hoga aur purana (cached) title dikh jaayega (bina API call kiye).
8.  **🐞 Common beginner mistakes:**
      * `NetInfo` (library) install na karna.
      * `NetInfo.fetch()` ko har baar call karna (jabki `addEventListener` behtar hai).
      * `AsyncStorage` mein `JSON.stringify` (save karte time) aur `JSON.parse` (padhte time) karna bhool jaana (kyunki AsyncStorage sirf string save karta hai).
9.  **🌍 Real-world example / use-case:**
      * **NetInfo + Caching:** WhatsApp/Signal (offline mein bhi purane chats dikhata hai).
      * **SSL Pinning:** Har Banking App (HDFC, ICICI), Google Pay, PhonePe.
10. **✅ Quick checklist / TL;DR:**
      * `NetInfo` (library) se check karo user online hai ya nahi.
      * Online ho: API se data laao aur `AsyncStorage` mein cache (save) karo.
      * Offline ho: `AsyncStorage` se purana data dikhao.
      * High-Security apps ke liye `SSL Pinning` (native library) zaroori hai.
11. **❓ FAQs:**
      * **Q: Caching ke liye `AsyncStorage` se behtar kuch hai?**
          * A: Haan\! `AsyncStorage` bohot simple hai. Professional apps `React Query` (Module 10) ya `WatermelonDB` (Local Database - Module 6.11) use karte hain, jo caching bohot powerfully manage karte hain.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye code mein ek "Clear Cache" button add karo jo `AsyncStorage.removeItem(CACHE_KEY)` ko call kare.
13. **📚 Further reading / commands / links:**
      * [NetInfo (GitHub Docs)](https://github.com/react-native-netinfo/react-native-netinfo)
      * [SSL Pinning (Geeky theory)](https://www.google.com/search?q=https://owasp.org/www-community/Certificate_and_Public_Key_Pinning)

-----

### 6.2: Development Environment Setup (VS Code extensions)

1.  **🎯 Title / Short Summary:** VS Code extensions - Aapke code editor (VS Code) ko superpower dena 🦸.
2.  **🤔 Kya hai? (What?):** Yeh "Visual Studio Code" (code editor) ke liye chhote plugins (tools) hain jo React Native development ko bohot aasan, tez, aur error-free bana dete hain.
3.  **💡 Kyu important hai? (Why?):** Yeh aapka code automatically format (sundar) karte hain, code likhte time suggestions (autocomplete) dete hain, aur spelling/syntax errors batate hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Code likhna shuru karne se *pehle*.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapka code ganda (messy) dikhega, aapko har component (e.g., `<View>`) poora type karna padega, aur aap simple syntax errors (jaise comma bhool jaana) dhoondne mein time waste karenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Top 5 Zaroori Extensions (Inhe VS Code ke "Extensions" tab [Ctrl+Shift+X] mein search karke install karein):**
    <!-- end list -->
    1.  **ESLint:** (By Microsoft). Yeh aapke code ko "lint" (check) karta hai. Yeh JavaScript ke "rules" (niyam) laagu karta hai. Jaise: "Aapne variable (`x`) banaya par use nahi kiya" (Warning dega).
    2.  **Prettier - Code formatter:** (By Prettier). Yeh aapka code *automatic* `Save` (Ctrl+S) karne par format (sundar) kar deta hai. (Jaise extra space hataana, comma lagana).
    3.  **ES7+ React/Redux/React-Native snippets:** (By dsznajder). Yeh "snippets" (shortcuts) deta hai.
          * `rnc` (type karke Enter) -\> Poora React Native component (style, import ke saath) ban jaata hai.
          * `imrn` -\> `import { ... } from 'react-native'`
          * `usf` -\> `useState` hook.
    4.  **Material Icon Theme:** (By Philipp Kief). Yeh VS Code ke file explorer mein files/folders ke aage sundar icons (e.g., JS, TS, folder icons) dikhata hai.
    5.  **GitLens:** (By GitKraken). Yeh batata hai ki code ki *kis* line ko *kisne* aur *kab* badla tha. (Team mein kaam karne ke liye zaroori).
7.  **💻 Code example:** (Yeh dikhane ke liye hai ki snippet kaise kaam karta hai)
    ```javascript
    // 1. Aapne file kholi aur type kiya: 'rnc'
    // 2. Jaise hi aap Enter dabayenge, yeh extension neeche wala poora code
    //    automatic generate kar dega:

    import React, { Component } from 'react';
    import { View, Text, StyleSheet } from 'react-native';

    const App = () => {
      return (
        <View style={styles.container}>
          <Text>App</Text>
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: {
        flex: 1,
      },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * Upar ka poora code (import, component, styles, export) aapne *nahi* likha. Yeh `rnc` snippet ne 1 second mein generate kar diya.
      * **Prettier ka kaam:** Agar aapne ganda code (extra line/space) likha:
        `const     App   =    ()   =>   { ... }`
      * Jaise hi aap `Save` (Ctrl+S) karenge, Prettier use saaf kar dega:
        `const App = () => { ... }`
      * **🚀 Quick run expected output:** Aapka development 10 guna (10x) fast ho jaayega.
8.  **🐞 Common beginner mistakes:**
      * `Prettier` aur `ESLint` ko install karke configure na karna. (Install ke baad, VS Code settings [Ctrl+,] mein jaakar `Format On Save` ko `true` karna zaroori hai).
      * Snippets (jaise `rnc`) yaad na rakhna aur sab kuch haath se type karna.
9.  **🌍 Real-world example / use-case:** Har professional developer in tools ko use karta hai.
10. **✅ Quick checklist / TL;DR:**
      * `ESLint`: Rules (niyam) check karta hai.
      * `Prettier`: Code format (sundar) karta hai (`Format On Save`).
      * `ES7+... Snippets`: Shortcuts (`rnc`, `usf`) deta hai.
      * `GitLens`: Git history (kisne likha) batata hai.
11. **❓ FAQs:**
      * **Q: `Prettier` aur `ESLint` mein jhagda (conflict) ho toh?**
          * A: Haan, hota hai. Isiliye `eslint-config-prettier` (ek package) install karte hain jo ESLint ko batata hai ki "formatting ka kaam Prettier ka hai, tum sirf code quality check karo".
12. **🏋️‍♀️ Practice exercise:**
      * VS Code mein jaao, `ES7+ React/Redux/React-Native snippets` ko install karo.
      * Ek nayi file `Test.js` banao.
      * Usme `rnc` type karke `Enter` dabao.
13. **📚 Further reading / commands / links:**
      * [Top 10 VS Code Extensions (search on Google)](https://www.google.com/search?q=top+vs+code+extensions+for+react+native)

-----

### 6.3: Debugging (Flipper & React DevTools)

Debugging (error dhoondna) 80% development ka hissa hai. Hum iske har sub-topic ko detail mein dekhenge.

#### 6.3 (Sub-topic): `Toggle Element Inspector`

1.  **🎯 Title / Short Summary:** Element Inspector - Screen par 'Inspect Element' (web jaisa) karna.
2.  **🤔 Kya hai? (What?):** Yeh React Native ke "Dev Menu" (Phone shake karke ya `Ctrl+M`/`Cmd+D` daba kar) ka ek option hai. Ise on karne se aap app mein *kahin bhi* tap (touch) karke us component ki `style`, `props`, aur `state` dekh sakte hain.
3.  **💡 Kyu important hai? (Why?):** Yeh "Yeh button screen ke beech mein kyun nahi aa raha?" ya "Is `View` ki `padding` kitni hai?" jaise *layout* aur *styling* problems ko 1 minute mein solve kar deta hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapka UI (design) waisa nahi dikh raha jaisa aapne socha tha.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap `style={{ backgroundColor: 'red' }}` daal-daal kar (andaaze se) layout fix karte rahenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** App ko Debug mode mein (Emulator/Device par) chalao.
      * **Step 2:** Dev Menu kholo (Emulator par `Ctrl+M` ya `Cmd+D`, ya device ko shake karo).
      * **Step 3:** Menu mein se "Toggle Element Inspector" (ya "Show Inspector") par tap karo.
      * **Step 4:** Ab app mein kisi bhi component (Button, Text, View) par tap karo.
      * **Step 5:** Neeche ek window khul jaayegi jo us component ki saari styles (e.g., `padding: 10`, `flex: 1`) aur props dikha degi.
7.  **💻 Code example:** (Code nahi, yeh ek tool hai)
    \*
      * **🚀 Quick run expected output:** App ke upar ek overlay (jaali) aa jaayegi. Tap karne par, component highlight hoga aur neeche uski style (padding, margin, flex) dikhegi.
8.  **🐞 Common beginner mistakes:**
      * Dev Menu kholna na jaanna.
      * Inspector on karke *component* par tap karne ke bajaye *screen* par tap karte rehna.
      * "Network" tab (inspector mein) check na karna (yeh bhi network requests dikhata hai, Flipper jitna achha nahi).
9.  **🌍 Real-world example / use-case:**
      * "Mera `View` `flex: 1` le raha hai ya nahi?" -\> Tap karke check karo.
      * "In do buttons ke beech `margin` kitna hai?" -\> Tap karke check karo.
10. **✅ Quick checklist / TL;DR:**
      * Shake karo (ya `Ctrl+M`).
      * "Toggle Element Inspector" select karo.
      * UI element par tap karo.
      * Style/Props check karo.
11. **❓ FAQs:**
      * **Q: Yeh Chrome DevTools (Inspect Element) jaisa hai?**
          * A: Haan, bilkul wahi concept hai, par mobile app ke liye.
      * **Q: Flipper (next topic) behtar hai ya yeh?**
          * A: `Flipper` 10 guna behtar aur powerful hai. Lekin *jaldi* se style check karne ke liye Inspector achha hai.
12. **🏋️‍♀️ Practice exercise:**
      * Apne Module 4 ke `View` (box model) wale app ko chalao.
      * Inspector kholo aur `rowContainer` par tap karo. Dekho neeche `flexDirection: 'row'` dikh raha hai ya nahi.
13. **📚 Further reading / commands / links:**
      * [React Native Debugging Docs](https://reactnative.dev/docs/debugging)

-----

#### 6.3 (Sub-topic): `Reactotron`

1.  **🎯 Title / Short Summary:** Reactotron - `console.log` ka "baap" (Supercharged logger).
2.  **🤔 Kya hai? (What?):** Yeh ek **desktop app** (library) hai jise aap alag se install karte hain. Yeh aapke `console.log` ko ek sundar UI mein dikhata hai. Lekin iski asli power hai:
      * API calls (Requests/Responses) ko track karna.
      * Redux state (Global) ko live dekhna aur *badalna*.
      * Custom commands (jaise `AsyncStorage` clear karna) banana.
3.  **💡 Kyu important hai? (Why?):** `console.log` aapke Metro terminal (black window) mein hazaaron messages ke beech kho jaata hai. `Reactotron` har cheez (Logs, API, Redux) ko alag-alag, sundar UI mein dikhata hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Production-level apps mein. Jab aap Redux ya complex API calls debug kar rahe hon.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap Redux state (e.g., `user` object) dekhne ke liye har jagah `console.log(user)` lagate phirenge. Reactotron mein yeh live dikhta hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Reactotron Desktop App (PC/Mac par) download aur install karo.
      * **Step 2:** App mein library install karo: `npm install reactotron-react-native` (aur Redux ke liye `reactotron-redux`).
      * **Step 3:** Ek file `ReactotronConfig.js` banao aur use setup (connect) karo.
      * **Step 4:** `App.js` mein `import './ReactotronConfig'` karo.
      * **Step 5:** `console.log` ke bajaye `Reactotron.log('Hello')` use karo.
7.  **💻 Code example:** (`ReactotronConfig.js` - Setup file)
    ```javascript
    import Reactotron from 'reactotron-react-native';
    import AsyncStorage from '@react-native-async-storage/async-storage';
    // (Redux plugin ke liye)
    // import { reactotronRedux } from 'reactotron-redux';

    // Desktop app se connect karo
    Reactotron
      .setAsyncStorageHandler(AsyncStorage) // AsyncStorage ko track karne do
      .configure() // default config
      .useReactNative() // RN plugins
      // .use(reactotronRedux()) // Redux plugin
      .connect(); // Connect!
      
    // console.log ko 'Reactotron.log' se override kar do
    console.tron = Reactotron;

    export default Reactotron; // Export karo
    ```
    **✍️ Line-by-line explanation:**
      * `Reactotron.configure()...connect()`: Reactotron ko setup aur desktop app se connect kar rahe hain.
      * `console.tron = Reactotron;`: Ek shortcut banaya. Ab aap `console.log` ke bajaye `console.tron('Hello')` likh sakte hain, jo *sirf* Reactotron (aur terminal mein nahi) dikhega.
      * **🚀 Quick run expected output:** (Desktop App mein) Aapke app se `console.tron` messages, API calls, aur Redux state changes *live* desktop app mein aate hue dikhenge.
8.  **🐞 Common beginner mistakes:**
      * Desktop app (PC) open na karna (connection fail hoga).
      * `ReactotronConfig.js` ko `App.js` mein import na karna.
      * Phone/PC alag-alag WiFi par hona (dono same network par hone chahiye).
9.  **🌍 Real-world example / use-case:** "User login hua ya nahi?" -\> Reactotron kholo -\> Redux state -\> `user` object -\> check karo (bina code mein `log` lagaye).
10. **✅ Quick checklist / TL;DR:**
      * Yeh ek alag **Desktop App** hai.
      * `console.log` se behtar hai.
      * API calls, Redux state, AsyncStorage ko track karta hai.
      * `console.tron = Reactotron` se shortcut banate hain.
11. **❓ FAQs:**
      * **Q: Flipper vs Reactotron?**
          * A: **Flipper** (Facebook ka naya tool - next topic) ne Reactotron ko *lagbhag replace* kar diya hai. Flipper mein Network, Redux, Layout sab kuch *ek hi jagah* mil jaata hai. Naye projects ke liye **Flipper** seekhna behtar hai.
12. **🏋️‍♀️ Practice exercise:**
      * (Yeh poora setup maangta hai). Reactotron.github.io se desktop app download karo aur setup karne ki koshish karo.
13. **📚 Further reading / commands / links:**
      * [Reactotron Website](https://www.google.com/search?q=https://reactotron.github.io/reactotron/)

-----

#### 6.3 (Sub-topic): Comparison: `Flipper` vs `React Native Debugger`

1.  **🎯 Title / Short Summary:** Flipper (Naya) vs RN Debugger (Purana) - Best debugging tool kaunsa?
2.  **🤔 Kya hai? (What?):**
      * **Flipper:** Facebook (Meta) ka banaya hua *naya*, "platform" (desktop app) hai. Yeh "pluggable" hai. Isme aap Network, Layout, Redux, Logs, Device Logs (native crash) sab ek jagah dekh sakte hain.
      * **React Native Debugger (RND):** Yeh ek purana (par achha) standalone (desktop) app hai jo *sirf 3 cheezein* combine karta tha: Chrome DevTools (JS Debugging), Redux DevTools, aur React DevTools (Component inspector).
3.  **💡 Kyu important hai? (Why?):** Aapko ek "All-in-One" tool chahiye. `Flipper` aaj ka modern solution hai. RN 0.62+ se yeh *default* support ke saath aata hai.

> 💡 **Special Rule Note:** Hum inko ek comparison table mein dekhenge.

**Comparison Table: Flipper vs React Native Debugger**

| Feature | 🚀 Flipper (Modern Standard) | 🔧 React Native Debugger (Legacy) |
| :--- | :--- | :--- |
| **Kya hai?** | Ek "Platform" (Desktop App) jismein plugins (Network, Redux, Logs, Layout) install hote hain. | Ek App jo 3 tools (Chrome Debug, Redux, React) ko ek window mein jodta hai. |
| **⏰ Kab use karein? (When?)** | **Hamesha.** RN 0.62+ projects ke liye. Yeh naya standard hai. | Agar aap bohot purane project (RN \< 0.62) par kaam kar rahe hain. |
| **❌ Agar... (Consequences)** | Agar Flipper use nahi kiya, toh aapko 4 alag tools (RND, Terminal, Inspector) kholne padenge. | Agar RND (aaj) use kiya, toh aap *Native* logs (device crash), *Layout Inspector* (Flipper ka), aur *Network* (sundar UI) miss kar denge. |
| **Best Features** | **Layout Inspector** (UI debug), **Network** (API), **Redux**, **Device Logs** (Native crash). Sab ek jagah. | Redux DevTools (Time travel debugging). JS Debugging (Breakpoints). |
| **Setup** | Naye apps (RN 0.62+) mein *default* chalta hai. (Sirf desktop app install karna hai). | Alag se install karna padta hai aur app se connect karna padta hai. |
| **🐞 Common mistakes?** | Flipper (desktop app) na kholna. Plugins (jaise Redux) install na karna. | "Debug JS Remotely" (Dev Menu) on karna bhool jaana. |
| **🌍 Real-world example?** | Sabhi naye React Native apps. | Puraane projects jo abhi migrate nahi hue hain. |
| **❓ FAQs (related)?** | **Q: Flipper hi best hai?** <br> A: Haan. Yeh Facebook (jo RN banata hai) ka official tool hai. | **Q: RND ab bekaar hai?** <br> A: Bekaar nahi, par *purana* ho gaya hai. Flipper mein zyada features hain. |

-----

**(Baaqi 13-point format ke points)**

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Flipper):**
      * **Step 1:** [flipper.com](https://fbflipper.com/) se Desktop App (Mac/Windows/Linux) download aur install karo.
      * **Step 2:** Apna RN 0.62+ app `run-android` (ya `run-ios`) se chalao.
      * **Step 3:** Flipper desktop app kholo. Aapka app (e.g., "MyFirstApp") *automatic* list mein dikh jaayega.
      * **Step 4:** Us par click karo.
      * **Step 5 (Use):**
          * **Layout:** UI (View, Text) ko inspect karne ke liye (Element Inspector jaisa, par behtar).
          * **Network:** Saari Axios/Fetch API calls (Request/Response) dekhne ke liye.
          * **Redux DevTools:** (Plugin install karke) Redux state dekhne ke liye.
          * **Logs:** `console.log` aur *Native* (Android/iOS) logs dekhne ke liye.
7.  **💻 Code example:** (Yeh tool hai, code nahi)
    \*
      * **🚀 Quick run expected output:** Ek desktop app jismein aapke live app ka poora "X-Ray" (Layout, Network, State) dikhega.
8.  **✅ Quick checklist / TL;DR:**
      * **Flipper** = Modern, All-in-One debugging tool.
      * **RND** = Purana, sirf 3 tools.
      * Naye projects ke liye *sirf Flipper* use karein.
      * Flipper mein Layout, Network, Logs, Redux sab milta hai.
9.  **🏋️‍♀️ Practice exercise:**
      * Flipper (desktop app) [fbflipper.com](https://fbflipper.com/) se install karo.
      * Apna Module 6.1 (Axios) wala app chalao.
      * Flipper mein "Network" tab kholo aur dekho API call (jsonplaceholder) dikh rahi hai ya nahi.
10. **📚 Further reading / commands / links:**
      * [Flipper Official Docs](https://fbflipper.com/docs/getting-started/react-native/)

-----

#### 6.3 (Sub-topic): Comprehensive Debugging Guide & `ADB` commands

1.  **🎯 Title / Short Summary:** Debugging (error fix) kaise karein + `adb` (Android ka Doctor).
2.  **🤔 Kya hai? (What?):**
      * **Debugging Guide:** Error aane par kya-kya steps lene chahiye.
      * **`adb` (Android Debug Bridge):** Ek command-line tool (jo Android SDK ke saath aata hai) jo aapke computer ko aapke Android device/emulator se "baat" karata hai.
3.  **💡 Kyu important hai? (Why?):**
      * **Guide:** Error aane par darr (panic) nahi hona hai. Ek process follow karna hai.
      * **`adb`:** Yeh *native* (Android) level ki problems (jaise "Device offline", "App crash") ko fix karta hai. (Module 1.3 mein `adb reverse` dekha tha).
4.  **⏰ Kab/use karna chahiye? (When?):**
      * **Guide:** Jab bhi app mein Red Screen (Error) aaye.
      * **`adb`:** Jab app build na ho, install na ho, ya emulator connect na ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Bina **Guide:** Error dekh kar, `node_modules` delete karke (jo 90% time zaroori nahi hota) time waste karenge.
      * Bina **`adb`:** Aap native Android issues ko debug nahi kar payenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Debugging Guide):**
      * **Jab Red Screen (Error) aaye toh kya karein?**
      * **Step 1 (Padho):** Error ko *poora* padho. Woh 90% time batata hai ki galti kahan hai (e.g., "undefined is not an object (evaluating 'props.user.name')"). Iska matlab `props.user` `undefined` (null) hai.
      * **Step 2 (Copy):** Error message ko (Stack trace ke saath) *poora copy* karo.
      * **Step 3 (Google/Stack Overflow):** Error ko Google par paste karo. 99% chances hain ki kisi aur ko bhi yeh error aaya hai.
      * **Step 4 (Breakpoint/Log):** Agar error samajh nahi aa raha, toh error wali line se *theek pehle* `console.log(props.user)` (ya `console.tron`) laga kar dekho ki `user` mein kya aa raha hai.
      * **Step 5 (Flipper):** Flipper mein Network (kya API ne data diya?) aur Layout (kya UI render hua?) check karo.
7.  **💻 Code example:** (`adb` ki zaroori commands)
    ```bash
    # 1. Check karo kaunse devices connected hain
    adb devices

    # 2. Native logs (jaise app crash) ko real-time mein dekho
    # (Flipper yeh kaam UI mein kar deta hai, par yeh original tareeka hai)
    adb logcat *:S ReactNative:V ReactNativeJS:V

    # 3. Metro server ko device se connect karo (Agar 'Red Screen' aaye)
    # (Humne Module 1.3 mein dekha tha)
    adb reverse tcp:8081 tcp:8081

    # 4. Device par app ka data/cache clear karo (jab app ajeeb behave kare)
    adb shell pm clear com.myfirstapp 
    # ('com.myfirstapp' aapke package ka naam hai)

    # 5. Device (ya emulator) ko restart karo
    adb reboot
    ```
    **✍️ Line-by-line explanation:**
      * `adb devices`: List dikhata hai (e.g., `emulator-5554 device`). Agar "offline" dikhe, toh emulator restart karo.
      * `adb logcat ...`: Terminal mein Android ke *saare* native logs (Errors, Warnings) dikhata hai. (App crash debug karne ke liye).
      * `adb reverse ...`: Physical device ko Metro server se jodta hai.
      * `adb shell pm clear ...`: App ko "factory reset" kar deta hai (poora `AsyncStorage`, cache clear).
      * **🚀 Quick run expected output:** (Terminal mein output aayega jo aapko device ki stithi batayega).
8.  **🐞 Common beginner mistakes:**
      * Error ko *padhna* nahi, sirf dekhna.
      * `adb` command na chalna (iska matlab Android SDK `platform-tools` aapke `PATH` mein nahi hai - Module 1).
      * Har error ke liye `node_modules` delete karna.
9.  **🌍 Real-world example / use-case:**
      * **Guide:** "Cannot read property 'name' of undefined" -\> `console.log` karke dekha ki 'user' object hi `null` aa raha tha.
      * **`adb`:** App install ho raha hai par khul nahi raha -\> `adb logcat` chala kar dekha -\> "Native module not linked" (crash error) mil gaya.
10. **✅ Quick checklist / TL;DR:**
      * **Guide:** 1. Padho, 2. Copy, 3. Google, 4. `console.log`, 5. Flipper.
      * **`adb`:** Android ka helper tool.
      * `adb devices` (Check connection).
      * `adb reverse` (Connect server).
      * `adb logcat` (Check native crash).
11. **❓ FAQs:**
      * **Q: Breakpoint (JS Debugging) kaise karein?**
          * A: Dev Menu (`Ctrl+M`) kholo -\> "Debug" select karo. Isse Chrome (ya Flipper) mein ek tab khul jaayega. Wahaan `Sources` mein jaakar aap (web jaisa) breakpoint laga sakte hain.
12. **🏋️‍♀️ Practice exercise:**
      * Terminal kholo. `adb devices` chalao (jab emulator chalu ho). Dekho output kya aata hai.
13. **📚 Further reading / commands / links:**
      * [ADB Commands (Full List)](https://developer.android.com/tools/adb)

-----

### 6.4: Publishing (Expo Go se share karna)

*(Note: Yeh topic syllabus mein hai, par hum RN **CLI** path par hain, Expo par nahi. Phir bhi, iska concept jaanna zaroori hai)*

1.  **🎯 Title / Short Summary:** Expo Go - Apna "Debug" app bina cable (OTA) doston/clients ko share karna.
2.  **🤔 Kya hai? (What?):** `Expo Go` ek app hai jo aap (aur aapke client) Play/App Store se download karte hain. Jab aap *Expo CLI* se app banate hain, toh aapko `expo publish` (ya `eas update`) se ek *link* (URL) milta hai. Koi bhi us link ko `Expo Go` app mein khol kar aapka app (debug version) chala sakta hai.
3.  **💡 Kyu important hai? (Why?):** Yeh app (prototype) ko client/QA team ko *jaldi* se dikhane ke liye bohot achha hai. Unhe `.apk` (Android) ya `TestFlight` (iOS) ka lamba setup nahi karna padta.
4.  **⏰ Kab/use karna chahiye? (When?):** **Sirf agar aap "Expo" (Managed Workflow) use kar rahe hain.**
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Agar aap *React Native CLI* (jo hum seekh rahe hain) use kar rahe hain, toh yeh aapke liye **kaam ka nahi hai**. RN CLI users ko app share karne ke liye `.apk` (Release build) hi banana padta hai (Module 13).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Expo Users ke liye):**
    1.  Aap `npx expo start` chalate hain.
    2.  Terminal mein "Publish..." ka option aata hai.
    3.  Click karne par, Expo aapka JS bundle build karke apne server par daal deta hai.
    4.  Aapko ek link milta hai (e.g., `expo.dev/@username/my-app`).
    5.  Aap yeh link client ko bhejte hain. Woh `Expo Go` app mein ise kholte hain aur app chal jaata hai.
7.  **💻 Code example:** (Yeh command hai, code nahi)
    ```bash
    # (Yeh commands 'Expo' project ke liye hain, RN CLI ke liye nahi)

    # Naya update/publish karne ke liye (Modern Expo)
    npx eas update

    # (Purana tareeka)
    npx expo publish
    ```
8.  **🐞 Common beginner mistakes:**
      * **React Native CLI** project ko `expo publish` karne ki koshish karna (Yeh kaam nahi karega).
      * `Expo Go` mein app publish karke sochna ki app Play Store par chala gaya (Nahi, yeh sirf Expo ke server par gaya hai).
9.  **🌍 Real-world example / use-case:** Developer (Expo) ne naya feature banaya -\> `npx eas update` kiya -\> Link (QR code) Slack par QA team ko bheja -\> QA team ne `Expo Go` mein test kar liya.
10. **✅ Quick checklist / TL;DR:**
      * Yeh `Expo` (Managed Workflow) ka feature hai.
      * App (debug build) ko link (URL) ke zariye share karne deta hai.
      * `React Native CLI` (Bare Workflow) users ke liye yeh relevant *nahi* hai.
11. **❓ FAQs:**
      * **Q: Toh RN CLI user (main) client ko app kaise doon?**
          * A: Aapko "Release" `.apk` (Android) ya `.ipa` (iOS) file banani padegi (Module 13) aur unhe (e.g., email/Slack se) bhejna padega (jise "Internal Distribution" kehte hain).
12. **🏋️‍♀️ Practice exercise:**
      * (Yeh humare RN CLI path ke liye applicable nahi hai).
13. **📚 Further reading / commands / links:**
      * [Expo Sharing Apps Docs](https://www.google.com/search?q=https://docs.expo.dev/guides/sharing-apps/)

-----

### 6.5: Best Practices & Conventions (Folders, Naming)

1.  **🎯 Title / Short Summary:** Best Practices - Code ko "saaf" (clean) aur "manageable" (sambhala ja sake) rakhna.
2.  **🤔 Kya hai? (What?):** Yeh "niyam" (rules) hain (jo community ne banaye hain) taaki aapka project (100+ files) ganda (messy) na ho. Isme 2 cheezein main hain:
    1.  **Folder Structure:** Files ko kahan rakhein? (e.g., `src` folder).
    2.  **Naming Conventions:** Files/Components/Variables ka naam kaise rakhein?
3.  **💡 Kyu important hai? (Why?):** 6 mahine baad jab aap apna hi code dekhenge, toh aapko samajh nahi aayega ki `HomeScreen.js` kahan hai aur API call (`api.js`) kahan hai. Saaf structure se code dhoondna aur manage karna 10x aasan ho jaata hai.
4.  **⏰ Kab/use karna chahiye? (When?):** Project shuru (`init`) karne ke *pehle din* se.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap saari 100 files ko root folder mein daal denge (e.g., `App.js`, `HomeScreen.js`, `api.js`, `Button.js` sab ek saath). Yeh ek "khichdi" ban jaayegi.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Common Structure):**
      * **Folder Structure:**
          * Project root (`MyFirstApp/`)
              * `android/` (Native)
              * `ios/` (Native)
              * `node_modules/` (Libraries)
              * `App.js` (Root file, jismein Navigation/Redux setup hota hai)
              * `index.js` (Entry file, ise nahi chherna)
              * **`src/` (Source folder - Aapka 99% code yahan jaayega)**
                  * `assets/` (Images, Fonts)
                      * `images/`
                      * `fonts/`
                  * `components/` (Reusable components - e.g., `Button.js`, `Card.js`, `Header.js`)
                  * `constants/` (Fixed values - e.g., `colors.js`, `apiUrls.js`)
                  * `navigation/` (Navigation files - e.g., `RootNavigator.js`, `TabNavigator.js`)
                  * `screens/` (Har screen ek folder - e.g., `HomeScreen/`, `ProfileScreen/`)
                      * `HomeScreen/`
                          * `index.js` (ya `HomeScreen.js` - Main component)
                          * `styles.js` (Uski styles)
                  * `services/` (ya `api/`) (API calls - e.g., `api.js` (axios instance), `userApi.js`)
                  * `store/` (Redux files)
                      * `index.js` (Store setup)
                      * `userSlice.js` (User state)
                  * `utils/` (Helper functions - e.g., `helpers.js` (date format function))
      * **Naming Conventions:**
          * **Components:** `PascalCase` (e.g., `MyButton.js`, `UserProfile.js`).
          * **Variables/Functions:** `camelCase` (e.g., `const [isVisible, ...]`, `function fetchData() { ... }`).
          * **Folders:** `camelCase` (e.g., `profileScreen/`) ya `kebab-case` (e.g., `profile-screen/`).
7.  **💻 Code example:** (Yeh structure hai, code nahi)
    ```
    MyFirstApp/
    ├── App.js
    └── src/
        ├── assets/
        │   └── images/
        │       └── logo.png
        ├── components/
        │   ├── CustomButton.js
        │   └── Header.js
        ├── navigation/
        │   └── AppNavigator.js
        ├── screens/
        │   ├── HomeScreen/
        │   │   ├── index.js
        │   │   └── styles.js
        │   └── ProfileScreen/
        │       ├── index.js
        │       └── styles.js
        └── services/
            └── api.js
    ```
8.  **🐞 Common beginner mistakes:**
      * Saara code `App.js` mein likh dena.
      * Components (reusable) aur Screens (one-time) ko mix kar dena (e.g., `HomeScreen.js` ko `components/` mein daal dena).
      * `components/` ke andar `Button.js` (common naam) rakhna (`CustomButton.js` behtar hai).
9.  **🌍 Real-world example / use-case:** Har professional React Native project.
10. **✅ Quick checklist / TL;DR:**
      * Saara code `src/` folder mein daalo.
      * `src/` ke andar `components`, `screens`, `navigation`, `services`, `store`, `assets` folders banao.
      * Components: `PascalCase` (e.g., `UserProfile`).
      * Variables: `camelCase` (e.g., `userData`).
11. **❓ FAQs:**
      * **Q: Kya yeh "best" structure hai?**
          * A: Yeh "best" nahi, par "sabse common" (aam) hai. Har team ise thoda badal leti hai.
      * **Q: `index.js` (folder ke andar) kyun use karte hain?**
          * A: Taaki import aasan ho. `import HomeScreen from './screens/HomeScreen/index.js'` ke bajaye `import HomeScreen from './screens/HomeScreen'` likh sakte hain.
12. **🏋️‍♀️ Practice exercise:**
      * Apne project mein `src/` folder banao.
      * `src/components/` folder banao aur usme `CustomButton.js` (Module 4.1 `Pressable` wala code) move karo.
      * `src/screens/` folder banao aur usme `HomeScreen.js` (jo `CustomButton` ko import kare) banao.
13. **📚 Further reading / commands / links:**
      * [React Native Folder Structure (Google search)](https://www.google.com/search?q=react+native+folder+structure+best+practices)

-----

### 6.6: Flexbox (Layout design ki neev)

1.  **🎯 Title / Short Summary:** Flexbox - UI (Layout) ko align (set) karne ka tareeka 📐.
2.  **🤔 Kya hai? (What?):** Yeh ek "layout model" (design ka tareeka) hai. React Native mein (CSS jaisa) `float`, `grid` nahi hota. Layout (cheezon ko kahan rakhna hai) ka 100% kaam **Flexbox** se hi hota hai.
3.  **💡 Kyu important hai? (Why?):** Iske bina aap 2 cheezon ko "side-by-side" (row) nahi rakh sakte, ya kisi cheez ko screen ke "beech" (center) mein nahi laa sakte. Yeh `View` (Module 4.4) ki superpower hai.
4.  **⏰ Kab/use karna chahiye? (When?):** **Hamesha.** Har `StyleSheet` mein layout ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapke saare components (View, Text) ek ke neeche ek (column mein) chipak kar screen ke top-left mein dikhenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Sabse Zaroori):**
      * **`flex: 1`** (Rule \#1):
          * `flex: 1` (Parent `View` par) ka matlab hai: "Poori available screen (ya parent ki jagah) le lo".
          * `SafeAreaView` ko hamesha `flex: 1` dete hain.
      * **`flexDirection`** (Rule \#2):
          * Components (children) ko kaise arrange karna hai?
          * `flexDirection: 'column'` (Default): Ek ke neeche ek (A, B, C).
          * `flexDirection: 'row'`: Side-by-side (A B C).
      * **`justifyContent`** (Rule \#3):
          * `flexDirection` ki *main axis* (disha) par align karta hai.
          * Agar `flexDirection: 'column'` hai, toh yeh *vertical* (upar-neeche) align karega.
          * Agar `flexDirection: 'row'` hai, toh yeh *horizontal* (left-right) align karega.
          * `justifyContent: 'flex-start'` (Default): Shuru mein.
          * `justifyContent: 'center'`: Beech mein.
          * `justifyContent: 'flex-end'`: Aakhir mein.
          * `justifyContent: 'space-between'`: Beech mein barabar space (Pehla/Aakhri chipka hua).
          * `justifyContent: 'space-around'`: Sabke aas-paas barabar space.
      * **`alignItems`** (Rule \#4):
          * `flexDirection` ki *cross axis* (ulti disha) par align karta hai.
          * Agar `flexDirection: 'column'` hai, toh yeh *horizontal* (left-right) align karega.
          * Agar `flexDirection: 'row'` hai, toh yeh *vertical* (upar-neeche) align karega.
          * `alignItems: 'flex-start'`: Shuru mein.
          * `alignItems: 'center'`: Beech mein.
          * `alignItems: 'flex-end'`: Aakhir mein.
      * **Center karne ka mantra:** Screen ke *bilkul beech* mein laane ke liye (Parent `View` ko):
          * `flex: 1`
          * `justifyContent: 'center'`
          * `alignItems: 'center'`
7.  **💻 Code example:**
    ```javascript
    import React from 'react';
    import { StyleSheet, View, Text } from 'react-native';

    const App = () => {
      return (
        // 1. Parent: Poori screen (flex: 1) aur 'column' (default)
        // 'center' (justify) = vertical center
        // 'center' (align) = horizontal center
        <View style={styles.container}> 
          <Text>Screen ke Beech mein!</Text>
          
          {/* 2. Parent: 'row' (side-by-side) */}
          {/* 'space-around' (justify) = horizontal space
          // 'center' (align) = vertical center (row ki height ke) */}
          <View style={styles.row}>
            <View style={[styles.box, {backgroundColor: 'red'}]} />
            <View style={[styles.box, {backgroundColor: 'green'}]} />
            <View style={[styles.box, {backgroundColor: 'blue'}]} />
          </View>
        </View>
      );
    };

    const styles = StyleSheet.create({
      // Screen ke bilkul beech mein laane ka mantra
      container: {
        flex: 1, // Poori screen lo
        justifyContent: 'center', // Vertical align (kyunki direction 'column' hai)
        alignItems: 'center', // Horizontal align (kyunki direction 'column' hai)
        backgroundColor: '#f0f0f0',
      },
      row: {
        flexDirection: 'row', // Main axis 'horizontal' ho gayi
        width: '90%',
        height: 100,
        backgroundColor: '#fff',
        marginTop: 20,
        // Ab 'justifyContent' horizontal kaam karega
        justifyContent: 'space-around', 
        // Ab 'alignItems' vertical kaam karega
        alignItems: 'center', 
      },
      box: {
        width: 50,
        height: 50,
      }
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `styles.container`: `flex: 1`, `justifyContent: 'center'`, `alignItems: 'center'` -\> Iske andar jo `Text` hai, woh *bilkul* center mein aa gaya.
      * `styles.row`: `flexDirection: 'row'` -\> Isne children (boxes) ko side-by-side rakha.
      * `justifyContent: 'space-around'` (row mein): Boxes ko *horizontal* (left-right) phaila diya (space ke saath).
      * `alignItems: 'center'` (row mein): Boxes ko *vertical* (upar-neeche) us `row` (white dabba) ke beech mein rakha.
      * **🚀 Quick run expected output:** Text "Screen ke Beech mein\!" (bilkul center mein) dikhega. Uske neeche ek white dabba (`row`) dikhega, jiske andar Red, Green, Blue box *side-by-side* (beech mein space ke saath) rakhe honge.
8.  **🐞 Common beginner mistakes:**
      * `flex: 1` ka matlab na samajhna (yeh "ratio" hai, "pixel" nahi).
      * `justifyContent` aur `alignItems` `flexDirection` ke hisaab se "badal" jaate hain (row/column), isme confuse hona.
      * `View` ko `flex: 1` na dena aur sochna ki woh poori screen kyun nahi le raha.
9.  **🌍 Real-world example / use-case:** Har app ka layout.
      * Header (Left Icon, Title, Right Icon) = `flexDirection: 'row'`, `justifyContent: 'space-between'`.
      * Card (Image upar, Text neeche) = `flexDirection: 'column'` (default).
10. **✅ Quick checklist / TL;DR:**
      * `flex: 1` = Poori jagah le lo.
      * `flexDirection: 'row'` = Side-by-side.
      * `justifyContent`: Main axis (direction) par align.
      * `alignItems`: Cross axis (ulti) par align.
      * Center Mantra = `flex: 1, justifyContent: 'center', alignItems: 'center'`.
11. **❓ FAQs:**
      * **Q: CSS Flexbox aur RN Flexbox mein kya fark hai?**
          * A: 99% same hain. Sirf 2 fark:
            1.  RN mein default `flexDirection` **`'column'`** hai (Web mein `'row'` hota hai).
            2.  RN mein `flex` (e.g., `flex: 1`) sirf ek number leta hai.
12. **🏋️‍♀️ Practice exercise:**
      * Upar diye `styles.row` mein `justifyContent` ko `'space-between'` karke dekho (Red/Blue box kone mein chipak jaayenge).
      * `styles.row` mein `alignItems` ko `'flex-start'` karke dekho (Boxes row ke top par chale jaayenge).
13. **📚 Further reading / commands / links:**
      * [Flexbox Froggy (Game - Isse seekho\!)](https://flexboxfroggy.com/)
      * [RN Flexbox Docs](https://reactnative.dev/docs/flexbox)

-----

### 6.7: Icons & Fonts

#### 6.7 (Sub-topic): Icons & Fonts (Custom icons aur fonts) + `MaterialIcons` (`react-native-vector-icons`)

1.  **🎯 Title / Short Summary:** `react-native-vector-icons` - App mein "Settings" (gear) ya "Home" (ghar) jaisa icon laana.
2.  **🤔 Kya hai? (What?):** `react-native-vector-icons` ek bohot popular **library** hai jismein hazaaron (thousands) common icons (jaise `MaterialIcons`, `FontAwesome`, `Feather`) pehle se hote hain.
3.  **💡 Kyu important hai? (Why?):** Aap har icon (Home, Profile, Settings) ka `.png` (image) use nahi kar sakte (app size bohot bada ho jaayega). Vector icons "font" jaise hote hain. Aap inka `size` aur `color` (props se) badal sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Jab bhi aapko `Button` ya `Tab Bar` mein icon dikhana ho.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapko har chote icon ke liye alag-alag `Image` file (`.png`) manage karni padegi, jo bohot bura tareeka hai.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install react-native-vector-icons`
      * **Step 2 (Native Setup):** Is library ko *native setup* chahiye (kyunki yeh font files (.ttf) load karti hai).
          * `android/app/build.gradle` mein `apply from: ...` line add karni padti hai.
          * `ios/Info.plist` mein fonts add karne padte hain (`pod install` ke baad).
      * **Step 3:** Icon set import karo: `import Icon from 'react-native-vector-icons/MaterialIcons';`
      * **Step 4:** Component use karo: `<Icon name="settings" size={30} color="#000" />`
      * **Custom Fonts (Text ke liye):** Iska setup bhi same hai.
        1.  Font file (e.g., `Poppins-Regular.ttf`) ko `src/assets/fonts/` mein daalo.
        2.  `react-native.config.js` file banao aur font asset ko link karo.
        3.  `npx react-native-asset` (ya `link`) chalao.
        4.  Ab `style={{ fontFamily: 'Poppins-Regular' }}` use karo.
7.  **💻 Code example:** (Using `react-native-vector-icons`)
    ```javascript
    // 1. Pehle: npm install react-native-vector-icons
    // 2. Phir 'android/app/build.gradle' mein setup (Docs se dekh kar)
    // 3. Phir app ko 'run-android' se REBUILD karo

    import React from 'react';
    import { View, StyleSheet, Text } from 'react-native';
    // 4. Icon set (MaterialIcons) import karo
    import MaterialIcon from 'react-native-vector-icons/MaterialIcons';
    import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome';

    const App = () => {
      return (
        <View style={styles.container}>
          {/* 5. Icon component use karo */}
          <MaterialIcon name="settings" size={40} color="orange" />
          <Text style={styles.text}>Settings</Text>
          
          <FontAwesomeIcon name="user" size={30} color="blue" />
          <Text style={styles.text}>Profile (FontAwesome)</Text>
          
          {/* 6. Custom Font (Agar setup kiya ho) */}
          {/* <Text style={{ fontFamily: 'Poppins-Regular', fontSize: 20 }}>
            Custom Poppins Font
          </Text> */}
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
      text: { fontSize: 16, margin: 5 },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `import MaterialIcon from ...`: `MaterialIcons` set ko import kiya.
      * `<MaterialIcon name="settings" ... />`: Component use kiya.
      * `name="settings"`: Icon ka naam. (Yeh naam kahan se milega? Library ki website se).
      * `size={40}`: Icon ka size (font size jaisa).
      * `color="orange"`: Icon ka rang.
      * `<FontAwesomeIcon ... />`: Doosra icon set (FontAwesome) use kiya.
      * **🚀 Quick run expected output:** Screen par ek "gear" (settings) icon (orange color) aur ek "user" (profile) icon (blue color) dikhega (text ke saath).
8.  **🐞 Common beginner mistakes:**
      * **Step 2 (Native Setup)** `build.gradle` / `Info.plist` ko edit na karna.
      * Library install karke app ko `run-android` se **rebuild** na karna (yeh native change hai).
      * Icon ka `name` galat likhna (e.g., 'setting' ke bajaye 'settings').
      * Custom font (`fontFamily`) ka naam galat likhna.
9.  **🌍 Real-world example / use-case:** Har button, Tab bar, list item mein icons.
10. **✅ Quick checklist / TL;DR:**
      * `npm install react-native-vector-icons`.
      * Native setup zaroori hai (Gradle/Plist).
      * App rebuild zaroori hai.
      * `import Icon from 'react-native-vector-icons/ICON_SET_NAME'`.
      * `<Icon name="..." size={...} color="..." />`.
11. **❓ FAQs:**
      * **Q: Icon ke naam kahan milenge?**
          * A: [react-native-vector-icons GitHub](https://github.com/oblador/react-native-vector-icons) (ya Google "MaterialIcons cheatsheet").
      * **Q: Custom `.svg` icons (company ka logo) kaise use karein?**
          * A: Uske liye `react-native-svg` aur `react-native-svg-transformer` libraries aati hain (Module 1.3 Config Files topic yaad hai?).
12. **🏋️‍♀️ Practice exercise:**
      * Library setup karo (yeh mushkil step hai, docs dhyan se padhna).
      * `MaterialIcon` mein `name="home"` use karke dekho.
      * `Feather` (doosra set) se `name="heart"` icon dikhao.
13. **📚 Further reading / commands / links:**
      * [react-native-vector-icons (Setup Guide)](https://github.com/oblador/react-native-vector-icons)
      * [Custom Fonts (Guide)](https://blog.logrocket.com/adding-custom-fonts-react-native/)

-----

### 6.8: `AsyncStorage` (Phone par data store karna)

1.  **🎯 Title / Short Summary:** `AsyncStorage` - Phone par *chota*, *non-secure* (unsafe) data save karna. (Web ke `localStorage` jaisa).
2.  **🤔 Kya hai? (What?):** Yeh ek **library** (`@react-native-async-storage/async-storage`) hai jo aapko phone par data (key-value pairs) "permanently" (jab tak app install hai) save karne deti hai.
3.  **💡 Kyu important hai? (Why?):** Agar user app band karke vaapas khole, toh `useState` ka saara data *delete* ho jaata hai. Agar aapko kuch yaad rakhna hai (jaise "User ne intro screen dekh li hai" ya "Dark mode on hai"), toh use `AsyncStorage` mein save karna padta hai.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * App ki settings (e.g., `theme: 'dark'`) save karne ke liye.
      * User ne "Intro" screen dekh li hai ya nahi (`hasSeenIntro: true`).
      * API se aaya data (Caching) (jaisa 6.1 mein dekha).
      * **Kab NAHI:** Password, Auth Token, Credit Card. (Yeh "secure" nahi hai).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** User har baar app kholega, toh use app "naya" (fresh) jaisa milega. Uski settings (jaise Dark Mode) save nahi rahengi.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Install karo: `npm install @react-native-async-storage/async-storage`
      * **Step 2:** `run-android` (ya `pod install`).
      * **Step 3:** Yeh `key-value` store hai. Sab kuch *string* mein save hota hai.
      * **Step 4 (Save):** `await AsyncStorage.setItem('key', 'value');`
      * **Step 5 (Read):** `const value = await AsyncStorage.getItem('key');`
      * **Step 6 (Delete):** `await AsyncStorage.removeItem('key');`
      * **Object/Array save karna:** Pehle `JSON.stringify()` (save) aur fir `JSON.parse()` (read) karna padta hai.
7.  **💻 Code example:** (Dark Mode toggle ko save karna)
    ```javascript
    // 1. Pehle: npm install @react-native-async-storage/async-storage
    import React, { useState, useEffect } from 'react';
    import { View, Switch, StyleSheet, Text } from 'react-native';
    import AsyncStorage from '@react-native-async-storage/async-storage'; // 2. Import

    const THEME_KEY = '@app_theme'; // Key (hamesha constant banayein)

    const App = () => {
      const [isDarkMode, setIsDarkMode] = useState(false); // 3. State

      // 4. App khulte hi 'saved' theme load karo (useEffect)
      useEffect(() => {
        const loadTheme = async () => {
          try {
            const savedTheme = await AsyncStorage.getItem(THEME_KEY);
            if (savedTheme !== null) {
              // 'savedTheme' string "true" ya "false" ho sakta hai
              setIsDarkMode(JSON.parse(savedTheme)); // 5. Parse karke state set ki
            }
          } catch (e) { console.error('Failed to load theme.'); }
        };
        loadTheme();
      }, []);

      // 6. Jab bhi switch badle, state aur 'AsyncStorage' dono update karo
      const toggleTheme = async (newValue) => {
        setIsDarkMode(newValue); // State update
        try {
          // 7. 'newValue' (boolean) ko string mein save karo
          await AsyncStorage.setItem(THEME_KEY, JSON.stringify(newValue));
        } catch (e) { console.error('Failed to save theme.'); }
      };

      return (
        // 8. Style ko state ke hisaab se badlo
        <View style={[styles.container, isDarkMode ? styles.dark : styles.light]}>
          <Text style={isDarkMode ? styles.lightText : styles.darkText}>Dark Mode</Text>
          <Switch
            value={isDarkMode}
            onValueChange={toggleTheme} // 6. Hamara function
          />
        </View>
      );
    };

    const styles = StyleSheet.create({
      container: { flex: 1, alignItems: 'center', justifyContent: 'center' },
      light: { backgroundColor: '#fff' },
      dark: { backgroundColor: '#333' },
      lightText: { color: '#fff' },
      darkText: { color: '#333' },
    });

    export default App;
    ```
    **✍️ Line-by-line explanation:**
      * `const THEME_KEY = '@app_theme';`: Ek unique key banayi.
      * `useEffect(() => { ... })`: App load hote hi `loadTheme` call kiya.
      * `const savedTheme = await AsyncStorage.getItem(THEME_KEY);`: Phone se `THEME_KEY` ki value padhi (yeh `null` (agar pehli baar) ya string (e.g., "true") ho sakti hai).
      * `setIsDarkMode(JSON.parse(savedTheme));`: Value ko string (`"true"`) se vaapas boolean (`true`) mein `JSON.parse` karke state mein set kiya.
      * `const toggleTheme = async (newValue) => { ... }`: `Switch` ke `onValueChange` ke liye function.
      * `setIsDarkMode(newValue);`: UI (state) turant update kiya.
      * `await AsyncStorage.setItem(THEME_KEY, JSON.stringify(newValue));`: Nayi value (e.g., `false`) ko string (`"false"`) banakar phone par *save* (setItem) kar diya (agla app load ke liye).
      * **🚀 Quick run expected output:** Ek Dark Mode switch. Agar aap "On" karke app ko *band (poora kill)* karke vaapas kholenge, toh switch "On" hi rahega (kyunki value `AsyncStorage` se load ho gayi).
8.  **🐞 Common beginner mistakes:**
      * `JSON.stringify` (save) aur `JSON.parse` (read) karna bhool jaana (jab object/boolean/number save kar rahe hon).
      * `await` keyword bhool jaana (`setItem`/`getItem` `async` (Promise) hote hain).
      * **Password** ya **Auth Token** isme save kar dena (❌ **Bahut badi security galti\!**).
9.  **🌍 Real-world example / use-case:**
      * "Welcome" (Intro) screen dikha di? `AsyncStorage.setItem('seenIntro', 'true')`. Agli baar check karo, agar 'true' hai toh seedha Home screen dikhao.
      * User ki language preference (`'en'` ya `'hi'`).
10. **✅ Quick checklist / TL;DR:**
      * `npm install @react-native-async-storage/async-storage`.
      * `setItem(key, stringValue)` - Save.
      * `getItem(key)` - Read.
      * Non-string (Object, Boolean) ke liye `JSON.stringify`/`JSON.parse` zaroori hai.
      * **Yeh "SECURE" nahi hai.**
11. **❓ FAQs:**
      * **Q: Yeh "secure" kyun nahi hai?**
          * A: "Rooted" (Android) ya "Jailbroken" (iOS) device par koi bhi aapke app ka `AsyncStorage` data (plain text mein) padh sakta hai.
      * **Q: Toh Password/Token kahan save karein?**
          * A: **`Secure Storage`** (Next topic).
12. **🏋️‍♀️ Practice exercise:**
      * Ek `TextInput` banao. Uska `text` `AsyncStorage` mein save karo. App restart karne par `TextInput` mein purana text dikhna chahiye.
13. **📚 Further reading / commands / links:**
      * [AsyncStorage (GitHub Docs)](https://github.com/react-native-async-storage/async-storage)

-----

### 6.9: JSON Server

1.  **🎯 Title / Short Summary:** `JSON Server` - 5 minute mein *apni* fake (nakli) REST API banana.
2.  **🤔 Kya hai? (What?):** Yeh ek **NPM package** (`npm install -g json-server`) hai jise aap apne *computer* par install karte hain. Aap ek `db.json` file banate hain (data ke saath), aur `json-server --watch db.json` chalate hain. Yeh turant `localhost:3000` par *poori REST API* (GET, POST, PUT, DELETE) chala deta hai.
3.  **💡 Kyu important hai? (Why?):** Jab aap app bana rahe hote hain, tab (ho sakta hai) backend (server) taiyaar na ho. Aap `JSON Server` se *apni* fake API bana kar (e.g., `localhost:3000/users`) app development (Axios calls) poora kar sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):** Development ke shuruaati phase mein. Jab backend taiyaar na ho, ya jab aapko `POST`/`PUT` (data badalne wali) API calls test karni ho (JSONPlaceholder `POST` ko "fake" save karta hai, yeh "real" save karta hai `db.json` mein).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap `JSONPlaceholder` (jo sirf `GET` ke liye achha hai) par atke rahenge ya API banne ka intezaar karte rahenge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1 (Computer par, global):** `npm install -g json-server`
      * **Step 2:** Ek folder mein `db.json` file banao:
        ```json
        {
          "users": [
            { "id": 1, "name": "Rahul" },
            { "id": 2, "name": "Priya" }
          ],
          "posts": [
            { "id": 1, "title": "Hello", "userId": 1 }
          ]
        }
        ```
      * **Step 3 (Computer terminal):** `json-server --watch db.json`
      * **Step 4:** Ho gaya\! Aapke computer par API chalu ho gayi:
          * `http://localhost:3000/users` (GET)
          * `http://localhost:3000/users/1` (GET)
          * `http://localhost:3000/users` (POST)
      * **Step 5 (App se connect karna):** Agar aap *Emulator* use kar rahe hain, toh `localhost` ke bajaye `10.0.2.2` (Android Emulator ka special IP) use karna padta hai:
          * `axios.get('http://10.0.2.2:3000/users')`
      * **Step 6 (Physical Device):** Agar *Physical device* use kar rahe hain, toh aapko apne *computer ka WiFi IP* (e.g., `192.168.1.5`) use karna padega:
          * `axios.get('http://192.168.1.5:3000/users')`
7.  **💻 Code example:** (App mein `fetchData` function, 6.1 jaisa)
    ```javascript
    // (Assume 'db.json' aur 'json-server' computer par chalu hai)

    // Android Emulator se connect karne ke liye
    const API_URL = 'http://10.0.2.2:3000/users'; 
    // (Ya physical device ke liye: 'http://YOUR_WIFI_IP:3000/users')

    const fetchData = async () => {
      try {
        const response = await axios.get(API_URL);
        setData(response.data); // data = [ {id: 1, name: 'Rahul'}, ... ]
      } catch (error) {
        console.error('JSON Server error:', error);
      }
    };
    ```
    **✍️ Line-by-line explanation:**
      * `const API_URL = 'http://10.0.2.2:3000/users'`: URL change kiya. `10.0.2.2` Android Emulator ka "gateway" hai jo computer ke `localhost` ko point karta hai.
      * `await axios.get(API_URL)`: `json-server` se data fetch kiya.
      * **🚀 Quick run expected output:** Aapka app (Axios 6.1 wala) ab `JSONPlaceholder` ke bajaye aapke *apne* computer par chal rahe `json-server` se "Rahul" aur "Priya" ka data fetch karega.
8.  **🐞 Common beginner mistakes:**
      * App (Emulator/Device) mein `localhost:3000` use karna. (Emulator/Device ka `localhost` *khud* device hota hai, computer nahi).
      * `10.0.2.2` (Emulator) ya `WiFi IP` (Physical device) use na karna.
      * `db.json` ka format (JSON) galat bana dena.
9.  **🌍 Real-world example / use-case:** Backend team API bana rahi hai. Frontend team (Aap) `json-server` se `db.json` (jo real API jaisa dikhta hai) bana kar poora app (UI, Redux, Navigation) taiyaar kar leti hai.
10. **✅ Quick checklist / TL;DR:**
      * `npm install -g json-server`.
      * `db.json` file banao.
      * `json-server --watch db.json` chalao.
      * App mein URL `http://10.0.2.2:3000` (Emulator) ya `http://YOUR_WIFI_IP:3000` (Device) use karo.
11. **❓ FAQs:**
      * **Q: Yeh `POST`/`DELETE` bhi karta hai?**
          * A: Haan\! Agar aap `axios.post('.../users', { name: 'Amit' })` bhejenge, toh `json-server` *automatic* `db.json` file mein "Amit" (id: 3) ko **add kar dega**.
      * **Q: iOS Simulator ke liye IP kya hai?**
          * A: iOS Simulator (Mac par) seedha `localhost:3000` use kar sakta hai.
12. **🏋️‍♀️ Practice exercise:**
      * `json-server` setup karo (`db.json` ke saath).
      * Apne Axios (6.1) wale app ka URL `10.0.2.2` par point karke *apna* data fetch karo.
13. **📚 Further reading / commands / links:**
      * [json-server (GitHub Docs)](https://github.com/typicode/json-server)

-----

### 6.10: `Secure Storage` & Comparison: `AsyncStorage` vs `Secure Storage`

1.  **🎯 Title / Short Summary:** `Secure Storage` - *Sensitive* data (Token, Password) ko *encrypt* (lock) karke save karna.
2.  **🤔 Kya hai? (What?):**
      * **`AsyncStorage` (Purana topic):** Plain text, non-secure.
      * **`Secure Storage`:** Yeh ek **library** hai (e.g., `react-native-keychain` ya `react-native-encrypted-storage`) jo data ko save karne se pehle *encrypt* karti hai. Yeh data ko Android ke `Keystore` aur iOS ke `Keychain` (jo OS ke secure hardware hote hain) mein save karti hai.
3.  **💡 Kyu important hai? (Why?):** **Security\!** Agar aapne User ka `Auth Token` `AsyncStorage` mein save kiya, toh "rooted" phone wala hacker use *chura* sakta hai aur aapke user ka account "hack" kar sakta hai. `Secure Storage` se data *encrypted* (locked) rehta hai.

> 💡 **Special Rule Note:** Hum inko ek comparison table mein dekhenge.

**Comparison Table: `AsyncStorage` vs `Secure Storage` (e.g., `react-native-keychain`)**

| Feature | 📁 `AsyncStorage` (Library) | 🔒 `Secure Storage` (Library) |
| :--- | :--- | :--- |
| **Kya save karein?** | **Non-sensitive data.** <br> (Settings, Theme, seenIntro, Cache) | **Sensitive data.** <br> (Auth Token, User Password, API Keys) |
| **Security Kaisi hai?** | **Bekaar (Non-secure).** <br> Data "plain text" (jaisa hai waisa) save hota hai. | **Excellent (Secure).** <br> Data OS-level par "Encrypted" (locked) hota hai. |
| **⏰ Kab use karein? (When?)** | Jab data chori hone se farak na pade (e.g., Dark Mode on hai ya off). | Jab data chori hone se account hack ho sakta ho (e.g., Login Token). |
| **❌ Agar... (Consequences)** | Agar `Token` isme save kiya, toh app *insecure* hai. | Agar `Theme` (setting) isme save ki, toh yeh *overkill* (zaroorat se zyada) hai, kyunki encryption/decryption (lock/unlock) thoda slow hota hai. |
| **Library** | `@react-native-async-storage/async-storage` | `react-native-keychain` (Popular) <br> `react-native-encrypted-storage` (Naya) |
| **🐞 Common mistakes?** | **Auth Token isme save karna.** (Sabse badi galti). | Choti-moti settings isme save karna. |
| **🌍 Real-world example?** | User ki language preference ('hi') save karna. | User ka `JWT Token` (Login token) save karna. |
| **❓ FAQs (related)?** | **Q: Data kahan save hota hai?** <br> A: Phone storage mein (documents folder, plain text file). | **Q: Data kahan save hota hai?** <br> A: iOS `Keychain` / Android `Keystore` (Hardware-backed secure area). |

-----

**(Baaqi 13-point format ke points - `react-native-keychain` ke liye)**

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (`react-native-keychain`):**
      * **Step 1:** Install: `npm install react-native-keychain`
      * **Step 2:** `run-android` (ya `pod install`).
      * **Step 3 (Save Token):** `await Keychain.setGenericPassword(username, password);`
          * (Yeh `username` (sirf ek key) aur `password` (data/token) leta hai).
      * **Step 4 (Read Token):** `const credentials = await Keychain.getGenericPassword();`
          * `credentials.password` mein aapka token milega.
      * **Step 5 (Delete Token):** `await Keychain.resetGenericPassword();`
7.  **💻 Code example:** (Axios Interceptor (6.1) ko `Keychain` ke saath jodna)
    ```javascript
    // (Yeh 6.1 ka 'api.js' example hai, 'AsyncStorage' ke bajaye 'Keychain' ke saath)

    // 1. Pehle: npm install react-native-keychain
    import axios from 'axios';
    import * as Keychain from 'react-native-keychain'; // 2. Import

    const api = axios.create({ baseURL: 'https://api.example.com/v1/' });

    // Request Interceptor
    api.interceptors.request.use(
      async (config) => {
        // 3. 'Keychain' se token (credentials) nikalo
        const credentials = await Keychain.getGenericPassword();
        
        if (credentials) {
          // 4. 'credentials.password' mein token/data hota hai
          config.headers.Authorization = `Bearer ${credentials.password}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    // (Response interceptor (401 logout) bhi zaroori hai)
    // Logout function mein 'await Keychain.resetGenericPassword();' call karo

    export default api;
    ```
    **✍️ Line-by-line explanation:**
      * `import * as Keychain from ...`: `Keychain` library ko import kiya.
      * `const credentials = await Keychain.getGenericPassword();`: Secure storage se credentials (object) padhe.
      * `if (credentials) { ... }`: Check kiya ki credentials hain ya nahi.
      * `config.headers.Authorization = ... credentials.password;`: Token ko `password` field se nikaal kar header mein daal diya.
      * **🚀 Quick run expected output:** (Login hone par) `Keychain.setGenericPassword('token', 'MY_JWT_TOKEN')` call hoga. Uske baad, har `api.get()` call *automatic* `Keychain` se token uthakar header mein laga kar bhejega.
8.  **✅ Quick checklist / TL;DR:**
      * **`AsyncStorage`** = Non-Secure (Settings, Theme).
      * **`Secure Storage`** (`Keychain`) = Secure (Token, Password).
      * Kabhi bhi Token `AsyncStorage` mein mat daalna.
9.  **🏋️‍♀️ Practice exercise:**
      * Apne 6.8 (AsyncStorage) wale code ko dekho. Socho: Kya `THEME_KEY` ko `Secure Storage` mein daalna chahiye? (Jawaab: Nahi, woh sensitive nahi hai).
10. **📚 Further reading / commands / links:**
      * [react-native-keychain (GitHub Docs)](https://github.com/oblador/react-native-keychain)
      * [react-native-encrypted-storage (Naya alternative)](https://github.com/emeraldsanto/react-native-encrypted-storage)

-----

### 6.11: Local Databases (SQLite, WatermelonDB, Realm)

1.  **🎯 Title / Short Summary:** Local Database - App ke andar *bohot saara* (Hazaaron items) data save karna (Offline App).
2.  **🤔 Kya hai? (What?):**
      * **`AsyncStorage`:** Sirf *chota* data (key-value) save karta hai.
      * **Local Database:** Yeh *poora database* (jaise `SQL`) aapke phone mein install kar deta hai. Isse aap *bohot saara, complex* (relationships wala) data save kar sakte hain (e.g., Hazaaron messages, posts).
      * **Options:**
        1.  **SQLite:** (Library: `react-native-sqlite-storage`). Purana, simple SQL database.
        2.  **Realm:** (Library: `realm`). Bohot fast, NoSQL (object-based) database.
        3.  **WatermelonDB (Recommended):** (Library: `watermelon-db`). Naya, *offline-first* apps ke liye bana hai. Yeh React Native ke liye optimized hai aur data (e.g., 10,000 items) ko bohot fast handle karta hai.
3.  **💡 Kyu important hai? (Why?):** Agar aapko WhatsApp (hazaaron messages) ya Notion (hazaaron notes) jaisa app banana hai jo *offline* bhi poora chale, toh aapko `AsyncStorage` (jo slow hai) ke bajaye *real database* chahiye.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab data *bohot bada* ho (1000+ items).
      * Jab data *complex* (related) ho (e.g., `Users` aur `Posts` (User ke bohot saare Posts)).
      * Jab "Offline-first" app banana ho (jo bina internet ke bhi poora chale).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Agar aapne 10,000 items `AsyncStorage` mein save kar diye, toh app bohot *slow* ho jaayega (data padhne/likhne mein).
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (WatermelonDB):**
      * Setup bohot complex hota hai (native setup, babel plugins, schema banana).
      * **Step 1 (Schema):** Aap batate hain ki aapka data kaisa dikhega (e.g., `Post` table mein `title` (string) aur `body` (string) hoga).
      * **Step 2 (Adapter):** Batate hain ki (Android par) `SQLite` use karna hai.
      * **Step 3 (Query):** Data `database.collections.get('posts').query(...)` se nikaalte hain.
      * **Fayda:** `WatermelonDB` "lazy" (observables) hota hai. Yeh `FlatList` (Module 3.1) ke saath milkar 10,000 items ko bhi *instant* render kar sakta hai (kyunki yeh sirf wahi 10 item memory mein laata hai jo screen par dikh rahe hain).
7.  **💻 Code example:** (Yeh *Sirf Concept* hai, setup bohot lamba hai)
    ```javascript
    // (Yeh WatermelonDB ka pseudo-code hai)

    // --- Step 1: Schema (models/Post.js) ---
    // class Post extends Model {
    //   static table = 'posts'
    //   @field('title') title
    //   @field('body') body
    //   @relation('users', 'user_id') user
    // }

    // --- Step 2: Component mein use karna ---
    // import { withObservables } from '@nozbe/watermelondb/react'

    // // Ek 'Post' component
    // const PostItem = ({ post }) => (
    //   <View>
    //     <Text>{post.title}</Text>
    //     <Text>{post.body}</Text>
    //   </View>
    // );

    // // 'database' se 'posts' ko query karna
    // const enhance = withObservables(['post'], ({ post }) => ({
    //   post: post.observe() // 'post' ko observe (live update) karo
    // }));

    // const EnhancedPostItem = enhance(PostItem);

    // --- Step 3: API se data aane par DB mein daalna ---
    // const response = await axios.get('/posts');
    // await database.write(async () => {
    //   response.data.forEach(postData => {
    //     database.collections.get('posts').create(post => {
    //       post.title = postData.title;
    //       post.body = postData.body;
    //     });
    //   });
    // });
    ```
    **✍️ Line-by-line explanation:**
      * Yeh setup (Schema, Adapter, Models) maangta hai.
      * Main concept: Aap API se data *ek baar* laate hain aur *poora* `WatermelonDB` mein daal dete hain.
      * Fir, aapka app *hamesha* `WatermelonDB` (local) se data padhta hai (jo bohot fast hai).
      * App background mein API se DB ko "sync" (update) karta rehta hai.
      * **🚀 Quick run expected output:** Ek app jo *bina internet* ke bhi poora (hazaaron posts ke saath) chalta hai.
8.  **🐞 Common beginner mistakes:**
      * `AsyncStorage` ko database samajhna.
      * Chote data (user settings) ke liye `WatermelonDB` setup karna (overkill).
      * `WatermelonDB` ka complex native setup (Babel, Android) sahi se na kar paana.
9.  **🌍 Real-world example / use-case:**
      * **WhatsApp, Signal, Telegram** (Hazaaron messages ko locally save karte hain).
      * **Notion, Evernote** (Notes ko offline save karte hain).
10. **✅ Quick checklist / TL;DR:**
      * `AsyncStorage` = Chota data (Key-Value).
      * Local DB (`WatermelonDB`, `Realm`) = Bada, Complex data (Tables, Relations).
      * Local DB "Offline-first" apps ke liye zaroori hai.
11. **❓ FAQs:**
      * **Q: Toh main kab kya use karoon?**
          * A: 1. Auth Token? -\> `Secure Storage` (Keychain).
          * 2.  Theme/Setting? -\> `AsyncStorage`.
          * 3.  10,000 posts/messages? -\> `WatermelonDB`.
      * **Q: Realm vs WatermelonDB?**
          * A: `WatermelonDB` React Native (aur `FlatList` performance) ke liye behtar optimized hai. `Realm` bhi bohot fast aur popular hai.
12. **🏋️‍♀️ Practice exercise:**
      * (Yeh bohot advanced hai). Abhi ke liye, sirf `WatermelonDB` ki official docs (website) dekho aur unka "Intro" video dekho.
13. **📚 Further reading / commands / links:**
      * [WatermelonDB (Docs)](https://watermelondb.dev/docs)
      * [Realm (Docs)](https://www.google.com/search?q=https://www.mongodb.com/docs/realm/sdk/react-native/)

-----

### 6.12: `Git` Commands (`revert`, `rebase`, `reset`, `delete branch`)

1.  **🎯 Title / Short Summary:** Git Commands - Code ke "version" (history) ko manage karna (Advanced).
2.  **🤔 Kya hai? (What?):** Git aapke code ka "snapshot" (photo) leta hai (jise `commit` kehte hain). Yeh commands us history ko *badalne* (modify) ya *theek* (fix) karne ke liye hain.
      * **`git revert`:** Ek `commit` (galti) ko *undo* (vaapas) karne ke liye ek *naya* `commit` banata hai. (Safe)
      * **`git reset`:** History ko *delete* kar deta hai (pichhle point par vaapas chala jaata hai). (Dangerous)
      * **`git rebase`:** Apni branch (kaam) ko doosri branch (e.g., `main`) ke "upar" (latest code par) le jaata hai.
      * **`git branch -d`:** Local (computer) branch ko delete karna.
3.  **💡 Kyu important hai? (Why?):** Team mein kaam karte time (`main`, `develop` branches), code ko *clean* (saaf) aur *up-to-date* rakhne ke liye yeh commands zaroori hain.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * `revert`: Jab aapne galti (`commit`) ko `push` (server par) kar diya hai aur use "safely" undo karna hai.
      * `reset`: Jab aapne `commit` kiya par `push` *nahi* kiya aur us galti ko history se *mitana* (delete) chahte hain.
      * `rebase`: Apni branch ko `main` se update karne ke liye (`merge` ke bajaye).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aapki Git history "messy" (gandi) ho jaayegi (bohot saare "merge commit" se), ya aap `push` ki hui galti ko `reset` karke poori team ki history kharab kar denge.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **`git revert HEAD`**: Aapke *aakhri* (HEAD) `commit` ko undo (ulta) karne ke liye ek *naya* `commit` banata hai. (History safe rehti hai).
      * **`git reset --hard HEAD~1`**: Aapke *aakhri* `commit` ko *delete* kar deta hai (aur code ko bhi). (History badal jaati hai). **Rule:** `reset` kabhi bhi `push` kiye hue code par mat chalao.
      * **`git rebase main`**: (Aap `feature` branch par hain) -\> Pehle `main` branch ka code laata hai, fir aapke (`feature`) commits ko uske upar *ek-ek karke* lagata hai. (History "linear" (seedhi) rehti hai).
7.  **💻 Code example:** (Commands)
    ```bash
    # (Aap 'my-feature' branch par hain)

    # 1. Galti commit ki, par 'push' nahi ki. Use mitana hai.
    git reset --hard HEAD~1 
    # (Aapka pichhla commit 'delete' ho gaya)

    # 2. Galti commit ki aur 'push' bhi kar di. (Oops!)
    # Use 'safely' undo karna hai.
    git revert HEAD
    # (Ek naya commit banega jo purane commit ko ulta kar dega)
    git push

    # 3. Apni branch ko 'main' se update karna hai (rebase)
    git fetch origin main # 'main' ka naya code laao
    git rebase origin/main
    # (Ab aapki branch 'main' ke latest code ke upar hai)

    # 4. Kaam khatm, branch merge ho gayi. Ab delete karo.
    git checkout main # Main par jao
    git branch -d my-feature # Local branch delete karo
    git push origin --delete my-feature # Server (remote) se delete karo
    ```
8.  **🐞 Common beginner mistakes:**
      * **`push` kiye hue code par `git reset` chala dena.** (Sabse badi galti, team ki history kharab kar deta hai).
      * `rebase` mein "conflicts" (jhagde) aane par darr jaana.
9.  **🌍 Real-world example / use-case:**
      * `revert`: Feature `push` kiya, par QA ne kaha "bug hai". Turant `git revert` karke galti ko production se hataya.
      * `rebase`: `main` branch mein 10 naye commits aa gaye. Apni `feature` branch ko `git rebase main` karke "update" kiya.
10. **✅ Quick checklist / TL;DR:**
      * `revert`: Naya commit (Undo, Safe).
      * `reset`: Delete commit (Dangerous, Sirf local par).
      * `rebase`: Linear history (Merge se behtar).
11. **❓ FAQs:**
      * **Q: `merge` vs `rebase`?**
          * A: `merge` (e.g., `git merge main`) ek "merge commit" banata hai (history "graph" jaisi). `rebase` history ko "seedha" (linear) rakhta hai. Teams `rebase` prefer karti hain.
12. **🏋️‍♀️ Practice exercise:**
      * Ek nayi branch `test-branch` banao.
      * 2 commit karo ("A", "B").
      * `git reset --hard HEAD~1` chalao (Dekho "B" delete ho gaya).
      * `git revert HEAD` chalao (Dekho "A" undo karne ke liye naya commit "Revert A" ban gaya).
13. **📚 Further reading / commands / links:**
      * [Atlassian Git Tutorials (Rebase, Reset)](https://www.atlassian.com/git/tutorials)

-----

### 6.13: Networking Tools (`dig` command)

1.  **🎯 Title / Short Summary:** `dig` command - Check karna ki server (domain) zinda (live) hai ya nahi.
2.  **🤔 Kya hai? (What?):** `dig` (Domain Information Groper) ek command-line tool (aapke PC/Mac ke terminal mein) hai jo **DNS** (Domain Name System) ko check karta hai. Yeh batata hai ki `api.example.com` *kis* IP address (e.g., `123.45.67.89`) par hai.
3.  **💡 Kyu important hai? (Why?):** Kabhi-kabhi aapki API (Axios) call fail hoti hai. Aapko lagta hai *aapke code* (Axios) mein galti hai. Lekin `dig` se pata chalta hai ki *server* (domain) hi down hai (uska IP hi nahi mil raha).
4.  **⏰ Kab/use karna chahiye? (When?):** Jab API call fail ho aur aapko check karna ho ki "Kya server (domain) live hai?"
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** Aap 1 ghanta apna Axios code debug karte rahenge, jabki galti server (domain) ki thi.
6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
      * **Step 1:** Apna PC/Mac ka terminal kholo.
      * **Step 2:** Type karo: `dig api.google.com` (ya jo bhi aapka API domain hai).
      * **Step 3:** Output dekho. Agar "ANSWER SECTION" mein IP address (e.g., `A ... 172.217.167.74`) mil raha hai, toh server *live* hai.
      * **Step 4:** Agar "status: NXDOMAIN" (Non-Existent Domain) aa raha hai, toh domain (ya aapka internet) down hai.
7.  **💻 Code example:** (Terminal command)
    ```bash
    # 1. Terminal (PC/Mac) mein yeh chalao
    dig api.instagram.com

    # --- Output (Example) ---
    # ; (Header...)
    # ;; QUESTION SECTION:
    # ;api.instagram.com.		IN	A

    # ;; ANSWER SECTION:
    # api.instagram.com.	3600	IN	CNAME	...
    # ...
    # ... 10.158.113.12 (Yeh IP mila, matlab server LIVE hai)

    # --- Error Output ---
    # ;; ->>HEADER<<- ... status: NXDOMAIN, ...
    # (NXDOMAIN = Domain (server) exist nahi karta ya down hai)
    ```
8.  **🐞 Common beginner mistakes:**
      * `dig` ko `npm` se install karne ki koshish karna (Yeh OS (Linux/Mac) ka tool hai).
      * (Windows par `dig` nahi hota, wahaan `nslookup` hota hai: `nslookup api.instagram.com`).
9.  **🌍 Real-world example / use-case:**
      * (Dev): "Mera login (POST) fail ho raha hai\!"
      * (Senior Dev): "Pehle `dig api.mycompany.com` karke dekh, server live hai ya nahi."
10. **✅ Quick checklist / TL;DR:**
      * `dig` = DNS (server IP) checker.
      * `dig api.example.com`
      * Agar "ANSWER SECTION" (IP) mila = Server Live.
      * Agar "NXDOMAIN" = Server Down.
11. **❓ FAQs:**
      * **Q: `ping` vs `dig`?**
          * A: `dig` DNS (IP) check karta hai. `ping` (e.g., `ping 8.8.8.8`) check karta hai ki kya *network* (IP tak ka raasta) chalu hai.
12. **🏋️‍♀️ Practice exercise:**
      * Terminal kholo. `dig google.com` chalao.
      * `dig facebook.com` chalao. Dekho dono ka IP (ANSWER SECTION) mil raha hai.
13. **📚 Further reading / commands / links:**
      * [dig command (Guide)](https://www.geeksforgeeks.org/dig-command-in-linux-with-examples/)

-----

Module 6 complete\! 🥵 Yeh bohot lamba aur technical module tha (API, Debugging, Flexbox, Storage). Inko master karne ka matlab hai aap "Professional" level ke bohot kareeb aa gaye hain.

Jab aap taiyaar hon, toh **"Module 7 ke notes do"** bolna\! 🧑‍💻

=============================================================


# MODULE-7 → Troubleshooting & Practical Fixes (Beginner Problems)


## 7.1: Build & Cache Hell (Part 1): `gradlew clean` vs `gradlew.bat`

1.  **🎯 Title / Short Summary:** `gradlew clean` - Android Build Cache Saaf Karna.

2.  **🤔 Kya hai? (What?):** Yeh ek command hai jo **Android build process** se bani puraani, temporary files (build cache) ko delete karti hai. `gradlew clean` (Mac/Linux) aur `gradlew.bat clean` (Windows) dono ek hi kaam karte hain, bas alag-alag Operating Systems ke liye hain.

3.  **💡 Kyun important hai? (Why?):** Kyunki purana cache naye code changes (khaaskar native code) ko reflect hone se rok sakta hai. Yeh "fresh" build ensure karta hai.

4.  **⏰ Kab/use karna chahiye? (When?):** ⚠️ **(Zaroori)** Ise tab use karein jab:

      * Aapne **native code** (Java/Kotlin/XML) mein koi change kiya ho, par app mein reflect nahi ho raha.
      * Aapne `build.gradle` file mein koi dependency change ki ho.
      * Aapka `npm run android` build **bina kisi clear reason ke fail** ho raha ho.
      * Aapko ajeeb "Resource" related errors aa rahe hon (jaise `Execution failed for task ':app:mergeDebugResources'`).
      * **Yeh kis error ko solve karta hai?:** Yeh `Task '...' failed`, "stale" (baasi) build data, ya resource merging errors ko fix karta hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Aapka native code change (e.g., `AndroidManifest.xml` mein permission add karna) app mein apply nahi hoga, aur aap sochte rahenge ki aapka JS code galat hai.
      * App purani (aur shayad galat) dependencies use karti rahegi.
      * Aap ghanton tak ek aisa bug dhoondhte rahenge jo asal mein hai hi nahi, bas **ziddi cache** ki vajah se hai. 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Yeh command chalaane ke liye, aapko apne project ke `android` folder ke andar jaana hoga.
    2.  Mac/Linux par: `cd android`, fir `./gradlew clean` chalao.
    3.  Windows par: `cd android`, fir `gradlew.bat clean` (ya sirf `gradlew clean`) chalao.
    4.  Yeh `android/app/build` aur `android/build` folders se compiled files ko delete kar dega.
    5.  Iske baad `cd ..` karke root folder mein wapas aao aur `npm run android` chalao.

7.  **💻 Code example (Terminal Command):**

    ```bash
    # Step 1: Android folder mein jao
    cd android

    # Step 2: Clean command chalao (Mac/Linux)
    ./gradlew clean

    # Step 2: Clean command chalao (Windows)
    gradlew.bat clean

    # Step 3: Wapas project root mein aao
    cd ..

    # Step 4: App ko dubara build karo
    npm run android
    ```

      * **✍️ Line-by-line explanation:**
          * `cd android`: Hum terminal ko bol rahe hain ki `android` directory ke andar chalo.
          * `./gradlew clean`: `android` folder ke andar `gradlew` (Gradle Wrapper) script ko execute karo aur use `clean` task do (jo build cache delete karta hai).
          * `cd ..`: Wapas pichle folder (project root) mein aao.
          * `npm run android`: Naya build shuru karo (jo ab fresh hoga).

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * Log `gradlew clean` ko project ke **root folder** mein chalaane ki koshish karte hain. (Yeh hamesha `android` folder ke andar chalti hai).
      * Log har chote-mote JS change (e.g., `App.js` mein text badalna) ke liye ise chalaate hain. (Yeh zaroori nahi hai aur time barbaad karta hai).
      * Windows users ka `gradlew clean` na chalna (unhe `gradlew.bat clean` chalaana hota hai).

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aapne ek naya native module (jaise `react-native-camera`) install kiya. `npm install` ke baad `pod install` kiya (iOS), lekin Android build fail ho raha hai. Is time `cd android && ./gradlew clean` chalaana best hai taaki Android build system fresh start ho aur naye module ko sahi se link kar paaye.

10. **✅ Quick checklist / TL;DR:**

      * Yeh command `android` folder ke andar chalti hai.
      * Ise **Native changes** ke baad ya **build fail** hone par chalao.
      * Yeh JS code changes ke liye *nahi* hai.

11. **❓ FAQs:**

      * **Q: Kya mujhe har `npm run android` se pehle `gradlew clean` karna chahiye?**
      * A: Bilkul nahi. Sirf tab jab build fail ho ya native changes reflect na ho.
      * **Q: `gradlew` aur `gradlew.bat` mein kya fark hai?**
      * A: `gradlew` Mac/Linux ke liye shell script hai, `gradlew.bat` Windows ke liye batch script hai. Kaam ek hi hai.
      * **Q: Yeh `npm start --reset-cache` se alag kaise hai?**
      * A: Woh (Module 7.4) JS cache clean karta hai, yeh (gradlew) Native (Android) cache clean karta hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne project ke `android/app/` folder mein jao. Wahan `build` naam ka ek folder hoga.
    2.  Ab terminal mein `cd android` aur fir `./gradlew clean` chalao.
    3.  Wapas `android/app/` folder mein check karo, `build` folder delete ho gaya hoga. ✅

13. **📚 Further reading / commands / links:**

      * Command: `cd android && ./gradlew clean`

-----

## 7.2: Build & Cache Hell (Part 2): Manual Cache Cleaning (`rm -rf android/build`...)

1.  **🎯 Title / Short Summary:** Manual "Scorched Earth" Cache Clean (Sabkuch mita do).

2.  **🤔 Kya hai? (What?):** Yeh `gradlew clean` se bhi ek step aage jaakar, manually (haath se) Android ke saare build folders (`build`, `.cxx`) ko delete karna hai.

3.  **💡 Kyun important hai? (Why?):** Kabhi-kabhi `gradlew clean` command bhi ziddi cache files ko saaf nahi kar paati. Yeh "scorched earth" (sab mita do) approach hai jo 100% fresh build guarantee karta hai.

4.  **⏰ Kab/use karna chahiye? (When?):** ⚠️ **(Zaroori)**

      * Jab `gradlew clean` chalaane ke **baad bhi** build fail ho raha ho.
      * Jab aapko "C++" related errors (jaise `cmake` ya `ndk` errors) aa rahe hon, jo React Native 0.69+ mein common hain.
      * Jab aapko lage ki Gradle daemon (background process) fass gaya hai aur purana data nahi chhod raha.
      * **Yeh kis error ko solve karta hai?:** `C++ build failed`, `cmake error`, `Task :app:processDebugResources FAILED` (jo `clean` se na ho), ya `Could not find ...` jabki file wahan ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Aap ek "unsolvable" bug mein phase rahenge jo asal mein sirf ek ziddi cache file ki vajah se tha.
      * Aapka build baar-baar C++ (cmake) error par fail hota rahega, kyunki `gradlew clean` `.cxx` (C++ cache) folder ko nahi chhedta.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Project ke root folder mein terminal kholo.
    2.  `android/build` folder ko delete karo (Yeh poore Android project ka main build folder hai).
    3.  `android/app/build` folder ko delete karo (Yeh *sirf* app module ka build folder hai).
    4.  `android/app/.cxx` folder ko delete karo (Yeh C++ NDK ka cache hai, *bahut zaroori* hai).

7.  **💻 Code example (Terminal Commands):**

    ```bash
    # (Mac/Linux)
    # Yeh saare folders ko ek saath delete kar dega
    rm -rf android/build android/app/build android/app/.cxx

    # (Windows)
    # Windows mein aapko yeh folders manually File Explorer se delete karne pad sakte hain
    # Ya 'rd' command use karein:
    rd /s /q "android\build"
    rd /s /q "android\app\build"
    rd /s /q "android\app\.cxx"
    ```

      * **✍️ Line-by-line explanation (Mac/Linux):**
          * `rm -rf`: `rm` (remove) command hai. `-r` (recursive - folder aur uske andar sabkuch) aur `-f` (force - bina pooche delete karo).
          * `android/build`: Pehla target.
          * `android/app/build`: Doosra target.
          * `android/app/.cxx`: Teesra target (C++ cache).

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * Log galti se `rm -rf android/app/src` (source code) ya `rm -rf android/app/build.gradle` (config file) delete kar dete hain. 🛑 **Aisa mat karna\!** Sirf `build` aur `.cxx` folders delete karne hain.
      * `rm -rf` ko root folder (`/`) mein chala dena (yeh aapka system delete kar dega). Hamesha dhyan rakhein ki aap project folder mein hon.

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aapne React Native 0.68 se 0.70 upgrade kiya. Sab kuch instructions ke hisaab se kiya, lekin build C++ (`cmake`) error de raha hai. Yeh isliye kyunki purane build files naye NDK/CMake system se conflict kar rahe hain. Manual `rm -rf android/app/.cxx` chalaana hi iska solution hai.

10. **✅ Quick checklist / TL;DR:**

      * Ise tabhi use karo jab `gradlew clean` fail ho jaaye.
      * `android/build`
      * `android/app/build`
      * `android/app/.cxx`
      * ... in teeno ko delete karna hai.

11. **❓ FAQs:**

      * **Q: `rm -rf` kya hai?**
      * A: "Remove Recursive Force". Yeh Linux/Mac mein files/folders ko permanently delete karne ki command hai.
      * **Q: Kya yeh safe hai?**
      * A: Haan, agar aap sirf `build` aur `.cxx` folders ko target kar rahe hain. Yeh folders agle build par waise bhi dubara ban jaate hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne project ke `android/app/` folder mein jao aur dekho `.cxx` folder hai ya nahi.
    2.  Agar hai, toh use manually delete karke dekho (ya command se).
    3.  `npm run android` chalao. Dekho build thoda zyada time lega, par `.cxx` folder wapas ban jaayega.

13. **📚 Further reading / commands / links:**

      * Ultimate command: `cd android && ./gradlew clean && cd .. && rm -rf android/build android/app/build android/app/.cxx`

-----

## 7.3: Build & Cache Hell (Part 3): `npm cache clean --force`

1.  **🎯 Title / Short Summary:** `npm cache clean --force` - NPM ke Cache ko Saaf Karna.

2.  **🤔 Kya hai? (What?):** Yeh command NPM (Node Package Manager) ke *global* cache ko forcefully clear karti hai. Yeh cache aapke computer par globally (system-wide) saved rehta hai, project ke andar nahi.

3.  **💡 Kyun important hai? (Why?):** Kabhi-kabhi NPM corrupted (kharab) ya purani package files download kar leta hai aur apne global cache mein save kar leta hai. Agli baar `npm install` karne par woh firse wahi kharab file utha leta hai.

4.  **⏰ Kab/use karna chahiye? (When?):** ⚠️ **(Zaroori)**

      * Jab `npm install` baar-baar fail ho raha ho, khaaskar `integrity check` errors par.
      * Jab aap sure hain ki package ka naya version release ho gaya hai, par `npm install` purana hi utha raha hai.
      * Jab aapko ajeeb "package not found" ya "dependency tree" errors aa rahe hon jo `rm -rf node_modules` karke bhi solve na hon.
      * **Yeh kis error ko solve karta hai?:** `npm ERR! code EINTEGRITY`, `npm ERR! checksum failed`, ya `npm install` ka fass jaana.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Aapka project ek **corrupted package** use karta rahega, jisse aage chalkar runtime errors aa sakte hain.
      * Aapka `npm install` kabhi poora nahi hoga, aur aap project setup hi nahi kar paayenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Terminal kholo (project folder mein hona zaroori nahi, yeh global hai).
    2.  `npm cache clean --force` chalao.
    3.  (Naye NPM versions mein `npm cache verify` use karne ko bolte hain, jo cache ko check aur fix karta hai, lekin `clean --force` abhi bhi ziddi cache ke liye hai).
    4.  Iske baad, apne project folder mein jao, `rm -rf node_modules` karo aur fir se `npm install` chalao.

7.  **💻 Code example (Terminal Command):**

    ```bash
    # Step 1: NPM ka global cache saaf karo
    npm cache clean --force

    # (Optional but Recommended) Step 2: Cache ko verify karo
    npm cache verify

    # Step 3: Ab apne project mein jao
    cd /path/to/your/project

    # Step 4: Purane packages hatao
    rm -rf node_modules

    # Step 5: Fresh install karo
    npm install
    ```

      * **✍️ Line-by-line explanation:**
          * `npm cache clean --force`: NPM ko bolta hai ki "tumhare paas jo bhi global cache hai, use bina pooche delete kar do".
          * `npm cache verify`: NPM se kehta hai ki check karo cache ki haalat aab thik hai ya nahi.
          * `rm -rf node_modules`: Project ke local packages delete karta hai.
          * `npm install`: NPM ko bolta hai ki ab network se *fresh* packages download karke lao (kyunki global cache saaf ho chuka hai).

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * Log sochte hain yeh `node_modules` ko delete karta hai. (Nahi\! Yeh global cache ko karta hai).
      * Log sochte hain yeh React Native (Metro/Gradle) ka cache clean karta hai. (Nahi, yeh sirf NPM ka cache hai).
      * Ise har `npm install` se pehle chalaana. (Zaroori nahi, sirf problem hone par).

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aapki team ne ek private NPM package (jo company ka internal hai) update kiya. Aap `npm install` kar rahe hain, par aapke system mein purana code aa raha hai kyunki aapke global NPM cache ne naya version fetch nahi kiya. `npm cache clean --force` karke `npm i` karne se 100% naya code aayega.

10. **✅ Quick checklist / TL;DR:**

      * Yeh `npm install` ke errors fix karta hai.
      * Yeh `node_modules` delete nahi karta, yeh **Global NPM Cache** delete karta hai.
      * `EINTEGRITY` error ka yeh pakka ilaaj hai.

11. **❓ FAQs:**

      * **Q: Kya yeh safe hai?**
      * A: Haan, 100% safe hai. Isse bura-se-bura yeh hoga ki aapka agla `npm install` thoda zyada time lega (kyunki sabkuch network se download hoga).
      * **Q: `yarn` users kya karein?**
      * A: Woh `yarn cache clean` chala sakte hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Terminal mein `npm cache verify` chalao. Yeh aapko aapke cache ka location aur size batayega.
    2.  (Optional) `npm cache clean --force` chala kar dekho.

13. **📚 Further reading / commands / links:**

      * Command: `npm cache clean --force`
      * Alternative: `npm cache verify`

-----

## 7.4: Comparison: Manual Cache vs. `npx react-native start --reset-cache`

1.  **🎯 Title / Short Summary:** Cache Wars: Native Cache (Manual) vs JS Cache (`--reset-cache`)
    *(Note: Special format "Comparison Topic" Rule 2 ke anusaar)*

2.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    React Native mein 2 alag-alag duniya hain, aur dono ka apna cache hai:

    1.  **Native Cache (Android/iOS):** Yeh aapka compiled Java/Kotlin/Swift code hai. Yeh `android/build` ya `ios/build` folders mein rehta hai. Jab `npm run android` fail hota hai, tab is cache ko saaf karte hain.
    2.  **Metro Bundler Cache (JavaScript):** Yeh aapka `App.js`, components, etc. (saara JS code) hai. Metro (React Native ka bundler) is JS code ko package karte waqt ek cache banata hai taaki 'Fast Refresh' tezi se ho sake. `npm start --reset-cache` *is* cache ko clear karta hai.

    **Farak saaf hai:** Native error? `gradlew clean`. JS error? `--reset-cache`.

3.  **💻 Code example (Commands):**

    ```bash
    # 1. Native Cache saaf karne ke liye (Manual/Gradle)
    cd android && ./gradlew clean

    # 2. JavaScript (Metro) Cache saaf karne ke liye
    # (npm start ke saath)
    npm start -- --reset-cache

    # (npx ke saath)
    npx react-native start --reset-cache
    ```

      * **✍️ Line-by-line explanation:**
          * `./gradlew clean`: Android ke native build folders ko delete karta hai.
          * `npm start -- --reset-cache`: `npm start` (jo Metro server chalata hai) ko bolta hai ki "shuru hone se pehle apna purana JS cache delete kar dena". (Do `--` zaroori hain taaki `npm` command ko aage paas kar sake).

-----

### 📊 Comparison Table: Native vs JS Cache

| Feature | Manual Cache (e.g., `gradlew clean`, `rm -rf`) | `npm start --reset-cache` |
| :--- | :--- | :--- |
| **🤔 Kya hai? (What?)** | Yeh **Native Build Cache** ko delete karta hai (Android/iOS compiled code). | Yeh **Metro Bundler (JavaScript) Cache** ko delete karta hai. |
| **💡 Kyun important hai? (Why?)** | Native code (Java, Swift, XML) changes ko reflect karwane ke liye. | JavaScript/TypeScript code changes ko reflect karwane ke liye. |
| **⏰ Kab/Kyun use karein? (When?)** | 1. Jab `npm run android` fail ho. <br> 2. Native module add/remove kiya ho. <br> 3. `AndroidManifest.xml` change kiya ho. | 1. Jab JS/TS code change reflect na ho. <br> 2. "Fast Refresh" fass jaaye. <br> 3. `require()` errors aayein jo nahi aane chahiye. |
| **❌ Agar use nahi kiya toh? (If not used)** | Aapka app purane native code par chalta rahega. Build fail hota rahega. | Aapka app purana JS code dikhayega. Aapko "stale" (baasi) code dikhega. |
| **🐞 Common mistakes** | Log ise JS changes (e.g., `App.js` mein text change) ke liye chalaate hain. (Yeh zaroori nahi). | Log sochte hain yeh native build errors (`gradlew` wale) solve kar dega. (Bilkul nahi karega). |
| **🌍 Real-world example** | Aapne `react-native-permissions` install kiya. App rebuild karni padegi. `gradlew clean` best hai. | Aapne ek image file ka naam badla (e.g., `logo.png` se `my_logo.png`) par app abhi bhi `logo.png` dhoondh raha hai. `--reset-cache` zaroori hai. |
| **❓ FAQs** | **Kya yeh JS code affect karta hai?** (Nahi) | **Kya yeh native code affect karta hai?** (Nahi) |

-----

*(Regular 13-point format resumes)*

10. **✅ Quick checklist / TL;DR:**
      * Native code issue? `gradlew clean`.
      * JS code reflect na ho? `npm start -- --reset-cache`.
      * Dono alag-alag cheezein hain.
11. **🏋️‍♀️ Practice exercise:**
    1.  App chalao. `App.js` mein text badlo (Metro update karega).
    2.  Ab `npm start -- --reset-cache` chalao aur dekho bundler ko start hone mein thoda zyada time lagega (kyunki woh cache bana raha hai).
12. **📚 Further reading / commands / links:**
      * The Ultimate Cache Clean (JS + Native): `cd android && ./gradlew clean && cd .. && rm -rf node_modules && npm cache clean --force && npm install && npm start -- --reset-cache` (Yeh Nuclear option hai, jab kuch kaam na kare 😅).

-----

## 7.5: The `package-lock.json` Problem (Kab delete karna chahiye?)

1.  **🎯 Title / Short Summary:** `package-lock.json` - Kab Delete Karna Chahiye (Aur Kab Bilkul Nahi).

2.  **🤔 Kya hai? (What?):** Yeh file aapke `node_modules` folder ka ek "blueprint" ya "snapshot" hai. Yeh record rakhti hai ki *exactly* kaun sa version (aur uski dependencies) install hua hai.

3.  **💡 Kyun important hai? (Why?):** Yeh **consistency** (ek jaisa) ensure karta hai. Is file ki vajah se hi aapki team mein sabke paas *same* `node_modules` folder hota hai, jisse "mere machine par toh chalta hai" waali problem nahi hoti.

4.  **⏰ Kab delete karein? (When?):** ⚠️ **(Zaroori)**

      * **Normally, KABHI NAHI.** Ise delete *nahi* karna chahiye.
      * **Exception (Last Resort):** Sirf tab delete karein jab `npm install` ajeeb "dependency conflict" errors de raha ho jo `rm -rf node_modules && npm i` se solve na ho rahe hon.
      * Jab aapne `package.json` mein bahut saari dependencies *manually* change ki hon aur `npm install` unhe handle na kar paa raha ho.
      * **Yeh kis error ko solve karta hai?:** Complex `npm ERR! ERESOLVE` (dependency tree conflicts) jo `npm install --force` se bhi na ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Yeh ulta hai: **Ise delete *nahi* karna chahiye normally.** Agar aapne ise bina wajah delete kar diya, toh:
      * Aapki app mein "works on my machine" problem aa jaayegi.
      * Aapke co-worker ki app mein alag packages (minor versions) install ho sakte hain aur aapki app mein alag.
      * Production build mein aisi dependencies jaa sakti hain jo test nahi hui hain, kyunki `npm install` har baar alag-alag sub-dependencies utha sakta hai.

6.  **🧑‍🏫 Step-by-step (The *Right* Way to fix conflicts):**

    1.  **Step 1 (Preferred):** `rm -rf node_modules` (Sirf packages delete karo).
    2.  **Step 2:** `npm install` (Lockfile se install karo).
    3.  **Step 3 (If Step 2 fails):** `npm install --force` (Koshish karo).
    4.  **Step 4 (Last Resort):** `rm package-lock.json` (Lockfile delete karo).
    5.  **Step 5:** `rm -rf node_modules` (Dubara delete karo).
    6.  **Step 6:** `npm install` (Yeh ab nayi `package-lock.json` bana dega).

7.  **💻 Code example (Terminal Command):**

    ```bash
    # 🛑 GALAT TAREKA (Jo beginners karte hain)
    # rm package-lock.json
    # npm install

    # ✅ SAHI TAREKA (Jab problem ho)
    # 1. Pehle simple try
    rm -rf node_modules
    npm install

    # 2. Agar fail ho, tabhi 'Lockfile' ko haath lagao
    rm -rf node_modules
    rm package-lock.json
    npm install
    ```

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * Beginners ise har `npm install` se pehle delete kar dete hain. 🛑 **Maha-paap\!** Aisa mat karna. Yeh file aapki dost hai, dushman nahi.
      * Log ise `.gitignore` mein daal dete hain. (Nahi\! Ise **hamesha Git mein commit karna** hota hai taaki poori team sync mein rahe).

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aap ek purane project par aaye. `npm install` kiya aur 50 dependency conflict errors (`ERESOLVE`) aa gaye. Aapne `node_modules` delete kiye, fir bhi errors. Is point par `package-lock.json` delete karke fresh `npm install` karna shayad zaroori ho, taaki NPM naya dependency tree bana sake.

10. **✅ Quick checklist / TL;DR:**

      * `package-lock.json` ko hamesha Git mein **commit** karo.
      * Ise normally **delete mat karo**.
      * Sirf "dependency hell" mein hi ise (aur `node_modules` ko) delete karke fresh `npm install` karo.

11. **❓ FAQs:**

      * **Q: `package.json` vs `package-lock.json`?**
      * A: `package.json` batata hai *kya-kya* chahiye (e.g., "react: 18.x"). `package-lock.json` batata hai *exactly kya* install hua (e.g., "react: 18.2.0").
      * **Q: `yarn` users kya karein?**
      * A: Unke paas `yarn.lock` file hoti hai. Same rules apply.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne `package-lock.json` file ko VS Code mein khol kar dekho.
    2.  Samajhne ki koshish karo ki yeh dependency tree ko (e.g., 'react' kin cheezon par depend karta hai) kaise map karta hai.

13. **📚 Further reading / commands / links:**

      * [NPM Docs: package-lock.json](https://docs.npmjs.com/cli/v7/configuring-npm/package-lock-json)

-----

## 7.6: Common Build Errors Explained

1.  **🎯 Title / Short Summary:** Common Build Errors (Aur Unka Asli Matlab).

2.  **🤔 Kya hai? (What?):** `npm run android` chalaate waqt aane wale kuch sabse common errors ka breakdown aur unka solution.

3.  **💡 Kyun important hai? (Why?):** Error message ko samajhna bug fix karne ka pehla step hai. Agar aap error padhna seekh gaye, toh aap 90% problem khud solve kar sakte hain.

4.  **⏰ Kab/use karna chahiye? (When?):** ⚠️ **(Zaroori)**

      * Jab aapka build fail ho aur aap terminal mein **laal text (red text)** dekhein. Hamesha error log mein *upar* scroll karke pehla `error:` ya `What went wrong:` dhoondho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Aap error message ko padhe bina, seedha poora log copy-paste karke Stack Overflow par daal denge aur galat solution follow karte rahenge.
      * Aap ghabra jaayenge aur sochange ki React Native bahut mushkil hai.

6.  **🧑‍🏫 Step-by-step explanation (Error Breakdown):**

    -----

    ### Error 1: `SDK location not found` (Ya `ANDROID_HOME` not set)

      * **🧠 Matlab:** React Native ko nahi pata ki aapka Android SDK (Android Studio ke tools) kahan rakha hai.
      * **🛠️ Fix:**
        1.  Apne system mein `ANDROID_HOME` environment variable set karo.
        2.  *Ya* (aasan tareeka) apne project ke `android` folder mein `local.properties` naam ki file banao.
        3.  Us file mein yeh likho (apna path daalna):
            ```properties
            # (Windows example)
            sdk.dir=C:\\Users\\YourName\\AppData\\Local\\Android\\sdk
            # (Mac example)
            sdk.dir=/Users/YourName/Library/Android/sdk
            ```

    -----

    ### Error 2: `Execution failed for task ':app:mergeDebugResources'`

      * **🧠 Matlab:** Android aapke resources (images, fonts, XMLs) ko merge (ek saath) nahi kar paa raha.
      * **🛠️ Fix:**
        1.  Yeh 99% aapki **image files ke naam** ki vajah se hota hai.
        2.  Android mein image names *sirf* lowercase (a-z), numbers (0-9), aur underscore (`_`) ho sakte hain.
        3.  Agar aapne `my-image.png` (dash use kiya) ya `MyImage.png` (capital letter) use kiya hai, toh build fail hoga.
        4.  **Solution:** Saari images ko `my_image.png` format mein rename karo.
        5.  Fir `cd android && ./gradlew clean` chalao.

    -----

    ### Error 3: `C++ build failed` / `cmake error` / `NDK not configured`

      * **🧠 Matlab:** Naye React Native (0.69+) mein C++ code (NDK) compile hota hai aur woh fail ho gaya.
      * **🛠️ Fix:**
        1.  **Android Studio** kholo -\> **SDK Manager** mein jao.
        2.  **SDK Tools** tab mein jao.
        3.  Check karo ki `NDK (Side by side)` aur `CMake` **installed** (checked) hain ya nahi. Nahi hain toh install karo.
        4.  Uske baad, Topic 7.2 (Manual Cache Clean) follow karo (`rm -rf android/app/.cxx`).

    -----

    ### Error 4: `Task :app:installDebug FAILED`

      * **🧠 Matlab:** App build ho gayi (APK ban gaya), par device/emulator par install nahi ho rahi.
      * **🛠️ Fix:**
        1.  Check karo ki device aachi tarah connected hai (`adb devices` chala kar dekho, device "authorized" dikhni chahiye).
        2.  Device/Emulator se purani app ko **manually uninstall** karo.
        3.  Fir se `npm run android` chalao.

7.  **💻 Code example:** (N/A - Yeh errors hain).

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * Log poora error log nahi padhte. Hamesha *upar* scroll karke pehla `error:` dhoondho.
      * Error message ka sirf aakhri part padhna (jo aksar "Build failed" hota hai). Asli error oopar chupa hota hai.

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aapne ek `image-1.png` file add ki. Build `mergeDebugResources` par fail ho gaya. Error padhne par pata chalega ki resource names mein dash (`-`) allowed nahi hai. Usko `image_1.png` rename karne se build fix ho jaayega.

10. **✅ Quick checklist / TL;DR:**

      * Hamesha error poora padho, oopar se neeche tak.
      * `SDK location` = `local.properties` file fix karo.
      * `mergeResources` = Image/file names (`my_image.png`) check karo.
      * `cmake` / `C++` = NDK/CMake install karo (Android Studio se) aur `.cxx` folder delete karo.

11. **❓ FAQs:**

      * **Q: Itne saare errors kyun aate hain?**
      * A: Kyunki React Native 2 system (JS aur Native) ko jodta hai. Build process complex hai, isliye errors aate hain.
      * **Q: Error samajh na aaye toh kya karein?**
      * A: Error ki *main line* (e.g., `mergeDebugResources`) ko copy karke Google ya Stack Overflow par search karo.

12. **🏋️‍♀️ Practice exercise:**

    1.  Jaan-boojh kar apne `assets` folder mein ek image ko `my-image.png` (dash ke saath) naam do.
    2.  `npm run android` chalao. Dekho build `mergeDebugResources` par fail ho jaayega.
    3.  Use `my_image.png` rename karo aur `gradlew clean` chalao. Ab build pass ho jaayega.

13. **📚 Further reading / commands / links:**

      * Commands: `adb devices`, `cd android && ./gradlew clean`

-----

## 7.7: Navigation Deep Dive: `initialRouteName="Login"`

1.  **🎯 Title / Short Summary:** React Navigation: `initialRouteName` (App kahan se shuru hogi).

2.  **🤔 Kya hai? (What?):** Yeh React Navigation (Stack Navigator) mein ek 'prop' hai jo batata hai ki jab navigator load ho, toh *sabse pehli* screen kaun si dikhani hai.

3.  **💡 Kyun important hai? (Why?):** Iske bina, Stack Navigator ko kaise pata chalega ki user ko `Login` screen dikhani hai ya `Home` screen? Yeh app ka entry point set karta hai.

4.  **⏰ Kab/use karna chahiye? (When?):** ⚠️ **(Zaroori)**

      * **Hamesha** jab bhi aap `createStackNavigator`, `createBottomTabNavigator`, ya `createDrawerNavigator` ka istemaal karein.
      * Aapko hamesha *explicitly* (saaf-saaf) batana chahiye ki default screen kaun si hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * React Navigation default mein uss screen ko utha lega jo aapne `Stack.Navigator` ke andar **sabse upar (pehli)** define ki hai.
      * **Problem:** Maan lo aapne 'Home' ko upar define kiya hai aur 'Login' ko neeche. Agar `initialRouteName="Login"` set nahi kiya, toh app seedha 'Home' par chali jaayegi (bina login ke\!). 😱
      * Isse aapka "authentication flow" (login logic) poora toot jaayega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Aap `Stack.Navigator` component banate hain.
    2.  Uske andar `Stack.Screen` components define karte hain (e.g., "Login", "Home", "Profile").
    3.  `Stack.Navigator` component ko ek prop paas karte hain: `initialRouteName`.
    4.  Is prop ki value *exactly* wahi string honi chahiye jo aapne kisi ek `Stack.Screen` ke `name` prop mein di hai.

7.  **💻 Code example:**

    ```javascript
    // App.js (using React Navigation)
    import { NavigationContainer } from '@react-navigation/native';
    import { createNativeStackNavigator } from '@react-navigation/native-stack';

    // Screens
    function LoginScreen() { /* ... */ }
    function HomeScreen() { /* ... */ }
    function ProfileScreen() { /* ... */ }

    const Stack = createNativeStackNavigator();

    function App() {
      const isUserLoggedIn = false; // Example logic

      return (
        <NavigationContainer>
          <Stack.Navigator 
            // 🎯 YEH HAI IMPORTANT
            // Logic ke basis par initial route set karna
            initialRouteName={isUserLoggedIn ? "Home" : "Login"} 
          >
            {/* Screens ko kisi bhi order mein define kar sakte hain */}
            <Stack.Screen name="Profile" component={ProfileScreen} />
            <Stack.Screen name="Login" component={LoginScreen} />
            <Stack.Screen name="Home" component={HomeScreen} />

          </Stack.Navigator>
        </NavigationContainer>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const Stack = createNativeStackNavigator();`: Hum ek stack navigator bana rahe hain.
          * `initialRouteName={isUserLoggedIn ? "Home" : "Login"}`: Hum navigator ko bata rahe hain. Agar user logged-in hai, toh "Home" screen se shuru karo, varna "Login" screen se shuru karo.
          * `name="Profile"`, `name="Login"`, `name="Home"`: Humne 3 screens define ki. Dekho, order (Profile pehle hai) se fark nahi padta, kyunki `initialRouteName` ne saaf bata diya hai ki kahan se shuru karna hai.

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * `initialRouteName` ki value (`"Login"`) aur `Stack.Screen` ke `name` (`"login"`) mein typo kar dena (yeh **Case-Sensitive** hai). Agar 'L' capital hai toh capital hi hona chahiye.
      * Yeh prop `Stack.Screen` par laga dena (Yeh `Stack.Navigator` par lagta hai).
      * Ise dena hi bhool jaana.

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Upar diya gaya example hi best real-world example hai. Aap `AsyncStorage` se check karte hain ki user ka token saved hai ya nahi (`isUserLoggedIn`). Uske basis par aap `initialRouteName` ko dynamic tareeke se "Home" ya "Login" set karte hain.

10. **✅ Quick checklist / TL;DR:**

      * Hamesha `Stack.Navigator` (ya Tab/Drawer) par `initialRouteName` set karo.
      * Value `name` prop se *exactly* match honi chahiye (case-sensitive).
      * Order se fark nahi padta agar yeh set kiya hai.

11. **❓ FAQs:**

      * **Q: Agar na doon toh kya hoga?**
      * A: List mein jo *pehli* `Stack.Screen` define ki hai, woh initial route ban jaayegi, jo shayad aap nahi chahte.
      * **Q: Kya isko change kar sakte hain?**
      * A: Haan, jaisa example mein dikhaya, aap ise state ya variable ke basis par dynamic set kar sakte hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein se `initialRouteName` prop ko poora hata kar chalao. Dekho app "Profile" screen se shuru hogi (kyunki woh list mein pehli hai).
    2.  Ab `initialRouteName="Home"` set karke chalao. Dekho app "Home" se shuru hogi.

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: Stack Navigator](https://reactnavigation.org/docs/stack-navigator)

-----

## 7.8: Native Changes: `When to Rebuild` (Kab App ko Rebuild Karna Zaroori hai?)

1.  **🎯 Title / Short Summary:** Native vs JS Change: Kab `npm run android` Dobaara Chalaana Hai.

2.  **🤔 Kya hai? (What?):** Yeh concept samjhata hai ki kab 'Fast Refresh' (jo fast hai) kaam karega aur kab poori app ko `npm run android` se rebuild (jo slow hai) karna padega.

3.  **💡 Kyun important hai? (Why?):** Aapka **development time** bachaane ke liye. Agar aap har chote JS change (like changing text) ke liye rebuild karenge, toh aapka development time 10x badh jaayega. Aur agar aap native change ke baad rebuild *nahi* karenge, toh app crash hoti rahegi.

4.  **⏰ Kab Rebuild karein? (When?):** ⚠️ **(Zaroori)**

      * **Jab bhi aap `npm install` ya `npm uninstall` karein:** Khaaskar agar us package mein native code ho (e.g., `react-native-camera`, `react-native-vector-icons`, `react-native-gesture-handler`).
      * **Jab bhi aap `android` ya `ios` folder ke andar *kisi bhi* file ko manually change karein:**
          * `AndroidManifest.xml` (e.g., permission add karna).
          * `build.gradle` (e.g., dependency version change karna).
          * `Info.plist` (iOS).
          * Koi bhi Java/Kotlin/Swift file add/edit/delete karna.
      * **Jab aap app icon ya splash screen change karein.**
      * **Yeh kis error ko solve karta hai?:** `Native module "..." cannot be null`, `... is not a function` (jab aapko pata hai ki function hai), `RNCamera is not available`, ya app ka Metro server se connect hote hi turant crash ho jaana.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):** ⚠️ **(Zaroori)**

      * Aap `npm install react-native-camera` karenge.
      * Aap `App.js` mein `<Camera>` component use karenge.
      * App crash ho jaayegi: `Error: Native module 'RNCamera' not found` (ya `cannot be null`).
      * Aap 1 ghanta yeh soch kar barbaad kar denge ki aapka JS code galat hai, jabki galti yeh thi ki native code ko *link* karne ke liye app ko rebuild (compile) hi nahi kiya gaya.

6.  **🧑‍🏫 Step-by-step explanation (Kab kya karein):**

    | Aapne kya change kiya? | Action | Kyun? |
    | :--- | :--- | :--- |
    | `App.js` mein Text/Style change kiya. | **Kuch mat karo.** | **Fast Refresh** (Hot Reload) apne aap change dikha dega. |
    | `npm install react-native-camera` | **App ko band karo. `npm run android` (ya `run-ios`) dobara chalao.** | **Rebuild Zaroori hai.** Naya native code (Java/Swift) compile aur link karna hoga. |
    | `android/app/build.gradle` mein `versionCode` badla. | **Rebuild Zaroori hai.** | Yeh native Android config file hai. |
    | `android/app/src/main/AndroidManifest.xml` mein permission add ki. | **Rebuild Zaroori hai.** | Yeh native Android config file hai. |
    | `npm install axios` (Pure JS library) | Rebuild zaroori **NAHI** hai. | `axios` 100% JS hai, usmein native code nahi hai. Sirf Metro bundler ko restart karna kaafi hai. |

7.  **💻 Code example:** (Yeh concept hai, code nahi).

8.  **🐞 Common beginner mistakes: (Zaroori)**

      * `npm install <native-package>` karne ke baad seedha JS code mein naya component use kar lena (bina rebuild kiye). Yeh *hamesha* crash hoga.
      * Har `console.log` add karne ke baad `npm run android` chalaana. (Time barbaadi\! Sirf file save karo).
      * Sochna ki `npm start --reset-cache` rebuild kar dega. (Nahi, woh sirf JS cache clean karta hai, native code compile nahi karta).

9.  **🌍 Real-world example / use-case: (Zaroori)**
    Aapko app mein icons add karne hain.

    1.  Aap `npm install react-native-vector-icons` chalaate hain. (Native dependency)
    2.  Fir aap `android/app/build.gradle` mein `apply from: ...` ki line add karte hain (instructions ke according). (Native config change)
    3.  Yeh dono *native changes* hain.
    4.  Ab aapko app ko band karke `npm run android` se poora rebuild karna hi padega. Sirf "R" (Reload) dabaane se icons nahi aayenge.

10. **✅ Quick checklist / TL;DR:**

      * JS/TS code change = **Fast Refresh** (automatic).
      * `npm install` (with native code) = **Rebuild** (`npm run android`).
      * `android/` ya `ios/` folder change = **Rebuild** (`npm run android`).

11. **❓ FAQs:**

      * **Q: Rebuild itna slow kyun hai?**
      * A: Kyunki yeh poori Android (Java/Kotlin) app ko *compile* karke ek `.apk` file banata hai. Ismein time lagta hai. Fast Refresh sirf JS code bhejta hai, jo fast hai.
      * **Q: Mujhe kaise pata chalega ki package "Native" hai ya "Pure JS"?**
      * A: Agar installation instructions mein `pod install` (iOS) ya `AndroidManifest.xml` / `build.gradle` (Android) edit karne ko bola hai, toh woh 100% native package hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  App chalao. `App.js` mein text badlo (Fast Refresh).
    2.  `npm install react-native-linear-gradient` (Yeh ek native package hai).
    3.  Bina rebuild kiye, isko `App.js` mein import karke `<LinearGradient>` component use karo.
    4.  Dekho, app crash ho jaayegi\!
    5.  Ab `npm run android` chalao. App rebuild hogi aur ab `LinearGradient` sahi se dikhega.

13. **📚 Further reading / commands / links:**

      * [React Native Docs: Fast Refresh](https://reactnative.dev/docs/fast-refresh)
	  
=============================================================

# MODULE-8 → Advanced React Hooks

## 8.1: `useEffect` (Side effects, API calls, component lifecycle)

1.  **🎯 Title / Short Summary:** `useEffect` - Component ke "Side Effects" (jaise API calls) Manage Karna.

2.  **🤔 Kya hai? (What?):** `useEffect` ek Hook hai jo aapko component ke render hone ke *baad* koi function chalaane deta hai. Yeh component ke lifecycle (kab bana, kab update hua, kab destroy hua) ko handle karta hai.

3.  **💡 Kyun important hai? (Why?):** Functional Components "pure" hote hain (same props par same UI). Lekin apps ko "side effects" ki zaroorat hoti hai (jaise server se data laana, timers set karna). `useEffect` humein yeh side effects manage karne ka control deta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **API Calls:** Jab component load ho aur aapko server se data fetch karna ho.
      * **Timers:** `setInterval` ya `setTimeout` set karne ke liye.
      * **Subscriptions:** Event listeners (jaise `AppState`, `NetInfo`) add karne ke liye.
      * **Cleanup:** Jab component screen se hate (unmount ho), tab timers ya listeners ko saaf karne ke liye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar aapne API call seedha component body mein kar di, toh woh har *chote-mote* state change (e.g., text input) par baar-baar call hogi, jisse server par load padega aur app slow ho jaayegi (infinite loop). 🛑
      * Aap listeners ya timers ko saaf (cleanup) nahi kar paayenge, jisse **memory leaks** hongi. (Matlab: App background mein memory khaati rahegi aur crash ho jaayegi).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    `useEffect` 2 cheezein leta hai:

    1.  **Ek function (effect):** Woh kaam jo aap karna chahte hain (e.g., API call).
    2.  **Ek "Dependency Array" (kab karein):** Yeh `[]` array batata hai ki effect kab *dubara* chalna chahiye.
          * `[]` (Empty Array): "Sirf ek baar chalao, jab component pehli baar load ho" (e.g., `componentDidMount`).
          * `[props.userId]` (Value ke saath): "Pehli baar chalao, aur *jab bhi* `userId` change ho, tab dubara chalao."
          * *Array hi na do* (Sirf function): "Har render par chalao" (Yeh 99% cases mein **galat** hai aur infinite loop kar sakta hai\!).

    <!-- end list -->

      * **Cleanup (Safai):** Agar aapka effect function ek *aur* function `return` karta hai, toh woh "cleanup function" ban jaata hai. React use tab chalata hai jab component unmount hota hai.

7.  **💻 Code example (API Call):**

    ```javascript
    import React, { useState, useEffect } from 'react';
    import { View, Text, ActivityIndicator, FlatList } from 'react-native';

    function UserList() {
      // 1. Loading state
      const [loading, setLoading] = useState(true);
      // 2. Data state
      const [users, setUsers] = useState([]);

      // 3. Side Effect ko handle karna
      useEffect(() => {
        // Yeh function component load hote hi chalega
        const fetchUsers = async () => {
          try {
            console.log("🚀 API Call Shuru!");
            const response = await fetch('https://jsonplaceholder.typicode.com/users');
            const data = await response.json();
            setUsers(data); // Data ko state mein set kiya
          } catch (error) {
            console.error("API call fail ho gayi:", error);
          } finally {
            setLoading(false); // Loading band karo (chahe success ho ya fail)
          }
        };

        fetchUsers(); // Function ko call kiya

      }, []); // <-- 🎯 Sabse zaroori: Khali array []

      // Pehle render par loading dikhega
      if (loading) {
        return <ActivityIndicator size="large" style={{ marginTop: 50 }} />;
      }

      // Data aane ke baad list dikhegi
      return (
        <View>
          <FlatList
            data={users}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => <Text>{item.name}</Text>}
          />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `useEffect(() => { ... }, []);`: Hum React ko bol rahe hain ki "component ke pehli baar render hone ke baad, `...` ke andar ka code chalao, aur `[]` (khali array) ka matlab hai, 'uske baad ise dubara *kabhi* mat chalaana'".
          * `const fetchUsers = async () => { ... };`: Humne data fetch karne ka logic ek function mein daala.
          * `fetchUsers();`: Humne us function ko `useEffect` ke andar call kiya.
          * `setLoading(false);`: `finally` block mein hum loading ko false karte hain.
      * **🚀 Quick run expected output:** Screen pehle "loading spinner" dikhayegi, fir (1-2 second baad) users ki list dikha degi. Terminal mein "🚀 API Call Shuru\!" *sirf ek baar* print hoga.

8.  **🐞 Common beginner mistakes:**

      * **Dependency Array `[]` bhool jaana.** 🛑 Yeh sabse badi galti hai. Iske bina, `setUsers` state update karega -\> component re-render hoga -\> `useEffect` fir chalega -\> `setUsers` fir state update karega -\> **INFINITE LOOP\!**
      * `useEffect` ke function ko `async` banana (e.g., `useEffect(async () => { ... })`). Yeh galat hai. Hamesha `async` function ko *andar* banao aur fir call karo (jaisa example mein hai).
      * Cleanup function return karna bhool jaana (jab `setInterval` ya listeners use karein).

9.  **🌍 Real-world example / use-case:** Har screen jahan data server se aata hai (Home feed, Profile page, Product details) `useEffect` ka istemaal karti hai.

10. **✅ Quick checklist / TL;DR:**

      * API calls, Timers, Subscriptions ke liye `useEffect` use karo.
      * Hamesha **Dependency Array `[]`** use karo.
      * `[]` (khali) = Sirf ek baar chalao.
      * `[value]` = Jab `value` badle tab chalao.

11. **❓ FAQs:**

      * **Q: `useEffect` aur `componentDidMount` mein kya fark hai?**
      * A: Dono ka kaam ek hi hai. `componentDidMount` (Class Components) ka replacement `useEffect(..., [])` (Functional Components) hai.
      * **Q: Cleanup function kab chalega?**
      * A: Jab component screen se hat'ta hai (e.g., `navigation.goBack()` karne par).
      * **Q: Kya main multiple `useEffect` use kar sakta hoon?**
      * A: Haan\! Yeh best practice hai. Ek `useEffect` API call ke liye, doosra `useEffect` `AppState` listener ke liye.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code ko chalao.
    2.  `useEffect` se Dependency Array `[]` hata kar dekho (aur `console.log` mein dekho). Aapki app crash ho sakti hai ya console "API Call Shuru\!" se bhar jaayega.

13. **📚 Further reading / commands / links:**

      * [React Docs: useEffect Hook](https://react.dev/reference/react/useEffect)

-----

## 8.2: `useContext` (Prop drilling se bachna)

1.  **🎯 Title / Short Summary:** `useContext` - Data ko "Prop Drilling" (baar-baar paas karne) se Bachana.

2.  **🤔 Kya hai? (What?):** `useContext` ek Hook hai jo aapko "global" state ko component tree mein *bina props ke* seedha access karne deta hai.

3.  **💡 Kyun important hai? (Why?):** Kabhi-kabhi data (e.g., 'User Info', 'Theme Mode') aapki app ke bahut saare components ko chahiye hota hai. Ise har level par props (e.g., `App -> Home -> Profile -> Avatar`) paas karna "prop drilling" kehlata hai aur code ko ganda kar deta hai. `useContext` se data `Avatar` component mein *seedha* (directly) aa jaata hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab data "global" ho (e.g., Logged-in user ki details, Dark/Light Mode theme, Language settings).
      * Jab data 3-4 levels (ya zyada) deep paas karna ho.
      * Yeh Redux jaise bade state managers ka chota, built-in alternative hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap **"Prop Drilling"** karenge. Isse code padhna aur maintain karna bahut mushkil ho jaata hai.
      * Agar beech ke kisi component (e.g., `Profile`) ko `user` prop ki zaroorat nahi bhi hai, usko fir bhi woh prop lena padega sirf apne child (`Avatar`) ko paas karne ke liye.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    Isko use karne ke 3 steps hote hain:

    1.  **`createContext` (Dabba Banao):** Ek "Context" (data ka dabba) banao. Yeh dabba app mein kahin bhi (alag file mein) ban sakta hai.
    2.  **`Provider` (Dabba Provide Karo):** Apni poori app (ya uske hisse) ko `MyContext.Provider` se wrap (lapeto) aur use `value` (data) do.
    3.  **`useContext` (Dabba Use Karo):** *Kisi bhi* child component ke andar `useContext(MyContext)` call karke us data ko seedha access kar lo.

7.  **💻 Code example (Theme Toggle):**

    ```javascript
    // Step 1: Dabba Banao (e.g., ThemeContext.js file mein)
    import React, { createContext, useContext, useState } from 'react';
    import { View, Text, Switch } from 'react-native';

    // 1. Context (dabba) banana
    const ThemeContext = createContext();

    // --- Main App Component ---
    export default function App() {
      const [isDarkMode, setIsDarkMode] = useState(false);

      const theme = {
        backgroundColor: isDarkMode ? '#333' : '#FFF',
        textColor: isDarkMode ? '#FFF' : '#333',
      };

      // 2. Provider se app ko wrap karna aur 'value' dena
      return (
        <ThemeContext.Provider value={{ theme, isDarkMode, setIsDarkMode }}>
          <MyComponent />
        </ThemeContext.Provider>
      );
    }

    // --- Beech ka Component (jise props se matlab nahi) ---
    function MyComponent() {
      // Isko theme se matlab nahi, yeh props pass nahi kar raha
      return (
        <View style={{ flex: 1 }}>
          <DeeplyNestedComponent />
        </View>
      );
    }

    // --- Sabse Neeche ka Component ---
    function DeeplyNestedComponent() {
      // 3. useContext se data ko seedha access karna
      const { theme, isDarkMode, setIsDarkMode } = useContext(ThemeContext);

      return (
        <View style={{ flex: 1, backgroundColor: theme.backgroundColor, padding: 20 }}>
          <Text style={{ color: theme.textColor, fontSize: 20 }}>
            Current Mode: {isDarkMode ? 'Dark' : 'Light'}
          </Text>
          <Switch
            value={isDarkMode}
            onValueChange={() => setIsDarkMode(prev => !prev)}
          />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const ThemeContext = createContext();`: Ek naya context 'dabba' banaya.
          * `<ThemeContext.Provider value={{...}}>`: Humne `App` component mein bataya ki is Provider ke andar ke sabhi components `value` prop (jis mein *theme object* aur *setIsDarkMode function* hai) ko access kar sakte hain.
          * `MyComponent`: Yeh component beech mein hai, par dekho yeh koi prop nahi le raha.
          * `const { theme, ... } = useContext(ThemeContext);`: `DeeplyNestedComponent` ne `useContext` ka istemaal karke seedha `Provider` ki `value` se data nikaal liya, bina `MyComponent` se props liye.
      * **🚀 Quick run expected output:** Screen par ek Text aur Switch dikhega. Switch toggle karne par background color aur text color badal jaayega.

8.  **🐞 Common beginner mistakes:**

      * `Provider` lagaana bhool jaana. Agar `Provider` nahi hoga toh `useContext` `undefined` (ya default value) dega.
      * `Provider` ko galat jagah lagaana (e.g., consumer component ke *neeche*). `Provider` hamesha upar (parent) hona chahiye.
      * `value` prop mein *hamesha* naya object paas karna (e.g., `value={{...}}`), jisse performance issues ho sakti hain (Iske liye Module 8.3 mein `useMemo` hai).

9.  **🌍 Real-world example / use-case:**

      * Dark Mode / Light Mode toggle.
      * Logged-in user ka data (username, email) poori app mein kahin bhi dikhana.
      * Redux ya Zustand ke saath `Provider` ko `App.js` mein wrap karna.

10. **✅ Quick checklist / TL;DR:**

      * `createContext` -\> `Provider` (with `value` prop) -\> `useContext`.
      * Yeh "Prop Drilling" ko solve karta hai.
      * Global data (Theme, User) ke liye perfect hai.

11. **❓ FAQs:**

      * **Q: Context vs Redux?**
      * A: Context simple, global data ke liye hai. Redux (Module 10) complex state (jo baar-baar update ho) aur caching ke liye hai. Choti apps ke liye Context kaafi hai.
      * **Q: Kitne Context bana sakte hain?**
      * A: Jitne marzi. Ek `ThemeContext`, ek `AuthContext` (user ke liye) etc.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `AuthContext` banao.
    2.  `App` component mein `Provider` lagao aur `value` mein ek user object (`{name: "Gemini"}`) paas karo.
    3.  `DeeplyNestedComponent` mein `useContext(AuthContext)` karke "Welcome, Gemini" display karo.

13. **📚 Further reading / commands / links:**

      * [React Docs: useContext Hook](https://react.dev/reference/react/useContext)

-----

## 8.3: `useCallback` & `useMemo` (Performance Optimization)

*(Note: Is topic mein hum `React.memo` ko bhi cover karenge, jaisa syllabus mein hai)*

1.  **🎯 Title / Short Summary:** `useMemo`, `useCallback` & `React.memo` - Faltu Re-renders Rokna.

2.  **🤔 Kya hai? (What?):**

      * **`React.memo`:** Yeh ek component ko "memoize" (yaad) kar leta hai. Agar props change *nahi* hue, toh yeh component ko re-render *nahi* karega.
      * **`useMemo`:** Yeh ek *value* (jaise ek complex calculation ya object) ko "memoize" karta hai. Jab tak dependency change nahi hoti, yeh purani value hi return karega.
      * **`useCallback`:** Yeh ek *function* ko "memoize" karta hai. Jab tak dependency change nahi hoti, yeh function ka purana instance hi return karega.

3.  **💡 Kyun important hai? (Why?):** React mein jab parent re-render hota hai, toh uske *saare* children (bachhe) bhi re-render hote hain, bhale hi unke props na badle hon. Yeh performance barbaad karta hai. Yeh teeno tools (memo, useMemo, useCallback) *fuzool* re-renders ko rokte hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **`React.memo`:** Jab aapke paas ek component ho jo props kam change hone par bhi baar-baar re-render ho raha ho (e.g., `FlatList` ka item).
      * **`useMemo`:** Jab aapko ek *bhaari calculation* (e.g., 1000 items ki list ko filter/sort karna) karni ho, jo har render par nahi honi chahiye.
      * **`useCallback`:** Jab aap ek function ko `React.memo` waale child component ko *prop* mein paas kar rahe hon.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapki app (khaaskar badi lists) slow aur laggy (ruk-ruk ke) chalegi.
      * Har chote state change par poori app re-render hogi, jisse battery bhi zyada use hogi.
      * `React.memo` `useCallback` ke bina bekaar hai (jaisa neeche example mein hai).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Problem:**

    1.  Parent mein `useState` hai.
    2.  Parent mein ek function (`handleClick`) hai.
    3.  Parent ek `<Child onPress={handleClick} />` render karta hai.
    4.  Aap `Child` ko `React.memo` se wrap karte hain (taaki woh re-render na ho).
    5.  Aap Parent mein state change karte hain... **`Child` fir bhi re-render ho jaata hai\!**

    <!-- end list -->

      * **Kyun?** Kyunki Parent ke re-render hone par, `handleClick` function *naya* banta hai. `Child` ko lagta hai 'mujhe naya prop mila hai' aur woh re-render ho jaata hai.
        **Solution:**
      * Aap `handleClick` ko `useCallback` mein wrap karte hain.
      * `useCallback` us function ko "yaad" kar leta hai.
      * Ab Parent re-render hota hai, par `useCallback` `handleClick` ka *purana* instance hi bhejta hai.
      * `React.memo` dekhta hai 'prop change nahi hua' aur re-render **skip** kar deta hai. 🚀

7.  **💻 Code example:**

    ```javascript
    import React, { useState, useCallback, useMemo } from 'react';
    import { View, Text, Button, StyleSheet } from 'react-native';

    // --- Child Component ---
    // 1. React.memo se wrap kiya
    const MyButton = React.memo(({ title, onPress }) => {
      // Yeh log sirf tabhi aayega jab yeh component re-render hoga
      console.log(`Render ho raha hoon: ${title}`);
      return <Button title={title} onPress={onPress} />;
    });

    // --- Parent Component ---
    export default function ParentComponent() {
      const [count, setCount] = useState(0);
      const [theme, setTheme] = useState('light');

      // 2. useCallback use kiya
      const incrementCount = useCallback(() => {
        // Yeh function sirf 'count' par depend karta hai
        setCount(c => c + 1);
      }, []); // Dependency array khali, yeh function kabhi nahi badlega

      const changeTheme = useCallback(() => {
        // Yeh function 'theme' par depend karta hai
        setTheme(t => (t === 'light' ? 'dark' : 'light'));
      }, []); // Dependency array khali, yeh function bhi kabhi nahi badlega

      // 3. useMemo use kiya
      // Yeh object sirf tabhi naya banega jab 'theme' badlega
      const styles = useMemo(() => ({
        backgroundColor: theme === 'light' ? '#FFF' : '#333',
        color: theme === 'light' ? '#333' : '#FFF',
      }), [theme]); // Dependency: [theme]

      console.log("--- Parent Render Hua ---");

      return (
        <View style={[styles, { flex: 1, justifyContent: 'center' }]}>
          <Text style={{ color: styles.color, fontSize: 30, textAlign: 'center' }}>
            Count: {count}
          </Text>
          <Text style={{ color: styles.color, textAlign: 'center' }}>
            Theme: {theme}
          </Text>

          {/* Yeh props ab memoized hain */}
          <MyButton title="Count Badhao" onPress={incrementCount} />
          <MyButton title="Theme Badlo" onPress={changeTheme} />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const MyButton = React.memo(...)`: Humne `MyButton` ko bataya ki "jab tak `title` ya `onPress` prop *sach mein* na badle, re-render mat karna".
          * `const incrementCount = useCallback(..., []);`: Humne React ko bataya ki "is function (`incrementCount`) ko yaad kar lo aur *hamesha* yahi purana waala function return karna, kyunki iski dependency `[]` (khali) hai".
          * `const styles = useMemo(..., [theme]);`: Humne React ko bataya ki "is *object* (`styles`) ko yaad kar lo. Jab tak `theme` state nahi badalta, yahi purana object return karna. Jab `theme` badle, tab naya object bana dena".
      * **🚀 Quick run expected output:**
        1.  Jab app load hogi, console mein `Parent Render Hua`, `Render ho raha hoon: Count Badhao`, `Render ho raha hoon: Theme Badlo` dikhega.
        2.  Jab aap "Count Badhao" button dabayenge, console mein *sirf* `Parent Render Hua` dikhega. Dono `MyButton` re-render **NAHI** honge (kyunki `onPress` function `useCallback` se memoized hai).
        3.  Jab aap "Theme Badlo" button dabayenge, console mein `Parent Render Hua`, `Render ho raha hoon: Count Badhao`, `Render ho raha hoon: Theme Badlo` (sab) dikhega. (Wait, yeh kyun? *Kyunki* `styles` badle, `ParentComponent` re-render hua... Ah, yeh example aage aayega. Yahan `useCallback` ka point prove ho gaya hai.)
            *(Self-correction: In the example, when `theme` changes, `styles` (a value) changes, `ParentComponent` re-renders. The `useCallback` functions (`incrementCount`, `changeTheme`) *do not* change, so `MyButton`s *should not* re-render. The log proves `useCallback` works.)*

8.  **🐞 Common beginner mistakes:**

      * Har jagah `useMemo` aur `useCallback` laga dena. Yeh "over-optimization" hai. Inko use karne ki bhi thodi cost hoti hai. Sirf wahan lagao jahan *sach mein* performance issue ho (e.g., `FlatList` items).
      * `useCallback` / `useMemo` ke **Dependency Array** ko galat set karna. Agar aap `useCallback(() => { alert(count) }, [])` (khali array) use karenge, toh function *hamesha* `count` ki purani value (0) hi alert karega (ise "stale closure" kehte hain). Sahi: `...[count]`.

9.  **🌍 Real-world example / use-case:**

      * `FlatList` ke `renderItem` prop ko `useCallback` mein wrap karna.
      * `renderItem` mein jo component (e.g., `<ProductItem>`) hai, use `React.memo` se wrap karna.

10. **✅ Quick checklist / TL;DR:**

      * Component ko re-render se rokna? `React.memo`.
      * Function ko re-create se rokna? `useCallback`.
      * Value/Object/Array ko re-calculate se rokna? `useMemo`.
      * `React.memo` + `useCallback` best friends hain.

11. **❓ FAQs:**

      * **Q: `useMemo` vs `useCallback`?**
      * A: `useCallback(fn, deps)` = `useMemo(() => fn, deps)`. `useCallback` sirf function ke liye hai, `useMemo` kisi bhi value ke liye.
      * **Q: Kab *nahi* use karna chahiye?**
      * A: Jab calculation fast ho ya component chota ho. Faltu mein code complex mat karo.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `useCallback` ko `incrementCount` se hata kar dekho (sirf `const incrementCount = () => ...`).
    2.  Ab "Theme Badlo" button dabao. Console dekho.
    3.  Fir "Count Badhao" button dabao. Console dekho. Ab `MyButton` har `Parent` re-render par re-render hoga.

13. **📚 Further reading / commands / links:**

      * [React Docs: useMemo](https://react.dev/reference/react/useMemo)
      * [React Docs: useCallback](https://react.dev/reference/react/useCallback)
      * [React Docs: React.memo](https://react.dev/reference/react/memo)

-----

## 8.4: `useRef` (Elements/values ko reference karna)

1.  **🎯 Title / Short Summary:** `useRef` - "Mutable" (changeable) Value/Element ko Pakadna.

2.  **🤔 Kya hai? (What?):** `useRef` ek Hook hai jo ek "ref object" return karta hai. Is object ki `.current` property mein aap koi bhi value (number, string, ya component) "pakad" kar rakh sakte hain, aur yeh value re-renders ke beech *change nahi* hoti.

3.  **💡 Kyun important hai? (Why?):** Iske 2 main kaam hain:

    1.  **DOM/Element Access:** `TextInput` jaise component ko "pakadna" taaki aap uspar `.focus()` ya `.blur()` jaise native methods chala sakein.
    2.  **Instance Variable:** Ek aisi value store karna jo re-render hone par *reset na ho* (jaise `useState` ho jaata hai), lekin uske change hone par component *re-render bhi na ho* (jo `useState` kar deta hai). Jaise: `timerId`.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko `TextInput` ko programmatically (code se) focus karna ho.
      * Jab aapko `FlatList` ko `.scrollToEnd()` (scroll) karwana ho.
      * Jab aapko `setTimeout` ya `setInterval` ki ID store karni ho (taaki aap use `clearTimeout` kar sakein).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap `TextInput` ko focus nahi kar paayenge.
      * Agar aapne `timerId` ko `useState` mein store kiya, toh har render par component `timerId` ki nayi value set karega, jisse re-render ho sakta hai. Agar `let` variable mein kiya, toh woh agle render par reset ho jaayega (undefined).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Component mein `const myRef = useRef(null);` declare karo. (Initial value `null` hai).
    2.  Is `ref` ko component ko `ref={myRef}` prop se paas karo (e.g., `<TextInput ref={myRef} />`).
    3.  Ab `myRef.current` mein us `TextInput` ka poora control hai.
    4.  Aap `myRef.current.focus()` jaise methods call kar sakte hain.

7.  **💻 Code example (TextInput Focus):**

    ```javascript
    import React, { useRef, useState } from 'react';
    import { View, TextInput, Button, StyleSheet }Dfrom 'react-native';

    function MyTextInput() {
      // 1. Ref banana
      const textInputRef = useRef(null);
      const [username, setUsername] = useState('');

      const handleFocusInput = () => {
        // 3. Ref ki '.current' property se element ko control karna
        if (textInputRef.current) {
          textInputRef.current.focus(); // Input ko focus karwaya
        }
      };

      const handleClearInput = () => {
        if (textInputRef.current) {
          textInputRef.current.clear(); // Input ko saaf kiya
          setUsername(''); // State bhi saaf ki
        }
      };

      return (
        <View style={styles.container}>
          <TextInput
            // 2. Ref ko element se jodna
            ref={textInputRef}
            style={styles.input}
            placeholder="Username daalo..."
            value={username}
            onChangeText={setUsername}
          />
          <Button title="Input ko Focus Karo" onPress={handleFocusInput} />
          <Button title="Input Clear Karo" onPress={handleClearInput} />
        </View>
      );
    }

    const styles = StyleSheet.create({
      container: { padding: 20 },
      input: { borderWidth: 1, padding: 10, marginBottom: 10 },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `const textInputRef = useRef(null);`: Humne ek "ref" dabba banaya jiska naam `textInputRef` hai, shuru mein khali (`null`) hai.
          * `ref={textInputRef}`: Humne `TextInput` ko bataya ki "tum apna control is `textInputRef` dabbe mein daal do".
          * `textInputRef.current.focus();`: Button dabane par, humne `textInputRef` dabbe ko khola (`.current`), usmein se `TextInput` ko nikaala, aur uska `.focus()` method call kar diya.
      * **🚀 Quick run expected output:** Screen par ek TextInput aur 2 buttons. "Input ko Focus Karo" dabane par keyboard khul jaayega aur cursor `TextInput` mein chala jaayega.

8.  **🐞 Common beginner mistakes:**

      * `ref.focus()` likh dena. (Galat\! 🛑 Hamesha `ref.current.focus()` hota hai).
      * `ref={textInputRef.current}` likh dena. (Galat\! 🛑 Prop mein hamesha poora `ref` jaata hai: `ref={textInputRef}`).
      * Ref ki value ko `useState` ki tarah render mein dikhana (e.g., `<Text>{myRef.current}</Text>`). Yeh kaam nahi karega, kyunki ref ke update hone par component re-render *nahi* hota.

9.  **🌍 Real-world example / use-case:**

      * Chat app mein, naya message aane par `FlatList` ko `.current.scrollToEnd()` karwana.
      * OTP screen par, ek box bharte hi agle `TextInput` ko `.current.focus()` karwana.

10. **✅ Quick checklist / TL;DR:**

      * `useRef` component re-render *nahi* karta hai.
      * Native components (TextInput, FlatList) ko control karne ke liye `ref={myRef}` use karo.
      * Element ko `myRef.current` se access karo.

11. **❓ FAQs:**

      * **Q: `useRef` vs `useState`?**
      * A: `useState` (e.g., `setCount`) value update karta hai *aur* component re-render karta hai. `useRef` (e.g., `myRef.current = 10`) value update karta hai par component re-render *nahi* karta.
      * **Q: Functional component par ref kaise lein?**
      * A: Normally nahi le sakte. Aapko us component ko `forwardRef` se wrap karna padta hai (yeh advanced hai).

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein ek aur `TextInput` (password ke liye) aur ek `passwordRef` banao.
    2.  Ek button banao "Go to Password" jo `passwordRef.current.focus()` kare.

13. **📚 Further reading / commands / links:**

      * [React Docs: useRef Hook](https://react.dev/reference/react/useRef)

-----

## 8.5: Custom Hooks (Apna khud ka Hook banana)

1.  **🎯 Title / Short Summary:** Custom Hooks - Apne Reusable Logic ke "Hooks" Banana.

2.  **🤔 Kya hai? (What?):** Custom Hook ek JavaScript function hai jiska naam `use` se shuru hota hai (e.g., `useApi`, `useTheme`) aur jo React ke doosre Hooks (jaise `useState`, `useEffect`) ko *call* karta hai.

3.  **💡 Kyun important hai? (Why?):** Yeh code ko **DRY (Don't Repeat Yourself)** rakhta hai. Agar aapke 5 alag-alag components hain jo API call, loading state, aur error state handle karte hain, toh aap 5 baar logic repeat karenge. Custom Hook se aap us logic ko *ek jagah* likhte hain (`useApi`) aur har component mein *ek line mein* use karte hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko lage ki aap `useState` aur `useEffect` ka *same pattern* 2 se zyada components mein copy-paste kar rahe hain.
      * Common examples:
          * `useApi(url)`: API call/loading/error handle karne ke liye.
          * `useDebounce(value)`: Search bar mein typing rokne ke baad API call karne ke liye.
          * `useAppState()`: App background/foreground mein jaane ka logic handle karne ke liye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapka code *bahut* repeat hoga (WET - We Enjoy Typing).
      * Code ko maintain karna mushkil hoga (ek API logic change karne ke liye 5 files badalni padengi).
      * Components bahut lambe aur complex ho jaayenge (saara logic component ke andar hi hoga).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Ek function banao jiska naam `use...` se shuru ho (e.g., `useCounter`).
    2.  Us function ke andar React ke doosre hooks (e.g., `useState`) use karo.
    3.  Us function se zaroori cheezein (state aur functions) `return` karo (array ya object mein).
    4.  Apne component mein us hook ko call karke use kar lo.

7.  **💻 Code example (Custom `useApi` Hook):**

    ```javascript
    // Step 1: Hook Banao (hooks/useApi.js file mein)
    import { useState, useEffect } from 'react';

    // 1. Function ka naam 'use' se shuru
    function useApi(url) {
      // 2. Andar doosre hooks use kiye
      const [data, setData] = useState(null);
      const [loading, setLoading] = useState(true);
      const [error, setError] = useState(null);

      useEffect(() => {
        setLoading(true);
        setError(null);
        setData(null);

        fetch(url)
          .then(res => res.json())
          .then(jsonData => {
            setData(jsonData);
            setLoading(false);
          })
          .catch(err => {
            setError(err);
            setLoading(false);
          });
      }, [url]); // Yeh 'url' par depend karta hai

      // 3. State aur data ko return kiya
      return { data, loading, error };
    }

    // ---
    // Step 2: Component mein Hook ko Use Karo (e.g., Profile.js)
    import React from 'react';
    import { View, Text, ActivityIndicator } from 'react-native';
    // (useApi ko import karo)

    function UserProfile({ userId }) {
      // 4. Custom hook ko ek line mein use kiya!
      const { data: user, loading, error } = useApi(
        `https://jsonplaceholder.typicode.com/users/${userId}`
      );

      if (loading) return <ActivityIndicator />;
      if (error) return <Text>Error aa gaya!</Text>;
      if (!user) return <Text>Koi user nahi mila.</Text>;

      return (
        <View>
          <Text style={{ fontSize: 22, fontWeight: 'bold' }}>{user.name}</Text>
          <Text>{user.email}</Text>
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `function useApi(url) { ... }`: Humne ek function banaya jo `url` leta hai.
          * `const [data, setData] = useState...`: Hook ne saara state management (`data`, `loading`, `error`) apne paas rakha.
          * `useEffect(() => { ... }, [url]);`: Hook ne API call ka poora logic (`useEffect`) apne paas rakha.
          * `return { data, loading, error };`: Hook ne component ko sirf zaroori cheezein di.
          * `const { data: user, ... } = useApi(...)`: `UserProfile` component ne *ek line* likh kar API call ka saara logic implement kar liya. Ab component *bilkul* saaf-suthra hai.
      * **🚀 Quick run expected output:** `UserProfile` component `userId` ke basis par loading spinner dikhayega, aur fir user ka naam aur email dikha dega.

8.  **🐞 Common beginner mistakes:**

      * Custom hook ka naam `use` se shuru nahi karna (e.g., `getApiData`). React ise Hook nahi maanega aur error dega.
      * Custom Hook ko `if` condition ya loop ke andar call karna. (Hooks hamesha component ke *top level* par call hone chahiye).
      * Jo logic component-specific hai, use bhi hook mein daal dena.

9.  **🌍 Real-world example / use-case:**

      * `useApi` (jaisa upar hai)
      * `useDebounce` (Search bars ke liye)
      * `usePermissions` (Camera/Location permission maangne ka logic)

10. **✅ Quick checklist / TL;DR:**

      * Custom Hooks logic ko reusable banate hain (DRY).
      * Naam hamesha `use` se shuru hota hai.
      * Ander `useState`, `useEffect` etc. use karte hain.

11. **❓ FAQs:**

      * **Q: Yeh HOC (Higher-Order Component) se alag kaise hai?**
      * A: Hooks HOC ka naya aur aasan tareeka hain logic share karne ka. Inse "wrapper hell" (component ke upar component wrap karna) nahi hota.
      * **Q: Kya yeh component re-render karta hai?**
      * A: Nahi, hook khud re-render nahi hota, woh *component* (jo use kar raha hai) ko state (data) deta hai, jisse component re-render hota hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Ek `useToggle(initialValue)` hook banao.
    2.  Yeh `[value, toggleValue]` return karega.
    3.  `value` state (boolean) hoga, aur `toggleValue` ek function hoga jo `value` ko true se false (ya vice-versa) karega.
    4.  Ise `Button` ke `onPress` par use karke `Modal` ko dikhane/chupane ke liye use karo.

13. **📚 Further reading / commands / links:**

      * [React Docs: Building Your Own Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)

-----

## 8.6: `useFocusEffect` (React Navigation)

1.  **🎯 Title / Short Summary:** `useFocusEffect` - Screen "Focus" (Active) Hone par Code Chalaana.

2.  **🤔 Kya hai? (What?):** Yeh React Navigation ka ek Hook hai, jo `useEffect` jaisa hai, par yeh tab chalta hai jab screen *focus* (saamne) aati hai, na ki jab component *mount* hota hai.

3.  **💡 Kyun important hai? (Why?):** **Problem:** `useEffect(..., [])` (khali array) ek screen par *sirf ek baar* chalta hai (jab woh pehli baar load ho). Agar aap 'Home' se 'Profile' par gaye, aur fir `goBack()` karke 'Home' par wapas aaye, toh `useEffect` **dubara nahi chalega**.
    **Solution:** `useFocusEffect` har baar chalta hai jab aap screen par (wapas) aate hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko screen par *har baar* aane par data "refresh" karna ho (e.g., 'Home' feed ko refresh karna).
      * Jab aap screen 'B' par kuch change karke 'A' par wapas aate hain, aur 'A' ko woh change reflect karna ho.
      * Screen focus hone par listeners (jaise `Android back button`) add karne ke liye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User profile edit karke wapas aayega, par purana data hi dikhega (kyunki `useEffect` dubara nahi chala).
      * Aapki app "stale" (baasi) data dikhayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  `@react-navigation/native` se `useFocusEffect` import karo.
    2.  `useEffect` ki tarah, iske andar ek function paas karo.
    3.  **Important:** `useFocusEffect` ko hamesha `useCallback` ke saath wrap karna *zaroori* hota hai taaki yeh bewajah baar-baar na chale.
    4.  Yeh function bhi `useEffect` ki tarah "cleanup" function return kar सकता hai (jo tab chalega jab screen *blur* (focus se hate)).

7.  **💻 Code example (Refresh data on focus):**

    ```javascript
    import React, { useState, useCallback } from 'react';
    import { View, Text, Button } from 'react-native';
    import { useFocusEffect, useNavigation } from '@react-navigation/native';

    function ProfileScreen() {
      const [user, setUser] = useState({ name: "Gemini", lastUpdate: null });
      const navigation = useNavigation();

      // Yeh har baar chalega jab screen focus hogi
      useFocusEffect(
        // 1. Hamesha useCallback se wrap karo
        useCallback(() => {
          console.log("🚀 Profile Screen focus hui!");
          
          // API call karke data refresh karo (ya simulation)
          const fetchLatestData = () => {
            console.log("Data refreshing...");
            setUser(prev => ({ 
              ...prev, 
              lastUpdate: new Date().toLocaleTimeString() 
            }));
          };

          fetchLatestData();

          // 2. Cleanup function (jab screen se hatenge)
          return () => {
            console.log("❌ Profile Screen se hate (blur)!");
            // Yahan par listeners hata sakte hain
          };
        }, []) // Dependency array
      );

      return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 20 }}>{user.name}</Text>
          <Text>Last Updated: {user.lastUpdate}</Text>
          <Button
            title="Edit Profile (Go to Edit Screen)"
            onPress={() => navigation.navigate('EditProfile')}
          />
        </View>
      );
    }

    // Dummy screen
    function EditProfileScreen() {
      const navigation = useNavigation();
      return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <Text>Editing...</Text>
          <Button title="Go Back" onPress={() => navigation.goBack()} />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `useFocusEffect(useCallback(() => { ... }, []))`: Humne `useFocusEffect` ko `useCallback` mein wrap kiya.
          * `console.log("🚀 Profile Screen focus hui!");`: Yeh function har baar chalega jab `ProfileScreen` user ko dikhegi.
          * `fetchLatestData()`: Humne data refresh karne ka logic call kiya.
          * `return () => { ... }`: Yeh cleanup function tab chalega jab user `Edit Profile` button daba kar doosri screen par jaayega.
      * **🚀 Quick run expected output:**
        1.  Aap 'Profile' par aayenge. "Last Updated:" mein time aa jaayega.
        2.  Aap "Go to Edit Screen" button dabayenge.
        3.  Aap "Go Back" button dabayenge.
        4.  Aap 'Profile' par wapas aayenge. "Last Updated:" mein time **fir se update** ho jaayega (kyunki `useFocusEffect` dubara chala). Agar `useEffect` hota, toh time update nahi hota.

8.  **🐞 Common beginner mistakes:**

      * `useFocusEffect` ko `useCallback` ke bina use karna. Isse performance issues ho sakti hain.
      * `useFocusEffect` ko `useEffect` ki jagah har jagah use karna. (Nahi\! Agar data sirf ek baar (mount par) laana hai, toh `useEffect` hi best hai. `useFocusEffect` thoda "heavy" hai).

9.  **🌍 Real-world example / use-case:**

      * Twitter feed: Har baar 'Home' tab par aane par naye tweets fetch karna.
      * Bank App: 'Balance' screen par har baar aane par balance refresh karna.

10. **✅ Quick checklist / TL;DR:**

      * Screen *har baar* focus hone par code chalaana? `useFocusEffect`.
      * Screen *sirf ek baar* load hone par code chalaana? `useEffect`.
      * `useFocusEffect` ko hamesha `useCallback` mein wrap karo.

11. **❓ FAQs:**

      * **Q: `useEffect` vs `useFocusEffect`?**
      * A: `useEffect` component lifecycle (mount/unmount) par chalta hai. `useFocusEffect` navigation state (focus/blur) par chalta hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `useFocusEffect(useCallback(...))` ko `useEffect(...)` (bina `useCallback`) se badal kar dekho.
    2.  Ab 'Edit Profile' par jaakar wapas aao. Dekho, "Last Updated" time change *nahi* hoga.

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: useFocusEffect](https://reactnavigation.org/docs/use-focus-effect/)
	  
=============================================================
	  

# MODULE-9 → Advanced Navigation (React Navigation)

## 9.1: Tab Navigator (Bottom tabs)

1.  **🎯 Title / Short Summary:** `createBottomTabNavigator` - Instagram jaise Bottom Tabs Banana.

2.  **🤔 Kya hai? (What?):** Yeh React Navigation ka ek navigator hai jo screen ke neeche (bottom) mein Taps-based navigation (jaise Home, Search, Profile) banata hai.

3.  **💡 Kyun important hai? (Why?):** Yeh mobile apps (iOS aur Android) ka sabse common navigation pattern hai. Yeh user ko app ke main sections mein ek click par switch karne deta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapki app mein 3 se 5 *main* (aur equal importance waale) sections hon.
      * Jaise: Home, Search, Reels, Profile.
      * Isse user hamesha app ke main structure ko dekh sakta hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar aapke 5 main sections hain aur aapne Stack Navigator use kiya, toh user ko ek section (e.g., Profile) se doosre (e.g., Home) par jaane ke liye 4-5 baar "back" button dabana padega, jo bahut bura User Experience (UX) hai. 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Aapko `npm install @react-navigation/bottom-tabs` install karna hoga.
    2.  `createBottomTabNavigator` ko import karein.
    3.  Ek `Tab` object banayein (`const Tab = createBottomTabNavigator();`).
    4.  `Stack.Navigator` ki tarah, `Tab.Navigator` use karein.
    5.  `Stack.Screen` ki tarah, `Tab.Screen` use karein.
    6.  **Icons:** Sabse important, har `Tab.Screen` ko `options` prop mein `tabBarIcon` dena padta hai, jo icon dikhata hai.

7.  **💻 Code example:**

    ```javascript
    // Pehle install karein:
    // npm install @react-navigation/bottom-tabs
    // npm install react-native-vector-icons (Icons ke liye)

    import React from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
    import Icon from 'react-native-vector-icons/Ionicons'; // Icon library

    // Dummy Screens
    function HomeScreen() { /* ... */ }
    function SearchScreen() { /* ... */ }
    function ProfileScreen() { /* ... */ }

    // 1. Tab navigator banana
    const Tab = createBottomTabNavigator();

    export default function App() {
      return (
        <NavigationContainer>
          {/* 2. Tab Navigator ko render karna */}
          <Tab.Navigator
            // 3. Poore navigator ke liye default options
            screenOptions={({ route }) => ({
              // 4. Har tab ke liye icon set karna
              tabBarIcon: ({ focused, color, size }) => {
                let iconName;

                if (route.name === 'Home') {
                  iconName = focused ? 'home' : 'home-outline';
                } else if (route.name === 'Search') {
                  iconName = focused ? 'search' : 'search-outline';
                } else if (route.name === 'Profile') {
                  iconName = focused ? 'person' : 'person-outline';
                }

                // 5. Icon component ko return karna
                return <Icon name={iconName} size={size} color={color} />;
              },
              // 6. Active (focused) tab ka color
              tabBarActiveTintColor: 'tomato',
              tabBarInactiveTintColor: 'gray',
            })}
          >
            {/* 7. Screens ko define karna */}
            <Tab.Screen name="Home" component={HomeScreen} />
            <Tab.Screen name="Search" component={SearchScreen} />
            <Tab.Screen name="Profile" component={ProfileScreen} />
          </Tab.Navigator>
        </NavigationContainer>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const Tab = createBottomTabNavigator();`: Humne tab navigator factory banayi.
          * `screenOptions={({ route }) => ({ ... }`: Hum `Tab.Navigator` ko bata rahe hain ki *har* screen ke liye yeh options default hain. Yeh ek function leta hai jismein `route` milta hai.
          * `tabBarIcon: ({ focused, color, size }) => { ... }`: Yeh function icon set karne ke liye hai. `focused` (boolean) batata hai ki tab active hai ya nahi.
          * `if (route.name === 'Home') { ... }`: Hum route ke naam ke basis par decide kar rahe hain ki kaunsa icon (e.g., `home` ya `home-outline`) dikhana hai.
          * `return <Icon ... />;`: Icon component return kar rahe hain.
          * `tabBarActiveTintColor: 'tomato'`: Active tab 'tomato' color ki hogi.
          * `<Tab.Screen ... />`: Hum apni screens ko tabs ke roop mein register kar rahe hain.
      * **🚀 Quick run expected output:** Screen ke neeche 3 tabs (Home, Search, Profile) dikhenge jinke icons honge. Active tab 'tomato' color ka hoga.

8.  **🐞 Common beginner mistakes:**

      * `tabBarIcon` prop set na karna (icons nahi dikhenge).
      * `react-native-vector-icons` (ya koi aur icon library) ko install aur setup na karna.
      * `screenOptions` mein `route` ko destructure karna bhool jaana.
        Example `Note 11` (Syllabus): Yeh Stack se alag hai. Stack ek ke upar ek screen rakhta hai (back jaa sakte hain), Tab side-by-side rakhta hai (switch kar sakte hain).

9.  **🌍 Real-world example / use-case:**

      * **Instagram:** Home, Search, Reels, Shop, Profile tabs.
      * **WhatsApp:** Chats, Status, Calls (Yeh top tabs hain, par concept same hai).
      * **Spotify:** Home, Search, Library.

10. **✅ Quick checklist / TL;DR:**

      * 3-5 main sections ke liye use hota hai.
      * `npm install @react-navigation/bottom-tabs`
      * `tabBarIcon` prop sabse zaroori hai.

11. **❓ FAQs:**

      * **Q: 5 se zyada tabs rakh sakte hain?**
      * A: Rakh sakte hain, par woh mobile screen par fit nahi honge aur UX kharab karenge. 5 max hai.
      * **Q: Har tab ka header (title) kaise chupayein?**
      * A: `screenOptions={{ headerShown: false }}` set karke.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein ek chautha tab "Notifications" add karo.
    2.  Uska icon `notifications` ya `notifications-outline` set karo.

13. **📚 Further reading / commands / links:**

      * `npm install @react-navigation/bottom-tabs`
      * [React Navigation Docs: Bottom Tab Navigator](https://reactnavigation.org/docs/bottom-tab-navigator)

-----

## 9.2: Drawer Navigator (Side menu)

1.  **🎯 Title / Short Summary:** `createDrawerNavigator` - Gmail/Slack jaisa Side Menu Banana.

2.  **🤔 Kya hai? (What?):** Yeh React Navigation ka ek navigator hai jo screen ke left (ya right) se swipe karne par ek "drawer" (menu) kholta hai.

3.  **💡 Kyun important hai? (Why?):** Yeh un links (screens) ke liye perfect hai jo *zaroori* toh hain, par *hamesha* screen par nahi dikhne chahiye (jaise "Settings", "Logout", "About Us").

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapke paas 5 se zyada navigation items hon.
      * Jab items "main" (jaise Home) na hokar "secondary" (jaise Settings, Logout, Help) hon.
      * Jab aapko Tab Bar ki jagah bachaani ho.
      * Yeh `Note 11` (Syllabus) ka point hai: Tab (main sections) vs Drawer (secondary sections).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar aapne 8 items (Home, Profile, Settings, Logout, Help, etc.) ko Bottom Tab mein daal diya, toh woh poori tarah toot jaayega aur unusable hoga. 🛑
      * Aapko secondary items (jaise "Settings") ko zabardasti "Home" screen ke andar kahin button bana kar daalna padega, jo aachi practice nahi hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Aapko `npm install @react-navigation/drawer` aur uski dependencies (`react-native-gesture-handler`, `react-native-reanimated`) install karni hongi.
    2.  `createDrawerNavigator` ko import karein.
    3.  Ek `Drawer` object banayein (`const Drawer = createDrawerNavigator();`).
    4.  `Drawer.Navigator` aur `Drawer.Screen` ka istemaal karein.
    5.  Yeh automatically header mein ek "hamburger" icon (≡) add kar deta hai jisse drawer khulta hai.

7.  **💻 Code example:**

    ```javascript
    // Pehle install karein:
    // npm install @react-navigation/drawer
    // npm install react-native-gesture-handler react-native-reanimated

    // babel.config.js mein 'react-native-reanimated/plugin' add karna na bhoolein!

    import React from 'react';
    import { View, Text, Button } from 'react-native';
    import { NavigationContainer } from '@react-navigation/native';
    import { createDrawerNavigator } from '@react-navigation/drawer';
    import { useNavigation } from '@react-navigation/native'; // Header button ke liye

    // Dummy Screens
    function HomeScreen() {
      const navigation = useNavigation();
      return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Text>Home Screen</Text>
          {/* Header mein button manually add kar sakte hain (agar zaroorat ho) */}
          <Button title="Drawer Kholo" onPress={() => navigation.openDrawer()} />
        </View>
      );
    }

    function SettingsScreen() { /* ... */ }
    function LogoutScreen() { /* ... */ }

    // 1. Drawer navigator banana
    const Drawer = createDrawerNavigator();

    export default function App() {
      return (
        <NavigationContainer>
          {/* 2. Drawer Navigator ko render karna */}
          <Drawer.Navigator
            // 3. Default mein Home Screen dikhegi
            initialRouteName="Home"
            screenOptions={{
              // drawerActiveTintColor: 'blue',
            }}
          >
            {/* 4. Screens ko define karna */}
            <Drawer.Screen 
              name="Home" 
              component={HomeScreen} 
              options={{ title: 'Dashboard' }} // Header title
            />
            <Drawer.Screen 
              name="Settings" 
              component={SettingsScreen} 
            />
            {/* 5. Custom component se bhi screen ban sakti hai */}
            <Drawer.Screen 
              name="Logout" 
              component={LogoutScreen} 
              options={{ drawerLabel: 'Sign Out' }} // Menu mein alag naam
            />
          </Drawer.Navigator>
        </NavigationContainer>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `// npm install ...reanimated`: Yeh 2 libraries (gesture-handler aur reanimated) Drawer ke animation (slide effect) ke liye **bahut zaroori** hain.
          * `const Drawer = createDrawerNavigator();`: Humne drawer factory banayi.
          * `navigation.openDrawer()`: Yeh function (jo `useNavigation` se milta hai) code se drawer kholne ke kaam aata hai.
          * `<Drawer.Navigator ...>`: Navigator ko render kiya.
          * `<Drawer.Screen name="Home" ... />`: Screens ko register kiya.
          * `options={{ title: 'Dashboard' }}`: Isse 'Home' screen ka *header* title 'Dashboard' dikhega.
          * `options={{ drawerLabel: 'Sign Out' }}`: Isse 'Logout' screen ka *menu mein* jo naam hai, woh 'Sign Out' dikhega.
      * **🚀 Quick run expected output:** Screen par "Home Screen" dikhegi. Top-left mein ek hamburger icon (≡) hoga. Use dabane par (ya left se swipe karne par) ek menu khulega jismein 'Dashboard', 'Settings', aur 'Sign Out' likha hoga.

8.  **🐞 Common beginner mistakes:**

      * `react-native-gesture-handler` aur `react-native-reanimated` ko install na karna (ya `babel.config.js` mein plugin add na karna). Iske bina app **seedha crash** ho jaayegi. 🛑
      * Yeh sochna ki Drawer aur Stack ek doosre ki jagah le sakte hain. (Nahi, yeh dono alag-alag kaam karte hain aur aksar *ek saath* (nested) use hote hain).

9.  **🌍 Real-world example / use-case:**

      * **Gmail:** Left-swipe karke 'Inbox', 'Sent', 'Spam', 'Settings' ka menu kholna.
      * **Slack:** Workspaces (servers) ke beech switch karne ke liye.
      * Koi bhi app jismein 'Settings', 'Profile', 'Logout' jaise secondary links hon.

10. **✅ Quick checklist / TL;DR:**

      * Secondary items (Settings, Logout) ke liye use hota hai.
      * `npm install @react-navigation/drawer`
      * `reanimated` aur `gesture-handler` (dependencies) **zaroori** hain.

11. **❓ FAQs:**

      * **Q: Kya Drawer aur Bottom Tab ek saath use kar sakte hain?**
      * A: Haan\! Yeh bahut common pattern hai. Module 9.3 (Nested) mein dekhenge.
      * **Q: Drawer ko right side se kaise kholein?**
      * A: `Drawer.Navigator` par prop `drawerPosition="right"` set karke.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein "Help" aur "About Us" naam ki 2 aur dummy screens add karo.
    2.  "About Us" screen ka `drawerLabel` badal kar "Company Info" karke dekho.

13. **📚 Further reading / commands / links:**

      * `npm install @react-navigation/drawer react-native-gesture-handler react-native-reanimated`
      * [React Navigation Docs: Drawer Navigator](https://www.google.com/search?q=httpsmatop://reactnavigation.org/docs/drawer-navigator)

-----

## 9.3: Nested Navigation (Stack ke andar Tabs, etc.)

1.  **🎯 Title / Short Summary:** Nested Navigation - Navigators ke andar Navigators.

2.  **🤔 Kya hai? (What?):** Yeh ek navigator (e.g., Tab Navigator) ko ek doosre navigator (e.g., Stack Navigator) ki *screen* ke roop mein istemaal karne ka concept hai.

3.  **💡 Kyun important hai? (Why?):** Asli apps simple nahi hoti. Aapko aksar dono (Stack aur Tab) ki power ek saath chahiye hoti hai.

      * **Example:** Aap 'Home' tab par hain. Aap ek post par click karte hain. Ab aapko 'Post Details' screen par jaana hai. Yeh 'Post Details' screen tab ke *upar* aani chahiye (poori screen par) aur usmein back button hona chahiye. Yeh "Stack" behavior hai.
      * Isko solve karne ke liye hum *har tab ke andar* ek Stack Navigator rakhte hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko Tab Navigator ki screens se *aur aage* drill-down (deep) jaana ho (e.g., Home -\> Post Details).
      * Jab aapko Drawer Navigator ki screens se *aur aage* jaana ho (e.g., Settings (drawer) -\> Edit Profile (stack)).
      * **Common Pattern:** Stack (main) ke andar Tabs. Ya Tabs ke andar Stacks. (Dono common hain).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar aapne nesting nahi ki, toh 'Post Details' screen bhi ek *tab* ban jaayegi, aur user ko Bottom Tabs (Home, Search, Details) dikhenge. Yeh bahut ajeeb lagega.
      * Ya fir 'Post Details' screen poore Tab Navigator ko replace kar degi (Bottom Tabs gayab ho jaayenge), jo user ko confuse kar dega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Pattern: Tabs ke andar Stacks** (Sabse common)

    1.  Har Tab (Home, Search) ke liye ek alag Stack Navigator banao.
    2.  `HomeStack` mein 2 screens hongi: `HomeScreen` aur `PostDetailsScreen`.
    3.  `SearchStack` mein 1 screen hogi: `SearchScreen`.
    4.  Fir ek `TabNavigator` banao.
    5.  `Tab.Screen` mein `component` prop mein `HomeScreen` (Screen) dene ki bajaye, `HomeStack` (Navigator) de do.

7.  **💻 Code example (Har Tab ke andar ek Stack):**

    ```javascript
    import React from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
    import { createNativeStackNavigator } from '@react-navigation/native-stack';

    // (Dummy screens)
    function HomeScreen({ navigation }) { /* ... <Button title="Post Par Jao" onPress={() => navigation.navigate('PostDetails')} /> ... */ }
    function PostDetailsScreen() { /* ... */ }
    function SearchScreen() { /* ... */ }

    // 1. Stacks banana (Har tab ke liye ek)
    const Stack = createNativeStackNavigator();

    function HomeStack() {
      return (
        <Stack.Navigator>
          <Stack.Screen name="HomeFeed" component={HomeScreen} options={{ title: 'Home' }} />
          <Stack.Screen name="PostDetails" component={PostDetailsScreen} />
        </Stack.Navigator>
      );
    }

    function SearchStack() {
      return (
        <Stack.Navigator>
          <Stack.Screen name="SearchPage" component={SearchScreen} options={{ title: 'Search' }}/>
        </Stack.Navigator>
      );
    }

    // 2. Tab Navigator banana
    const Tab = createBottomTabNavigator();

    export default function App() {
      return (
        <NavigationContainer>
          {/* 3. Tab Navigator mein Stacks ko 'component' ke roop mein daalna */}
          <Tab.Navigator
            screenOptions={{
              headerShown: false, // ⚠️ Zaroori: Taaki 2 header na dikhein
              // (tabBarIcon logic yahan...)
            }}
          >
            {/* 'component' mein poora 'HomeStack' daal diya */}
            <Tab.Screen name="Home" component={HomeStack} />
            
            {/* 'component' mein poora 'SearchStack' daal diya */}
            <Tab.Screen name="Search" component={SearchStack} />
          </Tab.Navigator>
        </NavigationContainer>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `function HomeStack()`: Yeh ek *component* hai jo `Stack.Navigator` return karta hai. Ismein 'HomeFeed' aur 'PostDetails' screens hain.
          * `function SearchStack()`: Yeh doosra component hai jo `Stack.Navigator` return karta hai.
          * `screenOptions={{ headerShown: false }}`: Yeh **bahut zaroori** hai. `Tab.Navigator` ka header hum chupa rahe hain, taaki *sirf* andar waale `Stack.Navigator` (e.g., `HomeStack`) ka header dikhe. Agar yeh `false` nahi kiya toh 2 header (double header) dikhenge.
          * `<Tab.Screen name="Home" component={HomeStack} />`: Yahi magic hai. Humne `Tab.Screen` ke `component` prop ko `HomeScreen` (component) dene ki bajaye `HomeStack` (navigator component) diya hai.
      * **🚀 Quick run expected output:** App khulegi, 'Home' tab active hoga, header mein 'Home' likha hoga. 'Post Par Jao' button dabane par 'PostDetails' screen aayegi (bottom tabs *wahi* rahenge) aur header mein back button (stack behaviour) aa jaayega.

8.  **🐞 Common beginner mistakes:**

      * `headerShown: false` (Tab Navigator par) set na karna aur "Double Header" ki problem mein phas jaana.
      * Header ko kahan control karein, ismein confuse hona. (Rule: Jo navigator *andar* (child) hai (Stack), woh header control karega).
      * `navigation.navigate()` ko galat navigator se call karna.

9.  **🌍 Real-world example / use-case:**

      * **Har Badi App:** Instagram, Twitter, LinkedIn, Uber... har app nested navigation use karti hai.
      * **Instagram:** 'Home' tab (Stack) -\> 'Profile' (Stack.Screen) -\> 'Followers' (Stack.Screen).

10. **✅ Quick checklist / TL;DR:**

      * Yeh "Navigator ke andar Navigator" hai.
      * Common pattern: `Tab.Screen` ke `component` mein poora `Stack.Navigator` daal dena.
      * `headerShown: false` (outer navigator par) set karna yaad rakho.

11. **❓ FAQs:**

      * **Q: Kitne levels nest kar sakte hain?**
      * A: Jitne marzi, par 3-4 level se zyada complex ho jaata hai aur performance par asar pad sakta hai.
      * **Q: Ek tab se doosre tab ke *andar* ki screen par kaise navigate karein?**
      * A: `navigation.navigate('Search', { screen: 'SearchDetails' })` se. (Advanced).

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein "Profile" naam ka teesra tab add karo.
    2.  Uske liye `ProfileStack` banao jismein 2 screens hon: `ProfilePage` aur `EditProfile`.

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: Nesting Navigators](https://reactnavigation.org/docs/nesting-navigators)

-----

## 9.4: Authentication Flow (Login/Signup ke baad app flow)

1.  **🎯 Title / Short Summary:** Authentication Flow - Login/Signup aur Main App ko Alag Karna.

2.  **🤔 Kya hai? (What?):** Yeh ek pattern hai jismein hum "Authentication" screens (Login, Signup) ko "Main App" screens (Home, Profile) se poori tarah alag rakhte hain, aur user ke 'logged in' state ke basis par decide karte hain ki kaunsa group dikhana hai.

3.  **💡 Kyun important hai? (Why?):**

      * **Security:** Yeh ensure karta hai ki bina login ke user *kisi bhi haalat mein* 'Home' ya 'Profile' screen ko access na kar paaye.
      * **Cleanliness:** Login/Signup ka flow (Stack) aapke main app (Tab/Drawer) flow se alag rehta hai.
      * **UX:** Login karne ke baad, user ko 'Login' screen par wapas 'back' nahi jaana chahiye. Flow poora clear hona chahiye.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Hamesha.** Har app jismein login/signup hai, usko yeh flow use karna chahiye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User login karke 'Home' par aayega, aur agar woh phone ka back button dabayega, toh woh wapas 'Login' screen par chala jaayega (jabki woh logged in hai\!). 🛑 Yeh bahut bura UX hai.
      * Aapko har screen par check karna padega `if (userIsLoggedIn)` warna app crash ho sakti hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Ek global state (Context ya Redux se) banate hain jo batata hai `isUserLoggedIn` (true/false).
    2.  2 alag-alag Stack Navigators banate hain:
          * `AuthStack` (ismein: Login, Signup, ForgotPassword screens).
          * `AppStack` (ismein: Main Tab/Drawer Navigator).
    3.  `App.js` mein (ya top-level par) `NavigationContainer` ke *andar* ek `if` condition lagate hain:
          * `if (isUserLoggedIn === true)` -\> `AppStack` dikhao.
          * `if (isUserLoggedIn === false)` -\> `AuthStack` dikhao.
    4.  Jab user login karta hai, hum `isUserLoggedIn` ko `true` set kar dete hain. React apne aap `AuthStack` ko hata dega aur `AppStack` dikha dega.

7.  **💻 Code example (Using Context):**

    ```javascript
    import React, { useState, useContext, createContext } from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    import { createNativeStackNavigator } from '@react-navigation/native-stack';
    // (Dummy screens... LoginScreen, HomeScreen, TabNavigator, etc.)

    // 1. Auth Context banana (Module 8.2)
    const AuthContext = createContext();

    // 2. Auth Provider banana
    function AuthProvider({ children }) {
      const [isLoggedIn, setIsLoggedIn] = useState(false);

      const login = () => setIsLoggedIn(true);
      const logout = () => setIsLoggedIn(false);

      return (
        <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
          {children}
        </AuthContext.Provider>
      );
    }

    // 3. Stacks banana
    const Stack = createNativeStackNavigator();

    // Yeh screens tab dikhengi jab user login NAHI hai
    function AuthStack() {
      // const { login } = useContext(AuthContext); // (LoginScreen mein use hoga)
      return (
        <Stack.Navigator>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Signup" component={SignupScreen} />
        </Stack.Navigator>
      );
    }

    // Yeh screens tab dikhengi jab user login HAI
    function AppStack() {
      // (Yahan aapka poora Tab/Drawer Navigator ho sakta hai)
      return (
        <Stack.Navigator>
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="Profile" component={ProfileScreen} />
        </Stack.Navigator>
      );
    }

    // 4. Root Navigator (Jo choose karega)
    function RootNavigator() {
      // 5. State (isLoggedIn) ko Context se lena
      const { isLoggedIn } = useContext(AuthContext);

      return (
        <NavigationContainer>
          {/* 6. Condition ke basis par Stack badalna */}
          {isLoggedIn ? <AppStack /> : <AuthStack />}
        </NavigationContainer>
      );
    }

    // 7. Final App
    export default function App() {
      return (
        // Poori app ko Provider se wrap karna
        <AuthProvider>
          <RootNavigator />
        </AuthProvider>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `AuthContext` aur `AuthProvider`: Humne ek global state banaya (jaisa Module 8.2 mein seekha) `isLoggedIn` ko store karne ke liye.
          * `AuthProvider`: Ismein `login` aur `logout` functions hain jo state badalte hain.
          * `AuthStack`: Sirf Login/Signup screens ka group.
          * `AppStack`: Main app (Home/Profile) screens ka group.
          * `RootNavigator`: Yeh component `AuthContext` se `isLoggedIn` ki value leta hai.
          * `NavigationContainer`: Container ko `RootNavigator` ke andar rakha.
          * `{isLoggedIn ? <AppStack /> : <AuthStack />}`: Yahi hai poora magic. Yeh JavaScript ka ternary operator hai. "Agar `isLoggedIn` true hai, toh `<AppStack />` dikhao, varna (else) `<AuthStack />` dikhao."
          * `export default function App()`: Final app `AuthProvider` se shuru hoti hai.
      * **🚀 Quick run expected output:** App khulegi, `isLoggedIn` false hoga, `AuthStack` dikhega (Login screen). Login button (jo `login()` call karega) dabane par, `isLoggedIn` true hoga, React re-render hoga, aur user ko `AppStack` (Home screen) dikhegi.

8.  **🐞 Common beginner mistakes:**

      * Conditional logic ko `NavigationContainer` ke *bahar* laga dena. (Logic hamesha container ke *andar* hona chahiye).
      * `isLoggedIn` state ko `App.js` mein (local state) rakhna aur Context/Redux use na karna, jisse `login` function ko props se neeche bhejte-bhejte "prop drilling" ho jaati hai.
      * Login karne ke baad `navigation.navigate('Home')` karna (jisse back jaane par Login screen aa jaati hai). Sahi tareeka state badalna hai.

9.  **🌍 Real-world example / use-case:**

      * Har app jismein Login hai (Facebook, Uber, Swiggy) 100% yahi pattern use karti hai.

10. **✅ Quick checklist / TL;DR:**

      * `isLoggedIn` state (Context/Redux) banao.
      * 2 alag stack banao: `AuthStack` (Login) aur `AppStack` (Home).
      * `NavigationContainer` ke andar `if (isLoggedIn)` logic se dono mein se ek dikhao.

11. **❓ FAQs:**

      * **Q: Bina Context ke kar sakte hain?**
      * A: Haan, Redux se kar sakte hain. Ya local `useState` se bhi, par Context sabse saaf tareeka hai.
      * **Q: Loading (Splash) screen kahan daalein?**
      * A: `isLoggedIn` ki initial value `null` (loading) rakho. Fir 3 conditions check karo: `if (loading) <SplashScreen />`, `else if (isLoggedIn) <AppStack />`, `else <AuthStack />`.

12. **🏋️‍♀️ Practice exercise:**

    1.  `LoginScreen` (jo `AuthStack` mein hai) mein ek button banao.
    2.  `onPress` par `useContext(AuthContext)` se `login` function ko call karo.
    3.  Dekho ki button dabaate hi poora Stack (Auth se App) badal jaata hai.

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: Authentication flows](https://reactnavigation.org/docs/auth-flow)

-----

## 9.5: Deep Linking (Link se app kholna)

1.  **🎯 Title / Short Summary:** Deep Linking - Website/Notification Link se App Kholna.

2.  **🤔 Kya hai? (What?):** Deep Linking woh process hai jisse ek URL (jaise `myapp://user/123` ya `https://my-app.com/user/123`) user ko seedha aapki app ke *andar* ek specific screen (e.g., User 123 ki profile) par le jaata hai.

3.  **💡 Kyun important hai? (Why?):** Yeh app engagement ke liye *critical* hai.

      * **Notifications:** Push notification (e.g., "Aapko naya message aaya hai") par click karke user seedha *uss* chat screen par jaana chahta hai, na ki Home screen par.
      * **Marketing:** Aap 'Forgot Password' email bhejte hain. Link par click karke seedha app ki 'Reset Password' screen khulni chahiye.
      * **Web-to-App:** Agar user mobile browser par aapki website (e.g., `my-app.com/post/456`) kholta hai, toh app usse pooch sakti hai "App mein kholna hai?".

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aap Push Notifications bhej rahe hon.
      * Jab aapki app ka website version bhi ho.
      * Jab aap email/SMS se marketing kar rahe hon.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User notification par click karega aur app ki Home screen par land karega. Fir usko manually uss chat/post ko dhoondhna padega. User confuse aur irritate ho jaayega. 🛑
      * Aap "web-to-app" ka faayda nahi utha paayenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    React Navigation mein yeh 2 hisson mein hota hai:

    1.  **React Native Side (JS):**
          * `NavigationContainer` ko ek `linking` prop dena padta hai.
          * `linking` prop mein aap ek configuration object (prefixes aur config) dete hain.
          * `prefixes`: Batata hai ki aapki app kaun se URL schemes (e.g., `myapp://`) sunti hai.
          * `config`: Batata hai ki URL ka kaunsa hissa (e.g., `/user/:id`) app ki kaun si screen (e.g., `Profile`) se map hoga.
    2.  **Native Side (Android/iOS):**
          * **Android:** Aapko `AndroidManifest.xml` mein 'Intent Filter' add karna padta hai taaki OS ko pata chale ki `myapp://` URLs ko aapki app par bhejna hai.
          * **iOS:** Aapko Xcode mein 'URL Types' set karna padta hai.
            *(Note: Hum yahan JS part par focus karenge).*

7.  **💻 Code example (JS Side):**

    ```javascript
    import React from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    import { createNativeStackNavigator } from '@react-navigation/native-stack';

    // (Dummy Screens: HomeScreen, ProfileScreen)
    // ProfileScreen 'route.params.id' expect karegi

    const Stack = createNativeStackNavigator();

    // 1. Linking Configuration
    const linkingConfig = {
      // 2. Prefixes (App ki schemes)
      prefixes: [
        'myapp://', // Custom scheme
        'https://app.my-app.com' // Website (Universal Link)
      ],
      
      // 3. Mapping (URL se Screen)
      config: {
        // App ki screens ka structure
        screens: {
          Home: 'home', // 'myapp://home' -> Home screen
          
          Profile: {
            path: 'user/:id', // 'myapp://user/123'
            parse: {
              id: (id) => `User-${id}`, // (Optional) Param ko parse kar sakte hain
            },
          },
          
          Settings: 'settings',
          
          NotFound: '*', // Agar koi link match na ho
        },
      },
    };

    function App() {
      return (
        // 4. Config ko 'linking' prop mein paas karna
        <NavigationContainer linking={linkingConfig} fallback={<Text>Loading...</Text>}>
          <Stack.Navigator>
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Profile" component={ProfileScreen} />
            <Stack.Screen name="Settings" component={SettingsScreen} />
            <Stack.Screen name="NotFound" component={NotFoundScreen} />
          </Stack.Navigator>
        </NavigationContainer>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const linkingConfig = { ... }`: Humne config object banaya.
          * `prefixes: ['myapp://', ...]`: Humne OS ko bataya ki 'myapp://' se shuru hone wale links hamare hain.
          * `config: { screens: { ... } }`: Humne URL aur Screens ki mapping ki.
          * `Home: 'home'`: Iska matlab hai ki `myapp://home` URL `Home` screen ko kholega.
          * `Profile: { path: 'user/:id' }`: Yaha magic hai. `user/` ke baad jo bhi aayega (e.g., `123`), woh `:id` parameter maan liya jaayega.
          * `myapp://user/123` URL `Profile` screen kholega aur `route.params` mein `{ id: '123' }` bhej dega.
          * `NotFound: '*'`: Wildcard route, agar kuch match na ho.
          * `<NavigationContainer linking={linkingConfig} ...>`: Humne `NavigationContainer` ko linking config se jod diya.
      * **🚀 Quick run expected output:**
          * App band hai.
          * Agar user `myapp://user/456` URL (e.g., SMS se) click karta hai.
          * OS user se poochega "Open in 'My App'?".
          * User "Yes" karega.
          * App khulegi aur *seedha* 'Profile' screen dikhayegi, jismein `route.params.id` ki value "456" (ya "User-456" agar parse use kiya) hogi.

8.  **🐞 Common beginner mistakes:**

      * Sirf JS side (linking config) setup karna aur Native side (`AndroidManifest.xml`) ko bhool jaana. (Yeh kaam nahi karega).
      * `prefixes` mein galat scheme (e.g., `http://` ki jagah `https://`) likh dena.
      * `path` mein parameter `:id` likhna par Screen (e.g., `ProfileScreen`) mein `route.params.id` ko handle na karna.

9.  **🌍 Real-world example / use-case:**

      * **Push Notification:** Notification payload mein `myapp://chat/789` bhejna.
      * **Forgot Password:** Email mein `https://app.my-app.com/reset-password/TOKEN123` link bhejna.

10. **✅ Quick checklist / TL;DR:**

      * Deep linking URL se app ki specific screen kholta hai.
      * JS Side: `NavigationContainer` ko `linking` prop (prefixes + config) chahiye.
      * Native Side: `AndroidManifest.xml` (Android) / `URL Types` (iOS) setup zaroori hai.

11. **❓ FAQs:**

      * **Q: Custom scheme (`myapp://`) vs Universal Link (`https://`)?**
      * A: `https://` (Universal Links / App Links) better hain, kyunki agar app install nahi hai, toh link browser mein website khol dega. `myapp://` tabhi kaam karega jab app installed hai (varna error aayega).
      * **Q: App khuli ho toh kaise handle karein?**
      * A: React Navigation isko automatically handle karta hai. Agar app khuli hai, toh `navigation.navigate()` ho jaayega; agar band hai, toh app khul kar seedha uss screen par jaayegi.

12. **🏋️‍♀️ Practice exercise:**

    1.  (Setup mushkil hai, par concept samjho). Apne `linkingConfig` mein `Settings` screen (jo `myapp://settings` se khule) ko map karo.
    2.  Android Emulator mein, terminal se yeh command chala kar test karo:
        `adb shell am start -W -a android.intent.action.VIEW -d "myapp://settings"`

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: Deep Linking](https://reactnavigation.org/docs/deep-linking)
      * [React Navigation Docs: Server Setup (Universal Links)](https://www.google.com/search?q=https://reactnavigation.org/docs/server-integration)

-----

## 9.6: Navigation Optimization (Keep-Alive Screens)

1.  **🎯 Title / Short Summary:** Navigation Optimization (`@react-navigation/bottom-tabs` ki Optimization).

2.  **🤔 Kya hai? (What?):** Syllabus mein `Note 36` (Navigation Optimization) `Bottom Tabs` (Note 11) se related hai. Yeh `BottomTabNavigator` ka default behavior hai ki jab aap ek tab se doosre par jaate hain, toh puraani tab "unmount" (destroy) *nahi* hoti. Woh "zinda" (keep-alive) rehti hai.

3.  **💡 Kyun important hai? (Why?):** **Performance aur UX\!**

      * **UX:** Imagine 'Home' tab par aapne 50 posts scroll kiye. Fir aap 'Search' tab par gaye (kuch search karne) aur wapas 'Home' tab par aaye. Agar 'Home' screen "keep-alive" *nahi* hoti, toh woh *fir se load* hoti aur aapko scroll position (top) par fek deti. 🛑
      * **Performance:** Screen ko baar-baar destroy aur re-create karne se performance kharab hoti hai.
      * `BottomTabNavigator` is problem ko default mein hi solve kar deta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * `createBottomTabNavigator` yeh "keep-alive" behavior **default mein deta hai.**
      * `Stack.Navigator` yeh behavior **default mein *nahi* deta** (jab aap back jaate hain, screen destroy ho jaati hai).
      * `Drawer.Navigator` bhi default mein "keep-alive" rakhta hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * (Yeh default hai, par agar yeh *na* hota, jaisa ki `createMaterialTopTabNavigator` mein hota hai):
      * User tab switch karke wapas aane par apni scroll position kho deta.
      * Screen ka state (e.g., `useState` mein data) reset ho jaata.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

      * `BottomTabNavigator` default mein `unmountOnBlur` prop ko `false` set karke rakhta hai.
      * `unmountOnBlur: false` (Default): Jab tab 'blur' (focus se hate) ho, toh use destroy (unmount) *mat* karo. Use zinda (keep-alive) rakho.
      * `unmountOnBlur: true` (Optional): Agar aapko *zabardasti* tab ko reset karwana hai (e.g., 'Search' tab par wapas aane par hamesha khali search bar dikhe), toh aap yeh prop `true` set kar sakte hain.

7.  **💻 Code example (Default vs Force Unmount):**

    ```javascript
    import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
    // (Dummy Screens: HomeScreen, SearchScreen)

    const Tab = createBottomTabNavigator();

    function MyTabs() {
      return (
        <Tab.Navigator>
          
          {/* BEHAVIOR 1: Default (Keep-Alive) */}
          {/* Aap Home par scroll karo, Search par jao, wapas Home par aao. */}
          {/* Scroll position WAHIN rahegi. ✅ */}
          <Tab.Screen 
            name="Home" 
            component={HomeScreen} 
          />

          {/* BEHAVIOR 2: Force Unmount (Reset) */}
          {/* Aap Search mein kuch type karo, Home par jao, wapas Search par aao. */}
          {/* Text GAYAB ho jaayega (kyunki component reset ho gaya). 🛑 */}
          <Tab.Screen 
            name="Search" 
            component={SearchScreen}
            // 1. Optimization ko manually 'off' karna
            options={{
              unmountOnBlur: true,
            }}
          />

        </Tab.Navigator>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `<Tab.Screen name="Home" ... />`: Ismein `unmountOnBlur` `false` (default) hai. Screen "keep-alive" rahegi.
          * `options={{ unmountOnBlur: true }}`: Humne `Search` screen ko bataya ki "jaise hi user is tab se hate (blur), is component ko memory se poora delete (unmount) kar dena".
      * **🚀 Quick run expected output:**
          * 'Home' tab (jo ek `FlatList` hai) ko scroll karo. 'Search' par jao. Wapas 'Home' par aao. Scroll position save rahegi.
          * 'Search' tab (jo ek `TextInput` hai) mein kuch type karo. 'Home' par jao. Wapas 'Search' par aao. `TextInput` khali ho jaayega.

8.  **🐞 Common beginner mistakes:**

      * Yeh na samajhna ki `BottomTabNavigator` (default: keep-alive) aur `StackNavigator` (default: destroy on back) alag-alag behave karte hain.
      * `unmountOnBlur: true` ko har jagah laga dena (performance barbaad karna) ya ise `false` set karne ki koshish karna (jo default hai).

9.  **🌍 Real-world example / use-case:**

      * **(Default behavior):** Instagram Home feed ki scroll position yaad rakhna.
      * **(`unmountOnBlur: true`):** Bank app ka "Transfer" tab. Aap wapas aao toh form reset ho jaana chahiye (security ke liye).

10. **✅ Quick checklist / TL;DR:**

      * `BottomTabNavigator` aur `DrawerNavigator` screens ko default mein "keep-alive" rakhte hain (state/scroll save rehta hai).
      * `StackNavigator` screens ko 'back' karne par destroy kar deta hai.
      * `unmountOnBlur: true` se aap "keep-alive" ko band kar sakte hain.

11. **❓ FAQs:**

      * **Q: `Stack.Navigator` ko "keep-alive" kaise karein?**
      * A: `BottomTabNavigator` ki tarah default support nahi hai. Aapko `react-navigation-stack` ki jagah `react-native-screens` (jo ab default hai) ka `replace` ya `push` use karna padta hai, ya fir `@react-navigation/stack` (community) mein `screenOptions={{ detachPreviousScreen: false }}` (jo experimental hai) use karna padta hai. Generally, Stack mein "keep-alive" nahi karte.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `SearchScreen` se `unmountOnBlur: true` hata do.
    2.  Ab `TextInput` mein type karke tabs switch karo. Dekho, ab text save (keep-alive) rehta hai.

13. **📚 Further reading / commands / links:**

      * [React Navigation Docs: `unmountOnBlur` (Bottom Tabs)](https://www.google.com/search?q=%5Bhttps://reactnavigation.org/docs/bottom-tab-navigator%23unmountonblur%5D\(https://reactnavigation.org/docs/bottom-tab-navigator%23unmountonblur\))
	  
=============================================================

# MODULE-10 → Professional State Management

## 10.1: Redux Toolkit (Modern Redux, `configureStore`, `createSlice`)

1.  **🎯 Title / Short Summary:** Redux Toolkit (RTK) - Complex Global State ko Aasani se Manage Karna.

2.  **🤔 Kya hai? (What?):** Redux Toolkit (RTK) Redux use karne ka **aaj ke time ka, official, aur aasan tareeka** hai. Yeh "purane Redux" ke bahut saare complex setup (boilerplate code) ko hata deta hai.

3.  **💡 Kyun important hai? (Why?):** Redux ek "global state container" hai. Yeh aapki app ka saara zaroori data (jaise User Info, Cart Items) ek "central store" (global variable) mein rakhta hai. `Note 31` (Syllabus) kehta hai ki yeh `Context API` (Module 8.2) ka powerful version hai. RTK ke `createSlice` se state update karna *bahut* aasan ho jaata hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapka global state **complex** ho (e.g., shopping cart, user settings, notifications).
      * Jab state logic (business logic) ko component se *bilkul* alag rakhna ho.
      * Jab `useContext` se performance issues aane lagein (kyunki Context re-render karta hai, RTK nahi karta).
      * Jab aapko state ke saath-saath *async* (API calls) logic bhi manage karna ho (`createAsyncThunk`).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap `useContext` aur `useState` se ek badi app manage karne ki koshish karenge, jisse aapka code "spaghetti code" (uljha hua) ban jaayega.
      * Ek component ka state doosre ko paas karne mein "prop drilling" karte-karte pareshan ho jaayenge.
      * State update ka logic har component mein bikhra hoga.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    RTK mein 3 main cheezein hoti hain:

    1.  **`configureStore` (Store Banana):** Yeh aapka central "dabba" (store) banata hai. Yeh `createStore` ka naya version hai jo automatically dev tools setup kar deta hai.
    2.  **`createSlice` (State ka Tukda):** Yeh magic hai\! 🎩 Ek "slice" (tukda) state ke ek hisse ko manage karta hai.
          * `name`: Slice ka naam (e.g., 'cart', 'user').
          * `initialState`: Shuru mein state kaisa dikhega (e.g., `{ items: [] }`).
          * `reducers`: Yeh *functions* hain jo state ko update karte hain (e.g., `addItemToCart`). RTK yahan "Immer" library use karta hai, jisse aap state ko *seedha* badal sakte hain (jaise `state.items.push(newItem)`), jo purane Redux mein allowed nahi tha.
    3.  **`Provider` aur `useSelector`/`useDispatch` (Use Karna):**
          * `<Provider store={store}>`: Poori app ko store se connect karna (Same as Context).
          * `useSelector((state) => state.cart.items)`: Store se data *read* (select) karna.
          * `useDispatch()`: Ek "action" (e.g., `addItemToCart(newItem)`) *dispatch* (bhejna) taaki state update ho.

7.  **💻 Code example (Simple Cart Slice):**

    ```javascript
    // Pehle install karein:
    // npm install @reduxjs/toolkit react-redux

    // 1. Slice Banao (features/cartSlice.js)
    import { createSlice } from '@reduxjs/toolkit';

    const cartSlice = createSlice({
      name: 'cart',
      initialState: {
        items: [], // Shuru mein cart khali
        total: 0,
      },
      // State badalne waale functions
      reducers: {
        addItem: (state, action) => {
          // RTK (Immer) ki vajah se hum seedha push kar sakte hain!
          const newItem = action.payload; // Jo item humne bheja
          state.items.push(newItem);
          state.total += newItem.price;
        },
        removeItem: (state, action) => {
          const itemIdToRemove = action.payload.id;
          // (Logic to find and remove item...)
          state.items = state.items.filter(item => item.id !== itemIdToRemove);
          // (Logic to update total...)
        },
      },
    });

    // Actions ko export karna (components mein use karne ke liye)
    export const { addItem, removeItem } = cartSlice.actions;
    // Reducer ko export karna (store mein jodne ke liye)
    export default cartSlice.reducer;

    // ---
    // 2. Store Banao (store.js)
    import { configureStore } from '@reduxjs/toolkit';
    import cartReducer from './features/cartSlice'; // Slice se reducer import kiya

    export const store = configureStore({
      reducer: {
        // Yahan saare slices ke reducers aayenge
        cart: cartReducer,
        // user: userReducer, (agar hota toh)
      },
    });

    // ---
    // 3. Provider Lagao (App.js)
    import React from 'react';
    import { Provider } from 'react-redux';
    import { store } from './store';
    // import MyAppComponent from './MyAppComponent';

    export default function App() {
      return (
        <Provider store={store}>
          <MyAppComponent />
        </Provider>
      );
    }

    // ---
    // 4. Component mein Use Karo (MyAppComponent.js)
    import React from 'react';
    import { View, Text, Button } from 'react-native';
    import { useSelector, useDispatch } from 'react-redux';
    import { addItem } from './features/cartSlice'; // Action import kiya

    function MyAppComponent() {
      // Store se data 'select' karna
      const cartItems = useSelector((state) => state.cart.items);
      const cartTotal = useSelector((state) => state.cart.total);

      // Action 'dispatch' (bhejne) ke liye setup
      const dispatch = useDispatch();

      const handleAddItem = () => {
        const newItem = { id: 1, name: 'Apple', price: 10 };
        // Action ko dispatch karna (payload ke saath)
        dispatch(addItem(newItem));
      };

      return (
        <View>
          <Text>Cart Items: {cartItems.length}</Text>
          <Text>Total Price: {cartTotal}</Text>
          <Button title="Add Apple" onPress={handleAddItem} />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `createSlice({...})`: State ka ek tukda (cart) define kiya, uska `initialState` bataya, aur `reducers` (functions `addItem`, `removeItem`) bataye.
          * `export const { addItem } = cartSlice.actions;`: `createSlice` ne `addItem` action creator (function) hamare liye bana diya, humne use export kar diya.
          * `configureStore({...})`: Ek global store banaya aur usko bataya ki `cart` naam ki state ko `cartReducer` handle karega.
          * `<Provider store={store}>`: Poori app ko Redux store se connect kar diya.
          * `useSelector((state) => state.cart.items)`: Component ne `useSelector` se store ke state mein se `cart.items` ko nikaal liya.
          * `const dispatch = useDispatch();`: Humne action bhejne waala "dispatch" function liya.
          * `dispatch(addItem(newItem));`: Humne `addItem` action (payload `newItem` ke saath) ko dispatch kiya. Redux ne isko `cartSlice` ke `addItem` reducer tak pahunchaya aur state update ho gaya.
      * **🚀 Quick run expected output:** Screen par "Cart Items: 0", "Total Price: 0" aur ek button dikhega. Button dabane par values "Cart Items: 1", "Total Price: 10" ho jaayengi.

8.  **🐞 Common beginner mistakes:**

      * `useSelector` mein poora state (`state`) return kar dena. (Sirf zaroori data `state.cart.items` return karein, varna har cheez change hone par component re-render hoga).
      * Reducer mein `action.payload` ko use karna bhool jaana.
      * Slice ke reducer ko `configureStore` mein register karna bhool jaana.
      * State ko "mutate" (seedha change) karne ki koshish karna (Waise RTK `Immer` se ise allow karta hai, par purane Redux mein yeh sabse bada paap tha).

9.  **🌍 Real-world example / use-case:**

      * Ek e-commerce app ka "Shopping Cart".
      * Ek music app ka "Now Playing" queue aur settings.
      * App-wide "User Authentication" state (user logged in hai ya nahi).

10. **✅ Quick checklist / TL;DR:**

      * RTK Redux ka naya, aasan tareeka hai.
      * `createSlice`: State + Reducers ek jagah.
      * `configureStore`: Sab slices ko jodkar store banana.
      * `Provider`: App ko connect karna.
      * `useSelector`: Data padhna.
      * `useDispatch`: Action bhejkar data badalna.

11. **❓ FAQs:**

      * **Q: RTK vs Purana Redux?**
      * A: RTK mein 90% kam code (boilerplate) likhna padta hai. `createSlice` sabkuch (actions, reducers) khud bana deta hai.
      * **Q: RTK vs Context API?** (Note 31)
      * A: Context simple data (jaise Theme) ke liye best hai. RTK complex data, performance, aur async logic (API calls ke liye `RTK Query` ya `createAsyncThunk`) ke liye bana hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `removeItem` ka logic poora karo.
    2.  Ek naya 'Remove' button banao jo `dispatch(removeItem({id: 1}))` call kare.

13. **📚 Further reading / commands / links:**

      * `npm install @reduxjs/toolkit react-redux`
      * [Redux Toolkit Official Docs](https://redux-toolkit.js.org/)

-----

## 10.2: React Query / TanStack Query (Server state, caching, fetching)

1.  **🎯 Title / Short Summary:** TanStack Query (React Query) - Server State ko Fetch, Cache, aur Sync Karna.

2.  **🤔 Kya hai? (What?):** Yeh ek "server-state" management library hai. Yeh global state (Redux) se alag hai. Iska kaam **API se data laana, use cache (yaad) rakhna, aur background mein update karte rehna** hai, taaki aapka data hamesha fresh rahe.

3.  **💡 Kyun important hai? (Why?):** Hum `useEffect` aur `useState` (`const [loading, setLoading]...`) use karke API calls karte hain. React Query yeh saara "boilerplate" (loading, error, data states) *hata* deta hai. Yeh automatically caching, background refresh, aur retry (fail hone par) handle karta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab bhi aapko app mein API se data (GET request) fetch karna ho.
      * Jab aapko data ko "stale" (baasi) hone se bachana ho (e.g., background mein refresh).
      * Jab aapko API calls retry karwani ho (network fail par).
      * Jab aapko data cache karna ho (taaki user screen par wapas aaye toh *turant* purana data dikhe, aur background mein naya fetch ho).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap har component mein `useState` (for `data`), `useState` (for `loading`), `useState` (for `error`), aur `useEffect` (for `fetch`) ka code copy-paste karte rahenge. 🛑
      * Aapko manual caching (AsyncStorage?), retry logic (try-catch loop?), aur background refresh (`useFocusEffect`?) ka complex code khud likhna padega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  **`QueryClientProvider`:** Poori app ko isse wrap karte hain (Jaise Redux Provider).
    2.  **`useQuery` (Data Fetch/GET):** Yeh Hook API se data fetch karne ke liye hai.
          * `queryKey`: Ek unique key (string ya array) jo is data ko pehchaanti hai (e.g., `['todos']` ya `['post', 1]`).
          * `queryFn`: Ek async function jo *actually* data fetch karta hai (e.g., `fetchTodos`).
          * **Return Karta hai:** `data`, `isLoading`, `isError`, `error`, `isSuccess`... (saare states).
    3.  **`useMutation` (Data Change/POST/PUT/PATCH):** Yeh Hook server par data *badalne* (create, update, delete) ke liye hai.
          * `mutationFn`: Ek async function jo data change karta hai (e.g., `createNewPost`).
          * **Return Karta hai:** `mutate` function (jise call karke mutation start karte hain), `isLoading`, `isSuccess`.

7.  **💻 Code example (`useQuery` & `useMutation`):**

    ```javascript
    // Pehle install karein:
    // npm install @tanstack/react-query

    import React from 'react';
    import { QueryClient, QueryClientProvider, useQuery, useMutation } from '@tanstack/react-query';
    import { View, Text, Button, ActivityIndicator, FlatList } from 'react-native';

    // 1. Client banana
    const queryClient = new QueryClient();

    // --- API Functions (alag file mein) ---
    const fetchTodos = async () => {
      console.log("🚀 API call... fetching todos");
      const res = await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5');
      return res.json();
    };

    const createTodo = async (newTodo) => {
      console.log("🚀 API call... creating todo");
      // (Fake POST request logic)
      return { ...newTodo, id: Math.random() }; 
    };

    // --- Component ---
    function TodoComponent() {
      // 2. useQuery se data fetch karna
      const { data: todos, isLoading, isError, error } = useQuery({
        queryKey: ['todos'], // Is data ki unique key
        queryFn: fetchTodos, // Data laane waala function
        // staleTime: 1000 * 60, // 1 min tak data ko fresh maano
      });

      // 3. useMutation se data change karna
      const { mutate: addTodo, isPending: isAddingTodo } = useMutation({
        mutationFn: createTodo,
        // 4. Success hone par:
        onSuccess: () => {
          // 'todos' key waale data ko invalidate (purana) declare karo
          // Taaki React Query use automatic REFETCH kare
          queryClient.invalidateQueries({ queryKey: ['todos'] });
        },
      });

      // --- Render logic ---
      if (isLoading) return <ActivityIndicator />;
      if (isError) return <Text>Error: {error.message}</Text>;

      return (
        <View>
          <Button 
            title={isAddingTodo ? "Adding..." : "Add New Todo"}
            onPress={() => {
              // 5. Mutate function ko call karna
              addTodo({ title: 'New Task', completed: false });
            }}
          />
          <FlatList
            data={todos}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => <Text>{item.title}</Text>}
          />
        </View>
      );
    }

    // --- App (Provider ke saath) ---
    export default function App() {
      return (
        // 1. Provider se wrap karna
        <QueryClientProvider client={queryClient}>
          <TodoComponent />
        </QueryClientProvider>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const queryClient = new QueryClient()`: React Query ka engine banaya.
          * `<QueryClientProvider client={queryClient}>`: Poori app ko engine se connect kiya.
          * `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })`: Humne kaha "data lao". Key hai `['todos']` aur function hai `fetchTodos`. React Query ne `isLoading`, `data` etc. sab de diya.
          * `useMutation({ mutationFn: createTodo, ... })`: Humne kaha "data badalne ki taiyari karo". Function hai `createTodo`.
          * `onSuccess: () => { queryClient.invalidateQueries(...) }`: **Yeh sabse important hai.** Jab naya todo *successfully* add ho jaaye, toh hum React Query ko bolte hain ki `['todos']` waala data "baasi" (stale/invalid) ho gaya hai, use *dubara fetch* karke lao.
          * `addTodo({ title: 'New Task' })`: Button dabane par humne `mutate` function (`addTodo`) ko call kiya.
      * **🚀 Quick run expected output:**
        1.  App khulegi, `ActivityIndicator` dikhega.
        2.  `fetchTodos` call hoga (console mein log aayega), 5 todos ki list dikhegi.
        3.  Aap "Add New Todo" dabayenge. Button "Adding..." ho jaayega.
        4.  `createTodo` call hoga.
        5.  `onSuccess` trigger hoga. `invalidateQueries` call hoga.
        6.  React Query *automatic* `fetchTodos` ko *dubara* call karega.
        7.  List refresh ho jaayegi (waise is example mein fake API hai, par real mein list update ho jaati).

8.  **🐞 Common beginner mistakes:**

      * `useQuery` ko `useEffect` ke andar daalna. (Nahi\! `useQuery` top level par rehta hai).
      * `queryKey` ko dynamic na banana (e.g., `['post', 1]` ki jagah hamesha `['post']` use karna, jisse har post ki detail par same data dikhe).
      * `useMutation` ke `onSuccess` mein `invalidateQueries` ko call *nahi* karna, jisse data add/delete hone ke baad bhi screen par purana data dikhta rehta hai.
      * **React Query ko Redux/Zustand se confuse karna.**

9.  **🌍 Real-world example / use-case:**

      * **(Redux/Zustand):** Theme (dark/light), Navigation state, User settings (jo server par nahi hain). Yeh **Client State** hai.
      * **(React Query):** User's Profile data, Twitter feed, Product list. Yeh **Server State** hai.
      * **Aksar dono saath mein use hote hain.**

10. **✅ Quick checklist / TL;DR:**

      * React Query (TanStack Query) **Server State** (API data) ke liye hai.
      * Yeh `useEffect` + `useState` (loading, error) ko replace karta hai.
      * `useQuery` = Data laana (GET).
      * `useMutation` = Data badalna (POST/PUT).
      * `invalidateQueries` = Data ko refresh karwana.

11. **❓ FAQs:**

      * **Q: Toh Redux (RTK) ki zaroorat hi nahi hai?**
      * A: Zaroorat hai. Redux *Client State* (App ka internal state) ke liye hai. React Query *Server State* (API se aaya data) ke liye hai.
      * **Q: Yeh data kahan cache karta hai?**
      * A: In-memory (RAM) mein. App band karke kholne par cache chala jaata hai (uske liye `redux-persist` jaisi cheez alag se lagani padti hai, ya RTK Query mein `rehydration`).

12. **🏋️‍♀️ Practice exercise:**

    1.  `useQuery` mein `staleTime: 5000` (5 second) add karo.
    2.  `fetchTodos` ke `console.log` ko dekho. App load par chalega.
    3.  Screen se hat kar wapas aao (within 5 sec). Log *nahi* aayega (cache se aaya). 5 sec baad aao, log *fir se* aayega (refresh).

13. **📚 Further reading / commands / links:**

      * `npm install @tanstack/react-query`
      * [TanStack Query Docs](https://tanstack.com/query/latest)

-----

## 10.3: `Zustand` (Halka-phulka global state manager)

1.  **🎯 Title / Short Summary:** Zustand 🐻 - Redux ka Simple, Halka-Phulka (Lightweight) Alternative.

2.  **🤔 Kya hai? (What?):** Zustand ek *bahut* chota, simple, aur fast global state management solution hai. Yeh Redux ki tarah 'central store' ka concept deta hai, par bina `Provider`, bina `dispatch`, aur bina "reducers" ke.

3.  **💡 Kyun important hai? (Why?):** Yeh `Context API` se zyada powerful hai (re-render optimize karta hai) aur `Redux` se 100 guna *aasan* hai. Ismein `Provider` se wrap karne ka jhanjhat hi nahi hai. Aap seedha hook (`useStore`) call karo aur state use karo.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko Redux *bahut* complex (bhaari) lage.
      * Jab aapko `Context API` se performance issues aa rahi hon (Context ke update hone par sab children re-render hote hain).
      * Choti se medium size apps ke liye yeh *perfect* hai.
      * Jab aapko Redux ke "boilerplate" (reducers, actions, dispatch) se nafrat ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap ya toh `Context API` se ladte rahenge (performance optimize karne ke liye) ya Redux ka poora bhaari setup karte baithenge, jabki aapka kaam 10 line ke Zustand store se ho sakta tha.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  `npm install zustand`.
    2.  `create` function se ek "store" (jo asal mein ek custom hook hai) banao.
    3.  Is `create` function mein aap `initialState` aur state *badalne waale functions* (jaise `increment`) ek saath define karte ho.
    4.  Bas\! Ab kisi bhi component mein is hook ko call karo.
    5.  `Provider` ki zaroorat **nahi** hai.

7.  **💻 Code example (Simple Counter):**

    ```javascript
    // Pehle install karein:
    // npm install zustand

    import React from 'react';
    import { View, Text, Button } from 'react-native';
    import { create } from 'zustand'; // Sirf 'create' import karna hai

    // 1. Store/Hook banana (store.js)
    // 'set' function state ko merge/update karta hai
    export const useCounterStore = create((set) => ({
      // 2. Initial State
      count: 0,
      
      // 3. Actions (State badalne waale functions)
      increment: () => {
        set((state) => ({ count: state.count + 1 }));
      },
      
      reset: () => {
        set({ count: 0 }); // Seedha state bhi set kar sakte hain
      },
      
      multiplyBy: (number) => {
        set((state) => ({ count: state.count * number }));
      }
    }));

    // ---
    // Component 1 (App.js)
    function CounterControls() {
      // 4. Hook se 'actions' ko nikaalna
      // Hum 'count' ko yahan nahi nikaal rahe (optimization)
      const increment = useCounterStore((state) => state.increment);
      const multiplyBy = useCounterStore((state) => state.multiplyBy);

      return (
        <View>
          <Button title="Increment" onPress={increment} />
          <Button title="Multiply by 2" onPress={() => multiplyBy(2)} />
        </View>
      );
    }

    // Component 2 (ChildComponent.js)
    function CounterDisplay() {
      // 4. Hook se 'state' ko nikaalna
      // Yeh component sirf 'count' par depend karta hai
      const count = useCounterStore((state) => state.count);

      return <Text style={{ fontSize: 30 }}>Count: {count}</Text>;
    }

    // Main App
    export default function App() {
      // 5. ⚠️ Dekho! Koi <Provider> nahi hai!
      return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <CounterDisplay />
          <CounterControls />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `import { create } from 'zustand'`: Zustand se `create` function liya.
          * `export const useCounterStore = create((set) => ({ ... }))`: Humne `useCounterStore` naam ka ek hook banaya. `create` humein `set` function deta hai.
          * `count: 0`: Initial state.
          * `increment: () => set((state) => ({ count: state.count + 1 }))`: `increment` naam ka function banaya jo `set` function ko call karke state update karta hai.
          * `const increment = useCounterStore((state) => state.increment);`: `CounterControls` ne *sirf* `increment` function nikaala.
          * `const count = useCounterStore((state) => state.count);`: `CounterDisplay` ne *sirf* `count` nikaala.
          * **Optimization:** Jab `increment` button dabta hai, `count` badalta hai. Zustand *sirf* `CounterDisplay` ko re-render karega (kyunki woh `count` par depend karta hai). `CounterControls` re-render **nahi** hoga (kyunki woh `increment` function par depend karta hai, jo change nahi hua). Yeh Context API se behtar hai.
      * **🚀 Quick run expected output:** Screen par "Count: 0" aur 2 buttons. "Increment" dabane par count badhega.

8.  **🐞 Common beginner mistakes:**

      * `useCounterStore()` (poora state) nikaal lena. (Galat 🛑). Hamesha selector use karo `useCounterStore((state) => state.count)`. Agar poora state nikaaloge toh optimization khatam ho jaayegi.
      * `set` function ko `async` samajhna. (Yeh sync hai).
      * `create` ke andar `useState` ya `useEffect` use karne ki koshish karna. (Nahi, yeh plain JS object hai).

9.  **🌍 Real-world example / use-case:**

      * (Note 31) Yeh Redux, Context, aur Zustand teeno hi "Client State" ke liye hain.
      * Choti app mein "Theme" (Dark/Light) manage karne ke liye.
      * Modal (popup) ka "open/close" state globally manage karne ke liye.

10. **✅ Quick checklist / TL;DR:**

      * Zustand = Simple Global State.
      * Koi `Provider` nahi.
      * `create` se hook banao.
      * Component mein hook ko *selector* ke saath call karo (e.g., `useStore(state => state.count)`).

11. **❓ FAQs:**

      * **Q: Zustand vs Redux?** (Note 31)
      * A: Zustand 1KB ka hai, Redux Toolkit \~13KB. Zustand mein koi boilerplate nahi, Redux mein hai. Redux mein behtar devtools (time travel debugging) hain. Choti apps ke liye Zustand, badi (enterprise) apps ke liye Redux.
      * **Q: Zustand vs Context?** (Note 31)
      * A: Zustand "selector" ki vajah se faltu re-renders ko rokta hai. Context mein agar ek value badalti hai, toh sabhi consumer re-render hote hain (jise `useMemo` se a\_apko\_ optimize karna padta hai).

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `reset` function ko `CounterControls` component mein use karo (ek "Reset" button bana kar).

13. **📚 Further reading / commands / links:**

      * `npm install zustand`
      * [Zustand GitHub (Docs)](https://github.com/pmndrs/zustand)

-----

## 10.4: `Context API` (Advanced) (Note 31)

*(Note: Hum Module 8.2 mein `useContext` ka basic cover kar chuke hain. Yahan hum `Note 31` ke hisaab se use Redux/Zustand se compare karenge aur "Advanced" patterns dekhenge.)*

1.  **🎯 Title / Short Summary:** Context API (Advanced) - State ko Optimize Karna.

2.  **🤔 Kya hai? (What?):** Yeh React ka built-in tareeka hai "prop drilling" se bachne ka. Advanced pattern mein hum seekhte hain ki Context se hone waale "unnecessary re-renders" ko kaise rokein.

3.  **💡 Kyun important hai? (Why?):** Basic `useContext` (Module 8.2) kaafi hai, lekin jab Context ki `value` (e.g., ek object jismein `state` aur `dispatch` dono hain) update hoti hai, toh us Context ko *use* karne waale *saare* components re-render ho jaate hain, bhale hi unhe uss badli hui value se matlab na ho.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko Redux/Zustand jaisi 3rd party library use *nahi* karni.
      * Jab aapka global state *simple* ho (e.g., Theme, User Info).
      * **Advanced Pattern:** Jab aap performance optimize karna chahte hon, tab aap 'State' aur 'Dispatch' ko *do alag Contexts* mein tod dete hain.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar `Note 31` ke baaki options (Redux, Zustand) use kiye, toh koi problem nahi.
      * Agar sirf Basic Context (Module 8.2) ko complex state ke liye use kiya, toh aapki app *slow* ho jaayegi (performance issues) kyunki sabkuch baar-baar re-render hoga.

6.  **🧑‍🏫 Step-by-step explanation (Advanced Pattern: Splitting Context):**
    **Problem:**

    ```js
    // Basic (Bad)
    const [state, setState] = useState(0);
    // Value mein 'state' (jo badalta hai) aur 'setState' (jo nahi badalta) dono hain
    return <MyContext.Provider value={{ state, setState }}>
    ```

    Jab `state` badlega, `value` object naya banega, aur woh components bhi re-render honge jo *sirf* `setState` (function) use kar rahe the.
    **Solution (Advanced):**

    1.  Do Context banao: `StateContext` (sirf data ke liye) aur `DispatchContext` (sirf functions ke liye).
    2.  Dono ke `Provider` se app wrap karo.
    3.  Jo component *sirf data dikhata hai*, woh `useContext(StateContext)` use kare.
    4.  Jo component *sirf data badalta hai*, woh `useContext(DispatchContext)` use kare.
    5.  Ab data change hone par, sirf data dikhane waale components hi re-render honge\! 🚀

7.  **💻 Code example (Advanced Pattern):**

    ```javascript
    import React, { createContext, useContext, useReducer } from 'react';
    // (useReducer, useState ka advanced version hai jo Context ke saath acha kaam karta hai)

    // 1. Do alag Context banana
    const CounterStateContext = createContext();
    const CounterDispatchContext = createContext();

    // 2. Reducer (State logic)
    function counterReducer(state, action) {
      switch (action.type) {
        case 'increment': return { count: state.count + 1 };
        default: throw new Error('Unknown action');
      }
    }

    // 3. Provider Component (Jo dono ko provide kare)
    function CounterProvider({ children }) {
      const [state, dispatch] = useReducer(counterReducer, { count: 0 });

      return (
        <CounterStateContext.Provider value={state}>
          <CounterDispatchContext.Provider value={dispatch}>
            {children}
          </CounterDispatchContext.Provider>
        </CounterStateContext.Provider>
      );
    }

    // --- Components ---
    function CounterDisplay() {
      // 4. Yeh sirf 'State' context use karta hai
      const state = useContext(CounterStateContext);
      console.log("Render: Display"); // Yeh re-render hoga
      return <Text>Count: {state.count}</Text>;
    }

    function CounterControls() {
      // 5. Yeh sirf 'Dispatch' context use karta hai
      const dispatch = useContext(CounterDispatchContext);
      console.log("Render: Controls"); // Yeh re-render NAHI hoga
      
      return (
        <Button 
          title="Increment" 
          onPress={() => dispatch({ type: 'increment' })} 
        />
      );
    }

    // 6. App
    export default function App() {
      return (
        <CounterProvider>
          <CounterDisplay />
          <CounterControls />
        </CounterProvider>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `CounterStateContext` & `CounterDispatchContext`: Do alag "dabbe" banaye.
          * `CounterProvider`: Ek component banaya jo dono `Provider` ko rakhta hai. `StateContext` ko `state` (data) diya, `DispatchContext` ko `dispatch` (function) diya.
          * `CounterDisplay`: Sirf `StateContext` se `state` liya.
          * `CounterControls`: Sirf `DispatchContext` se `dispatch` (function) liya.
          * **Result:** Jab `Button` dabega, `dispatch` call hoga, `state` badlega. `CounterDisplay` (jo `state` par depend karta hai) re-render hoga. Lekin `CounterControls` (jo `dispatch` par depend karta hai, aur `dispatch` function *change nahi hota*) re-render **nahi** hoga. Humne performance optimize kar di\!
      * **🚀 Quick run expected output:** Screen par "Count: 0" aur button. Button dabane par Count badhega. Console mein *sirf* "Render: Display" log hoga (har click par), "Render: Controls" *sirf ek baar* (shuru mein) log hoga.

8.  **🐞 Common beginner mistakes:**

      * Basic Context (Module 8.2) ko hi sabkuch (state + functions) `value={{...}}` mein daal dena, jisse har render par naya object banta hai aur sabkuch re-render hota hai.
      * (Note 31) Context ko Redux/Zustand se compare na kar paana.

9.  **🌍 Real-world example / use-case:**

      * Yeh pattern `useReducer` + `useContext` Redux ka "mini" version banane ke liye use hota hai, bina 3rd party library ke.

10. **✅ Quick checklist / TL;DR:**

      * Context API built-in hai, library nahi.
      * Performance issue: Default mein sab re-render hota hai.
      * Solution: State aur Dispatch (functions) ko *do alag-alag Context* mein split (tod) do.

11. **❓ FAQs:**

      * **Q: Toh yeh Redux/Zustand se behtar hai?**
      * A: (Note 31) Nahi. Zustand isse aasan hai (kyunki selector hai). Redux isse powerful hai (devtools, async middleware). Yeh "beech" ka raasta hai jab aapko library nahi chahiye.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein "decrement" action add karo (`counterReducer` mein `case 'decrement'`).
    2.  `CounterControls` mein ek naya "Decrement" button banao jo `dispatch({ type: 'decrement' })` call kare.

13. **📚 Further reading / commands / links:**

      * [React Docs: Scaling up with Reducer and Context](https://react.dev/learn/scaling-up-with-reducer-and-context)

-----

## 10.5: `Persistent State` (`redux-persist`)

1.  **🎯 Title / Short Summary:** `redux-persist` - Redux/Zustand State ko Phone par Save Karna.

2.  **🤔 Kya hai? (What?):** `redux-persist` (ya Zustand ka 'persist' middleware) ek library hai jo aapke global state (e.g., Redux store) ko *automatic* phone ki storage (`AsyncStorage`) mein save kar deti hai.

3.  **💡 Kyun important hai? (Why?):** **Problem:** Redux, Zustand, Context sab data 'in-memory' (RAM) mein rakhte hain. Jab user app ko *band karke dubara kholta hai*, toh saara state (e.g., cart, settings) **reset** (gayab) ho jaata hai\! 🛑
    **Solution:** `redux-persist` state ko `AsyncStorage` (phone ki disk) par save karta hai, aur jab app dubara khulti hai, toh us saved data ko *wapas* Redux store mein daal deta hai ("Rehydration").

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko global state (Theme, Cart, User Token) ko app restart hone ke baad bhi *yaad* rakhwana ho.
      * (Note 31) Yeh `AsyncStorage` (Module 6.8) ko Redux/Zustand (Module 10) se jodta hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User aapki app mein Dark Mode set karega. App band karke kholega, Light Mode ho jaayega.
      * User cart mein 5 item daalega. App band karke kholega, cart khali ho jaayega.
      * User login karega. App band karke kholega, woh logged out ho jaayega. (Bahut bura UX).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Redux Toolkit ke saath):**

    1.  `npm install redux-persist` aur `npm install @react-native-async-storage/async-storage`.
    2.  `redux-persist` ko `AsyncStorage` (storage engine) ke baare mein batana.
    3.  `persistConfig` object banana (jismein `key`, `storage`, aur 'whitelist'/'blacklist' batate hain ki kya save karna hai).
    4.  `configureStore` mein `reducer` ko `persistReducer` se wrap (lapetna) karna.
    5.  `redux-persist/integration/react` se `PersistGate` component nikaalna.
    6.  App ko `<Provider>` ke *andar* `<PersistGate>` se wrap karna. (PersistGate app ko tab tak "loading" state mein rakhta hai jab tak storage se data load na ho jaaye).

7.  **💻 Code example (RTK + redux-persist):**

    ```javascript
    // Pehle install karein:
    // npm install redux-persist @react-native-async-storage/async-storage

    // 1. (store.js) - Jahan 'configureStore' hai
    import { configureStore, combineReducers } from '@reduxjs/toolkit';
    import { 
      persistStore, 
      persistReducer,
      FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER // (Serializability errors se bachne ke liye)
    } from 'redux-persist';
    import AsyncStorage from '@react-native-async-storage/async-storage';
    import cartReducer from './features/cartSlice';
    // import userReducer from './features/userSlice';

    // 1. Saare reducers ko combine karna (agar 1 se zyada hain)
    const rootReducer = combineReducers({
      cart: cartReducer,
      // user: userReducer,
    });

    // 2. Persist Config banana
    const persistConfig = {
      key: 'root', // Storage mein 'root' key ke andar data save hoga
      storage: AsyncStorage, // Hum 'AsyncStorage' use kar rahe hain
      whitelist: ['cart', 'user'], // Sirf 'cart' aur 'user' slice ko save karo
      // blacklist: ['navigation'], // 'navigation' ko save MAT karo
    };

    // 3. Reducer ko 'persistReducer' se wrap karna
    const persistedReducer = persistReducer(persistConfig, rootReducer);

    // 4. Store ko 'persistedReducer' se banana
    export const store = configureStore({
      reducer: persistedReducer,
      // (Serializability errors se bachne ke liye middleware)
      middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
          serializableCheck: {
            ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
          },
        }),
    });

    // 5. 'persistor' banana
    export const persistor = persistStore(store);

    // ---
    // 6. (App.js) - Jahan 'Provider' hai
    import React from 'react';
    import { Provider } from 'react-redux';
    import { PersistGate } from 'redux-persist/integration/react'; // 👈 Naya component
    import { store, persistor } from './store'; // Dono ko import kiya
    import MyAppComponent from './MyAppComponent';
    import { ActivityIndicator } from 'react-native';

    export default function App() {
      return (
        <Provider store={store}>
          {/* 7. App ko 'PersistGate' se wrap karna */}
          <PersistGate 
            loading={<ActivityIndicator />} // Jab tak data load ho raha hai
            persistor={persistor} // Persistor ko paas kiya
          >
            <MyAppComponent />
          </Par
        </Provider>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `combineReducers`: `redux-persist` ko ek single 'root' reducer chahiye hota hai, isliye hum `combineReducers` se saare slices (cart, user) ko jod dete hain.
          * `persistConfig`: Humne config banayi. `key: 'root'` (storage mein key). `storage: AsyncStorage` (storage engine). `whitelist: ['cart']` (sabse zaroori: "Sirf cart slice ko save karna, baaki ko nahi").
          * `persistedReducer`: Humne apne main `rootReducer` ko `persistConfig` ke saath "wrap" kar diya.
          * `store = configureStore({ reducer: persistedReducer, ... })`: Humne store ko normal reducer ki jagah *wrapped* (persisted) reducer se banaya.
          * `middleware: ...`: Yeh extra code `redux-persist` ke non-serializable actions (FLUSH, REHYDRATE) ki warning ko ignore karne ke liye zaroori hai.
          * `persistor = persistStore(store)`: Humne store se `persistor` object banaya.
          * `PersistGate`: Yeh component app ko "pause" kar deta hai.
          * `loading={<ActivityIndicator />}`: Jab tak `AsyncStorage` se data load hokar Redux store mein *wapas* (rehydrate) nahi aa jaata, tab tak loading spinner dikhao.
          * `persistor={persistor}`: `PersistGate` ko `persistor` se connect kiya.
      * **🚀 Quick run expected output:**
        1.  App chalao, "Add Apple" (pichle example se) button dabao. Cart mein 1 item aa gaya.
        2.  App ko **poora band (kill) karo** aur dubara kholo.
        3.  Ek second ke liye `ActivityIndicator` (loading) dikhega.
        4.  App khulegi aur "Cart Items: 1" *pehlese hi* dikhega\! ✅ Data save ho gaya tha.

8.  **🐞 Common beginner mistakes:**

      * `PersistGate` ko `Provider` ke *bahar* laga dena. (Galat\! Yeh `Provider` ke andar aata hai).
      * `whitelist` ya `blacklist` set na karna. (Default mein poora store persist ho jaata hai, jismein forms ya navigation ka temporary state bhi ho sakta hai, jo hum nahi chahte).
      * `AsyncStorage` ko install na karna.

9.  **🌍 Real-world example / use-case:**

      * **(Note 31):** Redux, Zustand, Context state managers hain. `AsyncStorage` (Note 6.8, 30) data storage hai. `redux-persist` in dono ke beech ka *bridge* (pul) hai.
      * User ka Login Token (JWT) persist karna (taaki app band karke kholne par woh logged in rahe).
      * User ki app settings (e.g., `isDarkMode: true`) ko persist karna.

10. **✅ Quick checklist / TL;DR:**

      * Yeh Redux state ko `AsyncStorage` mein save karta hai.
      * `persistReducer` se reducer wrap karo.
      * `PersistGate` se app component wrap karo.
      * `whitelist` se batao ki *kya* save karna hai.

11. **❓ FAQs:**

      * **Q: Zustand ke saath kaise karein?**
      * A: Zustand mein yeh aur bhi aasan hai. `create` ke saath `persist` middleware use karna hota hai. [Zustand Docs](https://www.google.com/search?q=https://github.com/pmndrs/zustand/wiki/Persist-middleware)
      * **Q: Kya yeh `SecureStorage` (Note 6.10) use kar sakta hai?**
      * A: Haan\! Agar aapko sensitive data (jaise user token) save karna hai, toh `storage: AsyncStorage` ki jagah `storage: secureStorage` (custom banakar) de sakte hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne `persistConfig` mein `user` slice (agar banaya ho) ko `whitelist` karke dekho.
    2.  `whitelist` se `cart` ko hata kar dekho. Ab app restart karne par cart data gayab ho jaayega.

13. **📚 Further reading / commands / links:**

      * `npm install redux-persist @react-native-async-storage/async-storage`
      * [Redux Persist Docs](https://github.com/rt2zz/redux-persist)
	  
	  
=============================================================

# MODULE-11 → Performance & Animations

## 11.1: `Animated` API (React Native ki built-in animation)

1.  **🎯 Title / Short Summary:** `Animated` API - RN ki Built-in Animation Library.

2.  **🤔 Kya hai? (What?):** Yeh React Native ki core (built-in) library hai jo simple animations (jaise fade-in, move, scale) karne ke liye use hoti hai.

3.  **💡 Kyun important hai? (Why?):** Yeh animations ka starting point hai. Yeh aapko `Animated.Value` (ek special value) ko `Animated.timing` (animation function) se jodkar UI components (jaise `Animated.View`) ko animate karne deta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Simple animations jaise:
          * Ek button ko fade-in (opacity badhana).
          * Ek popup ko scale (chote se bada) karna.
          * Ek error message ko slide (move) karna.
      * Jab aapko koi 3rd party library (Reanimated) install nahi karni ho.
      * **Lekin (Spoiler):** Aaj kal 99% professional log Module 11.2 (`Reanimated`) use karte hain.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapki app "dead" (be-jaan) lagegi.
      * Par agar aapne iski jagah `Reanimated` (Module 11.2) use kiya, toh aapne sahi chunaav kiya hai.
      * **Problem:** `Animated` API "JS Bridge" par chalti hai. Agar JS thread busy hai (e.g., complex calculation ho rahi hai), toh aapka animation *ruk-ruk ke (laggy/janky)* chalega. 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Ek `Animated.Value` (animation ki value) `useRef` mein store karo. (e.g., `fadeAnim = useRef(new Animated.Value(0)).current`).
    2.  Ek function banao jo animation ko "start" kare.
    3.  Us function mein `Animated.timing` (time ke saath), `Animated.spring` (physics-based), ya `Animated.decay` use karo.
    4.  `timing` ko batao ki `fadeAnim` ko `toValue: 1` tak le jaana hai. `.start()` call karo.
    5.  Normal `<View>` ki jagah `Animated.View` use karo.
    6.  `Animated.View` ke `style` mein `opacity: fadeAnim` (special value) paas karo.

7.  **💻 Code example (Simple Fade-in):**

    ```javascript
    import React, { useRef, useEffect } from 'react';
    import { View, Button, Animated, StyleSheet } from 'react-native';

    // 1. 'View' ko 'Animated.View' se badalna zaroori hai
    const AnimatedView = Animated.createAnimatedComponent(View);

    function FadeInComponent() {
      // 2. Animated value ko useRef mein store karna (initial value 0 yaani invisible)
      const fadeAnim = useRef(new Animated.Value(0)).current;

      const fadeIn = () => {
        // 3. Animation ko define karna: 'timing'
        Animated.timing(fadeAnim, {
          toValue: 1, // Opacity ko 1 tak le jao
          duration: 2000, // 2 second mein
          useNativeDriver: true, // ⚠️ Performance ke liye zaroori
        }).start(); // 4. Animation ko shuru karna
      };

      // Component load hote hi animation start kar dega
      useEffect(() => {
        fadeIn();
      }, []);

      return (
        <AnimatedView
          style={[
            styles.box,
            {
              // 5. Normal '0' ya '1' ki jagah, 'fadeAnim' (special value) ko bind karna
              opacity: fadeAnim, 
            },
          ]}
        />
      );
    }

    const styles = StyleSheet.create({
      box: { width: 100, height: 100, backgroundColor: 'tomato' },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `const fadeAnim = useRef(new Animated.Value(0)).current;`: Humne ek "animation" value banayi jo `0` se shuru hogi.
          * `Animated.timing(fadeAnim, ...)`: Humne React ko bataya ki `fadeAnim` value ko time ke saath change karo.
          * `toValue: 1, duration: 2000`: Target value `1` hai (poori opacity), 2 second (2000ms) mein.
          * `useNativeDriver: true`: **Sabse Zaroori.** Yeh animation ko JS Bridge se hata kar *Native Thread* par bhej deta hai, jisse performance *bahut* achhi ho jaati hai (lag nahi hota). (Lekin yeh sab cheezon par kaam nahi karta, e.g., `height`, `width`).
          * `<AnimatedView style={{ opacity: fadeAnim }}>`: Humne `Animated.View` ki `opacity` ko `fadeAnim` value se *jod* diya. Jaise-jaise `fadeAnim` (0 se 1) badlega, box dikhne lagega.
      * **🚀 Quick run expected output:** Screen par ek laal dabba (box) 2 second ke dauraan dheere-dheere (fade-in) dikhega.

8.  **🐞 Common beginner mistakes:**

      * `useNativeDriver: true` ka istemaal *nahi* karna. Isse animation JS Bridge par chalta hai aur busy hone par "jank" (lag) karta hai.
      * Normal `<View>` ko animate karne ki koshish karna. (Error\! Aapko `Animated.View` use karna padega).
      * `Animated.Value` ko `useState` mein daal dena. (Nahi\! Ise hamesha `useRef` mein daalo taaki re-renders par reset na ho).

9.  **🌍 Real-world example / use-case:**

      * App ki Splash Screen ka dheere-dheere fade-out hona.
      * Ek 'Toast' message ka screen par slide-in aur slide-out hona.

10. **✅ Quick checklist / TL;DR:**

      * Yeh built-in hai, par JS Bridge par chalti hai (slow ho sakti hai).
      * Hamesha `useNativeDriver: true` use karo (jahan possible ho).
      * `Animated.Value` + `Animated.timing` + `Animated.View`.

11. **❓ FAQs:**

      * **Q: Yeh `Reanimated` se alag kaise hai?**
      * A: `Animated` JS thread se control hota hai (Native Driver se thodi help milti hai). `Reanimated` (agla topic) poori tarah Native (UI) Thread par chalta hai, 60fps guaranteed.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `duration` ko `5000` (5 second) karke dekho.
    2.  Ek "Fade Out" button banao jo `Animated.timing` se `toValue: 0` set kare.

13. **📚 Further reading / commands / links:**

      * [React Native Docs: Animated API](https://reactnative.dev/docs/animated)

-----

## 11.2: `React Native Reanimated` (Best performance, 60fps animations)

1.  **🎯 Title / Short Summary:** `React Native Reanimated` - 60fps Guaranteed, Professional Animations.

2.  **🤔 Kya hai? (What?):** Yeh `Animated` API ki 3rd party *replacement* hai. Yeh animations ko *poori tarah* JS Bridge se hatakar seedha Native (UI) Thread par chalata hai. (Note 35).

3.  **💡 Kyun important hai? (Why?):** **Performance\!** Kyunki yeh UI Thread par chalta hai, isliye JS Thread kitna bhi busy ho (bhaari API call, complex logic), aapka animation *kabhi nahi* rukegega (jank/lag nahi hoga). Yeh 60fps (frames-per-second) smooth animations ki guarantee deta hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Hamesha\!** Aaj kal (2024+), professional React Native development mein `Animated` API ki jagah `Reanimated` hi "default" hai.
      * Jab aapko complex gesture-based animations (drag-and-drop, pinch-to-zoom) banane hon (Module 11.3 ke saath).
      * Jab aapko 100% smooth 60fps animations chahiye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Agar aapne `Animated` API (bina `useNativeDriver`) use ki, toh aapki app ke animations JS thread busy hone par *lag* karenge, jisse user ko app "slow" aur "unprofessional" lagegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    *(Reanimated v2/v3 ka concept `Animated` se alag hai)*

    1.  **Hooks:** `Animated.Value` ki jagah Hooks use hote hain:
          * `useSharedValue`: Yeh `Animated.Value` jaisa hai (e.g., `const progress = useSharedValue(0);`). Yeh UI Thread par "live" rehta hai.
          * `useAnimatedStyle`: Yeh style object (e.g., `opacity`, `transform`) banata hai jo `sharedValue` par depend karta hai.
    2.  **Functions:** `Animated.timing` ki jagah "worklets" (special UI thread functions) use hote hain:
          * `withTiming(1, ...)`: `Animated.timing` ki jagah.
          * `withSpring(...)`: `Animated.spring` ki jagah.
    3.  **Component:** `Animated.View` ki jagah `Reanimated.View` (ya `Animated.View`) use hota hai.

7.  **💻 Code example (Simple Fade-in using Reanimated):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-reanimated
    // babel.config.js mein plugin add karna zaroori hai!

    import React, { useEffect } from 'react';
    import { View, Button, StyleSheet } from 'react-native';
    import Animated, { // 'Animated' ab 'react-native-reanimated' se import hoga
      useSharedValue, 
      useAnimatedStyle,
      withTiming,
    } from 'react-native-reanimated';

    function ReanimatedComponent() {
      // 1. Shared Value banana (initial opacity 0)
      const opacity = useSharedValue(0);

      // 2. Animated Style banana
      // Yeh 'useAnimatedStyle' hook 'opacity' (SharedValue) ko sunti hai
      const animatedStyle = useAnimatedStyle(() => {
        return {
          // Style ko 'opacity.value' se connect karna
          opacity: opacity.value,
        };
      });

      const fadeIn = () => {
        // 3. Shared Value ko 'withTiming' se update karna
        // Yeh JS thread block nahi karega
        opacity.value = withTiming(1, { duration: 2000 });
      };
      
      useEffect(() => {
        fadeIn();
      }, []);

      return (
        <View>
          {/* 4. 'Animated.View' par 'animatedStyle' ko lagana */}
          <Animated.View style={[styles.box, animatedStyle]} />
        </View>
      );
    }

    const styles = StyleSheet.create({
      box: { width: 100, height: 100, backgroundColor: 'tomato' },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `import Animated, ... from 'react-native-reanimated'`: Hum `react-native` se *nahi*, `react-native-reanimated` se import kar rahe hain.
          * `const opacity = useSharedValue(0);`: Ek "shared" value banayi (jo UI thread aur JS thread, dono access kar sakte hain).
          * `const animatedStyle = useAnimatedStyle(() => { ... });`: Ek "style" banaya jo UI thread par chalta hai. Humne kaha `opacity: opacity.value`.
          * `opacity.value = withTiming(1, ...);`: **Yahi magic hai.** Humne value ko *directly* ( `.value` se) update kiya. `withTiming` function UI thread ko batata hai ki is value ko 0 se 1 tak 2000ms mein le jao.
          * `<Animated.View style={[styles.box, animatedStyle]} />`: Humne `Animated.View` (Reanimated waala) liya aur use `animatedStyle` de diya.
      * **🚀 Quick run expected output:** Screen par ek laal dabba 2 second mein fade-in hoga. Yeh animation `Animated` API jaisa hi dikhega, par yeh 100% guaranteed 60fps par chalega, bhale hi JS thread par aag lagi ho.

8.  **🐞 Common beginner mistakes:**

      * `babel.config.js` mein `plugins: ['react-native-reanimated/plugin']` add karna **bhool jaana**. 🛑 Iske bina app seedha crash hogi.
      * `useSharedValue` ki value ko `opacity: opacity` (galat) likh dena. (Sahi hai: `opacity: opacity.value`).
      * Style ko `useAnimatedStyle` hook ke *bahar* define kar dena.

9.  **🌍 Real-world example / use-case:**

      * (Note 35) Complex **Bottom Sheet** (Module 11.6) gestures.
      * Draggable (drag & drop) items.
      * Pinch-to-zoom (Photo gallery).
      * `Skeleton Loaders` (Module 11.6) ka shimmer (chamkila) effect.

10. **✅ Quick checklist / TL;DR:**

      * Yeh `Animated` API ka modern replacement hai.
      * 60fps guaranteed (UI Thread par chalta hai).
      * `useSharedValue` (value) + `useAnimatedStyle` (style) + `withTiming` (animation).
      * `babel.config.js` plugin **zaroori** hai.

11. **❓ FAQs:**

      * **Q: Toh `Animated` API ko bhool jaayein?**
      * A: Lagbhag haan. Naye projects ke liye `Reanimated` hi use karein.
      * **Q: `useNativeDriver: true` (Animated) vs `Reanimated`?**
      * A: `useNativeDriver` limited hai (sirf `opacity`, `transform` par chalta hai). `Reanimated` har cheez (width, height, background color) ko UI thread par animate kar sakta hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `opacity` ke saath `transform` bhi add karo.
    2.  `useSharedValue` ko 0 se `withTiming(20)` (20 pixels move) karo (`translateX`). Dekho box fade-in bhi hota hai aur move bhi.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-reanimated`
      * [Reanimated Docs](https://docs.swmansion.com/react-native-reanimated/)

-----

## 11.3: `React Native Gesture Handler` (Complex gestures)

1.  **🎯 Title / Short Summary:** `React Native Gesture Handler` - Touch Gestures ko Handle Karna.

2.  **🤔 Kya hai? (What?):** Yeh ek library hai jo React Native ke default touch system (`PanResponder`) ko *replace* karti hai. Yeh complex touch gestures (jaise drag, pinch, rotate) ko *natively* (UI Thread par) handle karti hai.

3.  **💡 Kyun important hai? (Why?):** Yeh `Reanimated` ki "best friend" hai (Note 35). `Reanimated` (animation) + `Gesture Handler` (touch) = 60fps smooth gesture animations (jaise draggable bottom sheet).

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko `Button` ya `Pressable` se *zyada* kuch chahiye.
      * Drag and Drop (item ko kheench kar chhodna).
      * Pinch to Zoom (image ko zoom karna).
      * Swipe to Delete (list item ko swipe karna) (Note 35).
      * (Note 14) `react-navigation` bhi is library ko *use* karta hai (screen swipe-back gesture ke liye).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * React Native ka purana `PanResponder` use karna padega, jo JS Bridge par chalta hai.
      * Aapka drag-gesture JS thread busy hone par *atak* jaayega (e.g., aap ungli move kar denge, par box 1 second baad move hoga). 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Library install karo (aur `index.js` mein import zaroori hai).
    2.  `GestureDetector` component se gesture ko "detect" karo.
    3.  `Gesture` object (e.g., `Gesture.Pan()`, `Gesture.Pinch()`) se gesture ko "define" karo.
    4.  Gesture object mein event handlers (`.onUpdate()`, `.onEnd()`) lagao.
    5.  Yeh handlers `Reanimated` ke `useSharedValue` ko update karte hain.

7.  **💻 Code example (Draggable Box using Gesture Handler + Reanimated):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-gesture-handler react-native-reanimated

    import React from 'react';
    import { StyleSheet } from 'react-native';
    import Animated, {
      useSharedValue,
      useAnimatedStyle,
      withSpring,
    } from 'react-native-reanimated';
    import { Gesture, GestureDetector } from 'react-native-gesture-handler';

    function DraggableComponent() {
      // 1. Shared Values (X aur Y position ke liye)
      const translateX = useSharedValue(0);
      const translateY = useSharedValue(0);

      // 2. Gesture ko define karna (Pan = Drag)
      const panGesture = Gesture.Pan()
        // 3. Jab ungli move ho (Update)
        .onUpdate((event) => {
          // 'event.translationX' se value update karna
          translateX.value = event.translationX;
          translateY.value = event.translationY;
        })
        // 4. Jab ungli hate (End)
        .onEnd(() => {
          // Wapas 0,0 par bhej do (Spring animation ke saath)
          translateX.value = withSpring(0);
          translateY.value = withSpring(0);
        });

      // 5. Animated Style banana (Module 11.2 se)
      const animatedStyle = useAnimatedStyle(() => ({
        transform: [
          { translateX: translateX.value },
          { translateY: translateY.value },
        ],
      }));

      return (
        // 6. Gesture ko 'GestureDetector' se attach karna
        <GestureDetector gesture={panGesture}>
          {/* 7. 'Animated.View' ko 'GestureDetector' ke andar daalna */}
          <Animated.View style={[styles.box, animatedStyle]} />
        </GestureDetector>
      );
    }

    const styles = StyleSheet.create({
      box: { width: 100, height: 100, backgroundColor: 'tomato', borderRadius: 20 },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `useSharedValue(0)`: Humne box ki `X` aur `Y` position (translate) ko shared value mein store kiya.
          * `const panGesture = Gesture.Pan()`: Humne "pan" (drag) gesture banaya.
          * `.onUpdate((event) => { ... })`: Humne bataya ki jab ungli *move* ho, toh `translateX.value` ko gesture ki `event.translationX` se set kar do. Yeh sab UI Thread par ho raha hai.
          * `.onEnd(() => { ... })`: Jab ungli *hate*, toh `translateX.value` ko `withSpring(0)` (bounce effect) ke saath `0` par wapas set kar do.
          * `const animatedStyle = ...`: Style ko `translateX` aur `translateY` se connect kiya.
          * `<GestureDetector gesture={panGesture}>`: Humne `GestureDetector` ko `panGesture` ke saath "active" kiya.
          * `<Animated.View ... />`: Is `View` par ab woh gesture kaam karega.
      * **🚀 Quick run expected output:** Ek laal box. Aap use ungli se screen par kahin bhi drag kar sakte hain (bilkul smooth). Jab aap ungli chhodenge, woh bounce (spring) hokar wapas apni jagah (center) par aa jaayega.

8.  **🐞 Common beginner mistakes:**

      * `index.js` (ya `App.js`) mein `import 'react-native-gesture-handler';` (top par) add karna bhool jaana. 🛑 Iske bina Android par crash hoga.
      * `GestureHandlerRootView` se poori app ko wrap na karna (aaj kal zaroori hai).
      * `Gesture.Pan()` ko `useMemo` mein na daalna (purane tareeke mein) jisse har render par naya gesture banta tha. (Naya `Gesture` API isko solve kar deta hai).

9.  **🌍 Real-world example / use-case:**

      * (Note 35) Swipeable List (Gmail mein swipe-to-delete).
      * (Note 35) Bottom Sheet (jise drag karke upar-neeche karte hain).
      * Tinder ka swipe-left/right card.

10. **✅ Quick checklist / TL;DR:**

      * Yeh Native Gestures (touch) ke liye hai.
      * `Reanimated` ke saath best kaam karta hai (UI Thread par).
      * `GestureDetector` + `Gesture.Pan()` (ya `Pinch`, `Tap`).
      * `import 'react-native-gesture-handler';` (top-level `index.js`) zaroori hai.

11. **❓ FAQs:**

      * **Q: `Pressable` vs `GestureHandler` (Tap)?**
      * A: Simple click ke liye `Pressable`. Agar double-tap, long-press, ya complex logic chahiye toh `Gesture.Tap()` use karo.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `.onEnd()` waala part comment-out (hata) kar dekho.
    2.  Ab box ko drag karke chhodne par woh wahin ruk jaayega (wapas nahi aayega).

13. **📚 Further reading / commands / links:**

      * `npm install react-native-gesture-handler`
      * [Gesture Handler Docs](https://docs.swmansion.com/react-native-gesture-handler/)

-----

## 11.4: `FlatList` & `SectionList` Optimization (High performance lists)

1.  **🎯 Title / Short Summary:** `FlatList` Optimization - Lambi Lists ko Fast Banana.

2.  **🤔 Kya hai? (What?):** `FlatList` (Module 3.1) lambi lists dikhane ke liye hai. Lekin agar aapke paas 10,000 items hain, toh `FlatList` "lag" karne lagega. Yeh topic un techniques ke baare mein hai jisse `FlatList` ko super fast banaya jaata hai.

3.  **💡 Kyun important hai? (Why?):** Har app mein lists hoti hain (Twitter, Instagram, WhatsApp). Agar list scroll karna smooth (makhan) nahi hai, toh app bekaar maani jaati hai. (Note 33).

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab `FlatList` mein 100 se zyada items hon.
      * Jab list mein complex items (images, animations) hon.
      * Jab scroll karte waqt "blank spaces" (khaali jagah) dikh rahi ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Scroll karte waqt "jank" (lag) hoga.
      * JS thread busy hoga, app slow ho jaayegi.
      * Scroll karne par thodi der ke liye khaali jagah dikhegi (items render hone mein time lenge). 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Key Props):**

    1.  **`React.memo` (Sabse Zaroori):** Apne `renderItem` component (e.g., `<MyListItem>`) ko `React.memo` (Module 8.3) se wrap karo. Taaqi jab item ke props change na hon, toh woh faltu mein re-render na ho.
    2.  **`keyExtractor`:** Hamesha `keyExtractor={(item) => item.id.toString()}` (ya unique ID) do. Isse React ko pata chalta hai ki kaunsa item badla hai.
    3.  **`getItemLayout` (Golden Prop):** Agar aapke *saare* list items *same height* ke hain, toh yeh prop zaroor do. Isse `FlatList` ko calculation nahi karni padti. (e.g., `getItemLayout={(data, index) => ({ length: 50, offset: 50 * index, index })}`).
    4.  **`windowSize`:** (Default: 21). `FlatList` kitne items (aage aur peeche) memory mein rakhe. Ise kam (e.g., `11` ya `5`) karne se memory bachti hai, par fast scroll par blank space dikh sakti hai.
    5.  **Avoid Anonymous Functions:** `renderItem` mein anonymous function (e.g., `renderItem={() => <... />}`) mat do. Function ko component ke bahar define karo aur `useCallback` (Module 8.3) mein wrap karo (e.g., `renderItem={myRenderItem}`).
    6.  **`removeClippedSubviews`:** (Android par `true`). Off-screen items ko native side par remove kar deta hai, memory bachti hai (par bugs ho sakte hain, dhyaan se use karein).

7.  **💻 Code example (Optimization Props):**

    ```javascript
    import React, { useCallback } from 'react';
    import { View, Text, FlatList, StyleSheet } from 'react-native';

    // 1. renderItem ko 'React.memo' se wrap karna
    const MyListItem = React.memo(({ item }) => {
      console.log("Render ho raha hai: ", item.id); // Yeh kam se kam call hona chahiye
      return (
        <View style={styles.item}>
          <Text>{item.title}</Text>
        </View>
      );
    });

    // Dummy data (1000 items)
    const DATA = Array(1000).fill(0).map((_, i) => ({ id: `id-${i}`, title: `Item ${i}` }));
    const ITEM_HEIGHT = 50; // 3. Item ki height fix hai

    function OptimizedList() {
      
      // 2. renderItem ko 'useCallback' mein wrap karna
      const renderItem = useCallback(({ item }) => {
        return <MyListItem item={item} />;
      }, []);

      // 3. 'getItemLayout' define karna
      const getItemLayout = useCallback((data, index) => ({
        length: ITEM_HEIGHT,
        offset: ITEM_HEIGHT * index,
        index,
      }), []);

      return (
        <FlatList
          data={DATA}
          // 4. Sabhi optimization props
          renderItem={renderItem}
          keyExtractor={(item) => item.id}
          getItemLayout={getItemLayout}
          windowSize={11} // (Default 21 se kam)
          maxToRenderPerBatch={10} // Ek batch mein kitne render hon
          initialNumToRender={10} // Pehli baar mein kitne render hon
        />
      );
    }

    const styles = StyleSheet.create({
      item: { height: 50, justifyContent: 'center', borderBottomWidth: 1, padding: 10 },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `const MyListItem = React.memo(...)`: Humne item component ko `memo` kiya. Ab jab aap scroll karte hain, `FlatList` purane items ko destroy aur naye ko create karta hai. `memo` ensure karta hai ki item faltu mein re-render na ho.
          * `const renderItem = useCallback(...)`: `renderItem` function ko `useCallback` mein daala taaki parent ke re-render hone par yeh function naya na bane.
          * `getItemLayout`: **Yeh performance ke liye magic hai.** Hum `FlatList` ko pehle hi bata rahe hain ki har item 50px lamba hai. Ab `FlatList` ko scrollbar position ke liye calculation nahi karni padegi, seedha item par jump kar sakta hai.
          * `windowSize={11}`: Humne `FlatList` ko bola ki "current screen" (viewport) ke upar 5 item, neeche 5 item, aur beech ka 1 item (total 11) memory mein rakho.
      * **🚀 Quick run expected output:** Ek 1000 items ki list jo scroll karne par *bilkul* smooth (makhan) chalegi.

8.  **🐞 Common beginner mistakes:**

      * `FlatList` ke andar `ScrollView` use karna. (Maha-paap\! 🛑 Kabhi mat karna).
      * `getItemLayout` ko *na* dena (jabki item height fixed thi).
      * `renderItem` component ko `React.memo` se wrap *na* karna.
      * `keyExtractor` na dena.

9.  **🌍 Real-world example / use-case:**

      * Twitter feed, Instagram feed, WhatsApp chat list.
      * (Note 33) `FlashList` (Shopify ki) ek 3rd party library hai jo `FlatList` se bhi *zyada* fast hai. Professional apps ab `FlashList` par move ho rahi hain.

10. **✅ Quick checklist / TL;DR:**

      * `renderItem` ko `React.memo` se wrap karo.
      * `keyExtractor` hamesha do.
      * Agar height fixed hai, toh `getItemLayout` zaroor do (sabse important).
      * `renderItem` prop ko `useCallback` se wrap karo.

11. **❓ FAQs:**

      * **Q: Agar item ki height alag-alag (dynamic) ho toh?**
      * A: Toh `getItemLayout` nahi de sakte. Aise mein `FlashList` (3rd party) use karna best hai, jo dynamic height ko behtar handle karta hai.
        1Remember the user wants notes on module 11.5 and 11.6 next, not 12.1.
      * **Q: `ScrollView` vs `FlatList`?**
      * A: `ScrollView` saare (e.g., 1000) items ek saath render karta hai (app crash ho jaayegi). `FlatList` "virtualization" use karta hai (sirf 10-15 item render karta hai jo screen par dikh rahe hain). 10 se zyada item ke liye hamesha `FlatList`.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `getItemLayout` prop ko comment karke dekho.
    2.  `FlatList` mein `onScrollToIndexFailed` prop add karke dekho.

13. **📚 Further reading / commands / links:**

      * [React Native Docs: Optimizing FlatList](https://reactnative.dev/docs/optimizing-flatlist-configuration)
      * [FlashList (Shopify)](https://shopify.github.io/flash-list/) - `FlatList` ka replacement.

-----

## 11.5: Performance Profiling (Flipper, Profiler, `memo`) & Fast Refresh

*(Note: Is topic mein hum Module 8.3/11.4 ke `memo` (Note 49), `InteractionManager` (Note 49), `Lazy Loading` (Note 33, 49), aur `Fast Refresh` (Note 26) ko ek saath cover karenge, kyunki yeh sab performance se related hain.)*

1.  **🎯 Title / Short Summary:** Performance Profiling - Pata Lagana ki App Slow Kyun Hai.
2.  **🤔 Kya hai? (What?):** Profiling woh process hai jisse hum tools (jaise Flipper, React DevTools Profiler) ka use karke yeh check karte hain ki:
      * Kaunsa component faltu mein re-render ho raha hai?
      * Kaunsa function JS thread ko block (slow) kar raha hai?
      * Memory kahan leak ho rahi hai?
3.  **💡 Kyun important hai? (Why?):** Bina profiling ke performance theek karna "andhere mein teer chalaane" jaisa hai. Profiler aapko *exactly* batata hai ki problem kahan hai.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab aapko app "slow" (laggy) feel ho.
      * Launch (release) karne se pehle.
      * Jab JS Thread FPS (frame rate) drop ho (Flipper mein check kar sakte hain).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Aap `useMemo`, `useCallback` (Module 8.3) har jagah lagate rahenge ("Premature Optimization"), jabki shayad problem kahin aur ho.
      * Aapki app release hone ke baad users ko slow lagegi aur woh uninstall kar denge.

-----

### 🧑‍🏫 Concept Breakdown 1: Tools (Flipper & Profiler)

  * **Flipper (React Native ka official tool):**
      * Yeh ek desktop app hai.
      * **Crash Reports:** Dekh sakte hain app crash kyun hui.
      * **Network Inspector:** Saari API calls (request/response) dekh sakte hain (Module 6.3).
      * **React DevTools:** Components ka tree dekh sakte hain.
      * **Performance:** JS Thread aur UI Thread ka FPS (frame rate) real-time mein dekh sakte hain. (Agar JS thread FPS 60 se neeche (e.g., 30) hai, matlab app slow hai).
  * **React DevTools "Profiler":**
      * Yeh Flipper ke andar (ya standalone) milta hai.
      * Aap "Record" button dabate hain, app mein kuch kaam (e.g., scroll) karte hain, fir "Stop" karte hain.
      * Yeh aapko "flamegraph" (chart) dikhata hai.
      * **Chart mein:** Jo component *zyada time* le raha hai (ya *baar-baar* render ho raha hai), woh *lamba/yellow* dikhega.
      * **Solution:** Profiler batayega "Component X re-render hua kyunki iska prop Y badla". Fir aap `React.memo` (Note 49) ka use karke use rok sakte hain.

-----

### 🧑‍🏫 Concept Breakdown 2: Techniques (InteractionManager & Lazy Loading)

  * **`InteractionManager` (Note 49):**

      * **Problem:** Aap 'Home' screen se 'Profile' screen par navigate karte hain. Navigation *animation* (slide) ko 60fps par chalna hai (UI Thread). Lekin 'Profile' screen load hote hi `useEffect` mein bhaari API call (JS Thread) shuru kar deti hai. Dono ek saath hone se animation *lag* (jank) kar jaata hai.
      * **Solution:** `InteractionManager` (React Native se import hota hai).
      * `InteractionManager.runAfterInteractions(() => { ... })`
      * **Yeh kya karta hai:** Yeh React Native ko bolta hai, "Pehle saare animation (interaction) khatam ho jaane do (e.g., screen slide poori ho jaaye). Jab sab shaant ho jaaye, *tab* iske andar ka code (e.g., API call) chalaana."
      * **Code:**
        ```js
        import { InteractionManager } from 'react-native';
        useEffect(() => {
          InteractionManager.runAfterInteractions(() => {
            // 🚀 Ab yahan heavy API call karo
            // Animation (interaction) khatam hone ke baad
            fetchHeavyData();
          });
        }, []);
        ```

  * **Lazy Loading (Screens & Components) (Note 33, 49):**

      * **Problem:** Aapki app `App.js` mein 50 screens (Home, Profile, Settings...) import karti hai. User app kholta hai. React Native ko app *start* karne se pehle saari 50 screens ka JS code load karna padta hai. Isse App Start Time (TTR) *bahut* slow ho jaata hai.
      * **Solution:** "Lazy Loading".
      * **Yeh kya karta hai:** Hum code ko bolte hain, "Sirf `LoginScreen` ka code load karo. `HomeScreen` ka code tabhi load karna (network se/disk se) jab user *actually* login button dabaye."
      * **Code (React Navigation ke saath):**
        ```js
        // Galat ❌ (Sab pehle load hoga)
        import HomeScreen from './HomeScreen';
        <Stack.Screen name="Home" component={HomeScreen} />

        // Sahi ✅ (Lazy Loading)
        <Stack.Screen
          name="Home"
          // Component 'prop' ki jagah 'getComponent' (purana) ya seedha 'component' 
          // (aaj kal Navigation default mein lazy load karta hai, par JS bundle split ho tab)
          // Asli lazy loading (bundle splitting) Metro (bundler) ke saath complex hai.
          // Sabse aasan lazy loading:
          component={() => require('./HomeScreen').default} 
          // (Ya React.lazy + Suspense - jo RN mein ab better support hai)
        />
        ```
      * **(Note 49)** Yeh concept components (e.g., bhaari chart) par bhi apply hota hai.

-----

### 📊 Comparison: `Fast Refresh` vs `Hot Reloading` (Note 26)

(Note: Yeh development tools hain, performance *technique* nahi.)

| Feature | `Fast Refresh` (Modern) | `Hot Reloading` (Purana) |
| :--- | :--- | :--- |
| **🤔 Kya hai? (What?)** | Yeh code save karne par **sirf badla hua component** update karta hai, state (e.g., `useState`) *save* rakhta hai. | Yeh code save karne par **poori file** ko *reload* karta tha. |
| **💡 Kyun important hai? (Why?)** | **State bachata hai\!** Aap 5 screen aage navigation karke ek form bhar rahe hain, aur aapne Text (style) change karke save kiya... aap usi screen par, usi form data ke saath rahenge. | State (e.g., `useState`) *reset* kar deta tha. Aapko har save ke baad wapas us screen par navigate karke form bharna padta tha. 🛑 |
| **⏰ Kab/Kyun use karein? (When?)** | Yeh **default** hai (React Native 0.61+). Hamesha ON rakho. | Yeh ab *deprecated* (band) ho chuka hai. Hum ise use nahi karte. |
| **🌍 Real-world example** | Aap `counter` state (5) par hain. `Text` ka color badal kar save karte hain. `counter` abhi bhi (5) hi rahega. ✅ | Aap `counter` state (5) par hain. `Text` ka color badal kar save karte hain. `counter` reset hokar (0) ho jaayega. ❌ |

-----

*(Regular 13-point format resumes)*

10. **✅ Quick checklist / TL;DR:**
      * App slow hai? **Profiler** (Flipper/DevTools) se check karo "kyun?".
      * Faltu re-render? `React.memo` (Note 49) use karo.
      * Navigation animation (slide) 'lag' kar raha hai? `InteractionManager.runAfterInteractions` (Note 49) mein `useEffect` ka code daalo.
      * App start slow hai? Code ko "lazy load" (Note 33) karo.
      * `Fast Refresh` (Note 26) naya (acha) hai, `Hot Reloading` purana (bekaar) tha.
11. **❓ FAQs:**
      * **Q: `PureComponent` (Note 49) kya hai?**
      * A: Yeh `React.memo` ka "Class Component" version hai. Hum Functional Components use karte hain, isliye hum `React.memo` use karte hain. Dono ka kaam ek hi hai (shallow prop comparison).
12. **🏋️‍♀️ Practice exercise:**
    1.  Apne Dev Menu (shake device) mein "Show Performance Monitor" (ya Flipper) check karo. FPS dekho.
    2.  Ek button banao jo `useEffect` mein 5 second ka `for` loop chalaye (JS thread block). Dekho FPS (JS) 0 ho jaayega.
    3.  Ab us loop ko `InteractionManager.runAfterInteractions` mein daalo.
13. **📚 Further reading / commands / links:**
      * [React Native Docs: Profiling](https://reactnative.dev/docs/profiling)
      * [Flipper Docs](https://fbflipper.com/)

-----

## 11.6: Advanced Animations & UI (Lottie, Skeleton, BottomSheet)

1.  **🎯 Title / Short Summary:** Advanced UI - Lottie, Skeleton, BottomSheet, Swipeable.

2.  **🤔 Kya hai? (What?):** Yeh 4 alag-alag libraries/concepts hain jo aapki app ko "premium" feel dete hain (Note 35, 50).

      * **`Lottie` (Note 50):** Adobe After Effects mein bane *complex* (cartoon) animations ko app mein chalaana.
      * **`Skeleton Loaders` (Note 35):** Data load hone tak "ghost" (grey) boxes dikhana (jaise Facebook/LinkedIn).
      * **`BottomSheet` (Note 35):** Screen ke neeche se nikalne waala draggable (slide) panel (jaise Google Maps).
      * **`Swipeable Lists` (Note 35):** List item ko swipe-left/right karke actions (delete/edit) dikhana (jaise Gmail).

3.  **💡 Kyun important hai? (Why?):** Yeh UX (User Experience) ko 10x behtar banate hain.

      * `Lottie` boring `ActivityIndicator` (spinner) ko replace karta hai.
      * `Skeleton` user ko batata hai ki "data aa raha hai" (blank screen se behtar).
      * `BottomSheet` `Modal` (popup) ka behtar, modern alternative hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * `Lottie`: Splash screen, 'Order Placed' (success) screen, ya 'No Data Found' (empty) screen par.
      * `Skeleton`: List/Profile (data fetch) load hone se pehle.
      * `BottomSheet`: Filter/Options/Settings (jo neeche se aayein) ke liye.
      * `Swipeable`: `FlatList` mein "Delete" action ke liye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapki app "basic" aur "purani" lagegi. User ko data load hone par blank screen ya boring spinner dikhega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    -----

    ### 1\. `Lottie` Animations (Note 50)

      * **Library:** `lottie-react-native`
      * **Kaise chalta hai:**
        1.  Designer aapko ek `animation.json` file dega (LottieFiles.com se bhi download kar sakte hain).
        2.  `npm install lottie-react-native`.
        3.  `<LottieView source={require('./animation.json')} autoPlay loop />`
      * **Code:**
        ```js
        import LottieView from 'lottie-react-native';
        function MyAnimation() {
          return (
            <LottieView 
              source={require('../assets/success-check.json')}
              autoPlay={true} // Apne aap shuru ho
              loop={false} // Ek hi baar chale (success animation)
              style={{ width: 200, height: 200 }}
            />
          );
        }
        ```

    -----

    ### 2\. `Skeleton Loaders` (Note 35) (Module 2.4 advanced)

      * **Library:** `react-native-skeleton-placeholder` (ya khud `Reanimated` se bana sakte hain).
      * **Kaise chalta hai:** Yeh `react-native-linear-gradient` (Module 1.4) aur `Reanimated` (Module 11.2) ka use karke ek "shimmer" (chamkila) effect banata hai jo grey boxes par chalta hai.
      * **Code:**
        ```js
        import SkeletonPlaceholder from "react-native-skeleton-placeholder";
        function MyLoader() {
          return (
            <SkeletonPlaceholder>
              <SkeletonPlaceholder.Item width={60} height={60} borderRadius={50} /> // (Profile pic)
              <SkeletonPlaceholder.Item marginLeft={20}>
                <SkeletonPlaceholder.Item width={120} height={20} /> // (Naam)
                <SkeletonPlaceholder.Item marginTop={6} width={80} height={20} /> // (Username)
              </SkeletonPlaceholder.Item>
            </SkeletonPlaceholder>
          );
        }
        ```
      * **Data ke saath:** `if (isLoading) { return <MyLoader />; } else { return <MyProfileData />; }`

    -----

    ### 3\. `BottomSheet` (Note 35)

      * **Library:** `@gorhom/bottom-sheet` (Sabse famous, `Reanimated` aur `Gesture Handler` (Module 11.3) par chalta hai).
      * **Kaise chalta hai:** Yeh `BottomSheetModalProvider` (top-level) aur `BottomSheet` component deta hai.
      * **Code:**
        ```js
        import BottomSheet, { BottomSheetModalProvider } from '@gorhom/bottom-sheet';
        // (App.js mein <GestureHandlerRootView> aur <BottomSheetModalProvider> zaroori)

        function MyComponent() {
          const sheetRef = useRef(null);
          const snapPoints = useMemo(() => ['25%', '50%', '90%'], []); // Kitna khulega

          return (
            <BottomSheet
              ref={sheetRef}
              snapPoints={snapPoints}
            >
              <View>
                <Text>Options...</Text> 
              </View>
            </BottomSheet>
          );
        }
        ```

    -----

    ### 4\. `Swipeable Lists` (Note 35)

      * **Library:** `react-native-gesture-handler` (Module 11.3) mein `Swipeable` component hota hai.
      * **Kaise chalta hai:** `FlatList` ke `renderItem` mein har item ko `Swipeable` component se wrap karte hain.
      * **Code:**
        ```js
        import { Swipeable } from 'react-native-gesture-handler';

        // (Yeh function batata hai ki "right swipe" par kya dikhega)
        const renderRightActions = () => {
          return (
            <TouchableOpacity style={{ backgroundColor: 'red', justifyContent: 'center' }}>
              <Text style={{ color: 'white', padding: 20 }}>Delete</Text>
            </TouchableOpacity>
          );
        };

        function MyListItem() {
          return (
            <Swipeable renderRightActions={renderRightActions}>
              <View style={{ padding: 20, backgroundColor: 'white' }}>
                <Text>Item (Swipe Left)</Text>
              </View>
            </Swipeable>
          );
        }
        ```

7.  **🚀 Quick run expected output:**

      * **Lottie:** Ek smooth, complex JSON-based animation (jaise 'Success Checkmark').
      * **Skeleton:** Data aane se pehle 'ghost' layout (grey boxes) shimmer effect ke saath.
      * **BottomSheet:** Neeche se nikalne waala panel jo 3 stops (`snapPoints`) par rukta hai.
      * **Swipeable:** List item ko left swipe karne par 'Delete' button dikhna.

8.  **🐞 Common beginner mistakes:**

      * `Lottie`: JSON file ko `assets` mein daalna bhool jaana.
      * `Skeleton`: `react-native-linear-gradient` install na karna (dependency hai).
      * `BottomSheet`: `GestureHandlerRootView` aur `BottomSheetModalProvider` se app ko wrap na karna. 🛑
      * `Swipeable`: `react-native-gesture-handler` (v1) ka `Swipeable` use karna (v2 ka `GestureDetector` based behtar hai).

9.  **🌍 Real-world example / use-case:**

      * **Lottie:** Swiggy/Zomato ki "Order Placed" / "Food Delivered" animation.
      * **Skeleton:** Facebook/LinkedIn/Twitter ki home feed loading.
      * **BottomSheet:** Google Maps ka "Venue Details" panel.
      * **Swipeable:** Gmail/WhatsApp ki "Archive/Delete" functionality.

10. **✅ Quick checklist / TL;DR:**

      * `Lottie`: Complex JSON animations (`lottie-react-native`).
      * `Skeleton`: Loading placeholders (`react-native-skeleton-placeholder`).
      * `BottomSheet`: Draggable panel (`@gorhom/bottom-sheet`).
      * `Swipeable`: List item gestures (`react-native-gesture-handler`).

11. **❓ FAQs:**

      * **Q: Skeleton khud (Reanimated se) kaise banayein?**
      * A: `LinearGradient` (gradient) lo, aur `useSharedValue` + `withRepeat` + `withTiming` ka use karke uske `translateX` (position) ko animate (move) karo.

12. **🏋️‍♀️ Practice exercise:**

    1.  [LottieFiles.com](https://lottiefiles.com/) se ek "loading" animation (JSON) download karo.
    2.  Apne project ke `ActivityIndicator` ko hata kar `LottieView` se replace karo.

13. **📚 Further reading / commands / links:**

      * `npm install lottie-react-native`
      * `npm install react-native-skeleton-placeholder`
      * `npm install @gorhom/bottom-sheet`
      * (Swipeable `react-native-gesture-handler` ke saath aata hai)
	  
	  
=============================================================

# MODULE-12 → Interacting with Native Device

Yeh module "Professional" level ka hai. Hum Camera, Location, Fingerprint sensor, Bluetooth, aur Push Notifications jaise advanced features ko handle karna seekhenge. Chaliye, phone ke device features ko unlock karte hain\!

-----

## 12.1: Push Notifications (Firebase Cloud Messaging - FCM)

1.  **🎯 Title / Short Summary:** Push Notifications (FCM) - App band hone par bhi User ko Alerts Bhejna.

2.  **🤔 Kya hai? (What?):** Push Notifications woh "pop-up" messages (alerts) hain jo aapke phone par aate hain, bhale hi woh app (jaise WhatsApp, Instagram) *band* ho. Hum iske liye **Firebase Cloud Messaging (FCM)** (Google ka free service) use karte hain.

3.  **💡 Kyun important hai? (Why?):** Yeh user engagement (user ko app par wapas laane) ka sabse *powerful* tareeka hai. Isse aap user ko naye message, offers, ya updates ke baare mein bata sakte hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab user ko naya message aaye (WhatsApp).
      * Jab naya offer ya news ho (Zomato).
      * Jab koi event (jaise order delivery) trigger ho.
      * **`Push-Triggered Jobs` (Note 39):** Yeh advanced concept hai. Jab notification *aaye* (bhale hi user ne dekha na ho), aap background mein thoda code chala sakte hain (e.g., naya message data fetch karke store karna).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap user se tabhi baat kar paayenge jab woh app *kholega*.
      * Jaise hi user app band karega, aap usse "re-engage" (wapas bula) nahi kar paayenge. Aapki app "dead" lagegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `react-native-firebase` (Yeh best hai).
    **Setup Flow (Overview):**

    1.  **Firebase Project:** Firebase console (website) par project banao.
    2.  **App Register:** Apni Android (`google-services.json` file) aur iOS (`GoogleService-Info.plist` file) app ko Firebase project se connect karo.
    3.  **Library Install:** `npm install @react-native-firebase/app` aur `npm install @react-native-firebase/messaging`.
    4.  **Permission (iOS):** iOS par notification permission *maangni* padti hai.
    5.  **Token Generate:** Har phone (device) ki ek unique "FCM Token" (address) generate hoti hai.
    6.  **Token Save:** Is token ko aapko apne *server* (database) mein save karna hota hai.
    7.  **Send:** Jab aapko "User A" ko notification bhejni ho, aap apne server se Firebase ko bolte ho ki "iss token par yeh message bhej do".
    8.  **Receive:** App us message ko handle karti hai (foreground, background, ya app-killed state mein).

    **`Notification Channels` (Android) (Note 40):**

      * Android 8.0+ mein, aapko "Channels" banana *zaroori* hai.
      * Channel ek category hai (e.g., "Chat Messages", "Promotions").
      * User in channels ko alag-alag control kar sakta hai (e.g., "Chat" ki notification ON, "Promotions" ki OFF).
      * Aapko app start hote hi yeh channel register karna hota hai.

7.  **💻 Code example (App start par Token lena aur Messages sunna):**

    ```javascript
    // (index.js ya App.js)
    import React, { useEffect } from 'react';
    import { View, Text, Alert } from 'react-native';
    import messaging from '@react-native-firebase/messaging';

    // (Note 40): Android Notification Channel
    // Yeh app start hote hi bas ek baar karna hai
    async function createAndroidChannel() {
      const channelId = 'chat-messages'; // Channel ki ID
      const channel = new messaging.Android.Channel(
        channelId,
        'Chat Messages', // User ko dikhne waala naam
        messaging.Android.Importance.Max // (High/Max taaki popup aaye)
      );
      await messaging.android.createChannel(channel);
      console.log('Android Channel Created!');
    }

    function App() {
      // 1. iOS par permission maangna
      async function requestUserPermission() {
        const authStatus = await messaging().requestPermission();
        const enabled =
          authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
          authStatus === messaging.AuthorizationStatus.PROVISIONAL;

        if (enabled) {
          console.log('Authorization status:', authStatus);
          getFCMToken(); // Agar permission mili, toh token lo
        }
      }

      // 2. Device ka unique Token lena
      async function getFCMToken() {
        const fcmToken = await messaging().getToken();
        if (fcmToken) {
          console.log('Aapka Unique FCM Token:', fcmToken);
          // ⚠️ IMPORTANT: Is token ko apne server (Database) par bhejo!
          // sendTokenToMyServer(fcmToken);
        } else {
          console.log('Token nahi mila');
        }
      }

      useEffect(() => {
        // (Note 40) Channel banao
        if (Platform.OS === 'android') {
          createAndroidChannel();
        }
        
        // iOS Permission
        requestUserPermission();

        // 3. Message Listener (Jab App KHULI (Foreground) ho)
        const unsubscribe = messaging().onMessage(async remoteMessage => {
          Alert.alert(
            'Naya Message (Foreground):', 
            remoteMessage.notification.body
          );
        });

        // 4. Message Listener (Jab App Background ya KILLED state se khule)
        // User ne notification par 'tap' kiya
        messaging().onNotificationOpenedApp(remoteMessage => {
          console.log('Notification se app khuli (Background):', remoteMessage);
          // navigation.navigate('Chat', { chatId: remoteMessage.data.chatId });
        });

        // (App KILLED state se khulne ka check)
        messaging()
          .getInitialNotification()
          .then(remoteMessage => {
            if (remoteMessage) {
              console.log('Notification se app khuli (Killed):', remoteMessage);
            }
          });

        return unsubscribe;
      }, []);

      return <View><Text>FCM Setup!</Text></View>;
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `createAndroidChannel`: (Note 40) Android ke liye 'chat-messages' naam ka ek channel banaya.
          * `requestUserPermission`: iOS user se permission maangi.
          * `getFCMToken`: Device ka unique address (token) liya. Ise server par save karna *zaroori* hai.
          * `messaging().onMessage`: Yeh tab chalta hai jab app *khuli* (foreground) ho aur message aaye. Hum yahan `Alert` dikha rahe hain.
          * `messaging().onNotificationOpenedApp`: Yeh tab chalta hai jab user *background* mein padi app ki notification par *click* karta hai.
          * `messaging().getInitialNotification`: Yeh tab chalta hai jab app *band (killed)* thi aur user ne notification par *click* karke use khola.
      * **🚀 Quick run expected output:** App khulne par console mein "FCM Token" print hoga. Agar app khuli hai, toh notification aane par Alert dikhega.

8.  **🐞 Common beginner mistakes:**

      * Native setup (JSON/plist files) ko galat jagah (folder) mein daalna.
      * iOS par `requestPermission` call na karna.
      * Android par (Note 40) `Notification Channel` *na* banana (Android 8+ par notification dikhega hi nahi).
      * FCM Token ko server par save *nahi* karna (toh aap use bhejenge kaise?).
      * `onMessage` (foreground) aur `onNotificationOpenedApp` (background) ke logic mein confuse hona.

9.  **🌍 Real-world example / use-case:**

      * WhatsApp, Instagram, Zomato, Uber... har app FCM (ya iOS ka APN) use karti hai.
      * **(Note 39) `Push-Triggered Jobs`:** WhatsApp message aane par (notification aayi), background mein message ko decrypt karke database mein save kar leta hai, taaki jab aap app kholein toh chat *turant* dikhe (yeh `Headless JS` (Module 12.8) se hota hai).

10. **✅ Quick checklist / TL;DR:**

      * `react-native-firebase` library use karo.
      * Firebase project setup (JSON/plist) zaroori hai.
      * iOS par permission maango.
      * Android par Channel banao (Note 40).
      * `getToken()` se token lo aur server par save karo.
      * `onMessage` (Foreground) aur `onNotificationOpenedApp` (Background/Killed) ko handle karo.

11. **❓ FAQs:**

      * **Q: Bina Firebase ke kar sakte hain?**
      * A: Haan, par `react-native-push-notification` (3rd party) jaisi library use karni hogi, jiska setup *bahut* complex hai. FCM sabse aasan hai.
      * **Q: Local notifications (bina server) bhej sakte hain?**
      * A: Haan, (e.g., Reminder app). `react-native-push-notification` ya `notifee` library se aap `triggerNotification(time)` set kar sakte hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Firebase ka (free) project setup karo.
    2.  Apni app ka FCM token `console.log` se nikaalo.
    3.  Firebase Console (website) se "Send Test Message" ka option use karke uss token par message bhej kar dekho.

13. **📚 Further reading / commands / links:**

      * `npm install @react-native-firebase/app @react-native-firebase/messaging`
      * [React Native Firebase Docs (Messaging)](https://rnfirebase.io/messaging/usage)

-----

## 12.2: `Advanced Camera (VisionCamera)` (Note 37)

1.  **🎯 Title / Short Summary:** `react-native-vision-camera` - Professional, Fast Camera Banana.

2.  **🤔 Kya hai? (What?):** Yeh `react-native-camera` (purani) ya `react-native-image-picker` (Module 5.1) ka *bahut* advanced replacement hai. Yeh ek full-featured camera library hai jo high performance (60fps viewfinder) aur advanced features (jaise QR code scanning, AI facial recognition) "Frames" ke zariye deti hai.

3.  **💡 Kyun important hai? (Why?):** `react-native-image-picker` (Module 5.1) sirf image *select* karta hai (ya default camera kholta hai). `VisionCamera` aapko app ke *andar* hi Instagram/Snapchat jaisa *custom* camera UI banane deta hai. (Note 37).

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko "default" camera nahi, balki *custom* camera (apne buttons ke saath) banana ho.
      * Jab aapko QR code / Barcode scanner banana ho.
      * Jab aapko real-time "Frame Processing" karni ho (e.g., AI se live face detect karna).
      * Jab performance critical ho (yeh UI thread par chalta hai).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap `react-native-image-picker` use karenge, jo user ko app se *bahar* default camera app mein le jaayega. Isse UX toot jaata hai.
      * Aap purani `react-native-camera` (jo ab maintain nahi hoti) use karenge, jo slow hai aur bugs se bhari hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  `npm install react-native-vision-camera`.
    2.  `react-native-reanimated` (Module 11.2) iski dependency hai (Frame processing ke liye).
    3.  Native setup: `AndroidManifest.xml` aur `Info.plist` (iOS) mein Camera permissions add karni padti hain (Note 1.10, 13.8).
    4.  App start par Camera permission *maangni* padti hai.
    5.  `<Camera ... />` component ko render karna.
    6.  `ref` (Module 8.4) ka use karke `camera.current.takePhoto()` method se photo capture karna.

7.  **💻 Code example (Basic Camera View & Photo Capture):**

    ```javascript
    import React, { useRef, useEffect, useState } from 'react';
    import { View, Button, StyleSheet } from 'react-native';
    import { Camera, useCameraDevices } from 'react-native-vision-camera';

    function MyCameraScreen() {
      // 1. Camera permissions check karna
      const [hasPermission, setHasPermission] = useState(false);
      // 2. Available devices (front/back camera) ko get karna
      const devices = useCameraDevices();
      const device = devices.back; // Hum back camera use karenge
      
      const camera = useRef(null); // Camera ko control karne ke liye ref

      useEffect(() => {
        // 3. Permission maangna
        (async () => {
          const status = await Camera.requestCameraPermission();
          setHasPermission(status === 'authorized');
        })();
      }, []);

      // 4. Photo lene ka function
      const onTakePhoto = async () => {
        if (camera.current) {
          try {
            const photo = await camera.current.takePhoto({
              qualityPrioritization: 'speed', // Fast photo
              enableAutoStabilization: true, // Photo ko stable karna
            });
            console.log('Photo captured!', photo.path);
            // (Is photo.path ko UI par dikhao ya upload karo)
          } catch (e) {
            console.error('Photo capture failed:', e);
          }
        }
      };

      // 5. Render logic
      if (!device || !hasPermission) {
        return <Text>Loading camera ya permission nahi hai...</Text>;
      }

      return (
        <View style={StyleSheet.absoluteFill}>
          {/* 6. Camera Viewfinder */}
          <Camera
            ref={camera}
            style={StyleSheet.absoluteFill}
            device={device}
            isActive={true} // Camera ko 'active' (ON) karna
            photo={true} // Photo mode enable
          />
          
          {/* 7. Custom button (jo viewfinder ke 'upar' dikhega) */}
          <View style={styles.captureButtonContainer}>
            <Button title="Click Photo" onPress={onTakePhoto} />
          </View>
        </View>
      );
    }

    const styles = StyleSheet.create({
      captureButtonContainer: {
        position: 'absolute',
        bottom: 50,
        alignSelf: 'center',
      },
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `useCameraDevices()`: Hook jo available cameras (front, back, wide-angle) ki list deta hai.
          * `devices.back`: Hum back camera select kar rahe hain.
          * `Camera.requestCameraPermission()`: App start par user se permission maang rahe hain.
          * `camera.current.takePhoto()`: `ref` (Module 8.4) ka use karke hum `Camera` component ke 'andar' ka function `takePhoto` call kar rahe hain.
          * `<Camera ... />`: Yeh component *full screen* (viewfinder) dikha raha hai.
          * `device={device}`: Camera ko bataya ki 'back' camera use karna hai.
          * `isActive={true}`: Camera ko chalu (ON) kiya.
          * `<Button ... />`: Yeh hamara *custom* capture button hai jo Camera component ke upar `position: 'absolute'` se rakha hai.
      * **🚀 Quick run expected output:** Full screen camera view (viewfinder) dikhega. Neeche ek button ("Click Photo") hoga. Button dabane par photo capture hogi aur console mein uska path (e.g., `file://...`) print hoga.

8.  **🐞 Common beginner mistakes:**

      * `AndroidManifest.xml` (Android) ya `Info.plist` (iOS) mein Camera permissions add karna **bhool jaana**. 🛑 (App seedha crash hogi).
      * `await Camera.requestCameraPermission()` (JS se permission) maangna bhool jaana.
      * `<Camera>` component ko `isActive={true}` prop na dena (viewfinder kaala dikhega).
      * `device` select na karna (`useCameraDevices` se).

9.  **🌍 Real-world example / use-case:**

      * (Note 37) **Instagram:** Custom filters, zoom, flash controls waala camera.
      * **Paytm/PhonePe:** QR Code scanner (jo `useFrameProcessor` hook se banta hai).
      * Document scanner apps.

10. **✅ Quick checklist / TL;DR:**

      * Yeh custom (in-app) camera ke liye hai.
      * Native permissions (`AndroidManifest/Info.plist`) **zaroori** hain.
      * JS permissions (`requestCameraPermission`) **zaroori** hain.
      * `useCameraDevices` se device chuno.
      * `ref.current.takePhoto()` se photo lo.

11. **❓ FAQs:**

      * **Q: QR Code kaise scan karein?**
      * A: `react-native-vision-camera-v3-barcode-scanner` jaisa "Frame Processor" plugin use karna padta hai. `Camera` component ko `frameProcessor` prop dena hota hai jo real-time mein frames ko analyze karta hai.
      * **Q: Video record kar sakte hain?**
      * A: Haan, `camera.current.startRecording()` aur `stopRecording()` methods hote hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein ek aur button "Switch Camera" banao.
    2.  `useState` (`const [cam, setCam] = useState('back')`) ka use karke `device` ko `devices.back` aur `devices.front` ke beech switch karke dekho.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-vision-camera`
      * (Iske liye `react-native-reanimated` bhi zaroori hai)
      * [VisionCamera Docs](https://react-native-vision-camera.com/)

-----

## 12.3: `Geolocation` (Live location tracking) (Note 37)

1.  **🎯 Title / Short Summary:** Geolocation - User ki Current Location (Latitude/Longitude) Get Karna.

2.  **🤔 Kya hai? (What?):** Yeh ek API hai jo phone ke GPS hardware se user ki *current* geographical location (latitude, longitude) nikaalne mein madad karta hai. (Note 37).

3.  **💡 Kyun important hai? (Why?):** Yeh "location-aware" apps ke liye zaroori hai. Iske bina, Swiggy/Zomato ko kaise pata chalega ki aap kahan hain?

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **One-time location:** User ki current city (weather app) ya address (food delivery) pata karne ke liye. (`getCurrentPosition`)
      * **Live location tracking:** User ko map par 'live' move hote dikhane ke liye (Uber/Google Maps). (`watchPosition`)

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapki app user ko location-based services (e.g., "Nearby Restaurants", "Directions") nahi de paayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `@react-native-community/geolocation` (RN se core se nikal kar 3rd party ho gayi hai).

    1.  Library install karo.
    2.  Native setup: `AndroidManifest.xml` aur `Info.plist` (iOS) mein Location permissions (`ACCESS_FINE_LOCATION`) add karni padti hain (Note 1.10, 13.8).
    3.  App mein *JS se permission* maangni padti hai (`PermissionsAndroid` (Android) ya `requestAuthorization` (iOS)).
    4.  **`Geolocation.getCurrentPosition(successCallback, errorCallback)`:** Ek baar location deta hai.
    5.  **`Geolocation.watchPosition(successCallback, errorCallback)`:** Jab bhi location *change* hoti hai, yeh baar-baar data deta hai (live tracking).
    6.  **`Geolocation.clearWatch(watchId)`:** Tracking ko rokne ke liye.

7.  **💻 Code example (Get Current Location):**

    ```javascript
    // Pehle install karein:
    // npm install @react-native-community/geolocation

    import React, { useState } from 'react';
    import { View, Text, Button, PermissionsAndroid, Platform } from 'react-native';
    import Geolocation from '@react-native-community/geolocation';

    function LocationScreen() {
      const [location, setLocation] = useState(null);

      // 1. Android ke liye permission maangna
      const requestLocationPermissionAndroid = async () => {
        try {
          const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
            {
              title: 'Location Permission',
              message: 'App ko aapki location chahiye.',
              buttonNeutral: 'Ask Me Later',
              buttonNegative: 'Cancel',
              buttonPositive: 'OK',
            },
          );
          if (granted === PermissionsAndroid.RESULTS.GRANTED) {
            console.log('Location permission mili!');
            getLocation();
          } else {
            console.log('Location permission nahi mili');
          }
        } catch (err) {
          console.warn(err);
        }
      };
      
      // (iOS mein permission Info.plist se manage hoti hai, par 'when-in-use' ke liye call kar sakte hain)
      // Geolocation.requestAuthorization();

      // 2. Location get karne ka function
      const getLocation = () => {
        setLocation(null); // Loading state
        Geolocation.getCurrentPosition(
          // 3. Success Callback
          (position) => {
            console.log('Position:', position);
            const coords = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude,
            };
            setLocation(coords);
          },
          // 4. Error Callback
          (error) => {
            console.log('Error:', error.code, error.message);
            setLocation(null);
          },
          // 5. Options
          { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
        );
      };
      
      const handleGetLocation = () => {
        if (Platform.OS === 'android') {
          requestLocationPermissionAndroid();
        } else {
          // (iOS permission setup simpler hota hai, 'requestAuthorization')
          getLocation();
        }
      };

      return (
        <View>
          <Button title="Get My Location" onPress={handleGetLocation} />
          {location ? (
            <Text>
              Latitude: {location.latitude}, Longitude: {location.longitude}
            </Text>
          ) : (
            <Text>Location lene ke liye button dabao...</Text>
          )}
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `requestLocationPermissionAndroid`: (Note 13.8) Android par 'Runtime' permission maangne ka code.
          * `Geolocation.getCurrentPosition(...)`: Main function jo location maangta hai.
          * `(position) => { ... }`: Success callback. `position.coords` mein data milta hai.
          * `(error) => { ... }`: Error callback. (e.g., User ne GPS band kiya hua hai).
          * `enableHighAccuracy: true`: Phone ke 'fine' GPS ko use karne ko bolta hai (slow par accurate). `false` karne par 'coarse' (WiFi/Network) location (fast par less accurate) milti hai.
      * **🚀 Quick run expected output:** Button dabane par (Android par) permission popup aayega. "OK" karne par screen par user ka Latitude aur Longitude dikhega.

8.  **🐞 Common beginner mistakes:**

      * Native permissions (`AndroidManifest.xml` / `Info.plist`) mein location (`ACCESS_FINE_LOCATION`) add karna **bhool jaana**. 🛑 (App crash).
      * (Note 13.8) JS/Runtime permissions (`PermissionsAndroid.request`) maangna bhool jaana. (API error dega).
      * `enableHighAccuracy: true` ko test karna (emulator par jo GPS nahi hai) aur `timeout` (15 sec) error milna.

9.  **🌍 Real-world example / use-case:**

      * (Note 37) **Swiggy/Zomato:** `getCurrentPosition` se delivery address set karna.
      * **Uber/Ola:** `watchPosition` se driver (ya user) ki location ko live track karna.
      * **Weather App:** Current location ke basis par mausam dikhana.
      * **Advanced (Note 39):** `BackgroundGeolocation` (Module 12.8) - Jab app band ho tabhi location track karna (jaise 'Strava' running app).

10. **✅ Quick checklist / TL;DR:**

      * `@react-native-community/geolocation` use karo.
      * Native + JS permissions (Dono) zaroori hain.
      * `getCurrentPosition` = Ek baar location.
      * `watchPosition` = Live tracking.

11. **❓ FAQs:**

      * **Q: Location hamesha galat (ya 'null') kyun aa rahi hai?**
      * A: Check karo (1) Permissions di hain, (2) Phone ka GPS (Location service) ON hai, (3) Emulator (agar use kar rahe ho) mein location set hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  `getCurrentPosition` ko `watchPosition` se badlo.
    2.  `setLocation` ko `console.log` mein daalo (taaki state baar-baar set na ho).
    3.  Emulator mein location change karke dekho (ya real device par chal kar dekho), console mein location updates aane lagenge.

13. **📚 Further reading / commands / links:**

      * `npm install @react-native-community/geolocation`
      * [Geolocation Library Docs](https://github.com/react-native-geolocation/react-native-geolocation)

-----

## 12.4: `Local Authentication` (Fingerprint / Face ID) (Note 41)

1.  **🎯 Title / Short Summary:** Local Authentication - Fingerprint ya Face ID se App Unlock Karna.

2.  **🤔 Kya hai? (What?):** Yeh user ko app ke *andar* (app open karne par ya payment karne par) phone ke built-in hardware (Fingerprint Sensor, Face ID) se authenticate (verify) karwane ka tareeka hai. (Note 41).

3.  **💡 Kyun important hai? (Why?):**

      * **Security:** Yeh app ki security badhata hai. (e.g., Payment apps).
      * **Convenience (Aasani):** User ko baar-baar 6-digit PIN ya password nahi daalna padta. Sirf touch karke app unlock ho jaati hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * App launch (open) hone par (e.g., WhatsApp chat lock).
      * Payment confirm karne se pehle (e.g., GPay, PhonePe).
      * "Settings" jaise sensitive (naazuk) area ko protect karne ke liye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User ko aapki secure app (e.g., banking) use karne ke liye har baar manual PIN/Password daalna padega, jo frustrating (pareshan karne waala) hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `react-native-keychain` (Credentials save karne ke liye) ya `react-native-biometrics` (Direct check karne ke liye).
    *`react-native-biometrics`* (Simple & Direct)

    1.  `npm install react-native-biometrics`.
    2.  Native setup: `AndroidManifest.xml` (Android) mein `USE_BIOMETRIC` permission aur `Info.plist` (iOS) mein `NSFaceIDUsageDescription` (Face ID ka reason) add karna padta hai.
    3.  **`rnBiometrics.isSensorAvailable()`:** Check karta hai ki phone mein Fingerprint/FaceID hardware *hai* ya nahi.
    4.  **`rnBiometrics.simplePrompt({ promptMessage: '...' })`:** OS (Android/iOS) ka default Biometric popup (dialog) dikhata hai.
    5.  Agar success (user ne scan kiya) -\> Promise resolve.
    6.  Agar fail (cancel kiya ya match nahi hua) -\> Promise reject (error).

7.  **💻 Code example (Using `react-native-biometrics`):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-biometrics

    import React from 'react';
    import { View, Button, Alert } from 'react-native';
    import ReactNativeBiometrics from 'react-native-biometrics';

    const rnBiometrics = new ReactNativeBiometrics(); // (v3+ style)

    function BiometricScreen() {

      const handleBiometricAuth = async () => {
        // 1. Check karo sensor hai ya nahi
        const { available, biometryType } = await rnBiometrics.isSensorAvailable();

        if (!available) {
          Alert.alert('Sorry', 'Aapke phone par Biometrics available nahi hain.');
          return;
        }

        console.log('Sensor type:', biometryType); // e.g., 'FaceID', 'TouchID', 'Biometrics' (Android)
        
        try {
          // 2. OS ka popup dikhao
          const { success } = await rnBiometrics.simplePrompt({
            promptMessage: 'Confirm your identity',
            cancelButtonText: 'Cancel',
            // fallbackButtonText: 'Use PIN', // (Optional)
          });

          // 3. Result ko handle karo
          if (success) {
            Alert.alert('Success!', 'Aap verify ho gaye.');
            // (Ab user ko payment karne do ya app unlock karo)
          } else {
            Alert.alert('Failed', 'Authentication fail ho gaya.');
          }
        } catch (error) {
          // (User ne 'Cancel' dabaya ya 3 baar fail ho gaya)
          console.log('Biometric error:', error);
          Alert.alert('Cancelled', 'Authentication cancel kar diya gaya.');
        }
      };

      return (
        <View>
          <Button title="Unlock/Verify (Touch ID)" onPress={handleBiometricAuth} />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `rnBiometrics.isSensorAvailable()`: Pehle check kiya ki phone mein hardware (e.g., TouchID) hai bhi ya nahi.
          * `rnBiometrics.simplePrompt(...)`: Yeh OS (Android/iOS) ke *apne* (native) popup ko trigger karta hai. Humara UI nahi, OS ka UI dikhta hai.
          * `promptMessage: 'Confirm...'`: Yeh text popup mein dikhega.
          * `if (success)`: Agar `simplePrompt` success (true) return karta hai, matlab user ka fingerprint/face match ho gaya.
          * `catch (error)`: Agar user `Cancel` button dabata hai, toh yeh `catch` block mein jaata hai.
      * **🚀 Quick run expected output:** (Real device par hi chalta hai, emulator par nahi). Button dabane par phone ka default Fingerprint/Face ID popup khulega. Scan karne par "Success" alert aayega.

8.  **🐞 Common beginner mistakes:**

      * Native permissions (`USE_BIOMETRIC`, `NSFaceIDUsageDescription`) `Info.plist`/`AndroidManifest.xml` mein add karna **bhool jaana**. 🛑 (Crash).
      * Emulator par test karna. (Biometrics aksar real device par hi chalte hain).
      * `isSensorAvailable` ko check *na* karna (aur jiss phone mein sensor nahi, wahan `simplePrompt` call karke crash karwa dena).

9.  **🌍 Real-world example / use-case:**

      * (Note 41) **Google Pay / PhonePe:** Payment karne se pehle "Confirm" karwana.
      * **WhatsApp:** App kholte hi "Chat Lock" ko biometrics se unlock karna.
      * Banking apps (HDFC, ICICI) mein login karne ke liye.

10. **✅ Quick checklist / TL;DR:**

      * `react-native-biometrics` library use karo.
      * Native permissions (plist/manifest) zaroori hain.
      * `isSensorAvailable()` se pehle check karo.
      * `simplePrompt()` se OS ka popup dikhao.
      * Yeh Emulator par nahi, **Real Device** par test hota hai.

11. **❓ FAQs:**

      * **Q: `react-native-keychain` kya hai?**
      * A: `Keychain` (iOS) / `Keystore` (Android) phone ka *secure* vault hai. `react-native-keychain` library password/token ko *wahan* save karti hai aur *biometrics* se protect karti hai. `react-native-biometrics` (jo humne dekha) sirf *check* karta hai, kuch *save* nahi karta.

12. **🏋️‍♀️ Practice exercise:**

    1.  (Yeh real device par hi hoga). `isSensorAvailable()` ke response (`biometryType`) ko `Alert` karke dekho (taaki pata chale aapke phone mein 'FaceID' hai ya 'Biometrics' (fingerprint)).

13. **📚 Further reading / commands / links:**

      * `npm install react-native-biometrics`
      * [react-native-biometrics Docs](https://github.com/SelfLender/react-native-biometrics)

-----

## 12.5: Linking Native Modules (Custom Java/Swift code ko jodna)

1.  **🎯 Title / Short Summary:** Native Modules - Custom Java/Kotlin (Android) ya Swift/ObjC (iOS) Code Likhna aur Use React Native (JS) se Call Karna.

2.  **🤔 Kya hai? (What?):** Yeh "React Native" ka sabse advanced aur powerful feature hai. React Native aapko "bridge" (pul) banane deta hai taaki aapka JavaScript code *seedha* (directly) aapke likhe hue custom Native (Java/Swift) function ko call kar sake.

3.  **💡 Kyun important hai? (Why?):**

      * **Performance:** Agar koi cheez (e.g., Image processing, complex calculation) JS mein *bahut slow* hai, toh aap use Native (Java/Swift) mein likh sakte hain jo 100x fast chalta hai.
      * **Missing Features:** Agar React Native mein koi feature *hai hi nahi* (e.g., koi specific hardware access karna jo 3rd party library mein bhi nahi hai), toh aap uske liye native code khud likh sakte hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab performance *critical* ho (e.g., real-time image processing).
      * Jab aapko existing native (Android/iOS) SDK ko integrate karna ho.
      * Jab 3rd party library maujood na ho.
      * **Yeh "last resort" (aakhri raasta) hai.** 99% kaam 3rd party libraries (jaise `VisionCamera`) se ho jaata hai, jo khud yahi technique use karti hain.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap 100% JavaScript par nirbhar rahenge. Agar koi cheez JS mein slow hai (e.g., video compression), toh aapki app slow rahegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Android - Java):**
    (Yeh process complex hai, overview de raha hoon).

    1.  **Native Side (Java):**
          * `android/app/src/main/java/.../` ke andar ek nayi Java class (e.g., `CalendarModule.java`) banate hain.
          * Yeh class `ReactContextBaseJavaModule` ko `extends` karti hai.
          * Hum `getName()` method (e.g., return `"CalendarModule"`) likhte hain.
          * Hum `@ReactMethod` annotation ke saath ek function (e.g., `public void createCalendarEvent(String name, String location)`) banate hain.
    2.  **Native Side (Java Package):**
          * Ek `CalendarPackage.java` class banate hain jo `ReactPackage` ko implement karti hai.
          * Yeh `CalendarModule` ko "register" karti hai.
    3.  **Native Side (MainApplication.java):**
          * `MainApplication.java` mein `getPackages()` list ke andar `CalendarPackage` ko add karte hain.
    4.  **JS Side (JavaScript):**
          * Hum `NativeModules` (React Native se) import karte hain.
          * `const { CalendarModule } = NativeModules;`
          * Ab hum seedha JS mein `CalendarModule.createCalendarEvent("My Event", "My Location");` call kar sakte hain\!

    <!-- end list -->

      * **Bridge (Pul):** Jab aap JS mein `createCalendarEvent` call karte hain, React Native "Bridge" ke through Java/Kotlin mein `createCalendarEvent` function ko trigger kar deta hai.

7.  **💻 Code example (Sirf JS side - kaisa dikhega):**

    ```javascript
    // (Aapne Android Studio mein Java/Kotlin code likh liya hai)
    // (Aapne Xcode mein Swift/ObjC code likh liya hai)

    // Ab JS code (e.g., App.js) mein:

    import { NativeModules, Button } from 'react-native';

    // 1. Apne custom module ko NativeModules se nikaalna
    // Yeh naam (e.g., 'CalendarModule') wahi hona chahiye jo aapne
    // Java (getName()) ya Swift mein define kiya hai.
    const { CalendarModule, MyCustomSwiftModule } = NativeModules;

    function CustomModuleScreen() {
      
      const onAndroidCall = () => {
        // 2. Native Java/Kotlin function ko seedha JS se call karna
        if (CalendarModule) {
          CalendarModule.createCalendarEvent(
            'Party', 
            'My House',
            (eventId) => { // (Yeh 'Callback' hai jo Native se JS wapas aata hai)
              console.log('Event create ho gaya, ID:', eventId);
            }
          );
        }
      };

      const onIOSCall = () => {
        // (iOS Native function ko call karna)
        if (MyCustomSwiftModule) {
          // (Promises bhi support karta hai)
          MyCustomSwiftModule.doSomethingCool('data')
            .then(result => console.log(result))
            .catch(e => console.error(e));
        }
      };

      return (
        <View>
          <Button 
            title="Call Native Java Code" 
            onPress={onAndroidCall} 
          />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation (JS Side):**
          * `import { NativeModules }`: Humne React Native ka "Bridge" (pul) import kiya.
          * `const { CalendarModule } = NativeModules;`: `NativeModules` ek object hai jismein aapke register kiye hue *saare* custom native modules hote hain. Humne apna `CalendarModule` (jo Java mein banaya) usse nikaal liya.
          * `CalendarModule.createCalendarEvent(...)`: Hum JS mein ek object ka function call kar rahe hain, par yeh *asal mein* background mein Java (Android) function ko run kar raha hai.
      * **🚀 Quick run expected output:** (Native code likhne ke baad). Button dabane par Android (Java) code execute hoga (e.g., Android ka default Calendar khul jaayega).

8.  **🐞 Common beginner mistakes:**

      * Yeh "beginner" topic nahi hai. Yeh *advanced* topic hai.
      * Native code (Java/Swift) mein syntax error karna.
      * Module ko `MainApplication.java` (Android) ya `AppDelegate.m` (iOS) mein register *na* karna. (JS ko module `undefined` milega).
      * `getName()` (Java) mein galat naam return karna.
      * Threading (Native code UI thread par chalana) mein galti karna.

9.  **🌍 Real-world example / use-case:**

      * Har 3rd party library (`VisionCamera`, `Reanimated`, `GestureHandler`) Native Modules par hi bani hai.
      * Agar aapko ek bank ka "Payment SDK" (jo sirf Android/iOS ke liye hai) ko React Native app mein jodna hai, toh aapko yahi (Native Module) bridge banana padega.

10. **✅ Quick checklist / TL;DR:**

      * Yeh JS ko Native (Java/Swift) code call karne deta hai.
      * Performance ya "missing features" ke liye use hota hai.
      * Native side: Code likho (`@ReactMethod`).
      * Native side: Package banao.
      * Native side: Register karo (`MainApplication.java`).
      * JS side: `NativeModules` se import karke call karo.

11. **❓ FAQs:**

      * **Q: Yeh `Turbo Modules` se alag hai?**
      * A: `Turbo Modules` React Native ki "New Architecture" (Fabric) ka Native Modules likhne ka *naya* aur *fast* tareeka hai. Concept same hai, implementation alag (aur zyada efficient) hai. `JSI` (JavaScript Interface) use hota hai, "Bridge" nahi.

12. **🏋️‍♀️ Practice exercise:**

    1.  (Yeh complex hai). React Native ke official docs (neeche link hai) ko follow karke "Hello World" (Toast message) waala simple Native Module (Java) bana kar dekho.

13. **📚 Further reading / commands / links:**

      * [React Native Docs: Native Modules (Android)](https://www.google.com/search?q=https://reactnative.dev/docs/native-modules-android)
      * [React Native Docs: Native Modules (iOS)](https://www.google.com/search?q=https://reactnative.dev/docs/native-modules-ios)

-----

## 12.6: `Device Sensors (Accelerometer)` (Note 37)

1.  **🎯 Title / Short Summary:** Device Sensors - Phone ke Accelerometer (Harkat) ko Detect Karna.

2.  **🤔 Kya hai? (What?):** Yeh phone ke hardware sensors (Accelerometer, Gyroscope, Magnetometer) se *raw data* (x, y, z values) ko real-time mein stream (paana) hai. (Note 37).

      * **Accelerometer:** Phone ki harkat (acceleration) aur gravity (tilt/jhukaav) batata hai.
      * **Gyroscope:** Phone ke rotation (ghoomne) ki speed batata hai.
      * **Magnetometer:** Phone ke aas-paas ka magnetic field (compass) batata hai.

3.  **💡 Kyun important hai? (Why?):** Yeh "immersive" (anubhavik) apps banane ke kaam aata hai jo phone ke *physical* movement par react karti hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Accelerometer:**
          * "Shake" (hilaane) par action trigger karna (e.g., "Undo" ya "Report bug").
          * Game mein character ko phone tilt (jhuka) karke move karna (e.g., Temple Run).
          * Step Counter (Pedometer) apps.
      * **Gyroscope:** 360-degree photo/video viewers, VR (Virtual Reality).
      * **Magnetometer:** Compass (disha) app.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap phone ke "shake" gesture ya "tilt" controls jaise features nahi bana paayenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `react-native-sensors`

    1.  `npm install react-native-sensors`.
    2.  Ismein permissions ki zaroorat *nahi* padti (aksar).
    3.  Library se sensor (e.g., `accelerometer`) ko import karo.
    4.  Sensor data ek "Observable" (stream) hai. Humein use `subscribe` karna padta hai.
    5.  `useEffect` (Module 8.1) mein `subscribe` karo.
    6.  `useEffect` ke *cleanup function* mein `unsubscribe` karna **bahut zaroori** hai (varna memory leak hoga).

7.  **💻 Code example (Accelerometer Data):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-sensors

    import React, { useState, useEffect } from 'react';
    import { View, Text } from 'react-native';
    import { accelerometer, setUpdateIntervalForType, SensorTypes } from 'react-native-sensors';
    import { throttle } from 'lodash'; // (Optional: Faltu re-renders rokne ke liye)

    // Update interval set karna (e.g., har 400ms mein)
    setUpdateIntervalForType(SensorTypes.accelerometer, 400); // (ms)

    function SensorScreen() {
      // 1. State mein X, Y, Z data store karna
      const [data, setData] = useState({ x: 0, y: 0, z: 0 });

      useEffect(() => {
        // 2. Sensor ko 'subscribe' (sunna) shuru karna
        // 'throttle' (ya 'debounce') use karna taaki state har microsecond update na ho
        const subscription = accelerometer.subscribe(
          throttle(({ x, y, z }) => {
            // console.log({ x, y, z });
            setData({ x, y, z });
          }, 500) // Har 500ms mein 1 baar hi state update karo
        );

        // 3. Cleanup function (Sabse zaroori)
        // Jab component unmount ho, toh subscription band kar do
        return () => {
          subscription.unsubscribe();
        };
      }, []); // Khali array (sirf ek baar chalao)

      return (
        <View>
          <Text>Accelerometer Data:</Text>
          {/* Data ko round karke dikhana */}
          <Text>X: {data.x.toFixed(2)}</Text>
          <Text>Y: {data.y.toFixed(2)}</Text>
          <Text>Z: {data.z.toFixed(2)}</Text>
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `setUpdateIntervalForType(...)`: Hum sensor ko bol rahe hain ki "bahut fast data mat bhejo, har 400ms mein bhejo".
          * `accelerometer.subscribe(...)`: Humne accelerometer data stream ko "subscribe" kiya. Yeh humein (x, y, z) values deta rahega.
          * `throttle(..., 500)`: Yeh `lodash` ka ek helper hai. Sensor *bahut* fast data bhejta hai (e.g., 1 second mein 60 baar). Agar hum har baar `setData` call karenge, toh app slow ho jaayegi. `throttle` bolta hai ki "500ms mein sirf ek hi baar `setData` call karna".
          * `subscription.unsubscribe()`: `useEffect` ke `return` (cleanup) function mein humne sensor ko band (unsubscribe) kar diya. Agar yeh nahi kiya, toh component hatne ke baad bhi sensor background mein chalta rahega aur memory leak karega. 🛑
      * **🚀 Quick run expected output:** Screen par X, Y, Z ki values dikhengi. Phone ko hilane (tilt/move) par yeh values real-time mein badlengi.

8.  **🐞 Common beginner mistakes:**

      * `useEffect` ke cleanup function mein `unsubscribe()` call karna **bhool jaana**. 🛑 (Sabse badi galti, isse memory leak aur battery drain hoti hai).
      * `throttle` ya `debounce` use *na* karna, jisse sensor data state ko *bahut* tezi se (60fps) update karta hai, JS thread ko block kar deta hai aur app ko slow kar deta hai.

9.  **🌍 Real-world example / use-case:**

      * (Note 37) **"Shake to Undo"** gesture (iPhone). (Aap `x`, `y`, `z` ki values mein *achaanak* badlaav (spike) detect karte hain).
      * **Step Counter (Pedometer):** `accelerometer` data ko analyze karke steps (kadam) ginta hai.
      * **Temple Run / Racing Games:** Phone ko 'tilt' (jhuka) karke 'X' ya 'Y' value ke basis par player ko move karna.

10. **✅ Quick checklist / TL;DR:**

      * `react-native-sensors` library use karo.
      * Sensor ko `subscribe` karo.
      * `throttle` / `debounce` zaroor use karo (performance ke liye).
      * `unsubscribe` karna *kabhi mat bhoolo* (cleanup function mein).

11. **❓ FAQs:**

      * **Q: "Shake" kaise detect karein?**
      * A: Aapko `x`, `y`, `z` ki values ko `useState` (ya `useRef`) mein store karke pichli value se compare karna hota hai. Agar difference ek "threshold" (limit) se zyada ho, toh woh 'shake' hai. (Ya `react-native-shake` jaisi ready-made library use karo).

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye code mein `gyroscope` (accelerometer ki jagah) import karke dekho.
    2.  Phone ko rotate (ghuma) kar ke dekho, values change hongi.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-sensors`
      * [react-native-sensors Docs](https://react-native-sensors.github.io/)

-----

## 12.7: `Bluetooth (BLE)` (Note 37)

1.  **🎯 Title / Short Summary:** Bluetooth (BLE) - Smart Devices (Watch, Bands, Lights) se Connect Hona.

2.  **🤔 Kya hai? (What?):** Yeh phone ke Bluetooth hardware ko access karke aas-paas ke *BLE (Bluetooth Low Energy)* devices (jaise Smart Watch, Fitness Band, Heart-rate monitor, Smart Lights) ko *scan* (dhoondhna) aur unse *connect* (baat) karne ka tareeka hai. (Note 37).

3.  **💡 Kyun important hai? (Why?):** Yeh "IoT" (Internet of Things) apps ke liye critical hai. Iske bina, "Mi Fit" app "Mi Band" se connect nahi kar paati.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab aapko Smart Watch, Fitness Band, ya BLE sensor se connect karna ho.
      * Jab aapko "beacon" (BLE signal chhodne waale device) detect karna ho (e.t., museum guide).
      * *Note:* Yeh music speakers (Classic Bluetooth) se connect karne ke liye *nahi* hai, yeh "Low Energy" (chote) devices ke liye hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapki app phone ke aas-paas ke smart IoT devices se baat nahi kar paayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    (Yeh *bahut* complex hai, overview de raha hoon).
    **Library:** `react-native-ble-plx` (Sabse popular)

    1.  **Permissions:** `AndroidManifest.xml` (Android) mein `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT` (Android 12+) aur `ACCESS_FINE_LOCATION` (BLE scan ke liye zaroori) permissions chahiye. `Info.plist` (iOS) mein `NSBluetoothAlwaysUsageDescription`.
    2.  **Manager:** `BleManager` (library ka main object) ko initialize karna.
    3.  **Permissions (JS):** Runtime (JS) par Bluetooth aur Location (Android) permissions maangna.
    4.  **Scan:** `manager.startDeviceScan()` call karna. Yeh aas-paas ke BLE devices ko (jab woh 'advertising' kar rahe hon) dhoondhna shuru kar deta hai.
    5.  **Connect:** Jab device mil jaaye (e.g., `device.name === 'Mi Band 4'`), toh `manager.stopDeviceScan()` karke `device.connect()` call karna.
    6.  **Discover:** Connect hone ke baad, `device.discoverAllServicesAndCharacteristics()` call karna. (Har device mein "Services" (e.g., 'Heart Rate') aur "Characteristics" (e.g., 'Current Heart Rate Value') hoti hain).
    7.  **Read/Write/Monitor:** Aap `device.readCharacteristic(...)` (data padhna) ya `device.writeCharacteristic(...)` (data bhejna) ya `device.monitorCharacteristic(...)` (data real-time mein sunna) kar sakte hain.

7.  **💻 Code example (Sirf Scanning part):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-ble-plx
    // (Android 12+ ke liye 'react-native-permissions' bhi zaroori hai)

    import React, { useState, useEffect } from 'react';
    import { View, Text, Button, FlatList } from 'react-native';
    import { BleManager } from 'react-native-ble-plx';
    import { PermissionsAndroid } from 'react-native'; // (Note 13.8)

    // 1. Manager ko initialize karna (app start par ek baar)
    const manager = new BleManager();

    function BLEScreen() {
      const [devices, setDevices] = useState([]); // Mile hue devices ki list

      // 2. Android 12+ (API 31) ke liye permissions
      const requestBluetoothPermission = async () => {
        const grantedScan = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.BLUETOOTH_SCAN,
        );
        const grantedConnect = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.BLUETOOTH_CONNECT,
        );
        // (Location permission bhi zaroori hoti hai)
        
        return grantedScan === 'granted' && grantedConnect === 'granted';
      };

      // 3. Scan function
      const startScan = async () => {
        const permissionsGranted = await requestBluetoothPermission();
        if (!permissionsGranted) {
          console.log('Permission nahi mili');
          return;
        }

        console.log('Scanning shuru...');
        setDevices([]); // Purani list saaf karo

        // 4. Scan shuru karna
        manager.startDeviceScan(null, null, (error, device) => {
          if (error) {
            console.error('Scan Error:', error);
            manager.stopDeviceScan();
            return;
          }

          // 5. Device milne par list mein add karna
          if (device && device.name) { // Sirf naam waale device dikhao
            console.log('Device mila:', device.name, device.id);
            setDevices((prevDevices) => {
              // Duplicate check
              if (!prevDevices.find((d) => d.id === device.id)) {
                return [...prevDevices, device];
              }
              return prevDevices;
            });
          }
        });

        // 5 second baad scan rok do
        setTimeout(() => {
          manager.stopDeviceScan();
          console.log('Scan Roka.');
        }, 5000);
      };

      return (
        <View>
          <Button title="Scan for BLE Devices" onPress={startScan} />
          <FlatList
            data={devices}
            keyExtractor={(item) => item.id}
            renderItem={({ item }) => <Text>{item.name} (ID: {item.id})</Text>}
          />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `const manager = new BleManager()`: BLE library ka main controller banaya.
          * `requestBluetoothPermission`: (Note 13.8) Android 12+ par `BLUETOOTH_SCAN` aur `BLUETOOTH_CONNECT` permissions *maangna* padta hai.
          * `manager.startDeviceScan(null, null, (error, device) => ...)`: Scan shuru kiya. Yeh *har* device milne par is callback function ko call karega.
          * `if (device && device.name)`: Humne filter kiya ki sirf wahi device list mein daalo jinka koi naam ho.
          * `setDevices(...)`: Device ko state (list) mein add kiya (duplicate check ke saath).
          * `setTimeout(() => manager.stopDeviceScan(), 5000)`: Scan hamesha chalta rehta hai (battery drain). Humne use 5 second baad *rok* diya.
      * **🚀 Quick run expected output:** (Real device + Bluetooth ON karke). Button dabane par 5 second tak scanning hogi aur screen par aas-paas ke BLE devices (e.g., Smart Watch, TV, dusre phones) ke naam dikhne lagenge.

8.  **🐞 Common beginner mistakes:**

      * **(Note 13.8) Permissions\!** `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT` (Android 12+) aur `ACCESS_FINE_LOCATION` (Android 10+) permissions `AndroidManifest.xml` mein *aur* runtime (JS) par maangna bhool jaana. 🛑 (Scan kaam nahi karega).
      * `stopDeviceScan()` call karna bhool jaana (jisse battery drain hoti rehti hai).
      * Sochna ki yeh normal speakers (Classic Bluetooth) ko connect kar lega. (Nahi, yeh sirf BLE ke liye hai).

9.  **🌍 Real-world example / use-case:**

      * (Note 37) **Mi Fit / Boat / Noise app:** Fitness band se connect karke steps aur heart rate data *sync* (read) karna.
      * **Smart Home app:** Smart light (BLE) se connect karke uska color *change* (write) karna.

10. **✅ Quick checklist / TL;DR:**

      * `react-native-ble-plx` library use karo.
      * Yeh *BLE* (Low Energy) ke liye hai, Classic Bluetooth nahi.
      * Permissions (Manifest + JS) *bahut* zaroori hain (Bluetooth + Location).
      * Flow: `Scan` -\> `Stop Scan` -\> `Connect` -\> `Discover` -\> `Read/Write`.

11. **❓ FAQs:**

      * **Q: Bahut complex hai, aasan tareeka hai?**
      * A: Nahi. BLE communication inherently (apne aap mein) complex hota hai (services, characteristics). Yeh library use aasan banati hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  (Real device zaroori). Upar diye code ko chalao.
    2.  Apne Bluetooth settings mein jao aur dekho ki kitne device (e.g., earbuds, watch) hain. Dekho ki scan list mein unke naam aate hain ya nahi.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-ble-plx`
      * [react-native-ble-plx Docs](https://github.com/dotintent/react-native-ble-plx)

-----

## 12.8: `Background Tasks` (Timer, Fetch, Geolocation, Headless JS)

1.  **🎯 Title / Short Summary:** Background Tasks - Jab App Band (Background mein) ho, tab Code Chalana.

2.  **🤔 Kya hai? (What?):** Yeh woh techniques hain jisse aapki app *thoda* code (JS) run kar sakti hai, bhale hi user app ko minimize (background) kar de ya kill kar de. (Note 39).

3.  **💡 Kyun important hai? (Why?):** Iske bina, jaise hi user app minimize karega, aapki app "mar" jaayegi. Aap background mein data sync, location track, ya timer nahi chala paayenge.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **`BackgroundTimer` (Note 2):** Jab aapko *foreground* mein (app khuli hai) lamba `setTimeout` (e.g., 30 min) chalana ho jo app *background* jaane par bhi *na* ruke.
      * **`BackgroundFetch` (Note 39):** Jab app band ho, tab har 15-30 min mein *chupke se* (silently) data fetch karna ho (e.g., naye news articles).
      * **`BackgroundGeolocation` (Note 39):** Jab app band ho, tab user ki location track karni ho (e.g., running app, food delivery driver).
      * **`Headless JS` (Note 39):** Jab *Push Notification* (FCM) aaye (Module 12.1), tab app ko *bina khole* background mein code chalana ho (e.g., message save karna).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Normal `setTimeout` app background jaate hi (iOS par) ruk jaayega.
      * Aapki app ka data "baasi" (stale) rahega (jab tak user app kholega nahi).
      * Strava jaisi running app track nahi kar paayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    -----

    ### 1\. `BackgroundTimer` (Note 2)

      * **Library:** `react-native-background-timer`
      * **Problem:** React Native ka default `setTimeout` iOS par background mein 5 min baad band ho jaata hai.
      * **Solution:** Yeh library native (Java/Swift) timer use karti hai jo chalta rehta hai.
      * **Code:**
        ```js
        import BackgroundTimer from 'react-native-background-timer';
        // (App foreground mein hai, par background jaane par bhi chalega)
        BackgroundTimer.setTimeout(() => {
          console.log('30 minute ho gaye! (Background mein bhi)');
        }, 30 * 60 * 1000);
        ```
      * **Use-case:** OTP session (30 min) timeout karna. (Note 2).

    -----

    ### 2\. `BackgroundFetch` (Note 39)

      * **Library:** `react-native-background-fetch`
      * **Problem:** Har 30 min mein naye news articles check karne hain.
      * **Solution:** Yeh OS (Android/iOS) ko "request" karta hai. OS *apni marzi se* (jab phone idle ho, battery ho) har 15-30 min mein aapki app ko "jaagane" (wake up) ka mauka deta hai.
      * **Code:**
        ```js
        import BackgroundFetch from 'react-native-background-fetch';
        // (index.js ya App.js)
        BackgroundFetch.configure({
          minimumFetchInterval: 15, // (min. 15 minute)
        }, async (taskId) => {
          console.log('Background Fetch chala!');
          // (Yahan 'fetchNews()' chalao)
          BackgroundFetch.finish(taskId); // OS ko batao kaam khatam
        }, (error) => {
          console.log('BG Fetch fail', error);
        });
        ```

    -----

    ### 3\. `BackgroundGeolocation` (Note 39)

      * **Library:** `react-native-background-geolocation` (Yeh Paid/Premium hai par sabse achhi hai).
      * **Problem:** (Note 37) `watchPosition` (Module 12.3) app band hone par ruk jaata hai.
      * **Solution:** Yeh library phone ke native location system ko use karti hai. Jab phone 'move' hota hai, yeh app ko 'wake up' karti hai aur location data aapke server par HTTP POST karti hai.
      * **Use-case:** Strava (Running), Uber (Driver app).

    -----

    ### 4\. `Headless JS` (Note 39)

      * **Library:** `react-native-firebase` (FCM) ke saath built-in aata hai.
      * **Problem:** (Note 39) Push Notification (FCM) aayi, par user ne click nahi kiya. Humein data background mein save karna hai.
      * **Solution:** Yeh (sirf Android par) app ko *bina khole* background mein JS chalane deta hai.
      * **Code (index.js mein):**
        ```js
        import messaging from '@react-native-firebase/messaging';

        // (Yeh function 'index.js' mein register hota hai, App.js ke bahar)
        messaging().setBackgroundMessageHandler(async (remoteMessage) => {
          console.log('Message background mein handle hua (Headless JS)!', remoteMessage);
          // (Yahan database mein message save karo)
        });
        ```

7.  **🐞 Common beginner mistakes:**

      * Sochna ki background task *guaranteed* chalega. (Nahi, OS (khaaskar iOS) battery bachaane ke liye tasks ko *rok* sakta hai).
      * `BackgroundTimer` ka `stopTimeout` call na karna (memory leak).
      * `BackgroundFetch` ke `finish(taskId)` ko call na karna (OS aapki app ko block kar dega).

8.  **🌍 Real-world example / use-case:**

      * **Timer:** Bank app ka session timeout.
      * **Fetch:** News/Weather app ka data sync karna.
      * **Geolocation:** Strava/Uber.
      * **Headless JS:** WhatsApp (message notification aane par hi data save kar lena).

9.  **✅ Quick checklist / TL;DR:**

      * Background code chalane ke 4 main tareeke hain, sab alag-alag kaam ke liye hain.
      * `Timer`: Lamba timeout.
      * `Fetch`: Thode-thode time (15-30 min) par data sync.
      * `Geolocation`: App band hone par location tracking.
      * `Headless JS`: (Android only) Notification aane par code chalana.

10. **❓ FAQs:**

      * **Q: iOS par `Headless JS` (FCM) kyun nahi chalta?**
      * A: iOS "Silent Push Notifications" (Data-only) ka concept use karta hai, jo `AppDelegate` (Native code) mein handle hota hai. `react-native-firebase` isko thoda handle karta hai, par Android jitna reliable nahi.

11. **🏋️‍♀️ Practice exercise:**

    1.  `react-native-background-timer` install karo.
    2.  Ek `BackgroundTimer.setTimeout` (1 min ka) set karo.
    3.  `console.log` laga do. App ko minimize karke dekho, 1 min baad (terminal mein) log aa jaayega.

12. **📚 Further reading / commands / links:**

      * `npm install react-native-background-timer`
      * `npm install react-native-background-fetch`
      * [RN Firebase Docs (Headless JS)](https://www.google.com/search?q=https://rnfirebase.io/messaging/usage%23background-application-state)

-----

## 12.9: `Screenshot Prevention` (Note 43)

1.  **🎯 Title / Short Summary:** Screenshot Prevention - User ko App ka Screenshot Lene se Rokna.

2.  **🤔 Kya hai? (What?):** Yeh ek tareeka hai jisse hum *native* (OS) level par app ko bolte hain ki "iss screen ka content secure hai, iska screenshot (ya screen recording) allow mat karo". (Note 43).

3.  **💡 Kyun important hai? (Why?):**

      * **Security:** Banking apps (Account balance, QR code), Password manager, ya content apps (Netflix) nahi chahte ki user unke secure data ka screenshot le le.
      * **Privacy:** Snapchat jaisi apps privacy ke liye ise use karti hain.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Payment screen (QR Code, card details).
      * Bank account balance/statement screen.
      * Video streaming (DRM content) screen (e.g., Netflix).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * User aapki app ke *sensitive* (naazuk) data (jaise bank balance, credit card number) ka screenshot le sakta hai, jo ek bada security risk hai.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `react-native-screenshot-prevent` (ya native code se).

      * **Android (Native Code):**
          * Yeh *bahut aasan* hai. Aapko `MainActivity.java` (main native file) mein `onCreate` method ke andar sirf 1 line add karni hoti hai:
          * `getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);`
          * Isse *poori app* ka screenshot block ho jaata hai. (Screenshot kaala/blank aata hai).
      * **iOS (Tricky):**
          * iOS par screenshot ko *block* karna (Android ki tarah) *allowed nahi hai* (OS level par).
          * Snapchat/Signal jaisi apps "screenshot detection" (pata lagana) use karti hain.
          * Library (e.g., `react-native-screenshot-prevent`) ek "hack" use karti hai: woh ek hidden text field (secure) ko screen par active karti hai jisse screen recording kaali ho jaati hai, par screenshot (iOS 13+) *shayad* na ruke.
      * **Library (react-native-screenshot-prevent):**
          * Yeh library Android par wahi `FLAG_SECURE` ko JS se control karne deti hai.
          * `import { preventScreenCapture, allowScreenCapture } from 'react-native-screenshot-prevent';`
          * `preventScreenCapture();` (Screenshot block chalu).
          * `allowScreenCapture();` (Screenshot block band).

7.  **💻 Code example (Using library):**

    ```javascript
    // Pehle install karein:
    // npm install react-native-screenshot-prevent

    import React, { useEffect } from 'react';
    import { View, Text } from 'react-native';
    import { preventScreenCapture, allowScreenCapture } from 'react-native-screenshot-prevent';
    import { useFocusEffect } from '@react-navigation/native'; // (Module 8.6)

    function SecureBankingScreen() {
      
      // (Module 8.6)
      // Jab user is screen par 'focus' (aaye)
      useFocusEffect(
        React.useCallback(() => {
          // 1. Screenshot block chalu karo
          console.log('Secure screen: Screenshot Blocked!');
          preventScreenCapture();

          // 2. Cleanup: Jab user is screen se 'blur' (hate)
          return () => {
            console.log('Non-secure screen: Screenshot Allowed.');
            allowScreenCapture();
          };
        }, [])
      );

      return (
        <View>
          <Text>Aapka Bank Balance: $1,000,000</Text>
          <Text>(Aap iska screenshot nahi le sakte - Android par)</Text>
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `import { ... } from 'react-native-screenshot-prevent';`: Library se functions import kiye.
          * `useFocusEffect(...)`: Humne (Module 8.6) `useFocusEffect` use kiya.
          * `preventScreenCapture()`: Jaise hi user `SecureBankingScreen` par aaya, humne screenshot block chalu kar diya.
          * `return () => { allowScreenCapture(); }`: **(Sabse zaroori)** `useFocusEffect` ke *cleanup function* mein, jab user is screen se *hat* kar doosri (non-secure) screen (e.g., Home) par jaaye, humne screenshot block *hata* (allow) diya. Agar yeh nahi karte, toh poori app block ho jaati.
      * **🚀 Quick run expected output:**
          * **Android:** Jab yeh screen khuli hogi, user screenshot lega toh "Couldn't take screenshot" (ya blank image) aayega. Jab Home screen par jaayega, tab screenshot le paayega.
          * **iOS:** Screenshot *shayad* le paaye, par screen recording (video) blank (kaali) aayegi.

8.  **🐞 Common beginner mistakes:**

      * `allowScreenCapture()` (cleanup) ko call karna *bhool jaana*, jisse user poori app mein kahin bhi screenshot nahi le paata.
      * Sochna ki yeh iOS par 100% (Android jaisa) kaam karega. (Nahi, iOS par "detection" behtar hai, "prevention" mushkil).

9.  **🌍 Real-world example / use-case:**

      * (Note 43) **GPay / PhonePe:** Payment (QR code) screen par.
      * **Netflix / Hotstar:** Video chalte waqt (DRM content).
      * **Signal / Snapchat:** Privacy ke liye.

10. **✅ Quick checklist / TL;DR:**

      * `react-native-screenshot-prevent` library.
      * `preventScreenCapture()` (block).
      * `allowScreenCapture()` (unblock).
      * `useFocusEffect` (ya `useEffect`) mein *cleanup* (return function) mein `allow` call karna *bahut zaroori* hai.
      * Android par 100% block, iOS par limited (recording ruk jaati hai).

11. **❓ FAQs:**

      * **Q: Kya pata kar sakte hain ki user ne screenshot liya?**
      * A: Haan, `react-native-screenshot-detector` jaisi alag libraries aati hain jo "detection" (pata lagana) karti hain. Tab aap user ko warning dikha sakte hain (jaise Snapchat karta hai).

12. **🏋️‍♀️ Practice exercise:**

    1.  (Android par). Library install karke `preventScreenCapture()` ko `App.js` mein call karo (bina cleanup ke).
    2.  Dekho, poori app mein screenshot block ho jaayega.
    3.  Ab `useFocusEffect` waala code `SecureBankingScreen` par laga kar dekho.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-screenshot-prevent`
      * [react-native-screenshot-prevent Docs](https://github.com/killserver/react-native-screenshot-prevent)

=============================================================

# MODULE-13 → Testing, Deployment & TypeScript

Module 13 mein hum seekhenge ki app ko **release (launch)** kaise karte hain. Ismein hum app ko *Test* karna, *Deploy* (publish) karna, aur *Maintain* karna seekhenge. Yeh "Zero-to-Professional" guide ka "Professional" wala hissa hai. 🚀

-----

## 13.1: TypeScript (React Native ke saath setup karna)

1.  **🎯 Title / Short Summary:** TypeScript (TS) - Code mein "Type-Checking" (Errors) ko Compile-Time par Pakadna.

2.  **🤔 Kya hai? (What?):** TypeScript JavaScript (JS) ka ek "superset" (JS + Extra Features) hai. Iska sabse bada feature hai **Static Typing**. Aam JS mein aap `let x = 10;` ke baad `x = "hello";` kar sakte hain, par TS mein nahi.

3.  **💡 Kyun important hai? (Why?):**

      * **Kam Bugs:** Yeh "Type Errors" (jaise `undefined.function()`) ko *run-time* (app chalne par) se hata kar *compile-time* (code likhte waqt) par hi pakad leta hai.
      * **Auto-completion:** Code editor (VS Code) ko pata hota hai ki `user.` ke baad `name` aayega ya `email` (kyunki aapne "Type" define kiya hai), jisse development fast hota hai.
      * **Maintainability:** Badi (large-scale) apps ke liye TS zaroori hai. Isse code padhna aur maintain karna aasan hota hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Hamesha\!** Aaj kal (2024+), har naye professional React Native project ko TypeScript ke saath hi shuru karna chahiye.
      * Jab aap team mein kaam kar rahe hon (taaki sabka code consistent rahe).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapko `undefined is not a function` ya `props.user.name` (jabki `name` tha hi nahi) jaise run-time errors aate rahenge. 🛑
      * Badi apps ko maintain karna "nightmare" (bura sapna) ban jaayega.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  **Setup:** Naya RN project shuru karte waqt `npx react-native init MyApp --template react-native-template-typescript` command deni hoti hai.
    2.  **Files:** Aapki files `.js` ki jagah `.tsx` (TS + JSX) ya `.ts` (Normal TS) hongi.
    3.  **`tsconfig.json`:** Yeh file TS ke rules define karti hai.
    4.  **Typing (Main concept):**
          * Aap "Interface" ya "Type" banate hain jo 'props' ya 'state' ka "shape" (structure) batata hai.
          * e.g., `type UserProps = { name: string; age: number; }`
          * Fir aap component ko batate hain: `const UserCard = (props: UserProps) => { ... }`
          * Ab agar aap `props.ag` (typo) likhenge, VS Code *turant* error de dega.

7.  **💻 Code example (Setup aur Component):**

    ```bash
    # 1. Naya TS Project banana
    npx react-native init MyApp --template react-native-template-typescript

    # (Ya existing JS project mein 'typescript' add karna - jo mushkil hai)
    ```

    ```typescript
    // (MyApp/src/components/UserCard.tsx)

    import React from 'react';
    import { View, Text } from 'react-native';

    // 1. Props ka "Type" (shape) define karna
    type UserCardProps = {
      user: {
        id: string;
        name: string;
        age: number; // 'age' hamesha 'number' hona chahiye
      };
      onPress: () => void; // 'onPress' ek function hona chahiye jo kuch return nahi karta
    };

    // 2. Component ko batana ki woh 'UserCardProps' type ke props lega
    // (FC = Functional Component)
    const UserCard: React.FC<UserCardProps> = ({ user, onPress }) => {
      
      // 3. (Error) Agar aap yeh line likhenge, TS error dega:
      // const badData = user.email; 
      // Error: Property 'email' does not exist on type '{ id: string; name: string; age: number; }'.

      // 4. (Error) Agar aap 'age' ko text mein daalenge, TS error dega:
      // <Text>{user.age + " saal"}</Text> 
      // Error: Operator '+' cannot be applied to types 'number' and 'string'.

      return (
        <View onTouchEnd={onPress}>
          <Text>{user.name} ({user.age})</Text>
        </View>
      );
    };

    export default UserCard;
    ```

      * **✍️ Line-by-line explanation:**
          * `npx ... --template ...typescript`: Humne RN CLI ko bola ki "TypeScript" template waala project banao.
          * `type UserCardProps = { ... }`: Humne ek "type" (contract) banaya.
          * `name: string; age: number;`: Humne bataya ki `name` string hi hoga aur `age` number hi.
          * `onPress: () => void;`: Humne bataya `onPress` ek function hoga.
          * `React.FC<UserCardProps>`: Humne component ko `UserCardProps` contract se *jod* diya.
      * **🚀 Quick run expected output:** (Yeh run-time par nahi, development-time (VS Code) mein dikhega). Jaise hi aap `user.email` (jo type mein nahi hai) likhenge, VS Code mein laal (red) underline aa jaayega.

8.  **🐞 Common beginner mistakes:**

      * Har cheez ko `any` type kar dena (e.g., `props: any`). Yeh TS ko "band" (disable) karne jaisa hai aur TS ka poora purpose ( مقصد) khatam kar deta hai. 🛑
      * `.js` project mein `.tsx` file add karna (bina `tsconfig.json` setup kiye).
      * Library (e.g., `react-navigation`) ke types install na karna (e.g., `npm install @types/react-navigation`).

9.  **🌍 Real-world example / use-case:**

      * Har badi company (Microsoft, Google, Facebook, Airbnb) ab TS hi use karti hai.
      * Aapke poore React Native project ko stable (bharosemand) rakhne ke liye.

10. **✅ Quick checklist / TL;DR:**

      * TS (TypeScript) = JS + Types (Rules).
      * `npx ... --template ...typescript` se shuru karo.
      * `.tsx` files use karo.
      * `type` ya `interface` se 'Props' aur 'State' ka shape (contract) define karo.
      * `any` type use *mat* karo.

11. **❓ FAQs:**

      * **Q: Kya TS seekhna zaroori hai?**
      * A: Haan. 2024+ mein React/RN developer ke liye TS 'optional' nahi, 'zaroori' hai.
      * **Q: Kya yeh app ko slow karta hai?**
      * A: Nahi. TS *sirf* development (coding) ke time hota hai. Jab app *build* hoti hai, toh TS poora *compile* hokar normal JavaScript (JS) mein badal jaata hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Upar diye `UserCardProps` type mein `email?: string;` (question mark `?` ke saath) add karo.
    2.  `?` ka matlab hai yeh prop "optional" (zaroori nahi) hai.
    3.  Component mein `user.email` use karke dekho (ab error nahi aayega).

13. **📚 Further reading / commands / links:**

      * `npx react-native init MyApp --template react-native-template-typescript`
      * [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

-----

## 13.2: Unit Testing (Jest & React Native Testing Library)

1.  **🎯 Title / Short Summary:** Unit Testing - Check Karna ki Aapka Component/Function Sahi Kaam Kar Raha Hai.

2.  **🤔 Kya hai? (What?):** Unit Test ek *chota* code hai jo aapke *asli* code (e.g., ek function ya ek component) ko "test" karta hai.

      * **Jest:** React Native ke saath default mein aata hai. Yeh test "runner" hai.
      * **React Native Testing Library (RTL):** Yeh components (UI) ko test karne ka *modern* tareeka hai. Yeh check karta hai ki component *user* ko kaisa dikh raha hai (e.g., "Kya screen par 'Login' button hai?").

3.  **💡 Kyun important hai? (Why?):**

      * **Confidence (Bharosa):** Isse bharosa milta hai ki naya change (feature) daalne se purana code (e.g., Login logic) *toot* (break) nahi gaya hai.
      * **Documentation:** Tests code ke liye "live documentation" (zinda saboot) hote hain ki code ko kaise use karna hai.
      * **CI/CD (Module 13.4):** Tests ko automatic run karne ke liye zaroori.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Unit Tests (Jest):** Simple functions (e.g., `calculateTotalPrice(cart)`) ke liye.
      * **Component Tests (RTL):** UI Components (e.g., `LoginScreen.tsx`) ke liye.
      * Code ko `git push` karne se pehle.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap ek feature add karenge (`Edit Profile`), aur usse `Login` (purana feature) toot jaayega, aur aapko *pata bhi nahi chalega* (jab tak user complain na kare). 🛑
      * App bugs se bhar jaayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  React Native project mein `__tests__` naam ka folder hota hai.
    2.  Aap `MyComponent.tsx` ke liye `MyComponent.test.tsx` file banate hain.
    3.  **Arrange (Setup):** `render()` function (RTL se) component ko "render" (load) karta hai.
    4.  **Act (Kaam):** `fireEvent.press()` (RTL se) button par "click" (simulate) karta hai.
    5.  **Assert (Check):** `expect()` (Jest se) check karta hai ki "kya naya text screen par aaya?".

7.  **💻 Code example (Component Test using RTL):**

    ```tsx
    // (src/components/Counter.tsx) - Asli Component
    import React, { useState } from 'react';
    import { View, Text, Button } from 'react-native';

    export const Counter = () => {
      const [count, setCount] = useState(0);
      return (
        <View>
          <Text>Count: {count}</Text>
          <Button 
            title="Increment" 
            onPress={() => setCount(count + 1)} 
            testID="increment-button" // Test ke liye ID
          />
        </View>
      );
    };

    // ---
    // (__tests__/Counter.test.tsx) - Test File
    // Pehle install karein: npm install --save-dev @testing-library/react-native
    import React from 'react';
    import { render, fireEvent } from '@testing-library/react-native';
    import { Counter } from '../src/components/Counter';

    // 1. Test ko describe karna
    describe('Counter Component', () => {
      
      // 2. Pehla test case (initial state)
      it('shuru mein count 0 dikhata hai', () => {
        // Arrange: Component ko render karo
        const { getByText } = render(<Counter />);
        
        // Assert: Check karo
        // "kya 'Count: 0' text screen par hai?"
        expect(getByText('Count: 0')).toBeTruthy(); 
      });

      // 3. Doosra test case (button click)
      it('button dabane par count ko 1 karta hai', () => {
        // Arrange: Component render karo
        const { getByText, getByTestId } = render(<Counter />);

        // Act: 'increment-button' ID waale button ko dhoondho aur 'press' karo
        fireEvent.press(getByTestId('increment-button'));

        // Assert: Check karo ki count badla ya nahi
        // "kya ab 'Count: 1' text screen par hai?"
        expect(getByText('Count: 1')).toBeTruthy();
      });
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `describe('Counter...', ...)`: Ek "Test Suite" (group) banaya.
          * `it('shuru mein...', ...)`: Ek "Test Case" (individual test) banaya.
          * `const { getByText } = render(<Counter />);`: RTL ne component ko "render" kiya aur humein "helper" functions (jaise `getByText`) diye.
          * `expect(getByText('Count: 0')).toBeTruthy();`: Hum Jest ko bol rahe hain "Expect (ummeed) hai ki `getByText('Count: 0')` (jo text dhoondhega) `toBeTruthy` (sahi/mil gaya) hoga."
          * `fireEvent.press(getByTestId(...))`: Humne `testID` se button ko pakda aur `fireEvent.press` (RTL se) se uspar *nakli* click kiya.
          * `expect(getByText('Count: 1')).toBeTruthy();`: Humne check kiya ki click ke *baad* text `Count: 1` ho gaya.
      * **🚀 Quick run expected output (Terminal mein `npm test` chalaane par):**
        ```
        PASS  __tests__/Counter.test.tsx
        Counter Component
          ✓ shuru mein count 0 dikhata hai (5ms)
          ✓ button dabane par count ko 1 karta hai (3ms)
        ```

8.  **🐞 Common beginner mistakes:**

      * Component ki *andar* ki state (`useState`) ko test karne ki koshish karna. (Galat\! 🛑). RTL kehta hai "Sirf woh test karo jo *user* dekhta hai" (e.g., "Count: 0" text).
      * `testID` har jagah laga dena. (Pehle `getByText`, `getByRole` se try karo, `testID` aakhri raasta hai).

9.  **🌍 Real-world example / use-case:**

      * **Test Case:** "Login button ko disable hona chahiye jab tak username aur password dono na bhar diye jaayein."
      * **Test Case:** "API call fail hone par 'Error' message dikhna chahiye."

10. **✅ Quick checklist / TL;DR:**

      * `Jest` = Test Runner (default mein hai).
      * `RTL` (@testing-library/react-native) = Component Test Library.
      * Test karo "jo user dekhta hai", component ki state (implementation) nahi.
      * `render` (Arrange) -\> `fireEvent` (Act) -\> `expect` (Assert).

11. **❓ FAQs:**

      * **Q: Kitna test karein? 100%?**
      * A: 100% coverage (har line) zaroori nahi. Sirf "critical paths" (main features) test karo (e.g., Login, Payment). 70-80% kafi hai.
      * **Q: API calls (Axios) ko kaise test karein?**
      * A: "Mocking". Aap `jest.mock('axios')` ka use karke `axios` ko *nakli* (fake) response dene ko bolte hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  `Counter` component mein ek "Decrement" button add karo.
    2.  Ek naya test case (`.test.tsx` file mein) likho jo check kare ki "Decrement" button `Count: 0` se `-1` karta hai ya nahi.

13. **📚 Further reading / commands / links:**

      * `npm test` (Test chalaane ki command).
      * [React Native Testing Library Docs](https://callstack.github.io/react-native-testing-library/)

-----

## 13.3: End-to-End (E2E) Testing (Detox)

1.  **🎯 Title / Short Summary:** E2E Testing (Detox) - Poori App ko (Robot ki tarah) Chala kar Test Karna.

2.  **🤔 Kya hai? (What?):** Unit Test (Module 13.2) ek *component* ko test karta hai. E2E (End-to-End) Test *poori app* ko test karta hai. **Detox** ek library hai jo ek "robot" (automation) ki tarah kaam karti hai:

    1.  App ko (real build) install karti hai.
    2.  App ko kholti hai.
    3.  Text type karti hai (e.g., username).
    4.  Button par 'tap' (click) karti hai.
    5.  Check karti hai ki "kya agli screen (Home) aayi?".

3.  **💡 Kyun important hai? (Why?):** Yeh "User Journey" (user ka poora safar) ko test karta hai. Yeh 100% guarantee deta hai ki *sabkuch* (JS, Native, Navigation, Redux, API) *ek saath* milkar sahi kaam kar raha hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * App release (publish) karne se pehle "critical flows" (main safar) ko test karne ke liye.
      * Critical Flow 1: "Signup -\> Login -\> Logout".
      * Critical Flow 2: "Home -\> Search -\> Add to Cart -\> Checkout".
      * CI/CD (Module 13.4) pipeline mein (automatic run karne ke liye).

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapke Unit Tests (chote hisse) sab "PASS" honge, par jab user app chalaayega, toh `LoginScreen` se `HomeScreen` (Navigation) hi nahi chalega, kyunki dono ko *jodne* waala test aapne kabhi kiya hi nahi. 🛑

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    *(Setup complex hai, overview de raha hoon)*

    1.  **Setup:** Detox ka setup *bahut* complex hai. Aapko native tools (Android SDK/AVD, Xcode) setup karne padte hain.
    2.  **Test File:** Aap `.e2e.js` (ya `.test.js`) file likhte hain.
    3.  **Matchers:** `element(by.id('...'))` se component ko (uske `testID` se) pakadte hain.
    4.  **Actions:** `.typeText('...')`, `.tap()`, `.swipe('left')`.
    5.  **Expectations:** `expect(element(...)).toBeVisible()`.

7.  **💻 Code example (Login Flow Test):**

    ```javascript
    // (e2e/loginFlow.e2e.js) - Detox Test File

    // 1. Test ko describe karna
    describe('Login Flow', () => {

      // Har test se pehle app ko 'launch' (start) karna
      beforeAll(async () => {
        await device.launchApp(); 
      });

      // (Har test ke beech app ko 'reload' kar sakte hain)
      beforeEach(async () => {
        await device.reloadReactNative();
      });

      // 2. Pehla test case (Login)
      it('Login flow sahi se chalna chahiye', async () => {
        // Arrange: (App khul chuki hai)
        
        // Act 1: 'username' input ko dhoondho (testID se) aur text type karo
        await element(by.id('username-input')).typeText('testuser@gmail.com');
        
        // Act 2: 'password' input ko dhoondho aur text type karo
        await element(by.id('password-input')).typeText('123456');

        // Act 3: 'login-button' ko dhoondho aur tap karo
        await element(by.id('login-button')).tap();

        // Assert (Check):
        // "kya 'home-screen-welcome-text' (testID) waala element
        // 5 second ke andar 'visible' (dikhne) laga?"
        await expect(element(by.id('home-screen-welcome-text')))
          .toBeVisible()
          .withTimeout(5000); // (API call ke liye wait)
      });
      
      // (Doosra test case yahan likh sakte hain, e.g., 'Logout')
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `await device.launchApp()`: Detox ne Emulator/Simulator par app ko khola.
          * `await element(by.id('username-input'))`: Detox ne native component tree mein `testID="username-input"` waale element ko dhoondha. (Isliye `testID` zaroori hain).
          * `.typeText('...')`: Robot (Detox) ne us input mein text type kiya.
          * `.tap()`: Robot ne button par click kiya.
          * `await expect(...).toBeVisible()`: Humne "ummeed" ki (check kiya) ki login ke baad `home-screen-welcome-text` waala element screen par *dikh* raha hai.
      * **🚀 Quick run expected output (Terminal mein `detox test` chalaane par):**
          * Aap screen par Emulator (ya Simulator) ko *apne aap* chalte hue dekhenge.
          * App khulegi, text type hoga, button dabega, agli screen aayegi.
          * Terminal mein "PASS" aa jaayega.

8.  **🐞 Common beginner mistakes:**

      * Setup mein hi haar maan lena (Detox setup *sach mein* mushkil hai).
      * `testID` (Module 13.2) components mein add na karna. (Detox components ko `testID` se hi dhoondhta hai).
      * Async/Await (`await`) ka use na karna. (Detox ke har command (e.g., `.tap()`) ko `await` karna zaroori hai).

9.  **🌍 Real-world example / use-case:**

      * Har badi app (Wix, etc.) release se pehle apne 10-15 main "user flows" (jaise Login, Add to Cart) ko Detox se automatic test karti hai.

10. **✅ Quick checklist / TL;DR:**

      * `Detox` = Robot jo poori app (user journey) ko test karta hai.
      * `Unit Test` (RTL) (Component) vs `E2E` (Detox) (Poori App).
      * `testID` prop E2E testing ke liye *bahut zaroori* hai.
      * `element(by.id(...)).tap()`

11. **❓ FAQs:**

      * **Q: Detox vs Appium?**
      * A: `Detox` *sirf* React Native ke liye bana hai (White box testing). Yeh fast aur reliable hai. `Appium` "black box" hai, kisi bhi app (native/hybrid) ke liye chalta hai, par slow hai. RN ke liye `Detox` best hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  (Setup mushkil hai). Apni Login screen ke sabhi `TextInput` aur `Button` ko `testID` prop (e.g., `testID="login-username"`) do.
    2.  (Yeh `testID` RTL (Module 13.2) mein `getByTestId` se bhi use ho sakte hain).

13. **📚 Further reading / commands / links:**

      * `npm install -g detox-cli` (Global command).
      * `npm install detox` (Project mein).
      * [Detox Docs](https://wix.github.io/Detox/)

-----

## 13.4: CI/CD Pipeline (GitHub Actions / Fastlane)

1.  **🎯 Title / Short Summary:** CI/CD Pipeline - Code Push Karne par Automatic Testing aur Building.

2.  **🤔 Kya hai? (What?):**

      * **CI (Continuous Integration):** Ek process jisse jab bhi developer `git push` karta hai, ek server (jaise GitHub Actions) *automatic* code ko check karta hai (`lint`), tests (Jest/Detox) chalata hai, aur build (APK) banata hai.
      * **CD (Continuous Deployment):** Agar CI (tests) *pass* ho jaaye, toh app ko *automatic* Play Store / App Store (ya testing service) par "deploy" (upload) kar dena.
      * **Tools:** `GitHub Actions` (sabse popular) ya `Fastlane` (mobile ke liye special).

3.  **💡 Kyun important hai? (Why?):**

      * **Safety:** Yeh "gatekeeper" (darbaan) hai. Agar aapne *galat* code (jo test fail kare) push kiya, toh CI use `master` branch mein merge hi nahi hone dega.
      * **Speed:** Aapko har baar release ke liye *khud* (manually) build (`gradlew bundleRelease`) chalaana nahi padta.
      * **Consistency:** Har build *ek hi tareeke* (server par) banta hai ("Mere machine par toh chalta hai" waali problem khatam).

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jaise hi aap team (2+ log) mein kaam shuru karein.
      * Jaise hi aapka project "real" (production) ho jaaye.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Koi developer galat code (jo test fail kare) push kar dega aur poori app (master branch) toot jaayegi. 🛑
      * App ko release (publish) karna ek *manual* (haath se), slow, aur error-prone (galtiyon se bhara) process hoga.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (GitHub Actions):**

    1.  Aap apne project ke root mein `.github/workflows/` folder banate hain.
    2.  Uske andar ek `.yml` file (e.g., `main.yml`) banate hain.
    3.  `.yml` file mein "recipe" (steps) likhte hain.
    4.  **Recipe (example):**
          * `on: push: branches: [ main ]` (Kab chale? Jab `main` branch par `push` ho).
          * `jobs:` (Kaam kya karna hai?)
          * `build:` (Job ka naam)
          * `runs-on: ubuntu-latest` (Kahan chale? Linux server par).
          * `steps:` (Kya-kya karna hai?)
          * `step 1: uses: actions/checkout@v3` (Code ko server par download (checkout) karo).
          * `step 2: uses: actions/setup-node@v3` (Node.js setup karo).
          * `step 3: run: npm install` (Dependencies install karo).
          * `step 4: run: npm test` (Unit tests (Jest) chalao).
          * `step 5: run: cd android && ./gradlew assembleRelease` (APK banao - *agar* step 4 pass ho).

7.  **💻 Code example (Simple `.yml` file for GitHub Actions - CI only):**

    ```yaml
    # (.github/workflows/main.yml)

    # 1. Pipeline ka naam
    name: React Native CI

    # 2. Trigger (Kab chale?)
    # Jab 'main' branch par push ho, ya 'main' par 'pull_request' aaye
    on:
      push:
        branches: [ "main" ]
      pull_request:
        branches: [ "main" ]

    # 3. Jobs (Kaam)
    jobs:
      # Job ka naam
      test:
        # Kahan chalega (Server OS)
        runs-on: ubuntu-latest 

        # Steps (Recipe)
        steps:
        # Step 1: Code ko server par copy karna
        - name: Checkout code
          uses: actions/checkout@v4

        # Step 2: Node.js (e.g., version 18) setup karna
        - name: Setup Node.js
          uses: actions/setup-node@v4
          with:
            node-version: 18

        # Step 3: Dependencies (npm/yarn) install karna
        - name: Install dependencies
          run: npm install

        # Step 4: Unit tests (Jest) chalaana
        # Agar yeh step fail (error) hua, toh pipeline ruk jaayegi
        - name: Run unit tests
          run: npm test
          
        # (Aap yahan E2E test (Detox) ya 'lint' bhi chala sakte hain)
    ```

      * **✍️ Line-by-line explanation:**
          * `name: React Native CI`: Pipeline ka naam.
          * `on: push: branches: [ "main" ]`: Trigger.
          * `jobs: test:`: Ek job banayi jiska naam `test` hai.
          * `runs-on: ubuntu-latest`: Yeh job GitHub ke diye hue Linux (Ubuntu) server par chalegi.
          * `uses: actions/checkout@v4`: Yeh GitHub ka *bana-banaya* (pre-made) action (step) hai jo code ko "git clone" karta hai.
          * `run: npm install`: Server ke terminal par `npm install` command chalao.
          * `run: npm test`: Server ke terminal par `npm test` chalao.
      * **🚀 Quick run expected output:**
        1.  Aap code `git push` karenge.
        2.  GitHub mein "Actions" tab mein jaayenge.
        3.  Aapko "React Native CI" pipeline *chalti* hui dikhegi.
        4.  Agar `npm test` fail hua, toh wahan (Red Cross ❌) aa jaayega aur aapko email aa jaayega ki "CI failed\!".
        5.  Agar sab pass hua, (Green Check ✅) aa jaayega.

8.  **🐞 Common beginner mistakes:**

      * `.yml` file ke *syntax* (indentation/spaces) mein galti karna. (YAML spaces ko lekar bahut strict hai).
      * `npm install` (step 3) kiye bina `npm test` (step 4) chala dena. (Command fail ho jaayegi).
      * Server par (e.g., `ubuntu-latest`) Android SDK ya Java setup kiye bina *APK build* (`./gradlew assembleRelease`) chalaane ki koshish karna. (Iske liye `actions/setup-java` jaise special steps lagte hain).

9.  **🌍 Real-world example / use-case:**

      * **CI:** Har `pull_request` (PR) par automatic `npm test` chalaana. Agar test fail ho, toh PR ko *merge* karne se *block* kar dena.
      * **CD (Advanced):** `Fastlane` (ek tool) ka use karke build ko `sign` (Module 13.5) karna aur automatic Google Play Store (Internal Test track) par upload kar dena.

10. **✅ Quick checklist / TL;DR:**

      * CI/CD = Automatic Testing & Deployment.
      * `GitHub Actions` (server) + `.yml` file (recipe).
      * `on: push` (Trigger) -\> `jobs:` (Kaam) -\> `steps:` (Recipe).
      * Yeh 'Gatekeeper' (darbaan) hai jo toota (broken) code merge hone se rokta hai.

11. **❓ FAQs:**

      * **Q: GitHub Actions vs Fastlane?**
      * A: Dono *saath* mein use hote hain. `GitHub Actions` (CI server) `Fastlane` (tool) ko call karta hai. `Fastlane` mobile app building/signing/uploading (CD) ke liye *specialist* hai. `Fastlane` aapke local machine par bhi chal sakta hai.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne (GitHub par) project mein `.github/workflows/` folder banao.
    2.  Upar di gayi `main.yml` file copy-paste karke `git push` karo.
    3.  GitHub par "Actions" tab mein jaakar apni pipeline ko chalta dekho.

13. **📚 Further reading / commands / links:**

      * [GitHub Actions Docs](https://docs.github.com/en/actions)
      * [Fastlane Docs](https://fastlane.tools/) (Mobile CD ke liye)

-----

## 13.5: Publishing to App Store & Play Store (Real builds - AAB/IPA)

1.  **🎯 Title / Short Summary:** Publishing - App ko Aam Public (Users) tak (Play Store/App Store par) Pahunchana.
2.  **🤔 Kya hai? (What?):** Yeh "Zero-to-Professional" ka aakhri step hai. Yeh process hai jisse aap apne *development* (Debug) code ko ek *production* (Release) file (`.aab` Android ke liye, `.ipa` iOS ke liye) mein badalte hain aur use Google/Apple ko submit (jama) karte hain.
3.  **💡 Kyun important hai? (Why?):** Iske bina, aapki app *sirf* aapke computer aur emulator tak seemit (limited) hai. Users (public) isko download nahi kar sakte.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * Jab aapki app poori tarah test (Unit + E2E) ho chuki ho.
      * Jab aap "Version 1.0" launch karne ke liye taiyaar hon.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Aapki app users tak *kabhi nahi* pahunchegi.
      * (Note 42) Agar aapne "Debug" build release kar diya, toh woh *bahut slow* hogi, usmein Dev Menu hoga, aur woh *insecure* hogi. 🛑

-----

### 📊 Comparison: `Debug vs Release Builds` (Note 1.9, 42)

| Feature | `Debug` Build (Jo hum `npm run android` se chalate hain) | `Release` Build (Jo users ko dete hain) |
| :--- | :--- | :--- |
| **🤔 Kya hai? (What?)** | Development (coding) ke time test karne ke liye. | Final, optimized (fast) build jo Play Store par jaata hai. |
| **💡 Kyun important hai? (Why?)** | Ismein "Fast Refresh", "Dev Menu", "Element Inspector" jaise debugging tools hote hain. | Ismein *koi* debugging tool nahi hota. Yeh fast aur secure hota hai. |
| **💻 Code example (Command)** | `npm run android` (ya `run-ios`) | `cd android && ./gradlew bundleRelease` (Android) <br> `(Archive in Xcode)` (iOS) |
| **❌ Consequences (Agar release mein Debug use kiya)** | 1. App *bahut slow* hogi (JS code optimize nahi hai). <br> 2. **Insecure\!** User Dev Menu khol sakta hai, API calls dekh sakta hai. <br> 3. Play Store/App Store ise *reject* kar denge. | (N/A) |

-----

### 🧑‍🏫 Step-by-step (Publishing Concepts) (Note 42)

Yeh poora process (Note 42) hai:

1.  **`App Signing (Keystore)` (Note 42) (Android):**

      * **Kya hai?** Release build (`.aab`) banane se pehle, aapko use *sign* (digital signature) karna padta hai taaki Google Play ko pata chale ki yeh app *aapne* hi banayi hai.
      * **Kaise?** Aap ek `keystore` file (ek "digital chaabi" 🔑) banate hain (sirf ek baar).
      * **Command:** `keytool -genkey -v -keystore my-upload-key.keystore ...`
      * **Consequences:** Agar yeh `keystore` file *kho gayi*, toh aap us app ka *agla update kabhi nahi* daal paayenge. 🛑 (Ise 10 jagah backup rakho).
      * (iOS mein yeh "Certificates" aur "Provisioning Profiles" kehlata hai).

2.  **`Bundle Size Optimization` (Note 42):**

      * **Kya hai?** `.aab` (Android App Bundle) ya `.ipa` (iOS) file ka size (MB) kam se kam rakhna.
      * **Kyun?** Choti app (e.g., 20MB) = Zyada downloads. Badi app (e.g., 150MB) = Log download nahi karte.
      * **Kaise?**
          * Images ko `.png` ki jagah `.webp` format mein use karo.
          * `ProGuard` (neeche dekho) use karo.
          * Faltu (unused) packages ko `npm uninstall` karo.
          * `android { ... buildTypes { release { ... shrinkResources true } } }` (Gradle mein).

3.  **`Proguard (Code Obfuscation)` (Note 42):**

      * **Kya hai?** Proguard (Android) ek tool hai jo 2 kaam karta hai:
        1.  **Shrinking (Size kam karna):** Aapke *unused* (jo use nahi hua) Java/Kotlin code ko build se hata deta hai.
        2.  **Obfuscation (Code uljhana):** Aapke Java/Kotlin code (classes, functions) ka naam `MyAwesomeClass` se `a.b.c` mein badal deta hai.
      * **Kyun?** Size kam karta hai aur "Reverse Engineering" (code chori) ko *bahut mushkil* bana deta hai.
      * **Kaise?** `android/app/build.gradle` mein `enableProguardInReleaseBuilds = true` (ya `minifyEnabled true`) set karke.

4.  **`Crash Reports` (Note 42):**

      * **Kya hai?** Release (live) app mein *jab* crash ho (jo hoga hi), toh us crash ki *report* (details) aap tak (developer) pahunchaana.
      * **Kyun?** Agar app crash ho aur aapko pata hi na chale, toh aap use *fix* kaise karenge?
      * **Kaise?** 3rd party service (e.g., `Firebase Crashlytics` ya `Sentry`) install karni padti hai.
      * **Code:** `npm install @react-native-firebase/crashlytics`. (Yeh automatic native (Java/Swift) crash aur JS crash, dono ko pakad leta hai).

5.  **Final Build:**

      * **Android:** `cd android && ./gradlew bundleRelease`. Yeh `android/app/build/outputs/bundle/release/` mein `app-release.aab` file banata hai.
      * **iOS:** Xcode kholo, "Product" -\> "Archive" karo.
      * **Submit:** `app-release.aab` ko Google Play Console (website) par upload karo. 'Archived' `.ipa` ko App Store Connect (website) par upload karo.

6.  **🐞 Common beginner mistakes:**

      * `my-upload-key.keystore` file ko `git` mein push kar dena (ya kho dena). 🛑 (Maha-paap\! Yeh secret hai).
      * `Proguard` (minifyEnabled) `true` karne ke baad app ko *test* na karna. (Kabhi-kabhi Proguard zaroori code bhi hata deta hai, jisse app crash hoti hai. Iske liye "proguard-rules" likhni padti hain).
      * `Debug` APK (jo `android/app/build/outputs/apk/debug/`) ko release karne ki koshish karna.

7.  **🌍 Real-world example / use-case:**

      * Har app (Facebook, Swiggy) jo Play Store/App Store par hai, woh is poore (Note 42) process se guzri hai.

8.  **✅ Quick checklist / TL;DR:**

      * `Debug` (dev) vs `Release` (user).
      * `Keystore` (chaabi) ko sambhaal kar rakho (Android).
      * `ProGuard` (obfuscation) + `WebP` (images) = Size (`Bundle`) chota karo.
      * `Firebase Crashlytics` (crash reports) zaroor lagao.
      * **Android:** `.aab` file. **iOS:** `.ipa` file.

9.  **❓ FAQs:**

      * **Q: `.aab` (App Bundle) kya hai, `.apk` kyun nahi?**
      * A: `.apk` mein *saare* (har phone ke) resources hote hain (file badi hoti hai). `.aab` (Android App Bundle) ek 'smart' package hai. Google Play user ke *phone* (e.g., Samsung) ke hisaab se *automatic* 'optimized' (chota) `.apk` bana kar user ko deta hai. (Google ab `.aab` hi maangta hai).

10. **🏋️‍♀️ Practice exercise:**

    1.  React Native docs ko follow karke `my-upload-key.keystore` file generate (bana) karke dekho.
    2.  `android/app/build.gradle` mein `release` section mein `minifyEnabled true` set karke dekho.

11. **📚 Further reading / commands / links:**

      * [React Native Docs: Publishing (Android)](https://reactnative.dev/docs/signed-apk-android)
      * [React Native Docs: Publishing (iOS)](https://reactnative.dev/docs/publishing-to-app-store)

-----

## 13.6: Over-the-Air (OTA) Updates (CodePush)

1.  **🎯 Title / Short Summary:** OTA (Over-the-Air) Updates - App Store/Play Store ko Bypass (skip) karke App Update Karna.
2.  **🤔 Kya hai? (What?):** OTA (jaise `CodePush`) ek service hai jo aapko *sirf JavaScript (JS) code* (e.g., `App.js`, `HomeScreen.js`) ko seedha (directly) user ke phone par "sync" (bhejne) deti hai, bina Play Store/App Store par *naya* build (`.aab`/`.ipa`) submit kiye.
3.  **💡 Kyun important hai? (Why?):**
      * **Speed:** Play Store/App Store review process (jo 2-3 din le sakta hai) ko *skip* kar deta hai.
      * **Urgency:** Agar aapki app mein *critical bug* (jaise Login button kaam nahi kar raha) hai, toh aap use *5 minute* mein (OTA se) sab users ke liye fix kar sakte hain.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * JS-only bugs (e.g., `useState` logic galat hai, text galat hai, style galat hai) ko fix karne ke liye.
      * Chote-mote UI changes (e.g., button ka color) badalne ke liye.
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * Ek chote se JS bug (e.g., 1 line ka text change) ke liye bhi, aapko poora build (AAB/IPA) banakar, Play Store/App Store par submit karke, *2 din* (review) wait karna padega. 🛑
      * **(Note 45) VPS Setup:** Agar CodePush (Microsoft) jaisi service use nahi ki, toh aapko apna *khud ka server* (VPS) setup karna padega jo JS bundle (update file) ko host karega aur version check karega (jo *bahut* complex hai). `CodePush` yeh server (Note 45) aapko bana-banaya (free) deta hai.

-----

### 📊 Comparison: `OTA Update (CodePush)` vs `Complete App Update (Store)` (Note 46)

| Feature | OTA (Over-the-Air) Update (e.g., `CodePush`) | Complete Update (Play Store / App Store) |
| :--- | :--- | :--- |
| **🤔 Kya hai? (What?)** | Sirf JS code (aur assets/images) ko update karta hai. | Poori app (JS + **Native Code**) ko update karta hai. |
| **💡 Kab use karein? (When?)** | 1. **JS** bug fix. <br> 2. UI/Style change. <br> 3. 'Text' change. | 1. **Native** code change (e.g., `AndroidManifest.xml`). <br> 2. `npm install` (new **native** library e.g., Camera). <br> 3. App icon/Splash screen change. |
| **⏰ Speed (Raftaar)** | **Bahut Fast.** (5 min mein deploy). Koi review nahi. | **Bahut Slow.** (1-2 din review process). |
| **❌ Kab *Nahi* use kar sakte?** | **Native changes** (Java/Swift/Kotlin, Module 12) isse *nahi* bhej sakte. | Har cheez bhej sakte hain. |
| **🌍 Real-world example** | **(OTA):** "Login" button ka `onPress` logic galat hai, use fix karna. | **(Store):** Naya "Fingerprint Scan" (Module 12.4) feature add karna (jiske liye native code change hua). |

-----

*(Regular 13-point format resumes)*

6.  **🧑‍🏫 Step-by-step explanation (CodePush):**

    1.  **Service:** Microsoft `App Center` (website) par account banao.
    2.  **App:** App Center par 2 apps banao: `MyApp-Android` aur `MyApp-iOS`.
    3.  **Install:** `npm install react-native-code-push`.
    4.  **Setup (Native):** Library ko native (Android/iOS) project se link (setup) karna.
    5.  **Setup (JS):** `App.js` ko `codePush(options)` HOC (Higher-Order Component) se wrap (lapetna) karna.
          * `options = { checkFrequency: codePush.CheckFrequency.ON_APP_START }` (Jab app khule, tab update check karo).
    6.  **Deploy (Release Update):**
          * Aapne JS code mein bug fix kiya.
          * Aap *build* nahi banate.
          * Aap *terminal* se command chalate hain:
          * `appcenter codepush release-react -a YourApp/MyApp-Android -d Production`
    7.  **Sync:** Agli baar jab user app kholega, `CodePush` (step 5) server (App Center) se poochega, "Naya update hai?". Server bolega "Haan". CodePush naya JS bundle (update) *download* karega aur agli baar app start hone par *apply* kar dega.

7.  **💻 Code example (JS Side Setup):**

    ```javascript
    // (App.js)
    import React from 'react';
    import { View, Text } from 'react-native';
    import codePush from 'react-native-code-push'; // Library import

    // 1. CodePush options
    const codePushOptions = {
      checkFrequency: codePush.CheckFrequency.ON_APP_START, // Kab check karein?
      installMode: codePush.InstallMode.IMMEDIATE, // Download hote hi install karo
    };

    function App() {
      // (Aap yahan 'useEffect' mein codePush.sync() bhi use kar sakte hain)
      return (
        <View>
          <Text>Hello World! (Version 1)</Text>
          {/* (Aapne bug fix karke text ko "Version 1.1" kiya aur OTA deploy kiya) */}
          {/* (User app band karke kholega toh "Version 1.1" dikhega) */}
        </View>
      );
    }

    // 2. Poore App component ko 'codePush' HOC se wrap karna
    export default codePush(codePushOptions)(App);
    ```

      * **✍️ Line-by-line explanation:**
          * `import codePush from ...`: Library import ki.
          * `codePushOptions = { ... }`: Options set kiye. `ON_APP_START` matlab jab bhi user app khole, update check karo.
          * `export default codePush(codePushOptions)(App);`: Humne apne poore `App` component ko `codePush` ke "magic wrapper" se lapet diya. Ab yeh wrapper update check karne ka kaam khud karega.
      * **🚀 Quick run expected output:**
          * User ke paas v1 (Store se) hai.
          * Aapne v1.1 (JS change) `appcenter codepush release-react ...` (OTA) kiya.
          * User ne app (v1) band karke *dubara kholi*.
          * App khulte hi `codePush` ne update check kiya, download kiya.
          * User ne app *tisri baar* kholi (ya `IMMEDIATE` mode se app restart hui).
          * User ko "Hello World\! (Version 1.1)" (naya code) dikh gaya, bina Play Store update ke.

8.  **🐞 Common beginner mistakes:**

      * **(Note 46)** `npm install` (native package) karne ke baad OTA bhej dena. (Nahi\! 🛑 Native change = Hamesha Store Update).
      * `app.json` mein `version` (e.g., 1.0.0) badalna (native change) aur sochna ki OTA kaam karega. (Nahi, `CodePush` sirf *usi* native version (1.0.0) par JS update bhejta hai).
      * Deployment keys (Staging/Production) mein confuse hona.

9.  **🌍 Real-world example / use-case:**

      * **(Note 46)** Aapne Zomato (Version 5.0) download ki (Store Update).
      * Aapne app kholi, text mein 'Diwali Offer' dikh raha hai (OTA v5.0.1).
      * 2 din baad aapne app kholi, text badal kar 'Holi Offer' ho gaya (OTA v5.0.2). (Aapne store se update nahi kiya, sirf JS sync hua).

10. **✅ Quick checklist / TL;DR:**

      * OTA (CodePush) = Sirf JS code (bugs/UI) ko fast update karna.
      * Native code (Java/Swift/npm install) change = Hamesha Store Update.
      * `App Center` (Microsoft) (Note 45) server provide karta hai.

11. **❓ FAQs:**

      * **Q: Kya Apple/Google isko allow karte hain?**
      * A: Haan, jab tak aap app ka *main purpose* (e.g., banking se gaming) na badal dein. Bug fixes aur chote UI changes allowed hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  `App Center` (Microsoft) par (free) account banao.
    2.  Ek demo project (Android) ko App Center se connect (setup) karke dekho.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-code-push`
      * [App Center (CodePush) Docs](https://learn.microsoft.com/en-us/appcenter/distribution/codepush/rn-overview)
      * Command (deploy): `appcenter codepush release-react -a <owner>/<app-name> -d <deployment-name>`

-----

## 13.7: `Environment Variables` (`react-native-config`) (Note 44)

1.  **🎯 Title / Short Summary:** Environment Variables - API Keys ko Code se Alag Rakhna.

2.  **🤔 Kya hai? (What?):** Environment Variables (ENV vars) woh settings/keys hain jo *environment* (dev, staging, production) ke hisaab se badalti hain. Jaise: `API_BASE_URL` ya `API_KEY`. (Note 44).

3.  **💡 Kyun important hai? (Why?):** **Security\!** Aapko apni secret (gupt) `API_KEY` ko *seedha* (hardcode) JS code (`App.js`) mein *kabhi nahi* likhna chahiye.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab bhi aapke paas 'secret' keys (API keys, 3rd party keys) hon.
      * Jab aapke paas alag-alag environments hon:
          * **Dev:** `API_URL="http://localhost:3000"`
          * **Staging:** `API_URL="https://staging.myapi.com"`
          * **Production:** `API_URL="https://api.myapi.com"`

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap apni Secret API Key ko `git push` kar denge. 🛑
      * Aapka code *public* (GitHub par) ho jaayega aur koi bhi aapki key chura (steal) kar aapke server (aur paise) ka galat istemaal kar sakta hai.
      * Environment (Dev/Prod) badalne ke liye aapko *code change* karna padega. (Galat\! 🛑).

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**
    **Library:** `react-native-config`

    1.  `npm install react-native-config`.
    2.  Library ko native (Android/iOS) setup (Gradle) karna padta hai.
    3.  Project ke root mein `.env` naam ki file banate hain.
    4.  `.env` file ko `.gitignore` file mein *zaroor* add karte hain (taaki yeh GitHub par na jaaye).
    5.  `.env` file ke andar keys likhte hain.
    6.  JS code mein library se 'Config' import karke use karte hain.

7.  **💻 Code example:**

    ```bash
    # 1. (.env file) - (Yeh file root mein hai)
    # Yeh file .gitignore mein add kar di hai
    API_BASE_URL=https://api.myapi.com
    GOOGLE_MAPS_API_KEY=AIzaSyB... (My Secret Key)

    # 2. (.gitignore file)
    # ... (baaki sab)
    .env
    ```

    ```javascript
    // (src/api/axiosConfig.js)

    // 3. Library se import karna
    import Config from 'react-native-config';

    // 4. Config variables ko 'Config' object se padhna
    const BASE_URL = Config.API_BASE_URL; // (https://api.myapi.com)
    const API_KEY = Config.GOOGLE_MAPS_API_KEY; // (AIzaSyB...)

    console.log('Base URL:', BASE_URL); 
    console.log('API Key:', API_KEY); // (Yeh key code mein hardcoded nahi hai)

    // (Axios (Module 6.1) ke saath use)
    const apiClient = axios.create({
      baseURL: BASE_URL,
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `.env`: Humne key-value pairs (variables) define kiye.
          * `.gitignore`: Humne `.env` file ko 'ignore' kar diya (yeh GitHub par nahi jaayegi).
          * `import Config from ...`: Library ko import kiya.
          * `Config.API_BASE_URL`: Library ne `.env` file se variable ko padha aur native (Java/Swift) code ke through JS ko *securely* (build-time par) de diya.
      * **🚀 Quick run expected output:** `console.log` mein `BASE_URL` aur `API_KEY` ki values print hongi, bhale hi woh JS code mein *kahin likhi* (hardcoded) nahi hain.

8.  **🐞 Common beginner mistakes:**

      * `.env` file ko `.gitignore` mein add karna **bhool jaana**. 🛑 (Sabse badi galti, key leak ho jaayegi).
      * `react-native-config` ka *native setup* (Gradle/Xcode) na karna, jisse `Config` object `undefined` (khali) milta hai.
      * `.env` file badalne ke baad app ko *re-build* (`npm run android`) na karna. (Yeh variables *build-time* par set hote hain, 'Fast Refresh' se nahi).

9.  **🌍 Real-world example / use-case:**

      * (Note 44) Har professional app `react-native-config` (ya similar) use karti hai:
          * Production `API_URL` vs Staging/Dev `API_URL`.
          * Google Maps Key, Firebase Key, etc.

10. **✅ Quick checklist / TL;DR:**

      * Keys ko code se alag karne ke liye.
      * `.env` file banao.
      * `.env` ko `.gitignore` mein daalo.
      * `react-native-config` (library) se `Config.MY_KEY` karke use karo.
      * Change karne ke baad *Re-build* (e.g., `npm run android`) zaroori hai.

11. **❓ FAQs:**

      * **Q: `react-native-dotenv` vs `react-native-config`?**
      * A: `dotenv` JS (Babel) level par hai, `config` native (build) level par. `react-native-config` (Note 44) zyada robust (bharosemand) maana jaata hai alag-alag build types (Dev, Prod) ke liye.

12. **🏋️‍♀️ Practice exercise:**

    1.  `react-native-config` setup karo.
    2.  `.env` file banao aur `APP_NAME="My Super App"` likho.
    3.  `App.js` mein `console.log(Config.APP_NAME)` karke dekho (app re-build karke).

13. **📚 Further reading / commands / links:**

      * `npm install react-native-config`
      * [react-native-config Docs](https://github.com/luggit/react-native-config)

-----

## 13.8: `Permissions Handling` (Manifest vs Runtime) (Note 29, 38, 40)

1.  **🎯 Title / Short Summary:** Permissions (Ijaazat) - User se Camera/Location Use karne ki Ijaazat Maangna.
2.  **🤔 Kya hai? (What?):** Permissions 2 tarah ki hoti hain (Note 29, 38, 40):
    1.  **Manifest (Install-time):** Jo aap `AndroidManifest.xml` (Android) / `Info.plist` (iOS) mein define karte hain. Yeh app ko *batata* hai ki "main yeh permission (e.g., Camera) *use kar sakta hoon*".
    2.  **Runtime (Run-time):** Jo aap *JS code* (e.g., `PermissionsAndroid.request`) se user se *us pal* (runtime par) maangte hain jab aapko feature (e.g., Camera button click) use karna ho.
3.  **💡 Kyun important hai? (Why?):**
      * **Privacy (OS Level):** Android 6.0+ aur sabhi iOS versions *require* (zaroori) karte hain ki aap user se 'dangerous' (e.g., Location, Camera, Storage) permissions *runtime* par (jab zaroorat ho) maangein.
      * **UX (User Trust):** Agar aap app khulte hi 10 permissions (Camera, Location, Mic) maang lenge, toh user dar jaayega aur app uninstall kar dega. (Note 38). Permission tabhi maango jab *feature* use karna ho.
4.  **⏰ Kab/use karna chahiye? (When?):**
      * **Manifest (XML/plist):** Hamesha, har permission (e.g., `INTERNET`, `CAMERA`, `LOCATION`) ke liye jo app use karegi.
      * **Runtime (JS Code):** Sirf "dangerous" permissions (Camera, Location, Storage, Contacts) ke liye, aur tabhi jab *user* us feature (e.g., "Camera" button) par click kare. (Note 38).
5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**
      * **(Note 29) Manifest (XML) bhool gaye?** 🛑 App *seedha crash* ho jaayegi. OS (Android) app ko permission (e.g., `CAMERA`) use hi nahi karne dega, bhale hi user ne 'Allow' kiya ho.
      * **(Note 38) Runtime (JS) bhool gaye?** 🛑 (Android par) App crash ho jaayegi (permission nahi hai). (iOS par) API call fail ho jaayegi (e.g., Camera nahi khulega).
      * **(Note 40) Channel (Android 8+):** Agar *Notification* (Module 12.1) ki permission maangi par 'Channel' nahi banaya, toh (Android 8+) notification *dikhega hi nahi*.

-----

### 📊 Comparison: `Manifest (Install-time)` vs `Runtime (JS)` (Note 29, 38)

| Feature | Manifest (Install-time) (e.g., `AndroidManifest.xml`) | Runtime (Run-time) (e.g., `PermissionsAndroid.request`) |
| :--- | :--- | :--- |
| **🤔 Kya hai? (What?)** | App ki "capability" (kshamta) list. OS ko batata hai ki app *kya-kya* kar sakti hai. | User se (popup dikha kar) "ijaazat" (consent) maangna. |
| **💡 Kyun important hai? (Why?)** | (Note 29) Iske bina OS app ko *crash* kar dega (Security exception). | (Note 38) User privacy ke liye zaroori hai. |
| **⏰ Kab/use karein? (When?)** | App banane ke time (Build-time). Har permission (Internet, Camera, Location) yahan declare *honi* chahiye. | Feature use karne se *theek pehle* (Run-time). Sirf "dangerous" (Camera, Location, Contacts) ke liye. |
| **🌍 Real-world example** | `(AndroidManifest.xml)` <br> `<uses-permission android:name="android.permission.CAMERA" />` | `(Button onPress)` <br> `await PermissionsAndroid.request( PermissionsAndroid.PERMISSIONS.CAMERA );` |
| **❌ Agar nahi kiya toh?** | **App CRASH.** (Fatal Security Exception) | **App CRASH** (ya feature fail). (Permission Denied Error) |

-----

*(Regular 13-point format resumes)*

7.  **💻 Code example (Android Runtime Permission - Module 12.3 jaisa):**

    ```javascript
    // 1. Pehle Manifest mein add karo (android/app/src/main/AndroidManifest.xml)
    // <uses-permission android:name="android.permission.CAMERA" />

    // 2. Ab JS code mein (e.g., CameraScreen.js)
    import { PermissionsAndroid, Platform, Button } from 'react-native';

    const requestCameraPermission = async () => {
      // (iOS par Info.plist hi kaafi hai, JS mein 'request' ki zaroorat nahi)
      if (Platform.OS === 'android') {
        try {
          // 3. Runtime (JS) permission maangna
          const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.CAMERA,
            {
              title: 'Camera Permission Zaroori Hai',
              message: 'App ko photo lene ke liye camera chahiye.',
              buttonPositive: 'OK',
              buttonNegative: 'Cancel',
            }
          );
          
          // 4. Result check karna
          if (granted === PermissionsAndroid.RESULTS.GRANTED) {
            console.log('Camera permission mil gayi!');
            // (Ab 'VisionCamera' (Module 12.2) kholo)
          } else {
            console.log('Camera permission nahi mili.');
            // (User ko 'denied' message dikhao)
          }
        } catch (err) {
          console.warn(err);
        }
      }
    };

    function MyCameraComponent() {
      return <Button title="Camera Kholo" onPress={requestCameraPermission} />
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `<uses-permission ...CAMERA />`: Step 1 (Manifest) zaroori hai.
          * `PermissionsAndroid.request(...)`: Humne Android OS se 'CAMERA' permission (jo 'dangerous' hai) maangi.
          * `{ title: ..., message: ... }`: Yeh text user ko popup (dialog) mein dikhega. (Note 38 - Clear reason dena).
          * `granted === PermissionsAndroid.RESULTS.GRANTED`: Humne check kiya ki user ne 'OK' (Allow) dabaya ya 'Cancel' (Deny).
      * **🚀 Quick run expected output:** Button dabane par (agar pehli baar hai), Android ka default "Allow App to use Camera?" waala popup aayega.

8.  **🐞 Common beginner mistakes:**

      * Sirf JS (`PermissionsAndroid.request`) se permission maangna aur `AndroidManifest.xml` (Step 1) mein add karna **bhool jaana**. 🛑 (App 100% crash hogi).
      * App khulte hi `useEffect` mein 5 permissions (Camera, Mic, Location...) ek saath maang lena. (Bura UX\! 🛑 User 'Deny' kar dega).
      * (Note 40) Notification ke liye `POST_NOTIFICATIONS` (Android 13+) permission *na* maangna.

9.  **🌍 Real-world example / use-case:**

      * **(Note 38)** Instagram: App kholne par 'Notification' (optional) maangta hai. Par 'Camera' tab (feature) par click karne par hi 'Camera Permission' maangta hai (Contextual/Sahi time).

10. **✅ Quick checklist / TL;DR:**

      * **Dono zaroori hain:**
      * 1.  `AndroidManifest.xml` / `Info.plist` (Declare karna).
      * 2.  `PermissionsAndroid.request` (User se maangna).
      * (Note 38) Permission tabhi maango jab *zaroorat* ho (e.g., button click par), app khulte hi nahi.

11. **❓ FAQs:**

      * **Q: `react-native-permissions` library kya hai?**
      * A: `PermissionsAndroid` (jo humne dekha) sirf Android ke liye hai. `react-native-permissions` (3rd party) ek *behtar* library hai jo Android aur iOS *dono* ke permissions (e.g., `check()`, `request()`) ko ek hi API se handle karti hai. Professional apps ise use karti hain.

12. **🏋️‍♀️ Practice exercise:**

    1.  `AndroidManifest.xml` mein `READ_CALENDAR` permission add karo.
    2.  Ek button banao jo `PermissionsAndroid.PERMISSIONS.READ_CALENDAR` ko `request` kare.

13. **📚 Further reading / commands / links:**

      * `npm install react-native-permissions` (Recommended library).
      * [React Native Docs: PermissionsAndroid](https://reactnative.dev/docs/permissionsandroid)

-----

## 13.9: `File Upload (Multipart)` (Note 34)

1.  **🎯 Title / Short Summary:** File Upload (Multipart) - Image/File ko Phone se Server par Bhejna.

2.  **🤔 Kya hai? (What?):** Yeh woh technique (format) hai jisse hum *binary* file (jaise Image, PDF) ko JSON data (jaise username, email) ke *saath* (mix karke) server (API) par `POST` karte hain. Is format ko "Multipart/form-data" kehte hain.

3.  **💡 Kyun important hai? (Why?):**

      * `Axios` (Module 6.1) default mein `JSON` bhejta hai. Aap `JSON` mein *file* (binary) nahi bhej sakte.
      * (Note 34) Jab aap `react-native-image-picker` (Module 5.1) se image select karte hain, toh us image (file) ko *upload* karne ke liye yeh technique zaroori hai.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * Jab user ko "Profile Picture" upload karwana ho.
      * Jab user ko "Document" (PDF/Doc) upload karwana ho.
      * Jab form mein 'Text' (name) + 'File' (image) dono ek saath bhejna ho.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aap file (image) ko `JSON` mein bhej denge (e.g., Base64 string), jo server par *bahut zyada load* daalta hai, slow hota hai, aur standard tareeka nahi hai.
      * Aapki file upload `413 Request Entity Too Large` (ya similar) error par fail ho jaayegi.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  `ImagePicker` (Module 5.1) se image select karo. Humein `response.assets[0].uri` (file path) mil jaayega.
    2.  `FormData` (JavaScript mein built-in) ka ek 'dabba' (object) banao.
    3.  `formData.append(...)` se *sara* data (text aur file) us dabbe mein daalo.
    4.  **File ke liye:** `append` mein 3 cheezein zaroori hain:
          * `name`: Server (backend) ko jo naam chahiye (e.g., `profile_pic`).
          * `value`: File object (`{ uri, name, type }`).
          * `fileName`: File ka naam (e.g., `image.jpg`).
    5.  `Axios` (ya `fetch`) ko yeh *poora* `formData` (dabba) `data` ke roop mein bhej do.
    6.  Header mein `Content-Type: 'multipart/form-data'` set karna *zaroori* hai.

7.  **💻 Code example (Image Picker + Axios):**

    ```javascript
    import { launchImageLibrary } from 'react-native-image-picker'; // (Module 5.1)
    import axios from 'axios'; // (Module 6.1)

    const handleUpload = async () => {
      // 1. Image Picker se image lena
      const result = await launchImageLibrary({ mediaType: 'photo' });
      
      if (result.didCancel || !result.assets) {
        return; // User ne cancel kar diya
      }
      
      const image = result.assets[0];
      
      // 2. FormData (dabba) banana
      const formData = new FormData();

      // 3. File ko dabba mein daalna
      // Yeh object (uri, name, type) zaroori hai
      formData.append('profile_pic', { // 'profile_pic' = Server ki field
        uri: image.uri,
        name: image.fileName || 'profile.jpg', // 'profile.jpg' (fallback)
        type: image.type || 'image/jpeg', // 'image/jpeg' (fallback)
      });

      // 4. Text data ko dabba mein daalna
      formData.append('user_id', '123');
      formData.append('username', 'Gemini');

      // 5. Axios se 'formData' ko POST karna
      try {
        const response = await axios.post(
          'https://my-server.com/upload-profile', 
          formData, // 👈 JSON object nahi, poora 'formData'
          {
            // 6. Header (Sabse zaroori)
            headers: {
              'Content-Type': 'multipart/form-data',
              // (Axios aksar yeh header 'formData' dekh kar khud laga deta hai,
              // par 'fetch' ke saath zaroori hai)
            },
          }
        );
        console.log('Upload success:', response.data);
      } catch (error) {
        console.error('Upload fail:', error);
      }
    };
    ```

      * **✍️ Line-by-line explanation:**
          * `launchImageLibrary`: (Module 5.1) Image select ki, `image` object mila.
          * `const formData = new FormData();`: Khali "form" (dabba) banaya.
          * `formData.append('profile_pic', { ... });`: "dabba" mein file (image) daali. Humne 3 cheezein batai: server field `profile_pic`, file ka `uri` (path), `name`, aur `type` (MIME type).
          * `formData.append('user_id', '123');`: "dabba" mein text data daala.
          * `axios.post(..., formData, { headers: ... })`: Humne `axios` ko *poora dabba* (JSON nahi) bheja aur header mein bataya ki yeh 'multipart/form-data' hai.
      * **🚀 Quick run expected output:** (Button `onPress` par). Image select hogi, fir `axios` server par file aur data upload karega, aur console mein "Upload success" log hoga.

8.  **🐞 Common beginner mistakes:**

      * File object (`{ uri, name, type }`) ko galat format mein bhejna (e.g., sirf `uri` bhej dena).
      * `Content-Type: 'multipart/form-data'` header set na karna (server 400/415 error dega).
      * Server par `profile_pic` (field name) maanga hai, aur yahan se `image` (galat field name) bhej dena.

9.  **🌍 Real-world example / use-case:**

      * (Note 34) **Instagram:** Photo (file) + Caption (text) + Location (text) = Sab ek saath 'multipart' request mein upload hota hai.
      * **LinkedIn:** Profile pic (image) + Name (text) update karna.

10. **✅ Quick checklist / TL;DR:**

      * File (Image/PDF) upload = `multipart/form-data`.
      * `FormData` object (dabba) banao.
      * `formData.append('field_name', value)` se text daalo.
      * `formData.append('file_field', { uri, name, type })` se file daalo.
      * `axios` (ya `fetch`) se poora `formData` bhej do.

11. **❓ FAQs:**

      * **Q: Base64 vs Multipart?**
      * A: Base64 file ko text (string) bana deta hai. Yeh 33% *bada* (size) hota hai, slow hota hai, aur server par zyada CPU use karta hai. **Multipart** (file) hamesha best (efficient) tareeka hai.
      * **Q: `fetch` se kaise karein?**
      * A: `fetch(url, { method: 'POST', body: formData, headers: { 'Content-Type': 'multipart/form-data' } });`

12. **🏋️‍♀️ Practice exercise:**

    1.  [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (fake API) file upload support nahi karta.
    2.  Aapko (Note 6.9) `json-server` (local) ya `Mockoon` (tool) use karke ek fake '/upload' endpoint banana padega jo 'multipart' data accept kare.

13. **📚 Further reading / commands / links:**

      * [MDN Docs: FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
      * (Library: `react-native-image-picker` (Note 5.1))
	  
=============================================================

# MODULE-14 → Professional Development & Ecosystem

Module 14 aapko ek "Professional" se "Elite" developer banayega. Ismein hum seekhenge ki jab app *crash* ho toh use kaise sambhalein (Error Boundaries) aur app ko *sabke* liye (Accessibility) kaise banayein. Chaliye, is course ko finish line tak le jaate hain\! 🏁

-----

## 14.1: Error Handling (`Error Boundaries`)

1.  **🎯 Title / Short Summary:** `Error Boundaries` - Component Crash Hone par Poori App ko Bachana.

2.  **🤔 Kya hai? (What?):** `Error Boundary` (Error ki Seema) ek *Class Component* (haan, yeh functional nahi ho sakta\!) hai, jo apne "children" (neeche ke) components mein hone waale *JavaScript render errors* ko "pakad" (catch) leta hai.

3.  **💡 Kyun important hai? (Why?):** **Problem:** Agar aapke `HomeScreen` ke `UserProfile` component mein ek JS error (e.g., `user.name.firstName` jab `name` `null` ho) aa jaaye, toh React Native mein yeh *poori app ko crash* (band) kar dega. 🛑
    **Solution:** `Error Boundary` is crash ko rokta hai. Yeh *sirf* uss `UserProfile` component ko hatata hai aur uski jagah ek "fallback UI" (e.g., "Oops\! Kuch galat ho gaya") dikha deta hai. Baaki poori app (jaise `Header`, `TabBar`) chalti rehti hai\!

4.  **⏰ Kab/use karna chahiye? (When?):**

      * App ke *main* sections ko wrap (lapetne) ke liye (e.g., poori `HomeScreen` ko).
      * Har `FlatList` item (List Item) ko wrap karne ke liye (taaki ek galat item poori list ko crash na kar de).
      * `try...catch` block (jo `async` code/functions ko pakadta hai) `Error Boundaries` (jo *render* errors ko pakadta hai) ko replace nahi karta. Dono zaroori hain.
      * (Note 30) Yeh `AsyncStorage` ya `Redux` ke *andar* ke error nahi, `render()` method (UI) ke errors pakadta hai.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Aapke component mein ek chota sa `render` error (e.g., `null.property`) poori app ko *band* (crash) kar dega.
      * User ko "white screen of death" (ya seedha app close) dikhega.
      * Aapka user experience (UX) *bahut* bura hoga.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown:**

    1.  Yeh *sirf* Class Component ho sakta hai.
    2.  Aapko 2 special methods define karne hote hain:
          * `static getDerivedStateFromError(error)`: Jab error *hota* hai, yeh call hota hai. Yeh state (e.g., `hasError: true`) update karta hai.
          * `componentDidCatch(error, errorInfo)`: Yeh error ko *log* karne ke liye hai (e.g., `Firebase Crashlytics` (Module 13.5) par bhejne ke liye).
    3.  Aapke `render()` method mein, aap check karte hain:
          * `if (this.state.hasError)` -\> "Fallback UI" (Error message) dikhao.
          * `else` -\> `this.props.children` (Asli component) dikhao.
    4.  Fir aap apne "dangerous" component ko isse wrap kar dete hain.

7.  **💻 Code example:**

    ```javascript
    // 1. Error Boundary Component Banana (ErrorBoundary.js)
    // Yeh 'Class Component' hona zaroori hai!
    import React from 'react';
    import { View, Text, Button } from 'react-native';

    class ErrorBoundary extends React.Component {
      // 1. State banana
      constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
      }

      // 2. Step 1: Jab error ho, toh state update karo
      static getDerivedStateFromError(error) {
        // 'hasError: true' set karke fallback UI dikhayega
        return { hasError: true, error: error };
      }

      // 3. Step 2: Error ko 'log' (server par) bhejo
      componentDidCatch(error, errorInfo) {
        // Yahan aap error ko Crashlytics/Sentry par bhej sakte hain
        console.error("ErrorBoundary ne error pakda:", error, errorInfo);
        // logErrorToMyService(error, errorInfo);
      }

      render() {
        // 4. Step 3: Check karo
        if (this.state.hasError) {
          // Agar error hai, toh 'Fallback UI' dikhao
          return (
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 }}>
              <Text style={{ color: 'red', fontSize: 18, fontWeight: 'bold' }}>
                Oops! Something went wrong.
              </Text>
              <Text style={{ marginVertical: 10 }}>{this.state.error?.message}</Text>
              <Button title="Try Again" onPress={() => this.setState({ hasError: false })} />
            </View>
          );
        }
        
        // Agar error nahi hai, toh 'children' (asli component) dikhao
        return this.props.children;
      }
    }
    export default ErrorBoundary;

    // ---
    // 2. (App.js) - Error Boundary ko Use Karna
    import ErrorBoundary from './ErrorBoundary';
    // import MyRiskyComponent from './MyRiskyComponent'; // (Yeh component crash hoga)

    function App() {
      return (
        <View style={{ flex: 1 }}>
          <Header /> 
          
          {/* 3. Apne 'dangerous' component ko wrap karna */}
          <ErrorBoundary>
            <MyRiskyComponent /> 
            {/* Agar MyRiskyComponent crash hua, toh Header/Footer safe rahenge */}
          </ErrorBoundary>
          
          <Footer />
        </View>
      );
    }
    ```

      * **✍️ Line-by-line explanation:**
          * `class ErrorBoundary extends React.Component`: Error Boundary banaya.
          * `static getDerivedStateFromError(error)`: Yeh special method error hote hi state (`hasError: true`) set kar deta hai, jisse `render()` method ko pata chal jaata hai.
          * `componentDidCatch(error, errorInfo)`: Yeh error hone ke *baad* chalta hai, taaki aap error ko `console.log` ya `Crashlytics` par bhej sakein.
          * `if (this.state.hasError)`: `render()` mein check kiya ki agar state mein error hai, toh "Fallback UI" (e.g., "Oops...") dikhao.
          * `return this.props.children;`: Agar error nahi hai, toh jo component (children) wrap kiya hai, use normal dikhao.
          * `<ErrorBoundary><MyRiskyComponent /></ErrorBoundary>`: `App.js` mein humne `MyRiskyComponent` (jo crash ho sakta hai) ko `ErrorBoundary` (safety net) se wrap kar diya.
      * **🚀 Quick run expected output:**
          * Agar `MyRiskyComponent` (e.g., `null.property` ke kaaran) crash hota hai.
          * Poori app band *nahi* hogi.
          * `Header` aur `Footer` dikhte rahenge.
          * `MyRiskyComponent` ki jagah "Oops\! Something went wrong." waala (Fallback UI) dikhega.

8.  **🐞 Common beginner mistakes:**

      * `Error Boundary` ko Functional Component se banane ki koshish karna. (Nahi ban sakta\! 🛑).
      * Sochna ki yeh *har* error pakad lega. (Nahi\! Yeh `async` code (e.g., `fetch` ya `setTimeout`), Event Handlers (`onPress`), ya *khud* Error Boundary ke andar ke errors ko *nahi* pakadta hai. Yeh *sirf* `render` phase ke errors pakadta hai).
      * `try...catch` (async/functions ke liye) aur `Error Boundary` (render ke liye) ke beech confuse hona.

9.  **🌍 Real-world example / use-case:**

      * (Note 30) `react-query` (Module 10.2) ya `Redux` (Module 10.1) se data `null` aaya aur aapne `data.user.name` render kar diya -\> `Error Boundary` ise pakad lega.
      * Facebook ka Home Feed: Agar ek "Post" (jo ek component hai) crash hota hai, toh poora feed crash nahi hota. Sirf woh post 'Error' dikhata hai (kyunki har post `ErrorBoundary` se wrapped hota hai).

10. **✅ Quick checklist / TL;DR:**

      * `Error Boundary` ek *Class Component* hai.
      * Yeh 'children' ke *render* errors ko pakadta hai.
      * Yeh poori app ko crash hone se bachata hai aur 'Fallback UI' dikhata hai.
      * `getDerivedStateFromError` (state set karo) aur `componentDidCatch` (error log karo).

11. **❓ FAQs:**

      * **Q: Functional component se 100% nahi ban sakta?**
      * A: Nahi. Par `react-error-boundary` naam ki ek *library* hai jo aapko Functional Component mein (hook `useErrorHandler`) use karne deti hai, par parde ke peeche (behind the scenes) woh bhi Class Component hi use karti hai.
      * **Q: `onPress` (button click) ka error kaise pakdein?**
      * A: `onPress` ke function ke andar *normal* `try...catch` block se.

12. **🏋️‍♀️ Practice exercise:**

    1.  Ek `MyRiskyComponent` banao jo render mein `null.property` (e.g., `const [data, setData] = useState(null); return <Text>{data.name}</Text>;`) throw kare.
    2.  Use `ErrorBoundary` se wrap karke dekho (fallback UI dikhega).
    3.  `ErrorBoundary` hata kar dekho (poori app crash ho jaayegi).

13. **📚 Further reading / commands / links:**

      * [React Docs: Error Boundaries](https://reactjs.org/docs/error-boundaries.html)
      * (Library): `npm install react-error-boundary` (Aasan alternative).

-----

## 14.2: Accessibility (Screen Readers, Contrast, Touch Targets) (Note 48)

1.  **🎯 Title / Short Summary:** Accessibility (a11y) - App ko Sabhi Users (e.g., differently-abled) ke liye Usable Banana.

2.  **🤔 Kya hai? (What?):** Accessibility (jise "a11y" kehte hain) yeh ensure karne ka process hai ki aapki app ko *har koi* (jismein visual (dekhna), motor (haath), ya cognitive (samajhna) impairment (kami) ho) istemaal kar sake. (Note 48).

3.  **💡 Kyun important hai? (Why?):**

      * **Empathy (Hamdardi):** Ek professional developer ko "inclusive" (sabko shaamil karne waala) code likhna chahiye.
      * **Business:** Aap zyada users (market) tak pahunch sakte hain.
      * **Legal (Kaanooni):** Bahut se deshon mein (jaise USA) yeh *kaanoon* hai ki public apps accessible hon.

4.  **⏰ Kab/use karna chahiye? (When?):**

      * **Hamesha\!** Accessibility (a11y) ek "feature" nahi hai jise baad mein add kiya jaaye; yeh *development process* ka hissa hona chahiye, shuru se hi.

5.  **❌ Agar use nahi kiya to kya hoga? (If not used / consequences):**

      * Jo users 'blind' (dekh nahi sakte) hain, woh aapki app bilkul use nahi kar paayenge (kyunki 'Screen Reader' (e.g., TalkBack/VoiceOver) ko kuch samajh nahi aayega).
      * Jo users 'color blind' (rang nahi pehchaan sakte) hain, woh aapke "Red" error (bina text ke) ko "Green" se alag nahi kar paayenge.

6.  **🧑‍🏫 Step-by-step explanation / Concept breakdown (Main Concepts):**

    -----

    ### 1\. `accessibilityLabel` (Screen Readers ke liye)

      * **Problem:** Ek 'blind' user ko yeh button (`<Button>X</Button>` ya `<Icon name="close" />`) kaise pata chalega? Screen Reader use "X" ya "Icon" padhega, jo bekaar hai.
      * **Solution:** `accessibilityLabel` prop.
      * **Code:**
        ```js
        <TouchableOpacity accessibilityLabel="Close this window"> 
          <Icon name="close" size={30} /> 
        </TouchableOpacity>
        ```
      * **Result:** Screen Reader "X" nahi, "Close this window, Button" (pura context) padhega. ✅

    -----

    ### 2\. `accessibilityHint` & `accessibilityRole`

      * **`accessibilityRole`:** Component ka "type" batata hai. Isse Screen Reader ko pata chalta hai ki yeh kya hai.
      * **`accessibilityHint`:** User ko batata hai ki *kya hoga* (e.g., "Doube tap to activate"). (Yeh aksar OS khud add kar deta hai, `label` zyada zaroori hai).
      * **Code:**
        ```js
        <Button 
          title="Login" 
          accessibilityLabel="Login Button"
          accessibilityRole="button" // Bataya ki yeh 'button' hai
          onPress={...} 
        />

        <Text accessibilityRole="header">Welcome</Text> // Bataya ki yeh 'header' hai
        ```

    -----

    ### 3\. Touch Targets (Button ka Size) (Note 48)

      * **Problem:** Button bahut chote (e.g., 20x20 pixels) hain. Jinke haath kaanpte (motor impairment) hain ya ungliyan moti hain, woh use press nahi kar paayenge.
      * **Solution:** Apple/Google dono kehte hain ki *minimum* touch target `44x44` (Apple) ya `48x48` (Android) pixels hona chahiye.
      * **Kaise?** Agar aapka icon chota (e.g., 25x25) hai, toh uspar `padding` (e.g., `padding: 10`) dekar uska *touch area* bada karo (bhale hi icon utna hi bada dikhe).
      * **Code (using `hitSlop`):**
        ```js
        <Pressable 
          hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }} // Touch area bada karta hai
        >
          <Icon name="close" size={25} /> 
        </Pressable>
        ```

    -----

    ### 4\. Color Contrast (Note 48)

      * **Problem:** "Light grey" text ko "White" background par likhna. Jinki nazar kamzor hai (low vision) ya 'color blind' hain, unhe yeh *dikhega hi nahi*.
      * **Solution:** Hamesha "high contrast" (e.g., Black text on White background) use karo.
      * **Kaise?** Tools (jaise [Stark](https://www.getstark.co/) plugin (Figma/Sketch ke liye)) use karke check karo ki aapke colors (Text/Background) ka contrast ratio *minimum* `4.5:1` (WCAG standard) hai ya nahi.
      * **Red/Green Error:** Sirf 'color' (rang) par depend mat karo. Error (Red) ya Success (Green) dikhane ke liye hamesha 'text' (e.g., "Error: Password wrong") ya 'icon' (e.g., '❌') ka istemaal bhi karo.

7.  **💻 Code example (Sabko ek saath use karna):**

    ```javascript
    import { View, Text, Pressable, StyleSheet } from 'react-native';

    function AccessibleButton({ title, onPress }) {
      return (
        // Pressable 'TouchableOpacity' se behtar hai, default role 'button' hai
        <Pressable 
          onPress={onPress}
          style={styles.button}
          // 1. Label: Screen Reader yeh padhega
          accessibilityLabel={title} 
          // 2. Role: Bataya ki yeh 'button' hai
          accessibilityRole="button" 
          // 3. Hint (Optional)
          accessibilityHint={`Press karke ${title} action trigger hoga`}
          // 4. Touch Target (hitSlop)
          hitSlop={10} 
        >
          {/* 5. Contrast: White text on Dark background (High Contrast) */}
          <Text style={styles.text}>{title}</Text>
        </Pressable>
      );
    }

    const styles = StyleSheet.create({
      // 4. Touch Target (Minimum Size)
      button: {
        minHeight: 48, // Minimum touch size
        minWidth: 48,
        padding: 10,
        backgroundColor: '#000000', // (High Contrast)
        justifyContent: 'center',
      },
      text: {
        color: '#FFFFFF', // (High Contrast)
      }
    });
    ```

      * **✍️ Line-by-line explanation:**
          * `accessibilityLabel={title}`: Agar `title` "Login" hai, toh TalkBack "Login" padhega.
          * `accessibilityRole="button"`: TalkBack "Login, *Button*" padhega.
          * `minHeight: 48`: (Note 48) Humne minimum touch area 48px rakha.
          * `hitSlop={10}`: Humne touch area ko button ke size se bhi 10px *aur* bada kar diya.
          * `backgroundColor: '#000'`, `color: '#FFF'`: Black/White ka contrast ratio `21:1` (best) hai.
      * **🚀 Quick run expected output:**
          * (Normal user): Ek high-contrast (kaala) button dikhega.
          * (Blind user): Phone ka TalkBack/VoiceOver ON karke button par tap karne par, phone *bolkar* batayega: "Login, Button. Press karke Login action trigger hoga. Double tap to activate."

8.  **🐞 Common beginner mistakes:**

      * Sirf `Icon` (bina text ke) daal dena aur `accessibilityLabel` *na* dena. 🛑 (Blind user ke liye yeh button 'invisible' hai).
      * Low contrast (e.g., light-grey text on white) use karna.
      * Chote (e.g., 20x20px) touch targets (buttons) banana.
      * `accessibilityLabel` mein "Button" ya "Click" likh dena. (Galat\! 🛑 `accessibilityRole` ("button") yeh kaam khud karta hai. `Label` mein sirf "kaam" (e.g., "Close" ya "Save profile") likho).

9.  **🌍 Real-world example / use-case:**

      * (Note 48) **Har** professional app (Google, Apple, Microsoft) accessibility par *bahut* zor deti hai.
      * `FlatList` mein `accessibilityRole="list"` dena.
      * `Modal` (popup) mein `accessibilityViewIsModal={true}` dena (taaki Screen Reader peeche ke content ko na padhe).

10. **✅ Quick checklist / TL;DR:**

      * `accessibilityLabel`: Icons/Buttons ke liye **zaroori** hai (kya hai?).
      * `accessibilityRole`: Component ka "type" (e.g., 'button', 'header', 'list').
      * **Touch Target:** Minimum `48x48` px (ya `hitSlop` use karo).
      * **Contrast:** Dark/Light ka ratio `4.5:1` rakho. Sirf 'rang' par depend mat karo.

11. **❓ FAQs:**

      * **Q: Kaise test karein ki app accessible hai?**
      * A: **1. Manual:** Apne phone ka **TalkBack (Android) / VoiceOver (iOS)** ON karo aur *bina dekhe* (aankhein band karke) apni app chalaane ki koshish karo. (Aapko 5 min mein galti pata chal jaayegi). **2. Automatic:** Tools jaise "Accessibility Scanner" (Android) use karo.

12. **🏋️‍♀️ Practice exercise:**

    1.  Apne phone ka "TalkBack" (Android Settings -\> Accessibility) ya "VoiceOver" (iOS) ON karo.
    2.  Apni *khud ki* banayi hui (ya koi bhi) app use karke dekho.
    3.  Ek `<TouchableOpacity><Icon ... /></TouchableOpacity>` (bina `accessibilityLabel` ke) banao aur dekho TalkBack kya bolta hai (woh kuch dhang ka nahi bolega). Ab `accessibilityLabel` add karke dekho.

13. **📚 Further reading / commands / links:**

      * [React Native Docs: Accessibility](https://reactnative.dev/docs/accessibility)
      * [WCAG Guidelines (Standards)](https://www.w3.org/WAI/standards-guidelines/wcag/) (Rules)
      
      
=============================================================