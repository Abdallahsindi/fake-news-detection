const features = [
  { icon: '🧠', title: 'AI-Powered Analysis', desc: 'Advanced machine learning model trained to detect linguistic patterns associated with misinformation.' },
  { icon: '✅', title: 'Fact Verification', desc: 'Analyzes writing style, source attribution, and emotional tone to assess credibility.' },
  { icon: '📄', title: 'Detailed Reports', desc: 'Comprehensive breakdown of prediction confidence and detected linguistic indicators.' },
]

export default function FeaturesSection() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-10 fade-in-up">
      {features.map((f, i) => (
        <div
          key={i}
          className="glass-card rounded-3xl p-10 min-h-[280px] flex flex-col group transition-all duration-300
                     hover:-translate-y-3 hover:shadow-[0_20px_50px_rgba(59,130,246,0.2)]"
        >
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500/15 to-blue-600/10 border border-blue-500/15 flex items-center justify-center text-3xl group-hover:scale-110 transition-transform duration-300">
              {f.icon}
            </div>
          </div>
          <h3 className="text-white text-xl font-bold mb-3 text-center">{f.title}</h3>
          <p className="text-white/70 text-base leading-7 text-center flex-1">{f.desc}</p>
        </div>
      ))}
    </div>
  )
}
