#INDIPENDENT ALLELES



import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

def probability_at_least_n_organisms(k, N):
    total_offspring = 2 ** k
    probability_one_offspring = 0.25  # Probability of getting Aa Bb genotype in one offspring

    probability_at_least_N = 0
    for n in range(N, total_offspring + 1):
        probability_n_organisms = binomial_coefficient(total_offspring, n) * (probability_one_offspring ** n) * ((1 - probability_one_offspring) ** (total_offspring - n))
        probability_at_least_N += probability_n_organisms
    
    return probability_at_least_N
print(probability_at_least_n_organisms(5,8))
