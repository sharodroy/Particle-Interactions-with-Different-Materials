
#include "construction.hh"
#include "SensitiveDetector.hh"

// Include necessary Geant4 headers
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

MyDetectorConstruction::MyDetectorConstruction()
{}

MyDetectorConstruction::~MyDetectorConstruction()
{}

G4VPhysicalVolume *MyDetectorConstruction::Construct()
{
    G4NistManager *nist = G4NistManager::Instance();

    G4Material *Aluminum = nist->FindOrBuildMaterial("G4_Al");

    G4double energy[2] = {1.239841939*eV/0.2, 1.239841939*eV/0.9};
    G4double rindexAluminum[2] = {1.39, 1.39};

    G4MaterialPropertiesTable *mptAluminum = new G4MaterialPropertiesTable();
    mptAluminum->AddProperty("RINDEX", energy, rindexAluminum, 2);
    Aluminum->SetMaterialPropertiesTable(mptAluminum);

    G4double world_sizeXY = 1.2*m;
    G4double world_sizeZ  = 1.2*m;
    G4Material* world_mat = nist->FindOrBuildMaterial("G4_AIR");

    G4Box* solidWorld = new G4Box("World", 0.5*world_sizeXY, 0.5*world_sizeXY, 0.5*world_sizeZ);
    G4LogicalVolume* logicWorld = new G4LogicalVolume(solidWorld, world_mat, "World");
    G4VPhysicalVolume* physWorld = new G4PVPlacement(0, G4ThreeVector(), logicWorld, "World", 0, false, 0, true);

    G4Box* solidSlab = new G4Box("Slab", 0.5*world_sizeXY, 0.5*world_sizeXY, 0.5*10*cm);
    G4LogicalVolume* logicSlab = new G4LogicalVolume(solidSlab, Aluminum, "Slab");
    new G4PVPlacement(0, G4ThreeVector(0,0,0.5*world_sizeZ-0.5*10*cm), logicSlab, "Slab", logicWorld, false, 0, true);

    G4Box* solidDet = new G4Box("Detector", 0.5*world_sizeXY, 0.5*world_sizeXY, 0.5*1*cm);
    G4LogicalVolume* logicDet = new G4LogicalVolume(solidDet, world_mat, "Detector");
    new G4PVPlacement(0, G4ThreeVector(0,0,-0.5*world_sizeZ+0.5*1*cm), logicDet, "Detector", logicWorld, false, 0, true);

    return physWorld;
}

void MyDetectorConstruction::ConstructSDandField()
{
    SensitiveDetector* sensDet = new SensitiveDetector("SensitiveDetector");
    SetSensitiveDetector("Detector", sensDet);
}
