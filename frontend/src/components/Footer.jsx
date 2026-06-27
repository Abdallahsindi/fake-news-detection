import logoSrc from '../assets/logo-footer.svg'

export default function Footer() {
  return (
    <footer className="border-t border-white/5 mt-16 py-8">
      <div className="max-w-5xl mx-auto px-6">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <img src={logoSrc} alt="" className="w-6 h-6 opacity-40" />
            <p className="text-white/20 text-xs">
              Fake News Detection System &copy; 2026
            </p>
          </div>
          <p className="text-white/20 text-xs">
            Powered by Random Forest &middot; TF-IDF Vectorization
          </p>
        </div>
      </div>
    </footer>
  )
}
