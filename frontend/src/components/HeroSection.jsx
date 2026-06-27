import logoSrc from '../assets/logo.svg'

export default function HeroSection() {
  return (
    <div className="hero fade-in-up">
      <div className="flex justify-center mb-6">
        <img
          src={logoSrc}
          alt="Fake News Detection System"
          className="w-20 h-20 md:w-24 md:h-24 drop-shadow-lg fade-in"
          style={{ animationDelay: '0.1s' }}
        />
      </div>

      <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-medium tracking-wide uppercase">
        <span className="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse" />
        AI Powered
      </div>

      <h1 className="text-3xl md:text-4xl lg:text-5xl font-extrabold leading-snug mt-5">
        <span className="gradient-text">Fake News</span>
        <br />
        <span className="text-white">Detection System</span>
      </h1>

      <p className="text-white/50 text-sm md:text-base max-w-xl mx-auto leading-relaxed mt-4">
        AI-powered platform for detecting misinformation and verifying news authenticity.
        Enter a news article below to analyze its credibility.
      </p>
    </div>
  )
}
