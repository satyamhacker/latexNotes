# 📱 React Native: Zero-to-Professional Guide (Complete Instructions)

#### foundational (Beginner to Intermediate) ####

* **Module 1: React Native Introduction & Setup**
    * 1.1: Introduction to React Native (Kya, Kyun, Kaise) (Note 15)
    * 1.2: **Comparison:** Environment Setup (Expo vs React Native CLI) (Note 22)
    * 1.3: Setting Up React Native Project (Pehla App)
        * React Native CLI Commands (`init`, `start`, `run-android`) (Note 15, 16)
        * **Comparison:** `npm start` vs `npm run-android` (Kab Kya Chalaana Hai?) (Note 16)
        * `gradlew clean` (Kab aur Kyun?) (Note 15)
        * `adb reverse` (Note 16, 25)
        * Config Files (`metro.config.js`, `babel.config.js`) (Note 17)
        * NPM Commands (`list`, `outdated`, `audit`) (Note 18)
    * 1.4: Styling (StyleSheet, Inline vs External)
        * External StyleSheet (CSS vs RN `StyleSheet`) (Note 1)
        * `LinearGradient` (Note 8)
    * 1.5: State Management (Introduction with `useState` Hook)
        * **Comparison:** `useState` vs `react-hook-form` (Note 1)
    * 1.6: Additional Info: `onPress` vs `onClick`
        * `TouchableHighlight` (as `onPress` example) (Note 9)
    * 1.7: Additional Info: Console Methods (`log`, `warn`, `error`)
    * 1.8: Additional Info: WebView Support
    * 1.9: Additional Info: **Comparison:** Debug vs Release Builds (Note 42)
    * 1.10: Additional Info: Permissions (Android `AndroidManifest.xml`) (Note 29, 38, 40)

* **Module 2: Core Components & State (Legacy & Modern)**
    * 2.1: Class Components (Sirf samajhne ke liye)
    * 2.2: **Comparison:** Functional vs Class Components (Hum Functional kyun use karte hain)
    * 2.3: Props (Data paas karna)
    * 2.4: Activity Indicator (Loading spinner)
        * *Advanced:* `Skeleton Loaders` (Note 35)
    * 2.5: Buttons (Basic button)
    * 2.6: `TouchableHighlight` & TouchableWithoutFeedback (Note 9)

* **Module 3: Lists, Images & Modals**
    * 3.1: `FlatList` (Efficient scrollable lists) (Note 33, 49)
    * 3.2: SectionList (Grouped lists)
    * 3.3: `Image` (Local vs Network images)
        * `ImageBackground` (Note 14)
        * Image Optimization: `FastImage` (Note 34)
        * Image Caching (Note 34)
    * 3.4: `Modal` (Popup windows) (Note 3)
    * 3.5: `Alert` (Note 3)
    * 3.6: `react-native-swiper` (Note 7)

* **Module 4: UI Controls & Core APIs**
    * 4.1: `Pressable` (Modern touch handling)
    * 4.2: Switch (Toggle on/off)
    * 4.3: `ScrollView` (Simple scrolling content)
    * 4.4: `View` Component (The `div` of React Native)
    * 4.5: `Text` Component (Saara text isme)
    * 4.6: `TextInput` (User se input lena)
        * `KeyboardAvoidingView` (Note 1)
    * 4.7: DateTime Picker (Date/Time chunna)
    * 4.8: `Picker` / `RNPickerSelect` (Note 14, 19)
    * 4.9: `SafeAreaView` (Note 14, 19)
    * 4.10: `StatusBar` (Note 14)
    * 4.11: `Toast` (Note 14)
    * 4.12: `AppState` (App Lifecycle) (Note 2, 28)

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

