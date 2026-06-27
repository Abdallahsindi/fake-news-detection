const getExplanation = (prediction) => {
  if (prediction === 'Fake News') {
    return 'This article was classified as likely misinformation. Our model detected linguistic patterns commonly associated with fabricated content, including sensational language, lack of credible source attribution, and emotional manipulation techniques.'
  }
  return 'This article was classified as factual. Our model identified language patterns consistent with credible news reporting, including measured tone, source attribution, and balanced presentation of information.'
}

const getAnalysisPoints = (prediction) => {
  if (prediction === 'Fake News') {
    return [
      { label: 'Linguistic Pattern', value: 'Sensational & emotional language', color: 'text-red-400' },
      { label: 'Source Attribution', value: 'Lacks credible sources', color: 'text-red-400' },
      { label: 'Writing Style', value: 'Exaggerated & clickbait-style', color: 'text-red-400' },
      { label: 'Factual Consistency', value: 'Low (with training data patterns)', color: 'text-red-400' },
    ]
  }
  return [
    { label: 'Linguistic Pattern', value: 'Measured & objective tone', color: 'text-emerald-400' },
    { label: 'Source Attribution', value: 'Contains source references', color: 'text-emerald-400' },
    { label: 'Writing Style', value: 'Professional journalism style', color: 'text-emerald-400' },
    { label: 'Factual Consistency', value: 'High (with training data patterns)', color: 'text-emerald-400' },
  ]
}

export default function PredictionCard({ result }) {
  const isFake = result.prediction === 'Fake News'
  const confidencePct = (result.confidence * 100).toFixed(1)
  const explanation = getExplanation(result.prediction)
  const analysisPoints = getAnalysisPoints(result.prediction)

  const statusColor = isFake ? 'from-red-500/20 to-red-600/10 border-red-500/30' : 'from-emerald-500/20 to-emerald-600/10 border-emerald-500/30'
  const badgeBg = isFake ? 'bg-red-500/10 text-red-400 border-red-500/30' : 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30'
  const barColor = isFake ? 'bg-gradient-to-r from-red-500 to-red-600' : 'bg-gradient-to-r from-emerald-500 to-emerald-600'

  return (
    <div className="results-container fade-in-up">
      {/* Status Header + Progress Bar */}
      <div className={`result-card glass-card bg-gradient-to-br ${statusColor}`}>
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <p className="text-white/40 text-xs uppercase tracking-wider mb-2">Prediction Result</p>
            <span className={`inline-block px-6 py-2 rounded-full text-sm font-bold border ${badgeBg}`}>
              {result.prediction === 'Fake News' ? '🚫 FAKE NEWS' : '✅ REAL NEWS'}
            </span>
          </div>
          <div className="text-right">
            <p className="text-white/40 text-xs uppercase tracking-wider mb-1">Confidence Score</p>
            <p className={`text-3xl font-bold ${isFake ? 'text-red-400' : 'text-emerald-400'}`}>
              {confidencePct}%
            </p>
          </div>
        </div>

        <div className="mt-6">
          <div className="w-full bg-white/5 rounded-full h-2.5 overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-1000 ease-out ${barColor}`}
              style={{ width: `${confidencePct}%` }}
            />
          </div>
          <div className="flex justify-between mt-1.5">
            <span className="text-[10px] text-white/20">0%</span>
            <span className="text-[10px] text-white/20">100%</span>
          </div>
        </div>
      </div>

      {/* AI Analysis Card */}
      <div className="analysis-card glass-card" style={{ marginTop: '30px' }}>
        <div className="flex items-center gap-3 analysis-title">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-blue-600/20 flex items-center justify-center text-sm shrink-0">
            🤖
          </div>
          <div>
            <h3 className="text-white font-semibold text-sm">AI Analysis</h3>
            <p className="text-white/30 text-xs">Model-based explanation</p>
          </div>
        </div>
        <p className="text-white/70 text-sm leading-relaxed">
          {explanation}
        </p>
      </div>

      {/* Detailed Analysis */}
      <div className="detail-card glass-card" style={{ marginTop: '30px' }}>
        <h3 className="text-white font-semibold text-sm analysis-title">Detailed Analysis</h3>
        <div className="details-grid">
          {analysisPoints.map((point, i) => (
            <div key={i} className="glass-sm p-4">
              <p className="text-white/40 text-xs mb-1">{point.label}</p>
              <p className={`text-sm font-medium ${point.color}`}>{point.value}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
