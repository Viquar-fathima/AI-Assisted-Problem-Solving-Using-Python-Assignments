from typing import Dict, List, Final


class JobApplicantScorer:
    """
    Scoring system for job applicants based on objective features.
    Focuses on job-relevant qualifications only.
    """
    
    def __init__(self):
        # Scoring weights for different features (total should add up to 100)
        self.weights: Dict[str, int] = {
            'education': 20,
            'experience': 25,
            'skills': 20,
            'interview_score': 20,
            'portfolio': 10,
            'certifications': 5
        }
        
        # Education level scoring (0-100)
        self.education_scores: Dict[str, int] = {
            'high_school': 40,
            'associates': 60,
            'bachelors': 80,
            'masters': 90,
            'phd': 100
        }
        
        # Experience scoring (years of relevant experience)
        self.experience_max_score: int = 10  # Max years for full points
        self.experience_points_per_year: int = 10  # Points per year
        
        # Skills scoring (number of relevant skills)
        self.skills_max_score: int = 8  # Max skills for full points
        self.skills_points_per_skill: int = 12.5  # Points per skill
        
        # Interview score (0-100, directly used)
        # Portfolio score (0-100, based on quality/quantity of projects)
        # Certifications (number of relevant certifications)
        self.cert_max_score: int = 5  # Max certs for full points
        self.cert_points_per_cert: int = 20  # Points per certification
    
    def score_education(self, education_level: str) -> int:
        """Score education level (0-100)."""
        education_level = education_level.lower().replace(' ', '_')
        return self.education_scores.get(education_level, 0)
    
    def score_experience(self, years: float) -> float:
        """Score years of experience (0-100)."""
        if years < 0:
            return 0
        if years >= self.experience_max_score:
            return 100
        return min(100, years * self.experience_points_per_year)
    
    def score_skills(self, skill_count: int) -> float:
        """Score number of relevant skills (0-100)."""
        if skill_count < 0:
            return 0
        if skill_count >= self.skills_max_score:
            return 100
        return min(100, skill_count * self.skills_points_per_skill)
    
    def score_interview(self, interview_score: float) -> float:
        """Score interview performance (0-100)."""
        return max(0, min(100, interview_score))
    
    def score_portfolio(self, portfolio_score: float) -> float:
        """Score portfolio/projects (0-100)."""
        return max(0, min(100, portfolio_score))
    
    def score_certifications(self, cert_count: int) -> float:
        """Score number of certifications (0-100)."""
        if cert_count < 0:
            return 0
        if cert_count >= self.cert_max_score:
            return 100
        return min(100, cert_count * self.cert_points_per_cert)
    
    def calculate_total_score(self, applicant_data: Dict) -> Dict:
        """
        Calculate total score for an applicant.
        
        Expected applicant_data format:
        {
            'name': str (ignored in scoring),
            'education': str (high_school, associates, bachelors, masters, phd),
            'experience_years': float,
            'skills_count': int,
            'interview_score': float (0-100),
            'portfolio_score': float (0-100),
            'certifications_count': int
        }
        """
        # Calculate individual feature scores
        education_score = self.score_education(applicant_data.get('education', ''))
        experience_score = self.score_experience(applicant_data.get('experience_years', 0))
        skills_score = self.score_skills(applicant_data.get('skills_count', 0))
        interview_score = self.score_interview(applicant_data.get('interview_score', 0))
        portfolio_score = self.score_portfolio(applicant_data.get('portfolio_score', 0))
        cert_score = self.score_certifications(applicant_data.get('certifications_count', 0))
        
        # Calculate weighted total score
        total_score = (
            (education_score * self.weights['education']) +
            (experience_score * self.weights['experience']) +
            (skills_score * self.weights['skills']) +
            (interview_score * self.weights['interview_score']) +
            (portfolio_score * self.weights['portfolio']) +
            (cert_score * self.weights['certifications'])
        ) / 100
        
        # Determine recommendation
        if total_score >= 80:
            recommendation = "Highly Recommended"
        elif total_score >= 65:
            recommendation = "Recommended"
        elif total_score >= 50:
            recommendation = "Consider"
        else:
            recommendation = "Not Recommended"
        
        return {
            'total_score': round(total_score, 2),
            'recommendation': recommendation,
            'breakdown': {
                'education': {
                    'score': education_score,
                    'weighted': round(education_score * self.weights['education'] / 100, 2)
                },
                'experience': {
                    'score': experience_score,
                    'weighted': round(experience_score * self.weights['experience'] / 100, 2)
                },
                'skills': {
                    'score': skills_score,
                    'weighted': round(skills_score * self.weights['skills'] / 100, 2)
                },
                'interview': {
                    'score': interview_score,
                    'weighted': round(interview_score * self.weights['interview_score'] / 100, 2)
                },
                'portfolio': {
                    'score': portfolio_score,
                    'weighted': round(portfolio_score * self.weights['portfolio'] / 100, 2)
                },
                'certifications': {
                    'score': cert_score,
                    'weighted': round(cert_score * self.weights['certifications'] / 100, 2)
                }
            }
        }


def get_applicant_input() -> Dict:
    """Get applicant data from user input."""
    print("\n=== Job Applicant Scoring System ===\n")
    print("Note: Name and personal information are ignored in scoring.")
    print("Only job-relevant features are evaluated.\n")
    
    applicant_data = {}
    
    # Name (for display only, not used in scoring)
    applicant_data['name'] = input("Applicant name (for reference only): ").strip()
    
    # Education
    print("\nEducation levels: high_school, associates, bachelors, masters, phd")
    applicant_data['education'] = input("Education level: ").strip()
    
    # Experience
    try:
        applicant_data['experience_years'] = float(input("Years of relevant experience: "))
    except ValueError:
        applicant_data['experience_years'] = 0.0
        print("Invalid input, using 0 years")
    
    # Skills
    try:
        applicant_data['skills_count'] = int(input("Number of relevant skills: "))
    except ValueError:
        applicant_data['skills_count'] = 0
        print("Invalid input, using 0 skills")
    
    # Interview score
    try:
        applicant_data['interview_score'] = float(input("Interview score (0-100): "))
    except ValueError:
        applicant_data['interview_score'] = 0.0
        print("Invalid input, using 0")
    
    # Portfolio score
    try:
        applicant_data['portfolio_score'] = float(input("Portfolio/Projects score (0-100): "))
    except ValueError:
        applicant_data['portfolio_score'] = 0.0
        print("Invalid input, using 0")
    
    # Certifications
    try:
        applicant_data['certifications_count'] = int(input("Number of relevant certifications: "))
    except ValueError:
        applicant_data['certifications_count'] = 0
        print("Invalid input, using 0")
    
    return applicant_data


def display_results(applicant_data: Dict, results: Dict):
    """Display scoring results."""
    print("\n" + "="*60)
    print(f"APPLICANT: {applicant_data.get('name', 'N/A')}")
    print("="*60)
    print(f"\nTOTAL SCORE: {results['total_score']}/100")
    print(f"RECOMMENDATION: {results['recommendation']}")
    
    print("\n--- Score Breakdown ---")
    breakdown = results['breakdown']
    for category, scores in breakdown.items():
        print(f"{category.capitalize():20s}: {scores['score']:6.2f}/100 (Weighted: {scores['weighted']:6.2f})")
    
    print("\n--- Scoring Weights ---")
    scorer = JobApplicantScorer()
    for category, weight in scorer.weights.items():
        print(f"{category.capitalize():20s}: {weight}%")
    print("="*60 + "\n")


if __name__ == "__main__":
    scorer = JobApplicantScorer()
    
    # Get applicant data
    applicant_data = get_applicant_input()
    
    # Calculate scores
    results = scorer.calculate_total_score(applicant_data)
    
    # Display results
    display_results(applicant_data, results)
