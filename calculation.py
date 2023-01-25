import human
import coli
import ara
import eleg

urlhs = 'https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&query=%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29'
dths = human.hscal(urlhs)

urlco = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28Escherichia%20coli%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28model_organism%3A83333%29'
dtco = coli.cocal(urlco)

urlara = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28Arabidopsis%20thaliana%29%20AND%20%28model_organism%3A3702%29%20AND%20%28reviewed%3Atrue%29'
dtara = ara.aracal(urlara)

urleleg = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28C.%20elegans%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28model_organism%3A6239%29'
dteleg = eleg.elegcal(urleleg)


