"""Runs the algorithm for the three main steps."""
from init import *


def chemotaxis():
    Jlast = 0.0
    new_cell = Cell()
    for i in range(S):
        interaction(population[i])
        Jlast = population[i].fitness
        tumble_step(new_cell, population[i])  # tumble i bactu nd save new cell
        objective_function(new_cell)
        interaction(new_cell)
        for j in range(dimension):
            population[i].vect[j] = new_cell.vect[j]
        population[i].cost = new_cell.cost
        population[i].fitness = new_cell.fitness
        population[i].health += population[i].fitness

        for m in range(N_sl):
            if new_cell.fitness < Jlast:
                Jlast = new_cell.fitness
                swim_step(new_cell, population[i])

                objective_function(new_cell)
                interaction(new_cell)

                # copy
                for j in range(dimension):
                    population[i].vect[j] = new_cell.vect[j]
                population[i].cost = new_cell.cost
                population[i].fitness = new_cell.fitness
                population[i].health += population[i].fitness

            else:
                break


def optimization():
    for l in range(N_ed):
        for k in range(N_re):
            for j in range(N_ch):
                # chemotaxis()
                printf("best = %s, fe_count = %s", best, fe_count)
            # reproduction()
        # elimination_dispersal()
    print(
        "best found value: %s, number of function evaluations: %s", best,
        fe_count)

"""
void reproduction()
{
    /* sort the population in order of increasing health value */
    qsort(population, S, sizeof(Cell), (int(*)(const void*,const void*))compare);
    int i, j;
    /* Sr healthiest bacteria split into two bacteria, which are placed at the same location */
    for(i = S-Sr, j = 0; j < Sr; i++, j++)
    {
        population[i] = population[j];
    }
    for(i = 0; i < S; i++)
    {
        population[i].health = 0.0;
    }
}
"""