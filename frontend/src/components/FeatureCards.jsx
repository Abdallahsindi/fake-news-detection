const features = [
  {
    icon: '🧠',
    title: 'AI-Powered Analysis',
    desc: 'Advanced machine learning model trained to detect linguistic patterns associated with misinformation.',
  },
  {
    icon: '✅',
    title: 'Fact Verification',
    desc: 'Analyzes writing style, source attribution, and emotional tone to assess credibility.',
  },
  {
    icon: '📄',
    title: 'Detailed Reports',
    desc: 'Comprehensive breakdown of prediction confidence and detected linguistic indicators.',
  },
]

export default function FeatureCards() {
  return (
    <div className="features-grid fade-in-up">
      {features.map((f, i) => (
        <div key={i} className="glass-card p-6 group flex flex-col" style={{ animationDelay: `${i * 0.1}s` }}>
          <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500/10 to-blue-600/10 border border-blue-500/10 flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform duration-300 shrink-0">
            {f.icon}
          </div>
          <h3 className="text-white font-semibold text-sm mb-2">{f.title}</h3>
          <p className="text-white/40 text-xs leading-relaxed flex-1">{f.desc}</p>
        </div>
      ))}
    </div>
  )
}
