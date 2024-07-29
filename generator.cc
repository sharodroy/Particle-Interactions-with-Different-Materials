
#include "generator.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"

MyPrimaryGenerator::MyPrimaryGenerator()
{
    G4int n_particle = 1;
    fParticleGun = new G4ParticleGun(n_particle);

    G4ParticleTable* particleTable = G4ParticleTable::GetParticleTable();
    G4String particleName;
    G4ParticleDefinition* particle = particleTable->FindParticle(particleName="e-");
    // In the line above where it asks for particleName, define the particle you want to define.
    // The ones I used are protons, electrons, and positively and negatively charged muons.
    // Proton Input: proton
    // Electron Input: e-
    // Positively Charged Muons: mu+
    // Negatively Charged Muons: mu-

    fParticleGun->SetParticleDefinition(particle);
    fParticleGun->SetParticleEnergy(100000.0*MeV);
    // Define amount of Energy you want to shoot your particle at.
    // I used 100, 10000, and 100000 MeV for my data visualizations.
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., -0.5*m));
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., 0., 1.));
}

MyPrimaryGenerator::~MyPrimaryGenerator()
{
    delete fParticleGun;
}

void MyPrimaryGenerator::GeneratePrimaries(G4Event* anEvent)
{
    fParticleGun->GeneratePrimaryVertex(anEvent);
}
