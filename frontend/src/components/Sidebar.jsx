import logoSrc from '../assets/logo.svg'

const navItems = [
  { id: 'home', label: 'Home', icon: '🏠' },
  { id: 'about', label: 'About', icon: 'ℹ️' },
  { id: 'how-it-works', label: 'How It Works', icon: '🔍' },
]

export default function Sidebar({ active, setActive, mobileOpen, onClose }) {
  return (
    <>
      {mobileOpen && <div className="sidebar-overlay" onClick={onClose} />}

      <aside
        className={`
          sidebar
          fixed md:static inset-y-0 left-0 z-50
          bg-[#0a0e2a]/90 backdrop-blur-2xl border-r border-white/10
          transform transition-transform duration-300 ease-in-out
          ${mobileOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
          flex flex-col
        `}
      >
        <div className="p-5 border-b border-white/10">
          <div className="flex items-center gap-3">
            <img src={logoSrc} alt="Fake News Detection" className="w-9 h-9 shrink-0" />
            <div>
              <h2 className="text-white font-semibold text-xs leading-tight">Fake News</h2>
              <p className="text-white/40 text-[10px]">Detection System</p>
            </div>
          </div>
        </div>

        <nav className="flex-1 p-3 space-y-0.5">
          {navItems.map((item) => (
            <button
              key={item.id}
              onClick={() => { setActive(item.id); onClose?.() }}
              className={`
                w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm
                transition-all duration-200
                ${active === item.id
                  ? 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
                  : 'text-white/50 hover:text-white/80 hover:bg-white/5 border border-transparent'
                }
              `}
            >
              <span className="text-base">{item.icon}</span>
              <span className="font-medium">{item.label}</span>
            </button>
          ))}
        </nav>

        <div className="p-3 border-t border-white/10">
          <div className="glass-sm p-3">
            <p className="text-white/40 text-[10px] leading-relaxed">
              AI-powered misinformation detection using machine learning.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}
