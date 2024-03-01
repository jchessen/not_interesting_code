#include <cmath>
#include <cstdlib>
#include <iostream>
#include <random>
#include <fstream>

std::random_device rd; // Seed for random number engine
std::mt19937 gen(rd()); // Standard mersenne_twister_engine seeded with rd()

// Moyal Distribution Probability Density Function
double moyal_pdf(double x) {
    double mu = 0.0; // Location parameter for Moyal distribution
    double sigma = 1.0; // Scale parameter for Moyal distribution
    double z = (x - mu) / sigma;
    return (1 / (sqrt(2 * M_PI))) * exp(-0.5 * (z + exp(-z)));
}

// Function to sample from Moyal using MCMC and the Metropolis-Hastings algorithm
    std::vector<double> mcmc_moyal(int n_samples, double initial_value, double proposal_stddev) {
    std::normal_distribution<double> proposal_dist(0.0, proposal_stddev);
    std::vector<double> samples;
    samples.reserve(n_samples);
    
    double current_sample = initial_value;
    double proposal;
    double acceptance_ratio;
    
    for (int i = 0; i < n_samples; ++i) {
        proposal = current_sample + proposal_dist(gen); // Generate a proposal

        // Calculate acceptance ratio (assumes symmetric proposal distribution)
        acceptance_ratio = moyal_pdf(proposal) / moyal_pdf(current_sample);

        // Decide to accept or reject the proposal
        if ((acceptance_ratio > 1) || (acceptance_ratio > std::generate_canonical<double, 10>(gen))) {
            current_sample = proposal; // Accept
        }
        // else reject, keep current sample

        samples.push_back(current_sample);
    }

    return samples;
}

int main() {
    int n_samples = 10000; // Total number of samples to draw
    double initial_value = 0.0; // Initial value for the chain
    double proposal_stddev = 1.0; // Standard deviation for the proposal distribution

    std::vector<double> samples = mcmc_moyal(n_samples, initial_value, proposal_stddev);

    // Save samples to a CSV file
    std::ofstream outfile("moyal_samples.csv");
    for (double sample : samples) {
        outfile << sample << std::endl;
    }
    outfile.close();

    std::cout << "Saved " << n_samples << " MCMC samples to moyal_samples.csv" << std::endl;


    return 0;
}
