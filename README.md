# PROJECT SPECIFICATION: LỊCH VẠN NIÊN VIỆT NAM

## 1. THÔNG TIN TỔNG QUAN

### 1.1 Mô tả dự án
- **Tên dự án**: Lịch Vạn Niên Việt Nam
- **Loại website**: Web Application - Tra cứu lịch
- **Mục đích chính**: Cung cấp thông tin lịch âm dương, ngày tốt xấu, giờ hoàng đạo, và các thông tin phong thủy truyền thống Việt Nam
- **Đối tượng người dùng**: 
  - Người Việt Nam ở mọi lứa tuổi
  - Người quan tâm đến văn hóa truyền thống
  - Người cần tra cứu ngày giờ tốt cho các sự kiện quan trọng
- **Vấn đề giải quyết**: Tra cứu nhanh thông tin lịch âm, ngày tốt xấu, giờ hoàng đạo mà không cần sử dụng lịch giấy truyền thống

### 1.2 Phạm vi dự án
- **Timeline**: 4-6 tuần
- **Version**: v1.0 (MVP)
- **Deployment**: Vercel hoặc Netlify

---

## 2. YÊU CẦU KỸ THUẬT

### 2.1 Technology Stack
```
Frontend Framework: React 18+
Styling: Tailwind CSS
State Management: React Context API + useState/useReducer
Build Tool: Vite
Package Manager: npm
Date Library: date-fns, lunar-calendar-vi (hoặc tự implement)
```

### 2.2 Browser Support
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)
- Mobile browsers: iOS Safari, Chrome Mobile

### 2.3 Performance Requirements
- First Contentful Paint: < 1.5s
- Time to Interactive: < 2.5s
- Lighthouse Score: > 92
- Bundle size: < 500KB (initial load)

### 2.4 Storage & Data
- **Client-side storage**: localStorage (lưu preferences, ngày yêu thích)
- **Backend API**: None (tính toán client-side)
- **Database**: None (sử dụng algorithms để tính toán)
- **Authentication**: None

---

## 3. TÍNH NĂNG CHI TIẾT

### 3.1 Feature List
| STT | Tính năng | Độ ưu tiên | Mô tả ngắn |
|-----|-----------|------------|------------|
| 1 | Lịch tháng hiện tại | High | Hiển thị lịch dương với thông tin âm lịch |
| 2 | Chuyển đổi lịch âm-dương | High | Tra cứu ngày âm lịch tương ứng |
| 3 | Lịch vạn sự | High | Hiển thị ngày tốt/xấu cho từng việc |
| 4 | Giờ hoàng đạo | Medium | Hiển thị 12 giờ trong ngày |
| 5 | Thông tin can chi | Medium | Can chi ngày, tháng, năm |
| 6 | Ngày lễ Việt Nam | High | Hiển thị ngày lễ, tết |
| 7 | Tìm ngày tốt | Medium | Tìm ngày tốt theo mục đích |
| 8 | Lưu ngày quan trọng | Low | Bookmark các ngày đặc biệt |

### 3.2 Chi tiết từng tính năng

#### Feature 1: Lịch tháng hiện tại
**Mô tả**: Hiển thị lịch tháng với đầy đủ thông tin âm dương, màu sắc phân biệt ngày tốt/xấu

**User Story**: 
- Là người dùng, tôi muốn xem lịch tháng với thông tin âm lịch để biết ngày âm hôm nay và lên kế hoạch

**User Flow**:
1. User mở website
2. System hiển thị lịch tháng hiện tại
3. User click vào ngày bất kỳ
4. System hiển thị chi tiết ngày đó (modal/sidebar)

**Input/Output**:
- Input: Không cần (auto load tháng hiện tại)
- Output: 
  - Calendar grid 7x5 hoặc 7x6
  - Mỗi ô hiển thị: ngày dương, ngày âm, màu sắc ngày
  - Highlight ngày hôm nay
- Validation: N/A

**Hiển thị mỗi ngày**:
- Ngày dương (số to)
- Ngày âm (số nhỏ, màu xám) - VD: "Mùng 5"
- Tháng âm (nếu là ngày 1) - VD: "Tháng Giêng"
- Sao (tốt/xấu) - Dot màu đỏ/xanh/vàng
- Ngày lễ (nếu có) - Icon hoặc text nhỏ

**Edge Cases**:
- Tháng có 28/29/30/31 ngày
- Tháng nhuận âm lịch
- Năm nhuận dương lịch

#### Feature 2: Chuyển đổi lịch âm-dương
**Mô tả**: Công cụ tra cứu chuyển đổi giữa lịch âm và lịch dương

**User Story**: 
- Là người dùng, tôi muốn biết ngày 15/8 âm lịch năm nay là ngày nào dương lịch

**User Flow**:
1. User chọn tab "Tra cứu lịch"
2. User chọn loại tra cứu (Âm→Dương hoặc Dương→Âm)
3. User nhập ngày/tháng/năm
4. System hiển thị kết quả chuyển đổi + thông tin chi tiết

**Input/Output**:
- Input: 
  - Ngày (1-30), Tháng (1-12), Năm (1900-2100)
  - Checkbox tháng nhuận (cho âm lịch)
- Output:
  - Ngày tương ứng
  - Can chi ngày/tháng/năm
  - Sao tốt xấu
  - Giờ hoàng đạo
- Validation:
  - Ngày hợp lệ (1-31 cho dương, 1-30 cho âm)
  - Tháng hợp lệ (1-12)
  - Năm trong range (1900-2100)

**Error Handling**:
- Error message: "Ngày không hợp lệ. Vui lòng kiểm tra lại"
- Fallback: Highlight input bị lỗi màu đỏ

#### Feature 3: Lịch vạn sự
**Mô tả**: Hiển thị các việc nên làm và không nên làm trong ngày theo phong thủy

**Các việc cần hiển thị**:
- **Việc NÊN làm**: 
  - Khai trương
  - Động thổ, xây dựng
  - Cưới hỏi
  - Xuất hành, đi xa
  - Nhập trạch (dọn vào nhà mới)
  - An táng
  - Cầu tự, lễ bái
  
- **Việc KIÊNG làm**:
  - Tất cả các việc trên (nếu ngày xấu)

**User Flow**:
1. User click vào một ngày trong lịch
2. System hiển thị modal/panel chi tiết
3. Hiển thị 2 cột: "Nên làm" (xanh) và "Không nên làm" (đỏ)

**Data Structure**:
```javascript
const vanSu = {
  nenLam: ['Khai trương', 'Cưới hỏi', 'Xuất hành'],
  kiengLam: ['Động thổ', 'An táng']
}
```

#### Feature 4: Giờ hoàng đạo
**Mô tả**: Hiển thị 12 giờ trong ngày với thông tin giờ tốt/xấu

**12 Giờ theo địa chi**:
- Tý (23h-01h)
- Sửu (01h-03h)
- Dần (03h-05h)
- Mão (05h-07h)
- Thìn (07h-09h)
- Tỵ (09h-11h)
- Ngọ (11h-13h)
- Mùi (13h-15h)
- Thân (15h-17h)
- Dậu (17h-19h)
- Tuất (19h-21h)
- Hợi (21h-23h)

**Hiển thị**:
- Timeline dọc hoặc grid 12 ô
- Mỗi giờ có màu: Xanh (tốt), Đỏ (xấu), Vàng (bình thường)
- Icon hoặc ký hiệu 黃道 cho giờ hoàng đạo
- Highlight giờ hiện tại

#### Feature 5: Thông tin can chi
**Mô tả**: Hiển thị can chi của ngày, tháng, năm

**10 Thiên Can**: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
**12 Địa Chi**: Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi

**Hiển thị**:
```
Năm: Giáp Thìn (甲辰)
Tháng: Bính Thân (丙申)
Ngày: Kỷ Mão (己卯)
Giờ: [Tính theo giờ hiện tại]
```

**Thêm thông tin**:
- Ngũ hành (Kim, Mộc, Thủy, Hỏa, Thổ)
- Cung mệnh tương sinh/tương khắc
- Con giáp năm

#### Feature 6: Ngày lễ Việt Nam
**Mô tả**: Highlight và hiển thị các ngày lễ, tết

**Ngày lễ Dương lịch**:
- 01/01: Tết Dương lịch
- 14/02: Valentine
- 08/03: Quốc tế Phụ nữ
- 30/04: Giải phóng miền Nam
- 01/05: Quốc tế Lao động
- 01/06: Quốc tế Thiếu nhi
- 02/09: Quốc khánh
- 20/10: Phụ nữ Việt Nam
- 20/11: Ngày Nhà giáo
- 24/12: Giáng sinh
- 25/12: Giáng sinh

**Ngày lễ Âm lịch**:
- 01-03/01: Tết Nguyên Đán
- 15/01: Rằm tháng Giêng
- 10/03: Giỗ Tổ Hùng Vương
- 15/04: Phật Đản
- 05/05: Tết Đoan Ngọ
- 15/07: Vu Lan
- 15/08: Tết Trung Thu
- 23/12: Ông Táo chầu trời

**Hiển thị**: Badge/Label trên calendar, màu sắc khác biệt

#### Feature 7: Tìm ngày tốt
**Mô tả**: Tool tìm kiếm ngày tốt theo mục đích trong khoảng thời gian

**User Flow**:
1. User chọn mục đích (dropdown)
2. User chọn khoảng thời gian (date range picker)
3. System hiển thị list các ngày tốt sắp xếp theo độ tốt
4. User click vào ngày để xem chi tiết

**Mục đích**:
- Khai trương, mở cửa hàng
- Cưới hỏi
- Động thổ, xây dựng
- Xuất hành, đi xa
- Nhập trạch
- An táng
- Mua xe, mua nhà

**Output**:
- List card các ngày tốt
- Mỗi card hiển thị:
  - Ngày dương + ngày âm
  - Điểm số (★★★★★)
  - Can chi ngày
  - Lý do (sao tốt, giờ hoàng đạo nhiều...)
  - Button "Xem chi tiết"

#### Feature 8: Lưu ngày quan trọng
**Mô tả**: Cho phép user bookmark các ngày để xem lại sau

**User Flow**:
1. User click icon bookmark trên một ngày
2. System lưu vào localStorage
3. User có thể xem list ngày đã lưu ở tab riêng
4. User có thể thêm note cho ngày đã lưu

**Data Structure**:
```javascript
const savedDates = [
  {
    id: 'uuid',
    date: '2024-12-25',
    lunarDate: '25/11/2024',
    note: 'Ngày cưới',
    createdAt: timestamp
  }
]
```

---

## 4. THIẾT KẾ UI/UX

### 4.1 Layout Structure
```
Header
  └── Logo + Tên website
  └── Navigation Menu
      - Lịch tháng
      - Tra cứu lịch
      - Tìm ngày tốt
      - Ngày đã lưu
  └── Date Selector (Tháng/Năm)

Main Content
  └── Calendar Grid (Primary View)
      └── 7 cột (CN - T7)
      └── 5-6 hàng
  └── Detail Panel/Modal (khi click vào ngày)
      └── Thông tin chi tiết ngày
      └── Lịch vạn sự
      └── Giờ hoàng đạo
      └── Can chi

Sidebar (Optional - Desktop)
  └── Ngày hôm nay
  └── Quick info
  └── Lunar date

Footer
  └── Thông tin copyright
  └── Disclaimer
  └── Social links
```

### 4.2 Design System

**Colors**:
```css
/* Primary - Màu đỏ truyền thống */
Primary: #DC2626 (red-600)
Primary Light: #FCA5A5 (red-300)
Primary Dark: #991B1B (red-800)

/* Secondary - Màu vàng may mắn */
Secondary: #F59E0B (amber-500)
Secondary Light: #FDE68A (amber-200)

/* Accent - Màu xanh lá */
Accent: #10B981 (emerald-500)

/* Background */
Background: #FFFFFF
Background Secondary: #F9FAFB (gray-50)

/* Text */
Text Primary: #111827 (gray-900)
Text Secondary: #6B7280 (gray-500)

/* Status colors */
Good Day: #10B981 (green-500)
Bad Day: #EF4444 (red-500)
Normal Day: #F59E0B (amber-500)

/* Calendar specific */
Today Highlight: #DC2626 (red-600)
Weekend: #EF4444 (red-500)
Lunar Date: #6B7280 (gray-500)
Holiday: #DC2626 (red-600)
```

**Typography**:
```css
Font Family: 'Inter', 'Roboto', system-ui, sans-serif
Vietnamese Support: 'Be Vietnam Pro', 'Noto Sans'

Heading 1: 32px, 700 (Tên tháng năm)
Heading 2: 24px, 600 (Tiêu đề sections)
Heading 3: 20px, 600 (Tiêu đề cards)
Body Large: 16px, 400 (Nội dung chính)
Body: 14px, 400 (Text thường)
Caption: 12px, 400 (Ngày âm, note nhỏ)
Small: 10px, 400 (Labels)
```

**Spacing**:
- Base unit: 4px
- Scale: [4, 8, 12, 16, 20, 24, 32, 40, 48, 64]

### 4.3 Components List
| Component | Mô tả | Props chính |
|-----------|-------|-------------|
| CalendarGrid | Lưới lịch tháng | month, year, selectedDate, onDateClick |
| DateCell | Ô ngày trong lịch | date, lunarDate, isToday, isWeekend, isHoliday, status |
| DateDetailModal | Modal chi tiết ngày | date, lunarInfo, vanSu, gioHoangDao, onClose |
| DatePicker | Chọn ngày tháng năm | value, onChange, mode |
| VanSuCard | Card hiển thị vạn sự | nenLam[], kiengLam[] |
| GioHoangDaoTimeline | Timeline 12 giờ | hours[], currentHour |
| CanChiDisplay | Hiển thị can chi | nam, thang, ngay, gio |
| HolidayBadge | Badge ngày lễ | name, type |
| LuckyDayCard | Card ngày tốt | date, score, reason |
| ConvertForm | Form chuyển đổi lịch | type, onSubmit |
| SavedDateList | List ngày đã lưu | dates[], onDelete, onEdit |
| MonthNavigator | Điều hướng tháng | currentMonth, onPrev, onNext |

### 4.4 Responsive Design
- **Mobile**: < 640px
  - Stack layout
  - Calendar grid 7x5 compact
  - Modal fullscreen
  - Bottom sheet cho details
  
- **Tablet**: 640px - 1024px
  - Calendar grid larger
  - Sidebar collapsible
  - Modal centered
  
- **Desktop**: > 1024px
  - Sidebar always visible
  - Calendar grid spacious
  - Modal centered, max-width 800px
  
- **Approach**: Mobile-first

### 4.5 Interactions & Animations

**Calendar interactions**:
- Hover effect: Subtle scale (1.02) và shadow
- Click effect: Scale down (0.98)
- Selected date: Border đậm màu primary

**Transitions**:
- Duration: 200ms cho hover, 300ms cho modal
- Easing: ease-in-out

**Loading states**:
- Skeleton cho calendar grid khi chuyển tháng
- Spinner cho calculations phức tạp

**Micro-interactions**:
- Ripple effect khi click button
- Smooth scroll khi navigate giữa các sections
- Fade in/out cho modal
- Slide up cho bottom sheet (mobile)
- Confetti animation khi bookmark ngày (optional)

**Animations**:
- Fade in calendar khi load
- Slide animation khi chuyển tháng (prev/next)
- Bounce animation cho "ngày hôm nay"
- Pulse animation cho notifications

---

## 5. CẤU TRÚC DỮ LIỆU

### 5.1 Data Models

```javascript
// Thông tin ngày
const DayInfo = {
  // Dương lịch
  solarDate: Date,
  dayOfWeek: 0-6, // 0=CN, 6=T7
  
  // Âm lịch
  lunarDay: 1-30,
  lunarMonth: 1-12,
  lunarYear: number,
  isLeapMonth: boolean,
  
  // Can chi
  canChi: {
    nam: string, // "Giáp Thìn"
    thang: string,
    ngay: string,
    gio: string
  },
  
  // Ngũ hành
  nguHanh: {
    nam: 'Kim' | 'Mộc' | 'Thủy' | 'Hỏa' | 'Thổ',
    ngay: 'Kim' | 'Mộc' | 'Thủy' | 'Hỏa' | 'Thổ'
  },
  
  // Con giáp
  conGiap: string, // "Rồng"
  
  // Sao
  sao: {
    name: string,
    status: 'tot' | 'xau' | 'binh-thuong',
    description: string
  },
  
  // Vạn sự
  vanSu: {
    nenLam: string[],
    kiengLam: string[]
  },
  
  // Giờ hoàng đạo
  gioHoangDao: GioInfo[],
  
  // Ngày lễ (nếu có)
  holiday?: {
    name: string,
    type: 'solar' | 'lunar',
    isPublicHoliday: boolean
  }
}

// Thông tin giờ
const GioInfo = {
  diaChi: string, // "Tý", "Sửu"...
  timeRange: string, // "23:00-01:00"
  status: 'tot' | 'xau' | 'binh-thuong',
  canChiGio: string
}

// Ngày đã lưu
const SavedDate = {
  id: string,
  date: string, // ISO format
  lunarDate: string,
  note: string,
  category: 'wedding' | 'business' | 'travel' | 'other',
  createdAt: timestamp,
  reminderDays?: number // Nhắc trước X ngày
}

// User preferences
const UserPreferences = {
  defaultView: 'month' | 'list',
  showLunarDate: boolean,
  showHolidays: boolean,
  highlightWeekends: boolean,
  theme: 'light' | 'dark'
}
```

### 5.2 State Management Structure
```javascript
// Global State (Context)
const AppState = {
  // Calendar state
  currentDate: Date,
  selectedDate: Date | null,
  viewMode: 'month' | 'list' | 'search',
  
  // Data state
  monthData: DayInfo[], // 28-31 ngày
  savedDates: SavedDate[],
  
  // UI state
  isDetailModalOpen: boolean,
  isSearchModalOpen: boolean,
  isSidebarOpen: boolean,
  
  // User preferences
  preferences: UserPreferences,
  
  // Loading states
  isCalculating: boolean,
  error: string | null
}

// Actions
const actions = {
  setCurrentDate,
  selectDate,
  changeViewMode,
  saveDate,
  removeSavedDate,
  updatePreferences,
  navigateMonth, // prev/next
  searchGoodDays
}
```

### 5.3 Calculation Functions

```javascript
// Core functions cần implement
const lunarCalculations = {
  // Chuyển đổi dương → âm
  solarToLunar(day, month, year) => { lunarDay, lunarMonth, lunarYear, isLeapMonth },
  
  // Chuyển đổi âm → dương
  lunarToSolar(lunarDay, lunarMonth, lunarYear, isLeapMonth) => { day, month, year },
  
  // Tính can chi
  getCanChi(day, month, year) => { nam, thang, ngay },
  getCanChiGio(hour, day, month, year) => string,
  
  // Tính con giáp
  getZodiac(year) => string,
  
  // Tính ngũ hành
  getNguHanh(canChi) => 'Kim' | 'Mộc' | 'Thủy' | 'Hỏa' | 'Thổ',
  
  // Tính sao
  getSao(day, month, year) => { name, status, description },
  
  // Tính vạn sự
  getVanSu(canChi) => { nenLam[], kiengLam[] },
  
  // Tính giờ hoàng đạo
  getGioHoangDao(day, month, year) => GioInfo[],
  
  // Check ngày tốt
  isGoodDay(day, month, year, purpose) => boolean,
  
  // Tính điểm ngày (1-5 sao)
  calculateDayScore(dayInfo, purpose) => number
}
```

### 5.4 Local Storage Keys
```javascript
const STORAGE_KEYS = {
  SAVED_DATES: 'lich_van_nien_saved_dates',
  USER_PREFERENCES: 'lich_van_nien_preferences',
  LAST_VISITED_DATE: 'lich_van_nien_last_date',
  FAVORITE_PURPOSES: 'lich_van_nien_favorite_purposes'
}
```

### 5.5 Constants Data

```javascript
// 10 Thiên Can
const THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý'];

// 12 Địa Chi
const DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi'];

// 12 Con giáp
const CON_GIAP = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi'];

// Ngũ hành
const NGU_HANH = {
  'Giáp': 'Mộc', 'Ất': 'Mộc',
  'Bính': 'Hỏa', 'Đinh': 'Hỏa',
  'Mậu': 'Thổ', 'Kỷ': 'Thổ',
  'Canh': 'Kim', 'Tân': 'Kim',
  'Nhâm': 'Thủy', 'Quý': 'Thủy'
};

// Danh sách các việc trong vạn sự
const VAN_SU_ITEMS = {
  nenLam: [
    'Khai trương, mở cửa hàng',
    'Động thổ, xây dựng',
    'Cưới hỏi, ăn hỏi',
    'Xuất hành, đi xa',
    'Nhập trạch, dọn nhà',
    'An táng, mai táng',
    'Cầu tự, lễ bái',
    'Ký kết hợp đồng',
    'Giao dịch tài chính',
    'Cắt tóc, làm đẹp'
  ],
  kiengLam: [
    'Khai trương, mở cửa hàng',
    'Động thổ, xây dựng',
    'Cưới hỏi, ăn hỏi',
    'Xuất hành, đi xa',
    'Nhập trạch, dọn nhà',
    'An táng, mai táng',
    'Kiện tụng, tranh chấp',
    'Phẫu thuật',
    'Đầu tư lớn',
    'Cắt tóc, làm đẹp'
  ]
};

// Ngày lễ dương lịch
const SOLAR_HOLIDAYS = [
  { date: '01-01', name: 'Tết Dương lịch', isPublic: true },
  { date: '14-02', name: 'Valentine', isPublic: false },
  { date: '08-03', name: 'Quốc tế Phụ nữ', isPublic: false },
  { date: '30-04', name: 'Giải phóng miền Nam', isPublic: true },
  { date: '01-05', name: 'Quốc tế Lao động', isPublic: true },
  { date: '01-06', name: 'Quốc tế Thiếu nhi', isPublic: false },
  { date: '02-09', name: 'Quốc khánh Việt Nam', isPublic: true },
  { date: '20-10', name: 'Ngày Phụ nữ Việt Nam', isPublic: false },
  { date: '20-11', name: 'Ngày Nhà giáo Việt Nam', isPublic: false },
  { date: '24-12', name: 'Giáng sinh', isPublic: false },
  { date: '25-12', name: 'Giáng sinh', isPublic: false }
];

// Ngày lễ âm lịch (format: 'MM-DD')
const LUNAR_HOLIDAYS = [
  { date: '01-01', name: 'Tết Nguyên Đán (Mùng 1)', isPublic: true },
  { date: '01-02', name: 'Tết Nguyên Đán (Mùng 2)', isPublic: true },
  { date: '01-03', name: 'Tết Nguyên Đán (Mùng 3)', isPublic: true },
  { date: '01-15', name: 'Rằm tháng Giêng', isPublic: false },
  { date: '03-10', name: 'Giỗ Tổ Hùng Vương', isPublic: true },
  { date: '04-15', name: 'Phật Đản', isPublic: false },
  { date: '05-05', name: 'Tết Đoan Ngọ', isPublic: false },
  { date: '07-15', name: 'Vu Lan (Rằm tháng 7)', isPublic: false },
  { date: '08-15', name: 'Tết Trung Thu', isPublic: false },
  { date: '12-23', name: 'Ông Táo chầu trời', isPublic: false }
];

// Mục đích tra cứu ngày tốt
const PURPOSES = [
  { id: 'khai-truong', name: 'Khai trương, mở cửa hàng', icon: '🏪' },
  { id: 'cuoi-hoi', name: 'Cưới hỏi, ăn hỏi', icon: '💒' },
  { id: 'dong-tho', name: 'Động thổ, xây dựng', icon: '🏗️' },
  { id: 'xuat-hanh', name: 'Xuất hành, đi xa', icon: '✈️' },
  { id: 'nhap-trach', name: 'Nhập trạch, dọn nhà', icon: '🏠' },
  { id: 'an-tang', name: 'An táng, mai táng', icon: '⚰️' },
  { id: 'mua-xe', name: 'Mua xe, tài sản lớn', icon: '🚗' },
  { id: 'ky-ket', name: 'Ký kết hợp đồng', icon: '📝' }
];
```

---

## 6. YÊU CẦU BẢO MẬT

- [x] Input sanitization cho tất cả form inputs (date inputs)
- [x] XSS protection (React tự động escape)
- [x] Validate date range để tránh overflow
- [x] HTTPS only khi deploy production
- [x] No sensitive data (không có authentication)
- [x] Rate limiting không cần thiết (client-side only)
- [x] CSP headers khi deploy

**Specific security concerns**:
- Validate input dates nằm trong range 1900-2100
- Prevent calculation overflow với dates quá xa
- Sanitize user notes trong saved dates

---

## 7. YÊU CẦU ACCESSIBILITY (A11Y)

- [x] Semantic HTML tags (`<time>`, `<table>` cho calendar)
- [x] ARIA labels cho calendar navigation
  - `aria-label="Tháng trước"` cho prev button
  - `aria-label="Tháng sau"` cho next button
  - `aria-selected="true"` cho ngày được chọn
  - `aria-current="date"` cho ngày hôm nay
- [x] Keyboard navigation support
  - Tab: di chuyển giữa các controls
  - Arrow keys: navigate trong calendar grid
  - Enter/Space: select date
  - Esc: close modal
- [x] Focus indicators rõ ràng (outline 2px solid)
- [x] Alt text cho icons và decorative images
- [x] Color contrast ratio >= 4.5:1
  - Text màu đỏ trên nền trắng: check contrast
  - Status colors phải đủ contrast
- [x] Screen reader friendly
  - Announce ngày được chọn
  - Announce khi chuyển tháng
  - Read lunar date properly
- [x] Form labels rõ ràng
- [x] Skip to content link (nếu có nhiều navigation)

**Accessibility cho calendar**:
- Grid có `role="grid"` và proper ARIA attributes
- Mỗi ngày có `role="gridcell"`
- Announce format: "Thứ 2, ngày 15 tháng 8 năm 2024, âm lịch 12 tháng 7"

---

## 8. YÊU CẦU SEO

- [x] Meta tags đầy đủ
```html
<title>Lịch Vạn Niên Việt Nam - Tra Cứu Lịch Âm Dương</title>
<meta name="description" content="Tra cứu lịch vạn niên, lịch âm dương, ngày tốt xấu, giờ hoàng đạo, lịch vạn sự Việt Nam. Tìm ngày tốt cho khai trương, cưới hỏi, xuất hành.">
<meta name="keywords" content="lịch vạn niên, lịch âm, lịch dương, ngày tốt, giờ hoàng đạo, lịch vạn sự, xem lịch, tra cứu lịch">
```

- [x] Open Graph tags
```html
<meta property="og:title" content="Lịch Vạn Niên Việt Nam">
<meta property="og:description" content="Tra cứu lịch âm dương, ngày tốt xấu, giờ hoàng đạo">
<meta property="og:image" content="/og-image.jpg">
<meta property="og:type" content="website">
```

- [x] Twitter Card tags
- [x] Structured data (Schema.org)
```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Lịch Vạn Niên Việt Nam",
  "description": "Ứng dụng tra cứu lịch âm dương Việt Nam",
  "applicationCategory": "UtilitiesApplication",
  "operatingSystem": "Web"
}
```

- [x] Semantic URL structure
  - `/` - Trang chủ (lịch tháng)
  - `/tra-cuu` - Tra cứu chuyển đổi
  - `/tim-ngay-tot` - Tìm ngày tốt
  - `/ngay-da-luu` - Ngày đã lưu

- [x] Image optimization (WebP format)
- [x] Mobile-friendly (responsive)
- [x] Fast loading time (< 2s)
- [x] Proper heading hierarchy (H1 → H2 → H3)
- [x] Internal linking structure

**SEO Content Strategy**:
- H1: "Lịch Vạn Niên Việt Nam 2024-2025"
- H2: "Xem Lịch Âm Hôm Nay", "Tra Cứu Ngày Tốt"
- Rich content về ý nghĩa các ngày lễ, can chi, etc.

---

## 9. CODE STANDARDS

### 9.1 File Structure
```
lich-van-nien/
├── public/
│   ├── favicon.ico
│   ├── og-image.jpg
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Button.jsx
│   │   │   ├── Modal.jsx
│   │   │   ├── Badge.jsx
│   │   │   └── Card.jsx
│   │   ├── calendar/
│   │   │   ├── CalendarGrid.jsx
│   │   │   ├── DateCell.jsx
│   │   │   ├── MonthNavigator.jsx
│   │   │   └── DateDetailModal.jsx
│   │   ├── features/
│   │   │   ├── VanSuCard.jsx
│   │   │   ├── GioHoangDaoTimeline.jsx
│   │   │   ├── CanChiDisplay.jsx
│   │   │   ├── ConvertForm.jsx
│   │   │   └── LuckyDayFinder.jsx
│   │   └── layouts/
│   │       ├── Header.jsx
│   │       ├── Footer.jsx
│   │       └── MainLayout.jsx
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── ConvertPage.jsx
│   │   ├── SearchPage.jsx
│   │   └── SavedDatesPage.jsx
│   ├── hooks/
│   │   ├── useCalendar.js
│   │   ├── useLunarDate.js
│   │   ├── useLocalStorage.js
│   │   └── useDateDetail.js
│   ├── utils/
│   │   ├── lunarCalculations.js
│   │   ├── canChiCalculations.js
│   │   ├── vanSuCalculations.js
│   │   ├── dateHelpers.js
│   │   └── validators.js
│   ├── services/
│   │   └── storageService.js
│   ├── context/
│   │   └── AppContext.jsx
│   ├── constants/
│   │   ├── calendar.js
│   │   ├── holidays.js
│   │   └── vanSu.js
│   ├── styles/
│   │   └── globals.css
│   ├── assets/
│   │   ├── icons/
│   │   └── images/
│   ├── App.jsx
│   └── main.jsx
├── .gitignore
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── README.md
└── ALGORITHMS.md (giải thích thuật toán âm lịch)
```

### 9.2 Naming Conventions
- **Components**: PascalCase (e.g., `CalendarGrid.jsx`, `DateCell.jsx`)
- **Functions**: camelCase (e.g., `solarToLunar()`, `getCanChi()`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `THIEN_CAN`, `DIA_CHI`)
- **CSS classes**: kebab-case với Tailwind utilities
- **Files**: PascalCase cho components, camelCase cho utilities

### 9.3 Code Style
- Indent: 2 spaces
- Quotes: Single quotes cho strings
- Semicolons: Yes
- Max line length: 100 characters
- ESLint config: Standard + React

**Component structure**:
```javascript
// Imports
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Component
export const ComponentName = ({ prop1, prop2 }) => {
  // Hooks
  const [state, setState] = useState();
  
  // Effects
  useEffect(() => {}, []);
  
  // Handlers
  const handleClick = () => {};
  
  // Render helpers
  const renderSomething = () => {};
  
  // Return
  return (
    <div></div>
  );
};

// PropTypes
ComponentName.propTypes = {
  prop1: PropTypes.string.isRequired,
  prop2: PropTypes.number
};

// Default props
ComponentName.defaultProps = {
  prop2: 0
};
```

### 9.4 Comments & Documentation
```javascript
/**
 * Chuyển đổi ngày dương lịch sang âm lịch
 * @param {number} day - Ngày dương lịch (1-31)
 * @param {number} month - Tháng dương lịch (1-12)
 * @param {number} year - Năm dương lịch
 * @returns {Object} { lunarDay, lunarMonth, lunarYear, isLeapMonth }
 * @example
 * solarToLunar(25, 12, 2024)
 * // returns { lunarDay: 25, lunarMonth: 11, lunarYear: 2024, isLeapMonth: false }
 */
export const solarToLunar = (day, month, year) => {
  // Implementation
};

// Inline comments cho logic phức tạp
// Tính số ngày Julius Day để convert âm dương
const jd = Math.floor(/* formula */);
```

---

## 10. TESTING REQUIREMENTS

### 10.1 Testing Types
- [x] Unit Tests: Coverage target: 80%
- [x] Integration Tests
- [x] E2E Tests (critical flows)
- [ ] Visual Regression Tests (optional)
- [x] Performance Tests

### 10.2 Testing Tools
- Testing Framework: Vitest
- React Testing: React Testing Library
- E2E: Playwright (hoặc Cypress)
- Coverage: Vitest coverage

### 10.3 Test Scenarios

**Unit Tests**:
- [ ] Lunar calculations accuracy
  - Test known dates (e.g., Tết 2024 = 10/02/2024)
  - Test leap months
  - Test boundary years (1900, 2100)
- [ ] Can Chi calculations
  - Test known dates with known can chi
- [ ] Date validation
  - Valid dates
  - Invalid dates (30/02, 32/01, etc.)
- [ ] Vạn sự logic
- [ ] Giờ hoàng đạo calculations

**Integration Tests**:
- [ ] Calendar navigation (prev/next month)
- [ ] Date selection flow
- [ ] Convert form submission
- [ ] Save date functionality
- [ ] LocalStorage integration

**E2E Tests**:
- [ ] User can view current month calendar
- [ ] User can click a date and see details
- [ ] User can navigate to different months
- [ ] User can convert solar to lunar date
- [ ] User can search for lucky days
- [ ] User can save and view saved dates

**Edge Cases**:
- [ ] Tháng có 28/29/30/31 ngày
- [ ] Năm nhuận (dương lịch và âm lịch)
- [ ] Tháng nhuận âm lịch
- [ ] Dates ngoài range (before 1900, after 2100)
- [ ] Invalid date inputs
- [ ] Empty saved dates list
- [ ] Network offline (PWA behavior)

---

## 11. DEPLOYMENT & CI/CD

### 11.1 Build Process
```bash
npm run build
# Output: dist/
# Size target: < 500KB (gzipped)
```

**Build optimization**:
- Tree shaking
- Code splitting by route
- Lazy load heavy calculations
- Minify CSS/JS
- Optimize images (WebP, lazy load)

### 11.2 Environments
- **Development**: `http://localhost:5173`
  - Hot reload
  - Source maps
  - Debug mode
  
- **Staging**: `https://staging-lich-van-nien.vercel.app`
  - Same as production build
  - Test environment
  
- **Production**: `https://lichvannien.vn`
  - Optimized build
  - CDN enabled
  - Analytics enabled

### 11.3 CI/CD Pipeline
```yaml
# GitHub Actions workflow
1. Code push to repository
2. Run ESLint
3. Run Vitest tests
4. Build application
5. Run Lighthouse CI
6. Deploy to Vercel (auto)
```

### 11.4 Environment Variables
```
VITE_APP_NAME=Lịch Vạn Niên Việt Nam
VITE_APP_VERSION=1.0.0
VITE_ANALYTICS_ID=G-XXXXXXXXXX
VITE_BASE_URL=https://lichvannien.vn
```

**Note**: Không có sensitive env vars vì app chỉ client-side

---

## 12. CONSTRAINTS & LIMITATIONS

### 12.1 MUST HAVE (Bắt buộc)
- [x] Tính toán lịch âm chính xác (sai số 0%)
- [x] Hỗ trợ range 1900-2100
- [x] Responsive trên mobile/tablet/desktop
- [x] Offline-capable (PWA với service worker)
- [x] Fast loading (< 2s on 3G)
- [x] Tiếng Việt là ngôn ngữ chính
- [x] No external API dependencies
- [x] Browser support: Chrome, Firefox, Safari, Edge (latest 2)

### 12.2 MUST NOT (Không được phép)
- [x] KHÔNG sử dụng paid APIs hoặc services
- [x] KHÔNG yêu cầu user đăng nhập/đăng ký
- [x] KHÔNG thu thập personal data
- [x] KHÔNG có ads xâm lấn (có thể có ads nhẹ)
- [x] KHÔNG sai lệch thông tin văn hóa truyền thống
- [x] KHÔNG vi phạm bản quyền fonts, images
- [x] KHÔNG sử dụng localStorage cho sensitive data

### 12.3 NICE TO HAVE (Tốt nếu có)
- [ ] PWA installable (Add to Home Screen)
- [ ] Dark mode
- [ ] Export calendar to PDF
- [ ] Share functionality (share ngày tốt)
- [ ] Notifications/Reminders
- [ ] Multiple themes (màu sắc phong thủy)
- [ ] Multi-language (English, Chinese)
- [ ] Widget embedding cho other websites
- [ ] Calendar sync (Google Calendar integration)

### 12.4 Dependencies Restrictions
- Maximum dependencies: 15 packages
- Allowed libraries:
  - React, React-DOM
  - date-fns (date manipulation)
  - clsx (className utilities)
  - react-icons hoặc lucide-react
  - Tailwind CSS
- Bundle size limit: < 500KB gzipped
- License requirements: MIT, Apache 2.0, ISC only

**Core calculations MUST be custom-built** (không dùng thư viện tính âm lịch có sẵn nếu không đáng tin cậy)

---

## 13. SUCCESS CRITERIA

### 13.1 Definition of Done
- [x] Tất cả features hoạt động theo spec
- [x] Lunar calculations chính xác 100% (test với 100 ngày known)
- [x] UI responsive perfect trên 3 breakpoints
- [x] Pass tất cả test cases (>80% coverage)
- [x] No critical bugs, < 5 minor bugs
- [x] Lighthouse Performance >= 92
- [x] Lighthouse Accessibility >= 95
- [x] Code review approved
- [x] Documentation complete (README + ALGORITHMS.md)
- [x] SEO meta tags đầy đủ
- [x] PWA manifest configured

### 13.2 Acceptance Criteria

**Calendar View**:
- [x] User thấy lịch tháng hiện tại khi load page
- [x] User thấy rõ ngày hôm nay (highlight màu đỏ)
- [x] User thấy ngày âm dưới ngày dương
- [x] User thấy màu sắc ngày tốt/xấu
- [x] User thấy ngày lễ được đánh dấu

**Date Detail**:
- [x] User click vào ngày → modal hiện chi tiết
- [x] Modal hiển thị: âm lịch, can chi, vạn sự, giờ hoàng đạo
- [x] User có thể đóng modal (X button, Esc, click outside)

**Navigation**:
- [x] User click "Tháng trước" → chuyển sang tháng trước
- [x] User click "Tháng sau" → chuyển sang tháng sau
- [x] Transition smooth, không bị lag
- [x] URL update khi chuyển tháng (optional)

**Convert Feature**:
- [x] User chọn Âm→Dương hoặc Dương→Âm
- [x] User nhập date valid → kết quả hiển thị đúng
- [x] User nhập date invalid → error message rõ ràng
- [x] Kết quả hiển thị đầy đủ thông tin

**Lucky Day Search**:
- [x] User chọn mục đích từ dropdown
- [x] User chọn date range
- [x] System trả về >= 1 ngày tốt
- [x] Kết quả sort theo điểm từ cao → thấp
- [x] User click vào kết quả → xem chi tiết

**Save Dates**:
- [x] User click bookmark icon → ngày được lưu
- [x] Toast notification "Đã lưu ngày"
- [x] User xem list ngày đã lưu ở tab riêng
- [x] User có thể xóa ngày đã lưu
- [x] Data persist sau khi reload page

**Performance**:
- [x] Initial load < 2s on 4G
- [x] Calendar render < 100ms
- [x] Month navigation < 50ms
- [x] Calculation (convert, search) < 500ms

**Responsive**:
- [x] Mobile (375px): layout stack, calendar compact
- [x] Tablet (768px): sidebar collapsible
- [x] Desktop (1280px): sidebar fixed, calendar spacious

### 13.3 Quality Metrics
- Code coverage: >= 80%
- Lighthouse Performance: >= 92
- Lighthouse Accessibility: >= 95
- Lighthouse Best Practices: >= 90
- Lighthouse SEO: >= 95
- Cumulative Layout Shift (CLS): < 0.1
- First Input Delay (FID): < 100ms
- Largest Contentful Paint (LCP): < 2.5s

**Calculation Accuracy**:
- Test 100 known solar-lunar conversions: 100% accurate
- Test 50 known can chi dates: 100% accurate
- Cross-reference với lịch vạn niên truyền thống

---

## 14. MAINTENANCE & SUPPORT

### 14.1 Documentation Requirements
- [x] **README.md**:
  - Project overview
  - Tech stack
  - Installation steps
  - Development guide
  - Build & deployment
  - Folder structure
  
- [x] **ALGORITHMS.md**:
  - Giải thích thuật toán tính âm lịch
  - Công thức can chi
  - Logic vạn sự
  - References/sources
  
- [x] **CONTRIBUTING.md** (nếu open source):
  - Code style guide
  - How to contribute
  - Pull request process
  
- [x] **CHANGELOG.md**:
  - Version history
  - Feature additions
  - Bug fixes

### 14.2 Monitoring
- **Error tracking**: 
  - Console errors logging
  - Sentry (optional) cho production
  - Custom error boundary
  
- **Analytics**: 
  - Google Analytics 4
  - Track: page views, feature usage, conversions
  
- **Performance monitoring**:
  - Web Vitals tracking
  - Custom performance marks
  - Lighthouse CI on every deploy

**Key metrics to monitor**:
- Daily active users
- Most viewed months
- Most used features (convert, search, save)
- Error rate
- Performance scores
- Bounce rate

### 14.3 Update Strategy
- **Dependency updates**: Monthly security check
- **Security patches**: Within 24-48h
- **Feature updates**: 
  - Minor: Monthly
  - Major: Quarterly
  
**Version numbering**: Semantic versioning (MAJOR.MINOR.PATCH)
- 1.0.0: Initial release
- 1.1.0: New features
- 1.0.1: Bug fixes

### 14.4 Backup & Data
- **LocalStorage data**: 
  - User can export saved dates as JSON
  - Import functionality for data recovery
  
- **No backend**: No backup needed for calculations
  
---

## 15. RISKS & MITIGATION

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Lunar calculation inaccurate | High | Medium | Thoroughly test with known dates, cross-reference multiple sources, implement validation |
| Performance issues on old devices | Medium | Medium | Code splitting, lazy loading, optimize calculations, use Web Workers for heavy computations |
| Browser compatibility issues | Medium | Low | Test on all major browsers, use Babel for transpiling, polyfills for old browsers |
| LocalStorage quota exceeded | Low | Low | Implement limit on saved dates (max 100), show warning when approaching limit |
| Calculation takes too long | Medium | Low | Optimize algorithms, use memoization, show loading indicator |
| Cultural information inaccuracy | High | Medium | Research thoroughly, cite sources, add disclaimer, allow user feedback |
| SEO not effective | Medium | Medium | Implement all SEO best practices, rich content, backlinks strategy |
| User confusion with UI | Medium | Low | User testing, clear labels, tooltips, help section |

---

## 16. REFERENCES & RESOURCES

### 16.1 Design Assets
- Figma design: [To be created]
- Design inspiration:
  - https://www.lich-van-nien.com
  - https://lichviet.com
  - Traditional Vietnamese calendar designs
  
- Icons: Lucide React hoặc React Icons
- Fonts: 
  - Primary: Inter (Google Fonts)
  - Vietnamese: Be Vietnam Pro

### 16.2 Technical Documentation
- **Lunar Calendar Algorithms**:
  - Vietnamese Lunar Calendar (Âm Lịch Việt Nam)
  - Julius Day Number calculations
  - Traditional Vietnamese astronomy methods
  
- **References**:
  - "Lịch Việt Nam và các thuật toán tính toán"
  - Ngô Tất Tố's calendar research
  - Institute of Astronomy Vietnam
  
- **Open source references**:
  - https://github.com/tinyheero/lunar-calendar (for reference only)
  - Date-fns documentation
  
### 16.3 Cultural Resources
- Văn hóa dân gian Việt Nam về lịch âm
- Phong tục tập quán ngày tết
- Ý nghĩa can chi trong văn hóa Việt
- Lịch sử lịch vạn niên Việt Nam

### 16.4 Similar Projects
- Lich-van-nien.com
- Lichviet.com
- Xemlicham.com
- Google Calendar (for UX inspiration)

---

## 17. NOTES & ASSUMPTIONS

### 17.1 Assumptions
- Users primarily access from mobile devices (60%)
- Users are familiar with traditional Vietnamese calendar concepts
- Most common use case: checking current month
- Internet connection available (for initial load)
- Users understand basic Vietnamese
- LocalStorage is available and enabled

### 17.2 Important Notes
- **Calculation accuracy is CRITICAL**: Any error will damage credibility
- **Cultural sensitivity**: Must respect traditional beliefs and customs
- **No medical/fortune telling claims**: Disclaimer that info is for cultural reference only
- **Open to feedback**: Add feedback mechanism for users to report inaccuracies
- **Progressive enhancement**: Core features work without JS (where possible)
- **Future scalability**: Code structure allows adding new features easily

### 17.3 Questions & Clarifications Needed
- [ ] Specific lunar calculation method to use? (Vietnam Institute of Astronomy vs traditional)
- [ ] Include zodiac compatibility calculator?
- [ ] Add age calculation by lunar calendar?
- [ ] Include naming conventions for babies based on birth date?
- [ ] Add Feng Shui directions based on birth year?
- [ ] Support for historical dates (before 1900)?
- [ ] Monetization strategy (ads, premium features)?

### 17.4 Disclaimer Text
```
Lưu ý: Thông tin về lịch âm, ngày tốt xấu, giờ hoàng đạo được cung cấp 
dựa trên văn hóa truyền thống Việt Nam và mang tính chất tham khảo. 
Chúng tôi không chịu trách nhiệm về các quyết định cá nhân dựa trên 
thông tin này.
```

---

## 18. PHÂN TÍCH THUẬT TOÁN TÍNH ÂM LỊCH

### 18.1 Nguyên lý cơ bản
Âm lịch Việt Nam dựa trên:
- Chu kỳ trăng (29.5 ngày/tháng)
- Chu kỳ mặt trời (365.25 ngày/năm)
- Hệ thống can chi 60 năm

### 18.2 Steps to calculate
1. **Convert to Julius Day Number**:
   - Universal time system
   - Base: January 1, 4713 BC
   
2. **Calculate lunar month**:
   - New moon dates
   - Month length (29 or 30 days)
   
3. **Determine leap month**:
   - 7 leap months per 19 years
   - Leap month rules
   
4. **Calculate Can Chi**:
   - 10 Heavenly Stems cycle
   - 12 Earthly Branches cycle
   - 60-year cycle combination

### 18.3 Libraries & References
- Sử dụng thuật toán của Viện Khoa học Việt Nam
- Cross-reference với lịch truyền thống
- Test extensively với known dates

### 18.4 Edge Cases
- Tháng nhuận (leap month)
- Năm nhuận (leap year)
- Chuyển đổi giữa múi giờ
- Ngày đầu tháng âm lịch

---

## 19. ROADMAP & FUTURE FEATURES

### 19.1 Version 1.0 (MVP) - Launch
- ✅ Core calendar view
- ✅ Solar-Lunar conversion
- ✅ Vạn sự information
- ✅ Giờ hoàng đạo
- ✅ Can chi display
- ✅ Holidays marking
- ✅ Save dates functionality

### 19.2 Version 1.1 - Enhancement (Month 2-3)
- [ ] Dark mode
- [ ] PWA with offline support
- [ ] Share functionality
- [ ] Export calendar to image
- [ ] Search history
- [ ] Quick date picker widget

### 19.3 Version 1.2 - Advanced Features (Month 4-6)
- [ ] Zodiac compatibility calculator
- [ ] Age calculator (lunar age)
- [ ] Personal horoscope based on birth date
- [ ] Feng Shui directions calculator
- [ ] Lucky numbers generator
- [ ] Notification reminders for saved dates

### 19.4 Version 2.0 - Major Update (Month 7-12)
- [ ] Multi-language support (English, Chinese)
- [ ] Calendar widget for external websites
- [ ] API for developers
- [ ] Premium features (ad-free, advanced calculations)
- [ ] Social features (share lucky days)
- [ ] Integration with Google Calendar
- [ ] Mobile app (React Native)

### 19.5 Future Considerations
- [ ] AI-powered personal recommendations
- [ ] Community features (share experiences on lucky days)
- [ ] Historical dates database
- [ ] Educational content about Vietnamese culture
- [ ] Collaboration with cultural organizations

---

## 20. DEVELOPMENT PHASES

### Phase 1: Setup & Core Structure (Week 1)
**Tasks**:
- [x] Initialize Vite + React project
- [x] Setup Tailwind CSS
- [x] Configure ESLint, Prettier
- [x] Setup folder structure
- [x] Create basic layout components (Header, Footer)
- [x] Setup routing (if using React Router)
- [x] Create constants files
- [x] Setup Context API

**Deliverable**: Working dev environment with basic layout

---

### Phase 2: Lunar Calculation Engine (Week 1-2)
**Tasks**:
- [x] Research and implement Julius Day conversion
- [x] Implement Solar to Lunar conversion
- [x] Implement Lunar to Solar conversion
- [x] Implement Can Chi calculations
- [x] Implement Ngũ Hành calculations
- [x] Write unit tests for all calculations
- [x] Validate against known dates (100 test cases)
- [x] Document algorithms in ALGORITHMS.md

**Deliverable**: Accurate calculation engine with 100% test coverage

---

### Phase 3: Calendar UI (Week 2-3)
**Tasks**:
- [x] Create CalendarGrid component
- [x] Create DateCell component
- [x] Implement month navigation
- [x] Highlight today's date
- [x] Display lunar dates on each cell
- [x] Add holiday badges
- [x] Implement date selection
- [x] Add responsive design
- [x] Test on multiple devices

**Deliverable**: Fully functional calendar view

---

### Phase 4: Date Detail View (Week 3)
**Tasks**:
- [x] Create DateDetailModal component
- [x] Display full lunar information
- [x] Implement VanSuCard component
- [x] Implement GioHoangDaoTimeline component
- [x] Implement CanChiDisplay component
- [x] Add animations and transitions
- [x] Test modal interactions
- [x] Implement keyboard navigation

**Deliverable**: Comprehensive date detail view

---

### Phase 5: Conversion Feature (Week 4)
**Tasks**:
- [x] Create ConvertForm component
- [x] Implement form validation
- [x] Connect to calculation engine
- [x] Display conversion results
- [x] Add error handling
- [x] Implement form reset
- [x] Add examples/help text
- [x] Test edge cases

**Deliverable**: Working conversion tool

---

### Phase 6: Lucky Day Finder (Week 4-5)
**Tasks**:
- [x] Create search form UI
- [x] Implement date range picker
- [x] Implement purpose selector
- [x] Create scoring algorithm
- [x] Implement search function
- [x] Display results as cards
- [x] Add sort/filter options
- [x] Test with various scenarios

**Deliverable**: Lucky day search functionality

---

### Phase 7: Saved Dates Feature (Week 5)
**Tasks**:
- [x] Implement localStorage service
- [x] Create save/delete functionality
- [x] Create SavedDatesList component
- [x] Add notes/categories
- [x] Implement export/import
- [x] Add data validation
- [x] Test localStorage limits
- [x] Handle quota exceeded error

**Deliverable**: Complete saved dates feature

---

### Phase 8: Polish & Optimization (Week 5-6)
**Tasks**:
- [x] Performance optimization
  - Code splitting
  - Lazy loading
  - Memoization
  - Image optimization
- [x] Accessibility improvements
  - ARIA labels
  - Keyboard navigation
  - Screen reader testing
- [x] SEO optimization
  - Meta tags
  - Structured data
  - Sitemap
- [x] Error boundaries
- [x] Loading states
- [x] Empty states
- [x] Animations polish

**Deliverable**: Production-ready application

---

### Phase 9: Testing & QA (Week 6)
**Tasks**:
- [x] Write E2E tests (Playwright)
- [x] Cross-browser testing
- [x] Mobile device testing
- [x] Performance testing (Lighthouse)
- [x] Accessibility testing (axe)
- [x] User acceptance testing
- [x] Bug fixing
- [x] Documentation review

**Deliverable**: Fully tested application

---

### Phase 10: Deployment (Week 6)
**Tasks**:
- [x] Setup Vercel project
- [x] Configure environment variables
- [x] Setup custom domain
- [x] Configure CDN
- [x] Setup analytics
- [x] Setup error monitoring
- [x] Create deployment workflow
- [x] Deploy to production
- [x] Post-deployment testing
- [x] Monitoring setup

**Deliverable**: Live production website

---

## 21. MARKETING & LAUNCH STRATEGY

### 21.1 Pre-Launch (2 weeks before)
- [ ] Create social media accounts (Facebook, Instagram)
- [ ] Prepare launch content (posts, images, videos)
- [ ] Beta testing with small group
- [ ] Collect feedback and testimonials
- [ ] Prepare press release
- [ ] Contact Vietnamese media/blogs

### 21.2 Launch Day
- [ ] Publish on Product Hunt (optional)
- [ ] Post on social media
- [ ] Email announcement (if have list)
- [ ] Submit to Vietnamese web directories
- [ ] Post in relevant Facebook groups
- [ ] Reddit posts (r/vietnam, r/webdev)

### 21.3 Post-Launch (First month)
- [ ] Monitor user feedback
- [ ] Quick bug fixes
- [ ] Content marketing (blog posts about Vietnamese culture)
- [ ] SEO optimization based on search console data
- [ ] Engage with users on social media
- [ ] Collect testimonials
- [ ] Implement high-priority feature requests

### 21.4 Growth Strategy
- **Content Marketing**:
  - Blog về ý nghĩa các ngày lễ
  - Hướng dẫn chọn ngày tốt
  - Văn hóa can chi
  - Phong thủy cơ bản

- **SEO**:
  - Target keywords: "lịch vạn niên", "xem lịch âm", "tra cứu lịch"
  - Long-tail keywords: "ngày tốt cưới hỏi 2024"
  - Local SEO for Vietnam

- **Social Media**:
  - Daily tips về lịch và phong thủy
  - Infographics về can chi, ngũ hành
  - User-generated content
  - Engagement with Vietnamese community

- **Partnerships**:
  - Collaborate with Vietnamese cultural sites
  - Partner with wedding planners
  - Feng Shui consultants
  - Vietnamese bloggers

---

## 22. ANALYTICS & METRICS TO TRACK

### 22.1 User Behavior Metrics
- Page views per session
- Average session duration
- Bounce rate by page
- Most viewed months
- Most searched purposes (lucky day finder)
- Conversion rate (view → save date)
- Return visitor rate

### 22.2 Feature Usage
- Calendar interactions (clicks per session)
- Conversion tool usage frequency
- Lucky day searches per day
- Saved dates average per user
- Modal open rate
- Month navigation frequency

### 22.3 Performance Metrics
- Page load time (by device/connection)
- Time to Interactive
- Largest Contentful Paint
- Cumulative Layout Shift
- JavaScript error rate
- API call latency (if any)

### 22.4 Business Metrics (if applicable)
- Daily/Monthly Active Users (DAU/MAU)
- User retention rate (7-day, 30-day)
- Growth rate month-over-month
- Traffic sources breakdown
- Device type distribution
- Geographic distribution

### 22.5 Content Metrics
- Most popular holidays viewed
- Most searched lucky purposes
- Peak usage times (by hour/day)
- Seasonal trends

---

## 23. USER PERSONAS

### Persona 1: Bà Hoa (Traditional User)
- **Age**: 55-70
- **Tech savvy**: Low-Medium
- **Goal**: Check ngày giờ tốt cho cháu cưới, khai trương
- **Pain points**: Lịch giấy khó đọc, con cháu hỏi ngày tốt
- **Needs**: 
  - Interface đơn giản, chữ to
  - Thông tin chính xác
  - Dễ tra cứu ngày tốt
  - Có thể lưu các ngày quan trọng

### Persona 2: Anh Minh (Modern Professional)
- **Age**: 28-40
- **Tech savvy**: High
- **Goal**: Tra nhanh ngày âm cho dịp lễ, đặt lịch sự kiện
- **Pain points**: Thiếu app mobile tiện lợi, ads nhiều trên các trang khác
- **Needs**:
  - Fast loading, clean UI
  - Mobile-friendly
  - Share functionality
  - Integration với calendar app

### Persona 3: Chị Lan (Business Owner)
- **Age**: 35-50
- **Tech savvy**: Medium-High
- **Goal**: Chọn ngày tốt khai trương, mở chi nhánh, ký hợp đồng
- **Pain points**: Cần tìm nhiều ngày tốt để lựa chọn
- **Needs**:
  - Lucky day finder với filter chi tiết
  - Export/print functionality
  - Detailed explanations
  - Professional presentation

### Persona 4: Em Nam (Student/Young User)
- **Age**: 18-25
- **Tech savvy**: High
- **Goal**: Tìm hiểu văn hóa, tra ngày sinh âm lịch
- **Pain points**: Không hiểu rõ về văn hóa truyền thống
- **Needs**:
  - Modern UI/UX
  - Educational content
  - Social sharing
  - Gamification (optional)

---

## 24. COMPETITIVE ANALYSIS

### 24.1 Competitors
| Website | Strengths | Weaknesses | Our Advantage |
|---------|-----------|------------|---------------|
| lichviet.com | Established, lots of content | Old UI, slow, many ads | Modern UI, fast, clean |
| lich-van-nien.com | Good SEO, popular | Cluttered, outdated design | Better UX, mobile-first |
| xemlicham.com | Simple, fast | Limited features | More features, better design |
| Google Calendar | Familiar, syncing | No lunar info, no lucky days | Specialized for Vietnamese |

### 24.2 Market Gap
- **Modern, fast Vietnamese calendar app**
- **Mobile-first design**
- **Clean UI without intrusive ads**
- **Accurate calculations with transparency**
- **Progressive Web App capability**
- **Cultural education component**

### 24.3 Unique Value Propositions
1. **Most accurate** lunar calculations (documented algorithm)
2. **Fastest** loading time among competitors
3. **Best mobile experience** (PWA, responsive)
4. **Clean & modern** interface
5. **Completely free** with minimal ads
6. **Open source** (optional - builds trust)
7. **Educational** content about Vietnamese culture

---

## 25. MONETIZATION STRATEGY (OPTIONAL)

### 25.1 Phase 1: Free with Ads (Month 1-6)
- Google AdSense (non-intrusive)
- Native ads in feed
- Revenue: $50-200/month (estimated)

### 25.2 Phase 2: Freemium Model (Month 7+)
**Free Features**:
- Basic calendar view
- Conversion tool
- Limited lucky day searches (5/day)
- View saved dates (max 10)

**Premium Features** ($2.99/month or $19.99/year):
- Unlimited lucky day searches
- Unlimited saved dates
- Ad-free experience
- Export to PDF
- Priority support
- Advanced features (horoscope, compatibility)
- Custom notifications

### 25.3 Phase 3: B2B Services (Year 2)
- **Widget** for other websites ($9.99/month)
- **API access** for developers ($29/month)
- **White-label** solution for businesses
- **Custom integrations**

### 25.4 Alternative Revenue Streams
- Affiliate marketing (Feng Shui products)
- Sponsored content (cultural articles)
- Consulting services (choosing lucky dates)
- Mobile app (paid version)

**Note**: Keep free version feature-rich to build user base first

---

## 26. LEGAL & COMPLIANCE

### 26.1 Terms of Service
- Define usage rights
- Disclaimer about accuracy
- Limitation of liability
- Intellectual property rights
- User conduct rules

### 26.2 Privacy Policy
- Data collection (analytics only)
- Cookie usage
- LocalStorage data handling
- No personal information collected
- No data sharing with third parties
- GDPR compliance (if applicable)

### 26.3 Copyright & Licensing
- Original code: MIT License (if open source)
- Cultural information: Public domain or cited sources
- Icons/Images: Licensed properly
- Fonts: Open source or licensed

### 26.4 Disclaimer
```
MIỄN TRỪ TRÁCH NHIỆM

Thông tin trên website này được cung cấp với mục đích tham khảo về văn hóa 
truyền thống Việt Nam. Chúng tôi không đảm bảo tính chính xác tuyệt đối 
và không chịu trách nhiệm về bất kỳ quyết định nào được đưa ra dựa trên 
thông tin này.

Người dùng tự chịu trách nhiệm về các quyết định cá nhân liên quan đến 
ngày giờ, phong thủy, và các hoạt động khác dựa trên thông tin từ website.

Để có thông tin chính xác và tư vấn chuyên nghiệp, vui lòng tham khảo ý 
kiến của các chuyên gia về phong thủy, lịch pháp, hoặc các nhà tư vấn 
văn hóa truyền thống.
```

---

## 27. TECHNICAL CHALLENGES & SOLUTIONS

### Challenge 1: Lunar Calculation Accuracy
**Problem**: Âm lịch Việt Nam có nhiều biến thể, khó xác định thuật toán chính xác
**Solution**: 
- Research từ Institute of Astronomy Vietnam
- Cross-reference nhiều sources
- Test với 100+ known dates
- Document algorithm clearly
- Allow user feedback for corrections

### Challenge 2: Performance with Large Date Ranges
**Problem**: Tìm ngày tốt trong 1 năm = 365 calculations
**Solution**:
- Web Workers cho heavy calculations
- Memoization cho results
- Limit date range to 3 months default
- Progressive loading of results
- Cancel ongoing searches when user changes params

### Challenge 3: LocalStorage Quota
**Problem**: Saved dates có thể vượt quá 5-10MB limit
**Solution**:
- Compress data với LZ-string
- Limit saved dates to 100
- Warn user when approaching limit
- Provide export functionality
- Clear old/unused dates automatically

### Challenge 4: Cross-browser Date Handling
**Problem**: JavaScript Date có bugs với timezone, format
**Solution**:
- Use date-fns library consistently
- Always work in UTC internally
- Convert to local timezone only for display
- Thorough testing on all browsers

### Challenge 5: Mobile Keyboard on Date Input
**Problem**: Mobile keyboard covers input fields
**Solution**:
- Use native date picker on mobile
- Implement proper scroll-into-view
- Bottom sheet UI pattern for mobile
- Test on various devices

### Challenge 6: SEO for SPA
**Problem**: React SPA có thể có SEO issues
**Solution**:
- Server-side rendering với Vite SSR (optional)
- Pre-rendering với react-snap
- Proper meta tags
- Structured data
- Sitemap generation

---

## 28. ACCESSIBILITY CHECKLIST

### Keyboard Navigation
- [ ] Tab order logical and complete
- [ ] All interactive elements focusable
- [ ] Focus indicators visible (2px outline)
- [ ] Escape closes modals
- [ ] Arrow keys navigate calendar
- [ ] Enter/Space selects date
- [ ] Skip to main content link

### Screen Reader Support
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Error messages announced
- [ ] Calendar structure announced
- [ ] Date selection announced
- [ ] Loading states announced
- [ ] Success messages announced

### Visual Accessibility
- [ ] Color contrast >= 4.5:1 for text
- [ ] Color contrast >= 3:1 for UI elements
- [ ] Information not conveyed by color alone
- [ ] Text resizable to 200% without breaking
- [ ] No flashing content > 3 times/second
- [ ] Sufficient spacing between clickable elements (44x44px)

### Content Accessibility
- [ ] Headings hierarchical (H1 → H2 → H3)
- [ ] Semantic HTML elements used
- [ ] Language attribute set (lang="vi")
- [ ] Page title descriptive
- [ ] Link text descriptive
- [ ] Tables have proper headers (if used)

### Forms
- [ ] Labels associated with inputs
- [ ] Required fields indicated
- [ ] Error messages helpful and specific
- [ ] Success feedback provided
- [ ] Autocomplete attributes used
- [ ] Validation messages clear

### ARIA
- [ ] ARIA labels on icon buttons
- [ ] aria-current on today's date
- [ ] aria-selected on selected date
- [ ] role="dialog" on modals
- [ ] aria-live for dynamic updates
- [ ] aria-expanded for dropdowns

---

## 29. PERFORMANCE OPTIMIZATION CHECKLIST

### Loading Performance
- [ ] Code splitting by route
- [ ] Lazy load components below fold
- [ ] Lazy load images
- [ ] Preload critical resources
- [ ] Minify CSS and JS
- [ ] Compress images (WebP format)
- [ ] Use CDN for static assets
- [ ] Implement service worker (PWA)
- [ ] Tree shaking enabled

### Runtime Performance
- [ ] Memoize expensive calculations
- [ ] Use React.memo for components
- [ ] Optimize re-renders
- [ ] Debounce/throttle handlers
- [ ] Virtual scrolling for long lists
- [ ] Web Workers for calculations
- [ ] Avoid inline functions in render
- [ ] Use production build

### Bundle Size
- [ ] Analyze bundle with webpack-bundle-analyzer
- [ ] Remove unused dependencies
- [ ] Use lighter alternatives
- [ ] Import only needed functions
- [ ] Avoid large moment.js (use date-fns)
- [ ] Target < 500KB total

### Caching Strategy
- [ ] Cache calculation results
- [ ] Service worker caching
- [ ] LocalStorage for preferences
- [ ] Browser HTTP caching headers
- [ ] Cache-busting for updates

---

## 30. FINAL CHECKLIST BEFORE LAUNCH

### Functionality
- [ ] All features working as specified
- [ ] No console errors or warnings
- [ ] Forms validate correctly
- [ ] Error handling works
- [ ] Loading states display properly
- [ ] Data persists in localStorage
- [ ] Export/Import works

### Content
- [ ] All text in Vietnamese (no Lorem Ipsum)
- [ ] Spelling and grammar checked
- [ ] Cultural information accurate
- [ ] Disclaimer text present
- [ ] Contact information available
- [ ] About page complete

### Design
- [ ] Responsive on all breakpoints
- [ ] Consistent spacing and alignment
- [ ] Colors match design system
- [ ] Typography consistent
- [ ] Icons consistent style
- [ ] Animations smooth
- [ ] No visual bugs

### Technical
- [ ] SEO meta tags complete
- [ ] Favicon present
- [ ] Sitemap generated
- [ ] Robots.txt configured
- [ ] 404 page styled
- [ ] HTTPS enabled
- [ ] Analytics tracking working
- [ ] Error monitoring active

### Testing
- [ ] Cross-browser tested
- [ ] Mobile device tested
- [ ] Accessibility tested (axe)
- [ ] Performance tested (Lighthouse)
- [ ] User testing completed
- [ ] Bug fixes verified

### Legal
- [ ] Terms of Service page
- [ ] Privacy Policy page
- [ ] Disclaimer visible
- [ ] Copyright notice
- [ ] License information (if open source)

### Documentation
- [ ] README.md complete
- [ ] ALGORITHMS.md written
- [ ] Code commented
- [ ] Deployment guide written
- [ ] User guide available (optional)

---

## REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Current Date] | AI Assistant | Initial comprehensive specification for Lịch Vạn Niên Việt Nam project |
