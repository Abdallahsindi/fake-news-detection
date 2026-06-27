import logoSrc from '../assets/logo.svg'

export default function HeroSection() {
  return (
    <div className="flex flex-col items-center text-center pt-20 pb-12 fade-in-up">
      <img src={logoSrc} alt="Fake News Detection" className="w-28 h-28 drop-shadow-2xl" />

      <div className="mt-4 inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-[10px] font-semibold uppercase tracking-widest">
        <span className="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse" />
        AI Powered
      </div>

      <h1 className="mt-8">
        <span className="gradient-text text-7xl font-extrabold leading-none block">Fake News</span>
        <span className="text-white text-5xl font-extrabold leading-none block mt-2">Detection System</span>
      </h1>

      <div className="max-w-3xl mx-auto mt-8">
        <p className="text-gray-400 text-base sm:text-lg leading-relaxed">
          AI-powered platform for detecting misinformation and verifying news authenticity.
          Enter a news article below to analyze its credibility.
        </p>
      </div>
    </div>
  )
}
