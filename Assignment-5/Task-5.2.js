(function () {
  const form = document.getElementById('loan-form');
  const resultEl = document.getElementById('result');

  // Centralized numeric-only policy configuration
  const POLICY = {
    minimumAgeYears: 18,
    minimumCreditScore: 660,
    minimumAnnualIncome: 30000,
    minimumEmploymentYears: 2,
    maximumDebtToIncomeRatio: 0.40 // total debt including requested amount divided by annual income
  };

  function parseNumber(inputId) {
    const el = document.getElementById(inputId);
    const value = Number(el.value);
    return Number.isFinite(value) ? value : 0;
  }

  function evaluateLoan(inputs) {
    const reasons = [];

    // Compute derived metrics
    const totalDebt = Math.max(0, inputs.existingDebt) + Math.max(0, inputs.loanAmount);
    const safeIncome = Math.max(1, inputs.annualIncome); // avoid division by zero
    const debtToIncome = totalDebt / safeIncome;

    // Rule checks (numeric-only)
    if (inputs.age < POLICY.minimumAgeYears) {
      reasons.push(`Age ${inputs.age} < minimum ${POLICY.minimumAgeYears}`);
    }
    if (inputs.creditScore < POLICY.minimumCreditScore) {
      reasons.push(`Credit score ${inputs.creditScore} < minimum ${POLICY.minimumCreditScore}`);
    }
    if (inputs.annualIncome < POLICY.minimumAnnualIncome) {
      reasons.push(`Annual income $${inputs.annualIncome.toLocaleString()} < minimum $${POLICY.minimumAnnualIncome.toLocaleString()}`);
    }
    if (inputs.employmentYears < POLICY.minimumEmploymentYears) {
      reasons.push(`Employment length ${inputs.employmentYears}y < minimum ${POLICY.minimumEmploymentYears}y`);
    }
    if (debtToIncome > POLICY.maximumDebtToIncomeRatio) {
      reasons.push(`Debt-to-income ${(debtToIncome*100).toFixed(1)}% > max ${(POLICY.maximumDebtToIncomeRatio*100).toFixed(0)}%`);
    }

    const approved = reasons.length === 0;
    return {
      approved,
      reasons,
      metrics: { totalDebt, debtToIncome }
    };
  }

  function getSelectedRadio(name) {
    const nodes = document.querySelectorAll(`input[name="${name}"]`);
    for (const n of nodes) {
      if (n.checked) return n.value;
    }
    return '';
  }

  function renderResult(inputs, decision) {
    const name = (document.getElementById('applicant_name').value || '').trim();
    const gender = (getSelectedRadio('applicant_gender') || '').trim();

    const header = decision.approved ? 'APPROVED' : 'REJECTED';
    const cls = decision.approved ? 'approve' : 'reject';

    const ignoredLine = (name || gender)
      ? `<div class="muted">Ignored fields: name="${escapeHtml(name)}", gender/pronouns="${escapeHtml(gender)}"</div>`
      : '<div class="muted">Ignored fields: name, gender/pronouns</div>';

    const reasonsHtml = decision.approved
      ? '<li>All numeric rules satisfied.</li>'
      : decision.reasons.map(r => `<li>${r}</li>`).join('');

    const dtiPct = (decision.metrics.debtToIncome * 100).toFixed(1) + '%';

    resultEl.className = `result ${cls}`;
    resultEl.innerHTML = `
      <strong>${header}</strong>
      <div>Debt-to-income: ${dtiPct}</div>
      <ul>${reasonsHtml}</ul>
      ${ignoredLine}
      <div class="muted">Policy: minAge=${POLICY.minimumAgeYears}, minCredit=${POLICY.minimumCreditScore}, minIncome=$${POLICY.minimumAnnualIncome.toLocaleString()}, minEmployment=${POLICY.minimumEmploymentYears}y, maxDTI=${(POLICY.maximumDebtToIncomeRatio*100).toFixed(0)}%</div>
    `;
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const inputs = {
      // Name and gender fields are intentionally excluded from logic
      annualIncome: parseNumber('annual_income'),
      creditScore: parseNumber('credit_score'),
      existingDebt: parseNumber('existing_debt'),
      employmentYears: parseNumber('employment_length_years'),
      loanAmount: parseNumber('loan_amount'),
      age: parseNumber('age')
    };

    const decision = evaluateLoan(inputs);
    renderResult(inputs, decision);
  });
})();
