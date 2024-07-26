#include "SensitiveDetector.hh"
#include "G4Step.hh"
#include "G4Track.hh"
#include "G4TouchableHistory.hh"
#include <fstream>
#include <iomanip>

SensitiveDetector::SensitiveDetector(const G4String& name) : G4VSensitiveDetector(name)
{
    std::ofstream outfile;
    outfile.open("output.csv", std::ios::out);
    outfile << "EventID,ParticleName,PositionX,PositionY,PositionZ,Energy,MomentumX,MomentumY,MomentumZ" << std::endl;
    outfile.close();
}

SensitiveDetector::~SensitiveDetector()
{}

void SensitiveDetector::Initialize(G4HCofThisEvent* /*hce*/)
{}

G4bool SensitiveDetector::ProcessHits(G4Step* step, G4TouchableHistory* /*hist*/)
{
    G4Track* track = step->GetTrack();
    G4int eventID = G4RunManager::GetRunManager()->GetCurrentEvent()->GetEventID();
    G4String particleName = track->GetDefinition()->GetParticleName();
    G4ThreeVector position = track->GetPosition();
    G4double energy = track->GetKineticEnergy();
    G4ThreeVector momentum = track->GetMomentum();

    std::ofstream outfile;
    outfile.open("output.csv", std::ios::app);
    outfile << eventID << ","
            << particleName << ","
            << position.x() << ","
            << position.y() << ","
            << position.z() << ","
            << energy << ","
            << momentum.x() << ","
            << momentum.y() << ","
            << momentum.z() << std::endl;
    outfile.close();

    return true;
}

void SensitiveDetector::EndOfEvent(G4HCofThisEvent*)
{}
