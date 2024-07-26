
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
    G4ParticleDefinition* particle = particleTable->FindParticle(particleName="gamma");

    fParticleGun->SetParticleDefinition(particle);
    fParticleGun->SetParticleEnergy(1.0*MeV);
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., -0.5*1.2*m)); // Position at -0.6 m along z-axis
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., 0., 1.)); // Shoot particles towards +z direction
}

MyPrimaryGenerator::~MyPrimaryGenerator()
{
    delete fParticleGun;
}

void MyPrimaryGenerator::GeneratePrimaries(G4Event* anEvent)
{
    fParticleGun->GeneratePrimaryVertex(anEvent);
}
