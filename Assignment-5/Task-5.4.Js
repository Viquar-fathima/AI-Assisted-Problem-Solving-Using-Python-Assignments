(function () {
  const form = document.getElementById('applicant-form');
  const resultEl = document.getElementById('result');

  // Scoring configuration (matches Python version)
  const CONFIG = {
    weights: {
      education: 20,
      experience: 25,
      skills: 20,
      interview_score: 20,
      portfolio: 10,
      certifications: 5
    },
    educationScores: {
      'high_school': 40,
      'associates': 60,
      'bachelors': 80,
      'masters': 90,
      'phd': 100
    },
    experienceMaxYears: 10,
    experiencePointsPerYear: 10,
    skillsMaxCount: 8,
    skillsPointsPerSkill: 12.5,
    certMaxCount: 5,
    certPointsPerCert: 20
  };

  function parseNumber(inputId) {
    const el = document.getElementById(inputId);
    const value = Number(el.value);
    return Number.isFinite(value) ? value : 0;
  }

  function getSelectValue(selectId) {
    const el = document.getElementById(selectId);
    return el ? el.value : '';
  }

  function scoreEducation(educationLevel) {
    if (!educationLevel) return 0;
    return CONFIG.educationScores[educationLevel] || 0;
  }

  function scoreExperience(years) {
    if (years < 0) return 0;
    if (years >= CONFIG.experienceMaxYears) return 100;
    return Math.min(100, years * CONFIG.experiencePointsPerYear);
  }

  function scoreSkills(skillCount) {
    if (skillCount < 0) return 0;
    if (skillCount >= CONFIG.skillsMaxCount) return 100;
    return Math.min(100, skillCount * CONFIG.skillsPointsPerSkill);
  }

  function scoreInterview(interviewScore) {
    return Math.max(0, Math.min(100, interviewScore));
  }

  function scorePortfolio(portfolioScore) {
    return Math.max(0, Math.min(100, portfolioScore));
  }

  function scoreCertifications(certCount) {
    if (certCount < 0) return 0;
    if (certCount >= CONFIG.certMaxCount) return 100;
    return Math.min(100, certCount * CONFIG.certPointsPerCert);
  }

  function calculateScore(inputs) {
    // Calculate individual feature scores
    const educationScore = scoreEducation(inputs.education);
    const experienceScore = scoreExperience(inputs.experienceYears);
    const skillsScore = scoreSkills(inputs.skillsCount);
    const interviewScore = scoreInterview(inputs.interviewScore);
    const portfolioScore = scorePortfolio(inputs.portfolioScore);
    const certScore = scoreCertifications(inputs.certificationsCount);

    // Calculate weighted total score
    const totalScore = (
      (educationScore * CONFIG.weights.education) +
      (experienceScore * CONFIG.weights.experience) +
      (skillsScore * CONFIG.weights.skills) +
      (interviewScore * CONFIG.weights.interview_score) +
      (portfolioScore * CONFIG.weights.portfolio) +
      (certScore * CONFIG.weights.certifications)
    ) / 100;

    // Determine recommendation
    let recommendation, recommendationClass;
    if (totalScore >= 80) {
      recommendation = 'Highly Recommended';
      recommendationClass = 'highly-recommended';
    } else if (totalScore >= 65) {
      recommendation = 'Recommended';
      recommendationClass = 'recommended';
    } else if (totalScore >= 50) {
      recommendation = 'Consider';
      recommendationClass = 'consider';
    } else {
      recommendation = 'Not Recommended';
      recommendationClass = 'not-recommended';
    }

    return {
      totalScore: totalScore,
      recommendation: recommendation,
      recommendationClass: recommendationClass,
      breakdown: {
        education: {
          score: educationScore,
          weighted: (educationScore * CONFIG.weights.education) / 100
        },
        experience: {
          score: experienceScore,
          weighted: (experienceScore * CONFIG.weights.experience) / 100
        },
        skills: {
          score: skillsScore,
          weighted: (skillsScore * CONFIG.weights.skills) / 100
        },
        interview: {
          score: interviewScore,
          weighted: (interviewScore * CONFIG.weights.interview_score) / 100
        },
        portfolio: {
          score: portfolioScore,
          weighted: (portfolioScore * CONFIG.weights.portfolio) / 100
        },
        certifications: {
          score: certScore,
          weighted: (certScore * CONFIG.weights.certifications) / 100
        }
      }
    };
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  function renderResult(inputs, result) {
    const name = (document.getElementById('applicant_name').value || '').trim();
    const nameDisplay = name ? escapeHtml(name) : 'Applicant';

    // Build breakdown HTML
    const breakdownItems = Object.entries(result.breakdown).map(([category, scores]) => {
      const categoryLabel = category.charAt(0).toUpperCase() + category.slice(1);
      return `
        <div class="breakdown-item">
          <span class="breakdown-label">${categoryLabel}:</span>
          <span class="breakdown-score">${scores.score.toFixed(2)}/100 (Weighted: ${scores.weighted.toFixed(2)})</span>
        </div>
      `;
    }).join('');

    // Build weights info
    const weightsInfo = Object.entries(CONFIG.weights).map(([category, weight]) => {
      const categoryLabel = category.charAt(0).toUpperCase() + category.slice(1).replace('_', ' ');
      return `${categoryLabel}: ${weight}%`;
    }).join(', ');

    resultEl.className = `result ${result.recommendationClass}`;
    resultEl.innerHTML = `
      <div><strong>Applicant:</strong> ${nameDisplay}</div>
      <div class="total-score">Total Score: ${result.totalScore.toFixed(2)}/100</div>
      <div class="recommendation"><strong>Recommendation:</strong> ${result.recommendation}</div>
      
      <div class="breakdown">
        <strong>Score Breakdown:</strong>
        ${breakdownItems}
      </div>
      
      <div class="weights-info">
        <strong>Scoring Weights:</strong> ${weightsInfo}
      </div>
      
      <div class="muted" style="margin-top: 12px;">
        Note: Name is displayed for reference only and is not used in scoring calculations.
      </div>
    `;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const inputs = {
      // Name is intentionally excluded from scoring logic
      education: getSelectValue('education'),
      experienceYears: parseNumber('experience_years'),
      skillsCount: parseNumber('skills_count'),
      interviewScore: parseNumber('interview_score'),
      portfolioScore: parseNumber('portfolio_score'),
      certificationsCount: parseNumber('certifications_count')
    };

    const result = calculateScore(inputs);
    renderResult(inputs, result);
  });
})();
