import logoSrc from '../assets/logo.svg'

const navItems = [
  { id: 'home', label: 'Home', icon: '🏠' },
  { id: 'about', label: 'About', icon: 'ℹ️' },
  { id: 'how-it-works', label: 'How It Works', icon: '🔍' },
]

export default function Sidebar({ active, setActive, mobileOpen, onClose }) {
  return (
    <>
      {mobileOpen && (
        <div className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm md:hidden" onClick={onClose} />
      )}

      <aside
        className={`
          w-[240px] h-screen fixed top-0 left-0 z-50
          sidebar-glass rounded-r-2xl
          flex flex-col
          transition-transform duration-300
          ${mobileOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
        `}
      >
        <div className="p-5 border-b border-blue-500/10">
          <div className="flex items-center gap-2.5">
            <img src={logoSrc} alt="Fake News Detection" className="w-8 h-8 shrink-0" />
            <div>
              <h2 className="text-white font-semibold text-xs leading-tight">Fake News</h2>
              <p className="text-blue-400/50 text-[10px]">Detection System</p>
            </div>
          </div>
        </div>

        <nav className="flex-1 p-3 space-y-1">
          {navItems.map((item) => (
            <button
              key={item.id}
              onClick={() => { setActive(item.id); onClose?.() }}
              className={`w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all duration-300 cursor-pointer ${
                active === item.id
                  ? 'bg-gradient-to-r from-blue-600/30 to-blue-500/10 text-blue-400 border border-blue-500/20 shadow-sm shadow-blue-500/10'
                  : 'text-gray-400 hover:text-white/80 hover:bg-white/5 border border-transparent'
              }`}
            >
              <span className="text-base shrink-0">{item.icon}</span>
              <span>{item.label}</span>
            </button>
          ))}
        </nav>

        <div className="p-3 border-t border-blue-500/10">
          <div className="bg-white/[0.03] rounded-xl p-3 border border-blue-500/10">
            <p className="text-blue-400/40 text-[10px] leading-relaxed">
              AI-powered misinformation detection using machine learning.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}
